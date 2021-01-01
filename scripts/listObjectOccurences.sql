-- List occurences of a given object

.once scripts/out/listObjectOccurences.txt

SELECT time, type, artist, title, difficulty_name, creator
FROM
  objects
  INNER JOIN beatmaps ON beatmaps.beatmap_id = objects.beatmap_id
  INNER JOIN beatmap_sets on beatmap_sets.beatmap_set_id = beatmaps.beatmap_set_id
WHERE
      x = 256
  AND y = 192
  -- AND type = 'slider'
LIMIT 1000
