-- write a sql query from table which have id, transactions and status columns. a single transaction id can have 2 status in a table such as pending and refunded. a transaction can have both pending and return status. return unique transactions which have status pending and not refunded from same table
SELECT id, transactions, status
FROM your_table
WHERE status = 'pending'
  AND id NOT IN (
    SELECT id
    FROM your_table
    WHERE status = 'refunded'
  );
  
-- find 2nd highest salary
SELECT MAX(SALARY) FROM Employee WHERE SALARY < (SELECT MAX(SALARY) FROM Employee);
-- find 3r highest salary
SELECT * FROM `employee_table` ORDER BY `sal` DESC LIMIT 1 OFFSET 2;
-- find nth highest salary
SELECT * FROM employee WHERE salary= (SELECT DISTINCT(salary) FROM employee ORDER BY salary DESC LIMIT n-1,1);
-- find 4th highest salary
SELECT * FROM employee WHERE salary= (SELECT DISTINCT(salary) FROM employee ORDER BY salary DESC LIMIT 3,1);

-- COALESCE Example
INSERT INTO items (product, price, discount) VALUES ('A', 1000 ,10), ('B', 1500 ,20), ('C', 800 ,5), ('D', 500, NULL);
SELECT
	product,
	(price - COALESCE(discount,0)) AS net_price
FROM
	items;
