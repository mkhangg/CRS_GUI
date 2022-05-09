CREATE VIEW vRentalInfo AS
SELECT OrderDate, StartDate, ReturnDate, (RentalType * Qty) AS TotalDays, VEHICLE.VehicleID AS VIN, Description AS Vehicle, 
CASE
	WHEN VEHICLE.Type = 1 THEN 'Compact'
	WHEN VEHICLE.Type = 2 THEN 'Medium'
	WHEN VEHICLE.Type = 3 THEN 'Large'
	WHEN VEHICLE.Type = 4 THEN 'SUV'
	WHEN VEHICLE.Type = 5 THEN 'Truck'
	WHEN VEHICLE.Type = 6 THEN 'Van'
END AS Type, 
CASE 
	WHEN VEHICLE.Category = 1 THEN 'Luxury'
	WHEN VEHICLE.Category = 0 THEN 'Basic'
END AS Category,
CUSTOMER.CustID AS CustomerID, Name AS CustomerName, TotalAmount AS OrderAmount,
CASE 
	WHEN RENTAL.PaymentDate = 'NULL' THEN '0'
	ELSE TotalAmount
END AS RentalBalance
FROM RENTAL, VEHICLE, CUSTOMER
WHERE CUSTOMER.CustID = RENTAL.CustID AND VEHICLE.VehicleID = RENTAL.VehicleID
ORDER BY StartDate ASC;
