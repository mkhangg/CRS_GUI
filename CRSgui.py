'''
File Name: CRSgui.py
Class: CSE 3330 
Section: 04 
Group Member: SAO NGUYEN, KHANG NGUYEN
Group: 10
'''
from tkinter import *
from tkinter import font
import sqlite3

root = Tk()
root.title('CAR RENTAL SYSTEM')
root.geometry("350x450")
root.configure(bg='#0B0058')

#database
#create a database or connect to one
conn = sqlite3.connect('car_rental_system.db')
#create cursor
c = conn.cursor()

#SAVE CUSTOMER btn
def save_cust():
	#create a database or connect to one
	conn = sqlite3.connect('car_rental_system.db')
	#create cursor
	c = conn.cursor()

	#get customer id
	c.execute("SELECT MAX(custID) FROM CUSTOMER")
	cust_id = c.fetchall()
	print_id = 0
	for record in cust_id:
		print_id = record[0]

	#insert into table
	c.execute("INSERT INTO CUSTOMER VALUES ( :custID, :name, :phone)",
		{
			'custID': print_id + 1,
			'name': add_name.get(),
			'phone': add_phone.get()
		})

	#commit changes
	conn.commit()
	#close connection
	conn.close()
	#close the window
	add_cust.destroy()

#ADD CUSTOMER
def customer():
	global add_cust
	add_cust = Tk()
	add_cust.title('Add Cutomer')
	add_cust.geometry("380x250")

	#create a database or connect to one
	conn = sqlite3.connect('car_rental_system.db')
	#create cursor
	c = conn.cursor()

	global add_name
	global add_phone

	#label ADD NEW CUSTOMER
	cust_label = Label(add_cust, text = 'ADD NEW CUSTOMER', font=12, fg="#290046")
	cust_label.grid(row = 0, columnspan=6, padx=50, pady=(30,0), sticky=NS)

	#label NAME
	add_name_label = Label(add_cust, text = 'Name:                      FirstInitial. LastName')
	add_name_label.grid(row = 1, column = 0, padx=50, pady=(5,0), sticky=W)
	#label PHONE#
	add_phone_label = Label(add_cust, text = 'Phone #:                             (xxx) xxx-xxxx')
	add_phone_label.grid(row = 3, column = 0, padx=50, pady=(5,0), sticky=W)

	#textbox NAME
	add_name = Entry(add_cust, width = 34)
	add_name.grid(row = 2, column = 0, padx =50, pady=(0,5), sticky=NS)
	#textbox PHONE#
	add_phone = Entry(add_cust, width = 34)
	add_phone.grid(row = 4, column = 0, padx =50, pady=(0,5), sticky=NS)

	#SAVE CUTOMER btn
	submit_cust_btn = Button(add_cust, text='Save Customer', fg="white", bg="#290046", command=save_cust)
	submit_cust_btn.grid(row=5,  column=0,  columnspan = 3, pady=20, padx=50, ipadx=50, sticky=NS)

#SAVE VEHICLE
def save_vehicle():
	#create a database or connect to one
	conn = sqlite3.connect('car_rental_system.db')
	#create cursor
	c = conn.cursor()

	#insert new VEHICLE into table
	c.execute("INSERT INTO VEHICLE VALUES (:vehicleID, :description, :year, :type, :category)",
		{
			'vehicleID': add_vehicleID.get(),
			'description': add_description.get(),
			'year': add_year.get(),
			'type': type_clicked.get(),
			'category': cat_clicked.get()
		})

	#commit changes
	conn.commit()
	#close connection
	conn.close()
	#close the window
	add_vehicle.destroy()
	

