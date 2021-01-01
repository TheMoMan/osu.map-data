-- List coordinates and lengths of sliders sorted by frequency

.once scripts/out/sliderCoordsByFreq.txt

SELECT x, y, length, type, COUNT(*) as freq
FROM objects
WHERE type = 'slider'
GROUP BY x, y, length, type
ORDER BY freq DESC;
