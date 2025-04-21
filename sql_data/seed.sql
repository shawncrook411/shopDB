USE shop;

DELETE FROM ShopResult;
DELETE FROM Crew;
DELETE FROM Store;

SOURCE store.sql;
SOURCE employee.sql;
SOURCE shops.sql;