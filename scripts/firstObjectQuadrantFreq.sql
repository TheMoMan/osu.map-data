-- Gets frequency of the first non-spinner object in a map being placed in each quadrant

.once scripts/out/firstObjectQuadrantFreq.txt

SELECT
  CASE
    WHEN x < 256 AND y < 192 THEN 'topLeft'
    WHEN x > 256 AND y < 192 THEN 'topRight'
    WHEN x < 256 AND y > 192 THEN 'bottomLeft'
    WHEN x > 256 AND y > 192 THEN 'bottomRight'
    WHEN x = 256 AND y < 192 THEN 'top'
    WHEN x = 256 AND y > 192 THEN 'bottom'
    WHEN x < 256 AND y = 192 THEN 'left'
    WHEN x > 256 AND y = 192 THEN 'right'
    WHEN x = 256 AND y = 192 THEN 'centre'
    ELSE '???'
  END as quadrant,
  COUNT(*) as freq
FROM (
  SELECT beatmap_id, x, y, MIN(object_number)
  FROM objects
  WHERE type != 'spinner'
  GROUP BY beatmap_id
)
WHERE
  beatmap_id NOT IN (
    SELECT beatmap_id
    FROM beatmaps_web
    WHERE status = 'loved'
  )
GROUP BY quadrant
ORDER BY freq DESC
