## Marissa Lee
## CSD310 
## Milestone 3
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "67ChickenFat!7", ##Don't judge my password
    "host": "localhost",
    "database": "Outland",
    "raise_on_warnings": True
}

#Creating MySQL connection
def create_connection():
    try:
        # Connecting to the MySQL server
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            return connection
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist.")
        else:
            print(f"Error: {err}")
        return None

# Function to query results
def execute_query(connection, query):
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(query)
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    finally:
        cursor.close()

#Get location booking numbers
def bookings_bylocation(connection):
    query = (
        "SELECT Location.LocationName, COUNT(Trips.LocationID) AS bookings " ##Using foreign key from trips table to see where the trips are booekd
        "FROM Trips "
        "JOIN Location ON Trips.LocationID = Location.LocationID "
        "WHERE Location.LocationName IN ('Africa', 'Asia', 'Europe') "
        "GROUP BY Location.LocationName;"
    )

    result = execute_query(connection, query)
    if result:
        for row in result:
            print(f"{row['LocationName']} bookings: {row['bookings']}")

#Get purchasing data
def enough_customers_buy_equipment(connection):
    query = """
        SELECT COUNT(DISTINCT Orders.CustomerID) AS purchasing_customers
        FROM Orders
        JOIN Equipment ON Orders.EquipmentID = Equipment.EquipmentID
        WHERE Equipment.EquipmentType = 'Purchase'; ##Only counting number of customers who purchase, not rent
    """
    result = execute_query(connection, query)
    if result:
        purchasing_customers = result[0]['purchasing_customers']
        print(f"Number of customers who have bought equipment: {purchasing_customers}")

 #Are there inventory items that are over five years old?
def old_inventory_items(connection):
    query = """
        SELECT Equipment.EquipmentName, Equipment.EquipmentAge
        FROM Equipment
        WHERE Equipment.EquipmentAge > 5; ##They only want info on equipment over 5 years old
    """
    result = execute_query(connection, query)
    if result:
        for row in result:
            print(f" Equipment over 5 years old: {row['EquipmentName']} is {row['EquipmentAge']} years old.")

   
# Main function to call the other functions
def main():
    connection = create_connection()
    if connection:
        bookings_bylocation(connection)
        enough_customers_buy_equipment(connection)
        old_inventory_items(connection)
        connection.close()
    else:
        print("Unable to connect to the database.")

main()