#ADD NEW VEHICLE
def vehicle():
	global add_vehicle
	add_vehicle = Tk()
	add_vehicle.title('Add New Vehicle')
	add_vehicle.geometry("480x300")

	#create a database or connect to one
	conn = sqlite3.connect('car_rental_system.db')
	#create cursor
	c = conn.cursor()

	global add_vehicleID
	global add_description
	global add_year
	global type_clicked
	global cat_clicked

	#label ADD NEW VEHICLE 
	vehicle_label = Label(add_vehicle, text = 'ADD NEW VEHICLE', font=12, fg="#0059CB")
	vehicle_label.grid(row = 0, columnspan=7, padx=20, pady=(30,0), sticky=NS )

	#label VEHICLE ID
	add_vehicleID_label = Label(add_vehicle, text = 'Vehicle ID: ')
	add_vehicleID_label.grid(row = 1, column = 0, columnspan=7, padx=(15,0), pady=(20,0), sticky=W)
	#label DESCRIPTION
	add_description_label = Label(add_vehicle, text = 'Description: ')
	add_description_label.grid(row = 2, column = 0, columnspan=7, padx=(15,0), pady=(10,0), sticky=W)
	#label YEAR
	add_year_label = Label(add_vehicle, text = 'Year: ')
	add_year_label.grid(row = 3, column = 0, padx=(15,0), pady=(10,0), sticky=W)
	#label TYPE
	add_type_label = Label(add_vehicle, text = 'Type: ')
	add_type_label.grid(row = 3, column = 2, padx=(15,0), pady=(10,0), sticky=W)
	#label CATEGORY
	add_category_label = Label(add_vehicle, text = 'Category: ')
	add_category_label.grid(row = 3, column = 4, padx=(15,0), pady=(10,0), sticky=W)

	#textbox VEHICLE ID
	add_vehicleID = Entry(add_vehicle, width = 40)
	add_vehicleID.grid(row = 1, column = 2, columnspan=7, padx=(0,15), pady=(20,0), sticky=W)
	#textbox DESCRIPTION
	add_description = Entry(add_vehicle, width = 40)
	add_description.grid(row = 2, column = 2, columnspan=7, padx=(0,15), pady=(10,0), sticky=W)
	#textbox YEAR
	add_year = Entry(add_vehicle, width = 10)
	add_year.grid(row = 3, column = 1, pady=(10,0), sticky=W)

	#dropbox TYPE and CATEGORY
	#datatype of menu text
	type_clicked = StringVar(add_vehicle)	
	cat_clicked = StringVar(add_vehicle)	
	#initial menu text
	type_clicked.set("*")	
	cat_clicked.set("**")	
	#create drop down menu
	type_drop = OptionMenu(add_vehicle, type_clicked, 1, 2, 3, 4, 5, 6)
	type_drop.grid(row = 3, column = 3, pady=(10,0), sticky=W)
	cat_drop = OptionMenu(add_vehicle, cat_clicked, 0, 1)
	cat_drop.grid(row = 3, column = 5, pady=(10,0), sticky=W)

	#SAVE VEHICLE btn
	submit_vehicle_btn = Button(add_vehicle, text='Save Vehicle', fg="white", bg="#0059CB", command=save_vehicle)
	submit_vehicle_btn.grid(row=4,  column=0,  columnspan = 7, pady=20, padx=20, ipadx=50, sticky=N)

	#INFO
	#label TYPE
	type_label = Label(add_vehicle, text = '*Type = 1:Compact, 2:Medium, 3:Large, 4:SUV, 5:Truck, 6:VAN', fg="#0059CB")
	type_label.grid(row = 5, column = 0,  columnspan = 7, pady=(2,0), sticky=SW)
	#label CATEGORY
	category_label = Label(add_vehicle, text = '**Category = 0:Basic, 1:Luxury', fg="#0059CB")
	category_label.grid(row = 6, column = 0,  columnspan = 7, pady=(2,0), sticky=SW)

#SAVE RENTAL
def save_rental():
	#create a database or connect to one
	conn = sqlite3.connect('car_rental_system.db')
	#create cursor
	c = conn.cursor()

	#insert new RENTAL into table
	c.execute("INSERT INTO RENTAL VALUES(:custID, :vehicleID, :startDate, :orderDate, :rentalType, :qty, :returnDate, :totalAmount, :paymentDate)",
		{
			'custID': select_custid.get(), 
			'vehicleID': select_vehicleid.get(), 
			'startDate': start.get(), 
			'orderDate': order_date.get(), 
			'rentalType': rental_type_clicked.get(), 
			'qty': qty.get(), 
			'returnDate': return_date.get(), 
			'totalAmount': total.get(), 
			'paymentDate': payment_date.get()
		})

	#commit changes
	conn.commit()
	#close connection
	conn.close()
	#close the window
	add_rental.destroy()

