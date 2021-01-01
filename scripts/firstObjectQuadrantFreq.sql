-- Gets frequency of the first object in a map being placed in each quadrant

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
FROM objects
WHERE object_number = 0
GROUP BY quadrant
ORDER BY freq DESC
