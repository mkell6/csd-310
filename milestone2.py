## Marissa Lee
## Milestone 2
## Outland 
## Dec 03, 2023

import mysql.connector
from mysql.connector import errorcode


config = {
    "user": "root",
    "password":"pass",
    "host": "localhost",
    "database": "Outland",
    "raise_on_warnings": True
}

try:
    # Connecting to the MySQL server
    connection = mysql.connector.connect(**config)

    if connection.is_connected():
        cursor = connection.cursor()

        
        department_query = "SELECT * FROM Department" ## repeating for each table
        cursor.execute(department_query)

        print("\nDepartment Table:")
        for row in cursor.fetchall():
            print(row)

       
        employee_query = "SELECT * FROM Employee"
        cursor.execute(employee_query)

        print("\nEmployee Table:")
        for row in cursor.fetchall():
            print(row)

        customer_query = "SELECT * FROM Customer"
        cursor.execute(customer_query)

        print("\nCustomer Table:")
        for row in cursor.fetchall():
            print(row)

        orders_query = "SELECT * FROM Orders"
        cursor.execute(orders_query)

        print("\nOrders Table:")
        for row in cursor.fetchall():
            print(row)

        trips_query = "SELECT * FROM Trips"
        cursor.execute(trips_query)

        print("\nTrips Table:")
        for row in cursor.fetchall():
            print(row)


        guide_query = "SELECT * FROM Guide"
        cursor.execute(guide_query)

        print("\nGuide Table:")
        for row in cursor.fetchall():
            print(row)

        location_query = "SELECT * FROM Location"
        cursor.execute(location_query)

        print("\nLocation Table:")
        for row in cursor.fetchall():
            print(row)

        equipment_query = "SELECT * FROM Equipment"
        cursor.execute(equipment_query)

        print("\nEquipment Table:")
        for row in cursor.fetchall():
            print(row)
        
        cursor.close()
        connection.close() ##close connection

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)
