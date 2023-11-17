-- averge
SELECT score, COUNT(score) As number FROM second_table GROUP BY score ORDER BY number DESC;
