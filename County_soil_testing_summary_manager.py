import mysql.connector
import county_testsummary_into_database

class CountySoilTestingSummaryManager:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host="127.0.0.1",
            user="ombati",
            password="your_password",
            database="soilTest"
        )
        self.cursor = self.connection.cursor()

    def add_summary(self, county_id, total_farmers, avg_soil_quality_parameters, other_aggregated_data=None):
        try:
            query = "INSERT INTO CountySoilTestingSummary (CountyID, TotalFarmers, AverageSoilQualityParameters, OtherAggregatedData) VALUES (%s, %s, %s, %s)"
            values = (county_id, total_farmers, avg_soil_quality_parameters, other_aggregated_data)
            self.cursor.execute(query, values)
            self.connection.commit()
            print("Summary added successfully!")
        except mysql.connector.Error as error:
            print("Error adding summary:", error)

    def get_summary(self, county_id):
        try:
            query = "SELECT * FROM CountySoilTestingSummary WHERE CountyID = %s"
            self.cursor.execute(query, (county_id,))
            summary = self.cursor.fetchone()
            if summary:
                return summary
            else:
                print("Summary not found.")
                return None
        except mysql.connector.Error as error:
            print("Error fetching summary:", error)

    def update_summary(self, county_id, total_farmers=None, avg_soil_quality_parameters=None, other_aggregated_data=None):
        try:
            updates = []
            values = []
            if total_farmers is not None:
                updates.append("TotalFarmers = %s")
                values.append(total_farmers)
            if avg_soil_quality_parameters is not None:
                updates.append("AverageSoilQualityParameters = %s")
                values.append(avg_soil_quality_parameters)
            if other_aggregated_data is not None:
                updates.append("OtherAggregatedData = %s")
                values.append(other_aggregated_data)

            if not updates:
                print("No updates provided.")
                return

            query = "UPDATE CountySoilTestingSummary SET " + ", ".join(updates) + " WHERE CountyID = %s"
            values.append(county_id)
            self.cursor.execute(query, tuple(values))
            self.connection.commit()
            print("Summary updated successfully!")
        except mysql.connector.Error as error:
            print("Error updating summary:", error)

    def delete_summary(self, county_id):
        try:
            query = "DELETE FROM CountySoilTestingSummary WHERE CountyID = %s"
            self.cursor.execute(query, (county_id,))
            self.connection.commit()
            print("Summary deleted successfully!")
        except mysql.connector.Error as error:
            print("Error deleting summary:", error)

    def __del__(self):
        self.cursor.close()
        self.connection.close()

