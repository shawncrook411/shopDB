DROP DATABASE IF EXISTS SHOP;
CREATE DATABASE SHOP;
USE SHOP;

CREATE TABLE Store (
    StoreID SMALLINT UNSIGNED PRIMARY KEY,
    General_Manager VARCHAR(20)    
);

CREATE TABLE Crew (
    EmployeeID VARCHAR(20) NOT NULL PRIMARY KEY,
    First_Name VARCHAR(20) NOT NULL,
    Last_Name VARCHAR(20) NOT NULL,
    Manager BOOLEAN DEFAULT 0,
    StoreID SMALLINT UNSIGNED NOT NULL,
    HiredDate DATE DEFAULT (CURRENT_DATE),
    Manager_Certify_Date DATE DEFAULT NULL,

    FOREIGN KEY (StoreID) REFERENCES Store(StoreID)
);

CREATE TABLE ShopResult (
    ShopID SMALLINT UNSIGNED NOT NULL PRIMARY KEY,
    StoreID SMALLINT UNSIGNED NOT NULL,
    Shift VARCHAR(20) CHECK (Shift IN ('LUNCH', 'DINNER', 'PHANTOM')) NOT NULL,
    Time VARCHAR(20) CHECK (Time IN ('11-1:30', '1:30-4', '4-7', '7-10')) NOT NULL,
    TimeCode SMALLINT UNSIGNED CHECK (TimeCode <= 4),
    Type VARCHAR(20) CHECK (Type IN ('Regular', 'Online', 'Delivery', 'Call-In')) NOT NULL,
    Day DATE,

    Score SMALLINT UNSIGNED NOT NULL,
    Score_Service SMALLINT UNSIGNED NOT NULL,
    Score_Quality SMALLINT UNSIGNED NOT NULL,
    Score_Clean SMALLINT UNSIGNED NOT NULL,
    Score_Satisfaction SMALLINT UNSIGNED NOT NULL,

    Upsell BOOLEAN,
    Ticket_Time varchar(20),
    Small_Ticket_Time BOOLEAN,
    Large_Ticket_Time BOOLEAN,
    Fry_Quality BOOLEAN,
    Fry_Quantity BOOLEAN,
    Lobby_Clean BOOLEAN,
    Friendly_Greeting BOOLEAN,

    Cashier VARCHAR(20),

    FOREIGN KEY (Cashier) REFERENCES Crew(EmployeeID),
    FOREIGN KEY (StoreID) REFERENCES Store(StoreID)
);

ALTER TABLE Store
ADD FOREIGN KEY (General_Manager) REFERENCES Crew(EmployeeID);