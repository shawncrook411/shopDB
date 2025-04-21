SELECT * FROM STORE;
SELECT * FROM CREW;

SELECT ShopID, StoreID, Shift, Day, Score, 
Score_Service AS Service, Score_Quality AS Quality, Score_Clean AS Cleanliness, Score_Satisfaction AS Satisfaction, 
Ticket_Time AS "Ticket Time", Cashier FROM SHOPRESULT;