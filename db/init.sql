CREATE TABLE map_tracks (
    track_id SERIAL PRIMARY KEY,
    coordinates json,
    start_points json,
    created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);