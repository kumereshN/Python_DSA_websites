# Write your MySQL query statement below
SELECT MIN(p1.x - p2.x) AS shortest
FROM point p1
INNER JOIN point p2 on p1.x > p2.x;