#ADD RENTAL
def search_vehicle():
	#create a database or connect to one
	conn = sqlite3.connect('car_rental_system.db')
	#create cursor
	c = conn.cursor()

	#make global
	global select_vehicleid
	global order_date
	global return_date
	global payment_date
	global rental_type_clicked
	global qty
	global total

	#label SEARCH RESULT
	search_vehicle_label = Label(add_rental, text = 'SEARCH RESULT', font=12, fg="#0059CB")
	search_vehicle_label.grid(row = 12, columnspan=16, padx=10, pady=5, sticky=N)
	#label SEARCH RESULT format
	format_vehicle_label = Label(add_rental, text = 'Vehicle ID                                  Description                       Year', fg="#0059CB")
	format_vehicle_label.grid(row = 13, columnspan=16, padx=20, pady=0, sticky=W)

	#select SERACH RESULT
	c.execute("SELECT * FROM VEHICLE, RENTAL WHERE RENTAL.vehicleID = VEHICLE.vehicleID AND VEHICLE.type = :type AND VEHICLE.category = :cat GROUP BY VEHICLE.vehicleID HAVING (RENTAL.startDate < :startD AND RENTAL.returnDate < :startD) OR (RENTAL.startDate < :endD AND RENTAL.returnDate < :endD)",
		{
			'type': int(search_type_clicked.get()),
			'cat': int(search_cat_clicked.get()),
			'startD': start.get(),
			'endD': end.get()
		})
	
	#scrollbar CUSTOMER
	search_scroll = Scrollbar(add_rental)
	search_scroll.grid(row=14, column = 4, padx=(0,20), ipady=15, sticky=W)

	#show output to terminal
	search_records = c.fetchall()
	#CUSTOMER listbox
	search_list = Listbox(add_rental, width=50, height=3, font='Courier', yscrollcommand=search_scroll.set)
	#loop thru results show all tupple
	for record in search_records:
		search_list.insert(END, str(record[0]) +"   "+ str(record[1]) +"   "+ str(record[2]))
	search_list.grid(row=14, column = 0, padx=(20,0), columnspan=5 , sticky=W)
	search_scroll.config(command=search_list.yview)

	#label VEHICLE ID
	select_vehicleid_label = Label(add_rental, text = 'Vehicle ID: ')
	select_vehicleid_label.grid(row = 15, column = 0, columnspan = 3, padx=(25,0), pady=5, sticky=W)
	#textbox VEHICLE ID
	select_vehicleid = Entry(add_rental, width = 41)
	select_vehicleid.grid(row = 15, column = 1, columnspan = 3, padx=(0,20), pady=5, sticky=W)

	#label  ORDER RETURN PAYMENT RENTALTYPE QTY TOTALAMOUNT
	order_date_label = Label(add_rental, text = 'Order Date: ')
	order_date_label.grid(row = 16, column = 0, columnspan = 3, padx=(25,0), pady=(5,0), sticky=W)
	return_date_label = Label(add_rental, text = 'Return Date: ')
	return_date_label.grid(row = 16, column = 1, columnspan = 3, padx=(25,0), pady=(5,0), sticky=W)
	payment_date_label = Label(add_rental, text = 'Payment Date: ')
	payment_date_label.grid(row = 16, column = 2, columnspan = 3, padx=(25,0), pady=(5,0), sticky=W)
	rental_type_label = Label(add_rental, text = 'Rental Type: ')
	rental_type_label.grid(row = 18, column = 0, columnspan = 3, padx=(25,0), pady=(5,0), sticky=W)
	qty_label = Label(add_rental, text = 'Quantity: ')
	qty_label.grid(row = 18, column = 1, columnspan = 3, padx=(25,0), pady=(5,0), sticky=W)
	total_label = Label(add_rental, text = 'Total Amount: ')
	total_label.grid(row = 18, column = 2, columnspan = 3, padx=(20,0), pady=(5,0), sticky=W)
	
	#textbox ORDER RETURN PAYMENT 
	order_date = Entry(add_rental, width = 15)
	order_date.grid(row = 17, column = 0, columnspan = 3, padx=(25,0), pady=(0,5), sticky=W)
	return_date = Entry(add_rental, width = 15)
	return_date.grid(row = 17, column = 1, columnspan = 3, padx=(25,0), pady=(0,5), sticky=W)
	payment_date = Entry(add_rental, width = 15)
	payment_date.grid(row = 17, column = 2, columnspan = 3, padx=(25,0), pady=(0,5), sticky=W)

	#ENTALTYPdropbox  RENTALTYPE
	rental_type_clicked = StringVar(add_rental)
	rental_type_clicked.set("***")
	rental_type_drop = OptionMenu(add_rental, rental_type_clicked, 1, 7)
	rental_type_drop.grid(row = 19, column = 0, padx=(25,0), pady=(0,5), sticky=W)

	#textbox QTY TOTALAMOUNT
	qty = Entry(add_rental, width = 15)
	qty.grid(row = 19, column = 1, columnspan = 3, padx=(25,0), pady=5, sticky=W)
	total = Entry(add_rental, width = 15)
	total.grid(row = 19, column = 2, columnspan = 3, padx=(25,0), pady=5, sticky=W)

	#ADD RENTAL btn
	select_vehicle_btn = Button(add_rental, text='Add Rental',fg="white", bg="#004E03", command=save_rental)
	select_vehicle_btn.grid(row=20,  column=0, columnspan=16, pady=10, padx=5, ipadx=50, sticky=N)

	rentaltype_label = Label(add_rental, text = '***Rental Type = 0:Daily, 7:Weekly', fg="#004E03")
	rentaltype_label.grid(row = 21, column = 0,  columnspan = 7, sticky=SW)

	#commit changes
	conn.commit()
	#close connection
	conn.close()

	#clear the text boxes
	start.delete(0,END)
	end.delete(0,END)
	search_type_clicked.set("*")
	search_cat_clicked.set("**")

