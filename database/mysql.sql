--analytical functions
-- all analytical functions will be run with over keyword which means it is say what is the basis to do analytical operation

--rank() is a window function

select Ord_id, round(Sales) as Rounded Sales, Customer_name, 
    rank() over (order by sales desc) as sale_amount_rank 
    from market_fact_full 
    inner join cust_dimen using (Cust_id) 
    where Customer_name='raman';

with Rank_info as
(
    select Ord_id, round(Sales) as Rounded Sales, Customer_name, 
    rank() over (order by sales desc) as sale_amount_rank 
    from market_fact_full 
    inner join cust_dimen using (Cust_id) 
    where Customer_name='raman'
);

select Ord_id, Rounded Sales, Customer_name, sale_amount_rank
from Rank_info where sale_amount_rank < 10;

select Customer_name, cound(Ord_id) as Order_Count
rank() over(order by count(Ord_id) desc) as Order_Count_Rank
from cust_dimen
inner join
using(Cust_id)
group by Customer_name;

-- while the rank() function need not have consecutive values, the dense_rank() function must.
-- rank jumps up whenever the previous entries have similar values. If ten students had scored 495 marks instead of two, his rank would have become 11 but his dense rank would have remained as 2.

-- Movie Ranks
-- Given below is a table containing the top 10 movies according to their IMDb ratings.

-- IMDb Ratings
-- Title	                IMDb Rating	Dense Rank	Rank
-- The Shawshank Redemption	    9.2	        1	      1
-- The Godfather	            9.1	        2	      2
-- The Godfather: Part II	    9.0	        3	      3
-- The Dark Knight	            9.0	        3	      3
-- 12 Angry Men	                8.9	        4	      5
-- Schindler's List	            8.9	        4	      5
-- The Lord of the Rings: The Re8.9	        4	      5
-- Pulp Fiction	                8.9	        4	      5
-- The Good, the Bad and the Ugl8.8	        5(A)      9(B)
-- The Lord of the Rings: The Fe8.8	        5(A)      9(B)
 
-- Dense ranks are tightly packed, they have to be consecutive. 
-- The values of ranks depend on the number of similarly valued entries in a table, and they need not be consecutive. 
-- Since there are four entries with a rank 5, the next different entry would have a rank of 5 + 4 = 9.


-- Given a table named products with the following columns.
-- products(productCode, productName, productLine, productSale, quantityInStock)
-- Write a query to retrieve the ranks of the products in decreasing order of their quantities in stock.
select quantityInStock, rank() over (order by quantityInStock desc) as quantityRank from products;

select * rank() over(partition by ship_mode order by number_shipments desc) 'shipment_rank' from ship_table;
-- ranking counter will be reset on partition column which is known as partition ranking
-- rank() over (partition by <column_to_partition> order by <ordering_criterion>)

-- orderdetails table has columns orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber
-- There are some orders that have multiple order amounts corresponding to the same order. 
-- Write a query to retrieve the individual and total order amounts for each order along with the order numbers. 
-- Order the values in the increasing order of the order numbers. 
-- For similar order numbers, arrange the individual order amounts in the decreasing order.
SELECT orderNumber,
       productCode,
       SUM(quantityOrdered * priceEach) AS totalOrderAmount,
       SUM(quantityOrdered * priceEach) / SUM(quantityOrdered) AS individualOrderAmount,
       SUM(quantityOrdered) AS totalQuantityOrdered
FROM orderdetails
GROUP BY orderNumber, productCode
ORDER BY orderNumber ASC, individualOrderAmount DESC;

with order_ref
(
    SELECT orderNumber,
        SUM(quantityOrdered * priceEach)/SUM(quantityOrdered) AS individualOrderAmount,
        SUM(quantityOrdered * priceEach) AS totalOrderAmount
    FROM orderdetails
)

select orderNumber, individualOrderAmount, totalOrderAmount, rank() over(partition by orderNumber order by desc) from order_ref;

-- Named windows
-- define the window once, give it a name and then refer to the name in the 'over' clauses. 
-- A named window makes it easier to experiment with the window definition to observe the effect on the query results. 
-- You need only modify the window definition in the 'window' clause, rather than using multiple 'over' clause definitions.

-- rank the orders in the increasing order of the shipping cost for all orders placed by Raman. 
-- also display row number of each order.

select Ord_id, Discount, Customer_name,
row_number() over w as Discount_row_number,
rank() over w as Discount_Rank,
dense_rank() over w as Discount_Dense_Rank,
from market_fact_full
inner join cust_dimen
using(Cust_id)
where Customer_name = 'Raman'
window w as (order by Discount desc);

select *,
rank() over (partition by Ship_Mode order by count(*)) 'Rank',
dense_rank() over (partition by Ship_Mode order by count(*)) 'Dense Rank',
percent_rank() over (partition by Ship_Mode order by count(*)) 'Percent Rank'
from shipping_dimen;

select *,
rank() over w 'Rank',
dense_rank() over w 'Dense Rank',
percent_rank() over w 'Percent Rank'
from shipping_dimen
window w as (partition by Ship_Mode order by count(*))

-- Frames

-- Calculate the moving average shipping costs of all orders shipped in the year 2011.

-- moving averages are useful when sort the data using time

select shipping_cost, year(ship_date), month(ship_date),
avg(shipping_cost) over(order by year(ship_date), month(ship_date) rows unbounded preceding) 'Moving_Average' --all the previous rows
avg(shipping_cost) over(order by year(ship_date), month(ship_date) rows 9 preceding) 'Prev 10 moving average' --limiting the size of frame --only previous 9 rows including current row
from market_fact_full
inner join shipping_dimen
using(Ship_id);


-- The table given below contains the number of runs scored by Virat Kohli over the time period 2008-2019. 
-- Add another column which displays the 5-year moving average of the number of runs scored.
select *,
avg(Runs) over(order by year(Year) rows 4 preceding) as '5-year moving average'
from Kohli_Batting;