-- List occurences of a given object

.width 7 8 32 32 16 16

-- .once scripts/out/listObjectOccurences.txt

SELECT time, type, objects.beatmap_id, artist, title, difficulty_name, creator
FROM
  objects
  INNER JOIN beatmaps ON beatmaps.beatmap_id = objects.beatmap_id
  INNER JOIN beatmap_sets on beatmap_sets.beatmap_set_id = beatmaps.beatmap_set_id
WHERE
      x = 11
      -- AND x < 65
  AND y = 1
  -- AND time = 248234
  -- AND type = 'circle' 
  -- AND objects.beatmap_id = 256499
  AND beatmaps.beatmap_id NOT IN (
    SELECT beatmap_id
    FROM beatmaps_web
    WHERE status = 'loved'
  )
LIMIT 1000
