-- List maps which contain a given object

.once scripts/out/listMapsWithObject.txt

SELECT artist, title, difficulty_name, creator, COUNT(*) as freq
FROM
  objects
  INNER JOIN beatmaps ON beatmaps.beatmap_id = objects.beatmap_id
  INNER JOIN beatmap_sets on beatmap_sets.beatmap_set_id = beatmaps.beatmap_set_id
WHERE
      x = 256
  AND y = 192
  AND type != 'spinner'
GROUP BY artist, title, difficulty_name, creator
LIMIT 1000