#add new rental
def rental():
	global add_rental
	add_rental = Tk()
	add_rental.title('Add New Rental')
	add_rental.geometry("570x750")

	#create a database or connect to one
	conn = sqlite3.connect('car_rental_system.db')
	#create cursor
	c = conn.cursor()

	#SEARCH VEHICLE
	global start
	global end
	global search_type_clicked
	global search_cat_clicked
	global select_custid

	#label CHOOSE CUSTOMER 
	search_custid_label = Label(add_rental, text = 'CHOOSE CUSTOMER', font=12, fg="#290046")
	search_custid_label.grid(row = 0, columnspan=16, padx=10, pady=(20,0), sticky=N)
	#label CHOOSE CUSTOMER description
	format_custid_label = Label(add_rental, text = 'Customer ID   Name   Phone#', fg="#290046")
	format_custid_label.grid(row = 1, columnspan=16, padx=20, pady=(5,0), sticky=W)

	#scrollbar CUSTOMER
	cust_sb = Scrollbar(add_rental, orient=VERTICAL)
	cust_sb.grid(row=2, column = 4, padx=(0,20), ipady=15, sticky=W)
	#insert into table
	c.execute("SELECT * FROM CUSTOMER")
	#show output to terminal
	cust_records = c.fetchall()
	#listbox CUSOMER
	cust_list = Listbox(add_rental, width=50, height=3, font='Courier',yscrollcommand=cust_sb.set)
	for record in cust_records:
		cust_list.insert(END, str(record[0]) + "  " + str(record[1])+ "  " +str(record[2]))
	cust_list.grid(row=2, column = 0, padx=(20,0), columnspan=5 , sticky=W)
	cust_sb.config(orient=VERTICAL, command=cust_list.yview)

	#label CUSTOMER ID
	select_custid_label = Label(add_rental, text = 'Customer ID: ')
	select_custid_label.grid(row = 3, column = 0, padx=(20,0), pady=(5,0), sticky=W)
	#textbox CUSTOMER ID
	select_custid = Entry(add_rental, width = 41)
	select_custid.grid(row = 3, column = 1,columnspan=5 , padx=(0,5), pady=5, sticky=W)

	barr = Label(add_rental,text='------------------------------------------------------------------------------------------------------')
	barr.grid(row = 4, columnspan=5, sticky=N)

	#label SEARCH VEHICLE
	search_vehicle_label = Label(add_rental, text = 'SEARCH VEHICLE', font=12, fg="#0059CB")
	search_vehicle_label.grid(row = 5, columnspan=16, padx=10, pady=(10,0), sticky=N)


	#label STAR END TYPE CATEGORY
	start_label = Label(add_rental, text = 'Start Date: ')
	start_label.grid(row = 6, column = 0, padx=(25,0), pady=5, sticky=W)
	end_label = Label(add_rental, text = 'End Date: ')
	end_label.grid(row = 6, column = 1, padx=(25,0), pady=5, sticky=W)
	add_type_label = Label(add_rental, text = 'Type: ')
	add_type_label.grid(row = 6, column = 2, padx=(15,0), pady=(5,0), sticky=W)
	add_category_label = Label(add_rental, text = 'Category: ')
	add_category_label.grid(row = 6, column = 3, padx=(20,0), pady=(5,0), sticky=W)

	#textbox START END
	start = Entry(add_rental, width = 20)
	start.grid(row = 7, column = 0, padx=(25,0), pady=(0,5), sticky=W)
	end = Entry(add_rental, width = 20)
	end.grid(row = 7, column = 1, padx=(25,0), pady=(0,5), sticky=W)

	#label TYPE
	type_label = Label(add_rental, text = '*Type = 1:Compact, 2:Medium, 3:Large, 4:SUV, 5:Truck, 6:VAN', fg="#0059CB")
	type_label.grid(row = 9, column = 0,  columnspan = 7, padx=(20,0), pady=(2,0), sticky=SW)
	#label CATEGORY
	category_label = Label(add_rental, text = '**Category = 0:Basic, 1:Luxury', fg="#0059CB")
	category_label.grid(row = 10, column = 0,  columnspan = 7, padx=(20,0), pady=(2,0), sticky=SW)

	

	#dropbox TYPE CATEGORY
	#datatype of menu text
	search_type_clicked = StringVar(add_rental)
	search_cat_clicked = StringVar(add_rental)
	#initial menu text
	search_type_clicked.set("*")
	search_cat_clicked.set("**")
	#create drop down menu
	search_type_drop = OptionMenu(add_rental, search_type_clicked, 1, 2, 3, 4, 5, 6)
	search_type_drop.grid(row = 7, column = 2, padx=(15,0), pady=((0,5)), sticky=W)
	search_cat_drop = OptionMenu(add_rental, search_cat_clicked, 0, 1)
	search_cat_drop.grid(row = 7, column = 3, padx=(15,0), pady=((0,5)), sticky=W)

	#ADD RENTAL btn
	submit_vehicle_search_btn = Button(add_rental, text='Search Vehicle', fg="white", bg="#0059CB", command=search_vehicle)
	submit_vehicle_search_btn.grid(row=8,  column=0,  columnspan = 5, pady=5, padx=(10,0), ipadx=50, sticky=N)

	bar = Label(add_rental,text='------------------------------------------------------------------------------------------------------')
	bar.grid(row = 11, columnspan=5, sticky=N)

	#commit changes
	conn.commit()
	#close connection
	conn.close()

