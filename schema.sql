CREATE TABLE IF NOT EXISTS "beatmap_sets"(
  beatmap_set_id text primary key,
  title text not null,
  title_unicode text not null,
  artist text not null,
  artist_unicode text not null,
  creator text not null,
  source text,
  tags text
);
CREATE TABLE IF NOT EXISTS "beatmaps"(
  beatmap_id integer primary key,
  beatmap_set_id text not null,
  mode integer not null,
  difficulty_name text not null,
  hp_drain real not null,
  circle_size real not null,
  overall_difficulty real not null,
  approach_rate real not null,
  slider_multiplier real not null,
  slider_tick_rate real not null,
  stack_leniency real not null,
  FOREIGN KEY(beatmap_set_id)
    REFERENCES beatmap_sets (beatmap_set_id)
);
CREATE TABLE IF NOT EXISTS "objects"(
  object_number integer not null,
  beatmap_id integer not null,
  type text not null,
  time integer not null,
  x integer not null,
  y integer not null,
  new_combo integer not null,
  anchors text,
  length real,
  curve_type text,
  slides integer,
  PRIMARY KEY(object_number, beatmap_id)
  FOREIGN KEY(beatmap_id)
    REFERENCES beatmaps (beatmap_id)
);
CREATE TABLE IF NOT EXISTS 'beatmaps_web' (beatmap_id integer primary key, status text not null, foreign key (beatmap_id) references beatmaps (beatmap_set_id));
