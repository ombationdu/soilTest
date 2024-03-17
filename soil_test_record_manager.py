import mysql.connector
import soilTest_into_database

class SoilTestingRecordManager:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host="127.0.0.1",
            user="ombati",
            password="your_password",
            database="soilTest"
        )
        self.cursor = self.connection.cursor()

    def add_soil_testing_record(self, farmer_id, test_date, soil_quality_parameters, testing_results, relevant_information=None):
        try:
            query = "INSERT INTO SoilTesting (FarmerID, TestDate, SoilQualityParameters, TestingResults, RelevantInformation) VALUES (%s, %s, %s, %s, %s)"
            values = (farmer_id, test_date, soil_quality_parameters, testing_results, relevant_information)
            self.cursor.execute(query, values)
            self.connection.commit()
            print("Soil testing record added successfully!")
        except mysql.connector.Error as error:
            print("Error adding soil testing record:", error)

    def get_soil_testing_record(self, record_id):
        try:
            query = "SELECT * FROM SoilTesting WHERE TestingRecordID = %s"
            self.cursor.execute(query, (record_id,))
            record = self.cursor.fetchone()
            if record:
                return record
            else:
                print("Soil testing record not found.")
                return None
        except mysql.connector.Error as error:
            print("Error fetching soil testing record:", error)

    def update_soil_testing_record(self, record_id, farmer_id=None, test_date=None, soil_quality_parameters=None, testing_results=None, relevant_information=None):
        try:
            updates = []
            values = []
            if farmer_id:
                updates.append("FarmerID = %s")
                values.append(farmer_id)
            if test_date:
                updates.append("TestDate = %s")
                values.append(test_date)
            if soil_quality_parameters:
                updates.append("SoilQualityParameters = %s")
                values.append(soil_quality_parameters)
            if testing_results:
                updates.append("TestingResults = %s")
                values.append(testing_results)
            if relevant_information:
                updates.append("RelevantInformation = %s")
                values.append(relevant_information)

            if not updates:
                print("No updates provided.")
                return

            query = "UPDATE SoilTesting SET " + ", ".join(updates) + " WHERE TestingRecordID = %s"
            values.append(record_id)
            self.cursor.execute(query, tuple(values))
            self.connection.commit()
            print("Soil testing record updated successfully!")
        except mysql.connector.Error as error:
            print("Error updating soil testing record:", error)

    def delete_soil_testing_record(self, record_id):
        try:
            query = "DELETE FROM SoilTesting WHERE TestingRecordID = %s"
            self.cursor.execute(query, (record_id,))
            self.connection.commit()
            print("Soil testing record deleted successfully!")
        except mysql.connector.Error as error:
            print("Error deleting soil testing record:", error)

    def __del__(self):
        self.cursor.close()
        self.connection.close()