#update return
def update_return():
	#create a database or connect to one
	conn = sqlite3.connect('car_rental_system.db')
	#create cursor
	c = conn.cursor()

	c.execute("UPDATE RENTAL SET paymentDate = :returndate WHERE paymentDate == 'NULL'",
	{
		'returndate': select_return_date.get()
	})

	#commit changes
	conn.commit()
	#close connection
	conn.close()
	#close the window
	return_update.destroy()

#view rental
def rental_return():
	#create a database or connect to one
	conn = sqlite3.connect('car_rental_system.db')
	#create cursor
	c = conn.cursor()

	#label CHOOSE CUSTOMER description
	format_rental_label = Label(return_update, text = 'Customer ID   vehicle ID               Total Amount', fg="#527A00")
	format_rental_label.grid(row = 15, columnspan=16, padx=20, pady=(5,0), sticky=W)

	#VIEW LIST
	c.execute("SELECT * FROM RENTAL WHERE RENTAL.custID= :custid AND RENTAL.vehicleID= :vehicleid AND RENTAL.returnDate= :returndate",
	{
		'custid': select_cust_id.get(),
		'vehicleid': select_vehicleid.get(),
		'returndate': select_return_date.get()
	})

	return_sb = Scrollbar(return_update)
	return_sb.grid(row=16, column = 6, padx=(0,20), ipady=10, sticky=W)

	#show output to terminal
	return_records = c.fetchall()

	return_list = Listbox(return_update, width=50, height=2, font='Courier', yscrollcommand=return_sb.set)
	#loop thru results show all tupple
	for record in return_records:
		return_list.insert(END, str(record[0]) +"   "+ str(record[1]) +"   "+ str(record[7]))
	return_list.grid(row=16, column = 0, padx=(20,0), columnspan=5 , sticky=W)
	return_sb.config(command=return_list.yview)

	#RETURN RENTAL btn
	submit_update_btn = Button(return_update, text='Return Rental', fg="white", bg="#527A00", command=update_return)
	submit_update_btn.grid(row=17,  column=0,  columnspan = 5, padx=(10,0), ipadx=50, sticky=N)

	#commit changes
	conn.commit()
	#close connection
	conn.close()

