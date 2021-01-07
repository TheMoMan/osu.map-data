-- Gets frequency of each object type

.once scripts/out/objectTypeFreq.txt

SELECT type, count(*) as freq
FROM objects
WHERE beatmap_id NOT IN (
  SELECT beatmap_id
  FROM beatmaps_web
  WHERE status = 'loved'
)
GROUP BY type
