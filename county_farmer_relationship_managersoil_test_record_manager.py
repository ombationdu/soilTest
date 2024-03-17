import mysql.connector
import countyFarmer_into_database

class CountyFarmerRelationshipManager:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host="127.0.0.1",
            user="ombati",
            password="your_password",
            database="soilTest"
        )
        self.cursor = self.connection.cursor()

    def add_relationship(self, farmer_id, county_id, metadata=None):
        try:
            query = "INSERT INTO CountyFarmerRelationship (FarmerID, CountyID, RelationshipMetadata) VALUES (%s, %s, %s)"
            values = (farmer_id, county_id, metadata)
            self.cursor.execute(query, values)
            self.connection.commit()
            print("Relationship added successfully!")
        except mysql.connector.Error as error:
            print("Error adding relationship:", error)

    def get_relationship(self, farmer_id, county_id):
        try:
            query = "SELECT * FROM CountyFarmerRelationship WHERE FarmerID = %s AND CountyID = %s"
            self.cursor.execute(query, (farmer_id, county_id))
            relationship = self.cursor.fetchone()
            if relationship:
                return relationship
            else:
                print("Relationship not found.")
                return None
        except mysql.connector.Error as error:
            print("Error fetching relationship:", error)

    def update_relationship(self, farmer_id, county_id, metadata=None):
        try:
            query = "UPDATE CountyFarmerRelationship SET RelationshipMetadata = %s WHERE FarmerID = %s AND CountyID = %s"
            self.cursor.execute(query, (metadata, farmer_id, county_id))
            self.connection.commit()
            print("Relationship updated successfully!")
        except mysql.connector.Error as error:
            print("Error updating relationship:", error)

    def delete_relationship(self, farmer_id, county_id):
        try:
            query = "DELETE FROM CountyFarmerRelationship WHERE FarmerID = %s AND CountyID = %s"
            self.cursor.execute(query, (farmer_id, county_id))
            self.connection.commit()
            print("Relationship deleted successfully!")
        except mysql.connector.Error as error:
            print("Error deleting relationship:", error)

    def __del__(self):
        self.cursor.close()
        self.connection.close()

