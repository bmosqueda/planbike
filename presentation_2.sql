-- 60466217
SELECT COUNT(*) FROM registrobicis;

-- El registro menos reciente
SELECT * FROM registrobicis
ORDER BY Fecha_Retiro ASC
LIMIT 1;

-- El registro más reciente
SELECT * FROM registrobicis
ORDER BY Fecha_Retiro DESC
LIMIT 10;