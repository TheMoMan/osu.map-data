-- List occurences of a given object

.width 7 8 32 32 16 16

-- .once scripts/out/listObjectOccurences.txt

SELECT time, type, artist, title, difficulty_name, creator
FROM
  objects
  INNER JOIN beatmaps ON beatmaps.beatmap_id = objects.beatmap_id
  INNER JOIN beatmap_sets on beatmap_sets.beatmap_set_id = beatmaps.beatmap_set_id
WHERE
      x = 12
  AND y = 1
  -- AND time = 3834
  -- AND type = 'circle'
LIMIT 1000
