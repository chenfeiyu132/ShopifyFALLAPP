# ShopifyFALLAPP

## Question 1
1. The reason why the AOV(Average Order Value) is so high is becuase there exists extreme outliers in the data set in terms of order_amounts, with the max order amount being 704000. This would significantly skew the average order value towards the higher end(3145.128) when we naively calculate it by summing up the order amounts and dividing that by the number of rows/orders. A better way to evaluate this data would be to exclude outliers from the dataset by choosing to ignore order_amounts that are beyond the 99% quantile range. As we visualize the dataset we can see that most of the dataset are concentrated within a specific range and therefore choosing an effective quantile range to analyze would be an efficient solution here. One could also plot the AOV against the decrease in the upper quantile range of the data to visualize the significant drops in AOV as we exclude those extreme outliers(it should look like an exponential decay graph starting from 3145.128)

2. Another metric I would report is the difference between the best and worst performers in terms of revenue per shop excluding the top 5% quantile.

3. The value is 20757, which is interesting since the average revenue by shop is about 14211.65 even with the filtered top outliers. This could be attributed to the different target price range of the sneakers but considering the simplication already given in the situation where each shop only sells one model of shoe, it would be worth looking into the revenue gap with further data visualizations.

## Question 2

1. 54 orders were shipped by Speedy Express in total 

`SELECT COUNT(*) FROM Orders WHERE ShipperID = 1`

2. Peacock is the last name of the employee with the most orders(40)

`SELECT EmployeeID, COUNT(*) FROM Orders GROUP BY EmployeeID ORDER BY COUNT(*) DESC` - Used to find the number of orders ranked by largest to smallest

`SELECT * FROM Employees WHERE EmployeeID = 4` - Used to find the Employee info with ID 4 since this was the employeeID with most order count

3. Boston Crab Meat is the product ordered the most by customers in Germany

`SELECT ProductID, SUM(Quantity) FROM OrderDetails WHERE OrderID IN (SELECT OrderID FROM Orders WHERE CustomerID IN (SELECT CustomerID FROM Customers WHERE Country = 'Germany')) GROUP BY ProductID ORDER BY SUM(Quantity) DESC` - Finds the largest total quantity of products ordered by customers from Germany

`SELECT * FROM Products WHERE ProductID = 40` - Finds the product associated with ProductID 40(which has the largest total quantity found by the preivous query)