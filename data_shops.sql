DELETE FROM ShopResult;

INSERT INTO ShopResult (
    ShopID, StoreID, Shift, TimeCode, TypeCode, Day,
    Score, Score_Service, Score_Quality, Score_Clean, Score_Satisfaction,
    Upsell, Ticket_Time, Small_Ticket_Time, Large_Ticket_Time,
    Fry_Quality, Fry_Quantity, Lobby_Clean, Friendly_Greeting,
    Cashier
) VALUES (
    20233896, 1626, 'DINNER', 2, '1', "2025-01-06",
    95, 95, 100, 100, 100,
    1, '9.8', 0, 1,
    1, 1, 1, 1,
    'Ashley'
);

