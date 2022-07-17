from io import TextIOWrapper
from pathlib import Path

from flask import jsonify, render_template, request

from app.main import app
from app.core.parser import KmlHandler
from app.core.utils import build_map_with_track, get_distance
import app.core.crud.tracks as crud
from app.core.db.engine import Session
from app.core.points_handler import filter_points

PROJECT_DIR = Path(__file__).resolve().parents[2]


@app.route("/")
def base_page():
    return render_template("upload.html")


@app.route("/uploader", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        kml_file = TextIOWrapper(request.files["file"])
        start_points, points = KmlHandler().get_points(kml_file)
        print(start_points)
        with Session() as db:
            track = crud.create_track(db, points, start_points)
            track_id = track.track_id
        folium_map = build_map_with_track(start_points, points)
        distance = get_distance(points)
        folium_map.save(PROJECT_DIR / "templates/map.html")

        return render_template("main.html", track_id=track_id, distance=distance)

@app.route("/filters", methods=["POST"])
def apply_filters():
    if request.method == "POST":
        data = request.json
        with Session() as db:
            points = filter_points(db, data['form_data'], data['track_id'])
            old_track = crud.get_track(db, data['track_id'])
            start_points = old_track.start_points
            track = crud.create_track(db, points, start_points)
        distance = get_distance(points)
        folium_map = build_map_with_track(start_points, points)
        folium_map.save(PROJECT_DIR / "templates/map.html")
        return jsonify({'distance': distance})

@app.route("/map")
def map():
    return render_template("map.html")
