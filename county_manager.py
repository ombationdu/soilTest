import mysql.connector
import county_into_database

class CountyManager:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host="127.0.0.1",
            user="ombati",
            password="your_password",
            database="soilTest"
        )
        self.cursor = self.connection.cursor()

    def add_county(self, county_name, relevant_information=None):
        try:
            query = "INSERT INTO Counties (CountyName, RelevantInformation) VALUES (%s, %s)"
            values = (county_name, relevant_information)
            self.cursor.execute(query, values)
            self.connection.commit()
            print("County added successfully!")
        except mysql.connector.Error as error:
            print("Error adding county:", error)

    def get_county(self, county_id):
        try:
            query = "SELECT * FROM Counties WHERE CountyID = %s"
            self.cursor.execute(query, (county_id,))
            county = self.cursor.fetchone()
            if county:
                return county
            else:
                print("County not found.")
                return None
        except mysql.connector.Error as error:
            print("Error fetching county:", error)

    def update_county(self, county_id, county_name=None, relevant_information=None):
        try:
            updates = []
            values = []
            if county_name:
                updates.append("CountyName = %s")
                values.append(county_name)
            if relevant_information:
                updates.append("RelevantInformation = %s")
                values.append(relevant_information)

            if not updates:
                print("No updates provided.")
                return

            query = "UPDATE Counties SET " + ", ".join(updates) + " WHERE CountyID = %s"
            values.append(county_id)
            self.cursor.execute(query, tuple(values))
            self.connection.commit()
            print("County updated successfully!")
        except mysql.connector.Error as error:
            print("Error updating county:", error)

    def delete_county(self, county_id):
        try:
            query = "DELETE FROM Counties WHERE CountyID = %s"
            self.cursor.execute(query, (county_id,))
            self.connection.commit()
            print("County deleted successfully!")
        except mysql.connector.Error as error:
            print("Error deleting county:", error)

    def __del__(self):
        self.cursor.close()
        self.connection.close()
