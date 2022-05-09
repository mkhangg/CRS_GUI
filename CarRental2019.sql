/*******************************************************************************
   File Name: CRS.sql
   Class: CSE 3330 
   Section: 04 
   Group Member: SAO NGUYEN, KHANG NGUYEN
   Group: 10
********************************************************************************/
/*******************************************************************************
 SQL open command: 
 sqlite3
.read CRS.sql
 SQL import command:
.mode csv
.import '|tail -n +2 CUSTOMER.csv' CUSTOMER
.import '|tail -n +2 RENTAL.csv' RENTAL
.import '|tail -n +2 RATE.csv' RATE
.import '|tail -n +2 VEHICLE.csv' VEHICLE
 SQL export command: 
.mode column
.header on
   queries...
.output output.txt 
 ******************************************************************************/

/*******************************************************************************
   Drop Tables
********************************************************************************/
DROP TABLE IF EXISTS [CUSTOMER];

DROP TABLE IF EXISTS [RENTAL];

DROP TABLE IF EXISTS [VEHICLE];

DROP TABLE IF EXISTS [RATE];
/*******************************************************************************
   Create Tables
********************************************************************************/
CREATE TABLE [CUSTOMER]
(
   [CustID] INTEGER NOT NULL,
   [Name] NVARCHAR(50) NOT NULL,
   [Phone] NVARCHAR(24),
   CONSTRAINT [PK_CUSTOMER] PRIMARY KEY ([CustID])
);

CREATE TABLE [RENTAL]
(
   [CustID] INTEGER NOT NULL,
   [VehicleID] NVARCHAR(20) NOT NULL,
   [StartDate] NVARCHAR(10) NOT NULL,
   [OrderDate] NVARCHAR(10),
   [RentalType] INTEGER,
   [Qty] INTEGER,
   [ReturnDate] NVARCHAR(10),
   [TotalAmount] INTEGER,
   [PaymentDate] NVARCHAR(10),
   CONSTRAINT [PK_RENTAL] PRIMARY KEY ([CustID], [VehicleID], [StartDate]),
   FOREIGN KEY ([CustID]) REFERENCES [CUSTOMER] ([CustID])
      ON DELETE NO ACTION  ON UPDATE   NO ACTION,
   FOREIGN KEY ([VehicleID]) REFERENCES [VEHICLE] ([VehicleID])
      ON DELETE NO ACTION  ON UPDATE   NO ACTION
);

CREATE TABLE [VEHICLE]
(
   [VehicleID] NVARCHAR(50) NOT NULL,
   [Description] NVARCHAR(50),
   [Year] INTEGER,
   [Type] INTEGER NOT NULL,
   [Category] INTEGER NOT NULL,
   CONSTRAINT [PK_VEHICLE] PRIMARY KEY ([VehicleID])
);  

CREATE TABLE [RATE] 
(
   [Type] INTEGER NOT NULL,
   [Category] INTEGER NOT NULL,
   [Weekly] INTEGER,
   [Daily] INTEGER,
   CONSTRAINT [PK_RATE] PRIMARY KEY ([Type], [Category]),
   FOREIGN KEY ([Type]) REFERENCES [VEHICLE]([Type])
      ON DELETE NO ACTION  ON UPDATE   NO ACTION,
   FOREIGN KEY ([Category]) REFERENCES [VEHICLE]([Category])
      ON DELETE NO ACTION  ON UPDATE   NO ACTION
);



/*******************************************************************************
   Create Foreign Keys
********************************************************************************/
CREATE INDEX [IFK_CUSTOMER] ON [CUSTOMER] ([CustID]);
CREATE INDEX [IFK_VEHICLE] ON [VEHICLE] ([VehicleID]);
/*******************************************************************************