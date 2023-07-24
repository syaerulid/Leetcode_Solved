# Write your MySQL query statement below
-- output
SELECT
    event_day AS day,
    emp_id,
    SUM(out_time - in_time) AS total_time
FROM Employees
GROUP BY 1,2
ORDER BY 1;
