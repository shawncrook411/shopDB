SELECT Store.StoreID, Store.Store_Name, 
CONCAT_WS('', Crew.First_Name, ' ', Crew.Last_Name) AS General_Manager FROM STORE
LEFT JOIN Crew ON Crew.StoreID = Store.StoreID
WHERE (Crew.Manager = 2);

SELECT EmployeeID, StoreID, CONCAT_WS('', Crew.First_Name, ' ', Crew.Last_Name) AS Name,
HiredDate FROM CREW;

SELECT EmployeeID, StoreID, CONCAT_WS('', Crew.First_Name, ' ', Crew.Last_Name) AS "Manager Name",
IF(Manager = 1, 'Shift-Lead', 'General Manager') AS Role,
Manager_Certify_Date FROM CREW
WHERE (Crew.Manager >= 1);

SELECT ShopID, ShopResult.StoreID, Shift, Day, Score, 
Score_Service AS Service, Score_Quality AS Quality, Score_Clean AS Cleanliness, Score_Satisfaction AS Satisfaction, 
Ticket_Time AS "Ticket Time", CONCAT_WS('', Crew.First_Name, ' ', Crew.Last_Name) AS Cashier FROM SHOPRESULT   
LEFT JOIN Crew on Crew.EmployeeID = ShopResult.Cashier;