#add new return car
def return_car():
	global return_update
	return_update = Tk()
	return_update.title('Update Car Return')
	return_update.geometry("570x750")

	#create a database or connect to one
	conn = sqlite3.connect('car_rental_system.db')
	#create cursor
	c = conn.cursor()

	#make global
	global select_cust_id
	global select_vehicleid
	global select_return_date

	#label CUSTOMER LIST
	search_custid_label = Label(return_update, text = 'CUSTOMER LIST', font=12, fg="#290046")
	search_custid_label.grid(row = 0, columnspan=5, padx=10, pady=(10,5), sticky=N)
	#label CHOOSE CUSTOMER description
	format_custid_label = Label(return_update, text = 'Customer ID   Name   Phone#', fg="#290046")
	format_custid_label.grid(row = 1, columnspan=16, padx=20, pady=(5,0), sticky=W)

	#scrollbar CUSTOMER LIST
	cust_sb = Scrollbar(return_update, orient=VERTICAL)
	cust_sb.grid(row=2, column = 6, padx=(0,20), ipady=23, sticky=W)
	#insert into table
	c.execute("SELECT * FROM CUSTOMER")
	#show output to terminal
	cust_records = c.fetchall()

	cust_list = Listbox(return_update, width=50, height=4, font='Courier',yscrollcommand=cust_sb.set)
	for record in cust_records:
		cust_list.insert(END, str(record[0]) + "  " + str(record[1])+ "  " +str(record[2]))
	cust_list.grid(row=2, column = 0, padx=(20,0), columnspan=5 , sticky=W)
	cust_sb.config(orient=VERTICAL, command=cust_list.yview)

	bar = Label(return_update, text = '----------------------------------------------------------------------------------------------')
	bar.grid(row = 4, columnspan=5 )

	#label CUTSOMER ID
	select_cust_id_label = Label(return_update, text = 'Customer ID: ')
	select_cust_id_label.grid(row = 3, column = 0, padx=(20,0), pady=(5,0), sticky=W)
	#textbox CUSTOMER ID
	select_cust_id = Entry(return_update, width = 51)
	select_cust_id.grid(row = 3, column = 1,columnspan=5 , padx=(0,20), pady=10, sticky=W)

	#label VEHICLE LIST
	search_vehicle_label = Label(return_update, text = 'VEHICLE LIST', font=12, fg="#0059CB")
	search_vehicle_label.grid(row = 5, columnspan=4, padx=10,pady=(10,5), sticky=N)
	#label SEARCH RESULT format
	format_vehicle_label = Label(return_update, text = 'Vehicle ID                                  Description                       Year', fg="#0059CB")
	format_vehicle_label.grid(row = 6, columnspan=16, padx=20, pady=0, sticky=W)

	#vehicle VIEW
	c.execute("SELECT * FROM VEHICLE")

	search_scroll = Scrollbar(return_update)
	search_scroll.grid(row=7, column = 6, padx=(0,20), ipady=23, sticky=W)

	#show output to terminal
	search_records = c.fetchall()

	search_list = Listbox(return_update, width=50, height=4, font='Courier', yscrollcommand=search_scroll.set)
	#loop thru results show all tupple
	for record in search_records:
		search_list.insert(END, str(record[0]) +"   "+ str(record[1]) +"   "+ str(record[2]))
	search_list.grid(row=7, column = 0, padx=(20,0), columnspan=5 , sticky=W)
	search_scroll.config(command=search_list.yview)

	barr = Label(return_update, text = '----------------------------------------------------------------------------------------------')
	barr.grid(row = 9, columnspan=5 )

	#label VEHICLE ID
	select_vehicleid_label = Label(return_update, text = 'Vehicle ID: ')
	select_vehicleid_label.grid(row = 8, column = 0, columnspan = 3, padx=(25,0), pady=5, sticky=W)
	#textbox VEHICLE ID
	select_vehicleid = Entry(return_update, width = 51)
	select_vehicleid.grid(row = 8, column = 1, columnspan = 3, padx=(0,20), pady=5, sticky=W)

	#label RENTAL LIST
	search_rental_label = Label(return_update, text = 'RENTAL LIST', font=12, fg="#004E03")
	search_rental_label.grid(row = 10, columnspan=4, padx=10, pady=(10,5), sticky=N)
	#label SEARCH RESULT format
	format_vr_label = Label(return_update, text = 'Customer ID        Vehicle ID                       Return Date      Payment Date', fg="#004E03")
	format_vr_label.grid(row = 11, columnspan=16, padx=20, pady=0, sticky=W)

	#vehicle VIEW
	c.execute("SELECT * FROM RENTAL")

	rental_sb = Scrollbar(return_update)
	rental_sb.grid(row=12, column = 6, padx=(0,20), ipady=23, sticky=W)

	#show output to terminal
	rental_records = c.fetchall()

	rental_list = Listbox(return_update, width=50, height=4, font='Courier', yscrollcommand=rental_sb.set)
	#loop thru results show all tupple
	for record in rental_records:
		rental_list.insert(END, str(record[0]) +"   "+ str(record[1]) +"   "+ str(record[6]) +"  "+ str(record[8]))
	rental_list.grid(row=12, column = 0, padx=(20,0), columnspan=5 , sticky=W)
	rental_sb.config(command=rental_list.yview)

	#label RENTAL LIST
	select_rental_label = Label(return_update, text = 'Return Date: ')
	select_rental_label.grid(row = 13, column = 0, columnspan = 3, padx=(25,0), pady=5, sticky=W)
	#textbox RENTAL LIST
	select_return_date = Entry(return_update, width = 51)
	select_return_date.grid(row = 13, column = 1, columnspan = 3, padx=(0,20), pady=5, sticky=W)

	#sVIEW RENTAL btn
	submit_return_btn = Button(return_update, text='View Rental', fg="white", bg="#004E03", command=rental_return)
	submit_return_btn.grid(row=14,  column=0,  columnspan = 5, pady=10, padx=(10,0), ipadx=50, sticky=N)

	#commit changes
	conn.commit()
	#close connection
	conn.close()

