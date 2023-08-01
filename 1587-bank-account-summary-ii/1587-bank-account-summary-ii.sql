# Write your MySQL query statement below
SELECT 
  u.name AS name,
  SUM(amount) AS balance
FROM USERS u
RIGHT JOIN Transactions t
ON u.account = t.account
GROUP BY 1
HAVING SUM(amount) > 10000