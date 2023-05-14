SELECT employee_id,
       CASE
           WHEN employee_id % 2 != 0 AND SUBSTRING(name, 1, 1) <> 'M' THEN salary
           ELSE 0
       END AS bonus
FROM employees
ORDER BY employee_id;