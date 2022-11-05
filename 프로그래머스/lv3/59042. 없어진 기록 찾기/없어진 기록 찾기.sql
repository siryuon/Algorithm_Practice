SELECT O.ANIMAL_ID, O.NAME
FROM ANIMAL_INS I RIGHT OUTER JOIN ANIMAL_OUTS O ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE I.DATETIME IS NULL
ORDER BY O.ANIMAL_ID