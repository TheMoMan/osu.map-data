-- List maps that use only one type of object

.once scripts/out/mapsWithSingleType.txt

SELECT artist, title, difficulty_name, creator
FROM
  beatmaps
  INNER JOIN beatmap_sets ON beatmap_sets.beatmap_set_id = beatmaps.beatmap_set_id
WHERE beatmap_id IN (
  SELECT beatmaps.beatmap_id
  FROM
    objects
    INNER JOIN beatmaps ON beatmaps.beatmap_id = objects.beatmap_id
    GROUP BY type
    HAVING COUNT(*) = 1
)
