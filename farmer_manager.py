import mysql.connector
import farmer_into_database

class FarmerManager:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host="127.0.0.1",
            user="ombati",
            password="your_password",
            database="soilTest"
        )
        self.cursor = self.connection.cursor()

    

    def add_farmer(self, name, address, contact_information, county_id):
        try:
            query = "INSERT INTO Farmers (Name, Address, ContactInformation, CountyID) VALUES (%s, %s, %s, %s)"
            values = (name, address, contact_information, county_id)
            self.cursor.execute(query, values)
            self.connection.commit()
            print("Farmer added successfully!")
        except mysql.connector.Error as error:
            print("Error adding farmer:", error)

    def get_farmer(self, farmer_id):
        try:
            query = "SELECT * FROM Farmers WHERE FarmerID = %s"
            self.cursor.execute(query, (farmer_id,))
            farmer = self.cursor.fetchone()
            if farmer:
                return farmer
            else:
                print("Farmer not found.")
                return None
        except mysql.connector.Error as error:
            print("Error fetching farmer:", error)

    def update_farmer(self, farmer_id, name=None, address=None, contact_information=None, county_id=None):
        try:
            updates = []
            values = []
            if name:
                updates.append("Name = %s")
                values.append(name)
            if address:
                updates.append("Address = %s")
                values.append(address)
            if contact_information:
                updates.append("ContactInformation = %s")
                values.append(contact_information)
            if county_id:
                updates.append("CountyID = %s")
                values.append(county_id)

            if not updates:
                print("No updates provided.")
                return

            query = "UPDATE Farmers SET " + ", ".join(updates) + " WHERE FarmerID = %s"
            values.append(farmer_id)
            self.cursor.execute(query, tuple(values))
            self.connection.commit()
            print("Farmer updated successfully!")
        except mysql.connector.Error as error:
            print("Error updating farmer:", error)

    def delete_farmer(self, farmer_id):
        try:
            query = "DELETE FROM Farmers WHERE FarmerID = %s"
            self.cursor.execute(query, (farmer_id,))
            self.connection.commit()
            print("Farmer deleted successfully!")
        except mysql.connector.Error as error:
            print("Error deleting farmer:", error)

    def __del__(self):
        self.cursor.close()
        self.connection.close()

# Example usage:
# Initialize FarmerManager with database connection details
# farmer_manager = FarmerManager(host="your_host", user="your_username", password="your_password", database="your_database")
# Add, retrieve, update, or delete farmers using the methods provided by FarmerManager
