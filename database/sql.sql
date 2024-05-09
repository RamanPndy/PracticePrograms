-- write a sql query from table which have id, transactions and status columns. a single transaction id can have 2 status in a table such as pending and refunded. 
-- a transaction can have both pending and return status. return unique transactions which have status pending and not refunded from same table
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

-- List all students and their scholarship amounts if they have received any. 
-- If a student has not received a scholarship, display NULL for the scholarship details.
SELECT 
    Student.FIRST_NAME,
    Student.LAST_NAME,
    COALESCE(Scholarship.SCHOLARSHIP_AMOUNT, NULL) AS SCHOLARSHIP_AMOUNT,
    COALESCE(Scholarship.SCHOLARSHIP_DATE, NULL) AS SCHOLARSHIP_DATE
FROM 
    Student
LEFT JOIN 
    Scholarship ON Student.STUDENT_ID = Scholarship.STUDENT_REF_ID;

-- Write an SQL query to determine the nth (say n=5) highest GPA from a table.
SELECT * FROM Student ORDER BY GPA DESC LIMIT 5, 1;

-- Write an SQL query to determine the 5th highest GPA without using LIMIT keyword.
SELECT * FROM Student s1 
WHERE 4 = (
    SELECT COUNT(DISTINCT (s2.GPA)) 
    FROM Student s2
    WHERE s2.GPA >= s1.GPA
);

-- Write an SQL query to fetch the list of Students with the same GPA.
SELECT s1.* FROM Student s1, Student s2 WHERE s1.GPA = s2.GPA AND s1.Student_id != s2.Student_id;

-- Write an SQL query to show the second highest GPA from a Student table using sub-query.
SELECT MAX(GPA) FROM Student WHERE GPA NOT IN(SELECT MAX(GPA) FROM Student);

-- Write an SQL query to fetch the first 50% records from a table.
SELECT * FROM Student WHERE STUDENT_ID <= (SELECT COUNT(STUDENT_ID)/2 FROM Student);

-- semantic constraints impose additional restrictions on the values in a column. 
-- For example, all mobile numbers in India start with '+91', followed by 10 digits. 
-- Using a semantic constraint for this requirement ensures that we do not get incorrect data for any row: 
-- For example, a row with a phone number +91987654321 would not be allowed to enter the database as it has only 9 digits after the country code.