#add new view
def view():
	view_record = Tk()
	view_record.title('View Record')
	view_record.geometry("550x600")

	#create a database or connect to one
	conn = sqlite3.connect('car_rental_system.db')
	#create cursor
	c = conn.cursor()

	#label CUSTOMER LIST
	search_custid_label = Label(view_record, text = 'CUSTOMER LIST', font=12, fg="#290046")
	search_custid_label.grid(row = 0, columnspan=5, padx=10, pady=(10,5), sticky=EW)
	#label CHOOSE CUSTOMER description
	format_custid_label = Label(view_record, text = 'Customer ID   Name            Remain Balance', fg="#290046")
	format_custid_label.grid(row = 1, columnspan=16, padx=20, pady=(5,0), sticky=W)


	cust_sb = Scrollbar(view_record, orient=VERTICAL)
	cust_sb.grid(row=2, column = 6, columnspan=5, padx=(0,20), ipady=80, sticky=W)
	#insert into table
	c.execute("SELECT CUSTOMER.custID, CUSTOMER.name, RENTAL.totalAmount FROM CUSTOMER, RENTAL WHERE RENTAL.custID=CUSTOMER.custID AND RENTAL.paymentDate != 'NULL'")
	#show output to terminal
	cust_records = c.fetchall()

	cust_list = Listbox(view_record, width=50, height=10, font='Courier', highlightcolor="#290046",highlightthickness=2,yscrollcommand=cust_sb.set)
	for record in cust_records:
		cust_list.insert(END, str(record[0]) + "  " + str(record[1])+ "  " +str(record[2]))
	cust_list.grid(row=2, column = 0, padx=(20,0), columnspan=5 , sticky=W)
	cust_sb.config(orient=VERTICAL, command=cust_list.yview)

	bar = Label(view_record, text = '--------------------------------------------------------------------------------------------------------')
	bar.grid(row = 4)

	#label VEHICLE LIST
	search_vehicle_label = Label(view_record, text = 'VEHICLE LIST', font=12, fg="#0059CB")
	search_vehicle_label.grid(row = 5, columnspan=5, padx=10,pady=(10,5), sticky=EW)
	#label SEARCH RESULT format
	format_vehicle_label = Label(view_record, text = 'Vehicle ID                                  Description             Daily Price', fg="#0059CB")
	format_vehicle_label.grid(row = 6, columnspan=16, padx=20, pady=0, sticky=W)

	#vehicle VIEW
	c.execute("SELECT VEHICLE.vehicleID, VEHICLE.description, RATE.daily FROM VEHICLE, RATE WHERE VEHICLE.type=RATE.type AND VEHICLE.category=RATE.category")

	search_scroll = Scrollbar(view_record)
	search_scroll.grid(row=7, column = 6, columnspan=5, padx=(0,20), ipady=80, sticky=EW)

	#show output to terminal
	search_records = c.fetchall()

	search_list = Listbox(view_record, width=50, height=10, font='Courier', yscrollcommand=search_scroll.set)
	#loop thru results show all tupple
	for record in search_records:
		search_list.insert(END, str(record[0]) +"   "+ str(record[1]) +"   "+ str(record[2]))
	search_list.grid(row=7, column = 0, padx=(20,0), columnspan=5 , sticky=W)
	search_scroll.config(command=search_list.yview)


	#commit changes
	conn.commit()
	#close connection
	conn.close()

#create title label
home_label = Label(root, text = 'CAR RENTAL DATABASE', font='Arial 12 bold', fg="white", bg="#0B0058" )
home_label.grid(row = 0, pady=(20,10), sticky=N)

#create buttons
add_cust_btn = Button(root, text='Add Customer', font='Arial 11', command=customer)
add_cust_btn.grid(row=1, column=0, pady=(20,10), padx=23, ipadx=90)
add_vehicle_btn = Button(root, text='Add Vehicle', font='Arial 11', command=vehicle)
add_vehicle_btn.grid(row=2, column=0, pady=10, padx=23, ipadx=98)
add_rental_btn = Button(root, text='Add Rental', font='Arial 11', command=rental)
add_rental_btn.grid(row=3, column=0, pady=10, padx=23, ipadx=100)
add_return_btn = Button(root, text='Return Car', font='Arial 11', command=return_car)
add_return_btn.grid(row=4, column=0, pady=10, padx=23, ipadx=100)
add_view_btn = Button(root, text='View Record', font='Arial 11', command=view)
add_view_btn.grid(row=5, column=0, pady=10, padx=23, ipadx=94)

#commit changes
conn.commit()
#close connection
conn.close()
#executes my window
root.mainloop()