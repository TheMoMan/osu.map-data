-- List coordinates of circles by frequency
.output scripts/out/circleCoordsByFreq.txt

SELECT x, y, type, COUNT(*) as freq
FROM objects
GROUP BY x, y, type
ORDER BY freq DESC;
