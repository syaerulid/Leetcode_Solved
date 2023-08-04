SELECT 
    e.name AS Employee
FROM Employee m
INNER JOIN Employee e
ON m.id = e.managerId
WHERE e.salary > m.salary