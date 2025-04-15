USE shop;

DELETE FROM ShopResult;
DELETE FROM Crew;
DELETE FROM Store;

SOURCE data_store.sql;
SOURCE data_employee.sql;
SOURCE data_shops.sql;