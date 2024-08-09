-- Script that ranks country origins of bands, ordered by the number of fans
-- column names must be: Origin and nb_fans

SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC