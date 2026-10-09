SELECT * FROM ApexPlanet_dataanalytics;

---What are the top products by revenue
SELECT TOP 5
    Product,
    SUM(Total_Sales) AS Total_Revenue
FROM ApexPlanet_dataanalytics
GROUP BY Product
ORDER BY Total_Revenue DESC;

----which categories generate most revenue
SELECT
    Category,
    SUM(Total_Sales) AS Total_Revenue,
    SUM(Quantity) AS Units_Sold
FROM ApexPlanet_dataanalytics
GROUP BY Category
ORDER BY Total_Revenue DESC;

---which cities generate the highest sales 
SELECT
    City,
    COUNT(*) AS order_id,
    SUM(Total_Sales) AS Total_Sales
FROM ApexPlanet_dataanalytics
GROUP BY City
ORDER BY Total_Sales DESC;
