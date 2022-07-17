import re

from io import TextIOWrapper
from typing import List, Union, Tuple

from pykml import parser
from pykml.factory import KML_ElementMaker as KML


class KmlHandler:
    def _read(self, file: TextIOWrapper) -> KML.Document:
        """Reads and parses kml file from the stream

        Args:
            file (TextIOWrapper): File

        Returns:
            KML.Document: PyKML object
        """
        return parser.parse(file).getroot().Document

    def get_points(
        self, file: TextIOWrapper
    ) -> Union[Tuple[float], List[Union[float, float]]]:
        """Returns the coordinates of the path taken from the KML file

        Args:
            file (TextIOWrapper): File uploaded via the form on the website

        Returns:
            Union[Tuple[float], List[Union[float, float]]]: Start points for map overview
            and all coordinates of the tracked path
        """
        document = self._read(file)
        start_points = [float(document.LookAt.latitude), float(document.LookAt.longitude)]
        points = self._parse_kml_features(document.Folder)

        return start_points, points

    def _parse_kml_features(self, document: KML.Document) -> List[Union[float, float]]:
        """Extracts a LineString object from the document and parses the coordinates in it

        Args:
            document (KML.Document): PyKML object

        Returns:
            List[Union[float, float]]: Coordinates list (long, lat)
        """
        for feature in document.iterchildren():
            if hasattr(feature, "LineString"):
                return self._parse_coords(feature.LineString.coordinates.text)

    def _parse_coords(self, points: str) -> List[Union[float, float]]:
        """Converts a string with coordinates into a list with coordinates

        Args:
            points (str): Coordinates string

        Returns:
            List[List[float, float]]: Coordinates list (long, lat)
        """
        latlons = re.sub(r", +", ",", points.strip()).split()

        return [
            [float(c) for c in reversed(latlon.split(",")) if c != "0"]
            for latlon in latlons
        ]
