-- List coordinates of circles sorted by frequency

.once scripts/out/circleCoordsByFreq.txt

SELECT x, y, type, COUNT(*) as freq
FROM objects
WHERE type = 'circle'
GROUP BY x, y, type
ORDER BY freq DESC;
