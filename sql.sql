-- write a sql query from table which have id, transactions and status columns. a single transaction id can have 2 status in a table such as pending and refunded. a transaction can have both pending and return status. return unique transactions which have status pending and not refunded from same table
SELECT id, transactions, status
FROM your_table
WHERE status = 'pending'
  AND id NOT IN (
    SELECT id
    FROM your_table
    WHERE status = 'refunded'
  );
