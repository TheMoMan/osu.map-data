-- List coordinates and type of all objects sorted by frequency

.width 8 8 8 8 5
.once scripts/out/objectCoordsByFreq.txt

SELECT x, y, type, COUNT(*) as freq
FROM objects
WHERE beatmap_id NOT IN (
  SELECT beatmap_id
  FROM beatmaps_web
  WHERE status = 'loved'
)
GROUP BY x, y, type
ORDER BY freq DESC;
