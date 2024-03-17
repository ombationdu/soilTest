import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="ombati",
    password="your_password",
    database="soilTest"
)


cursor = connection.cursor()

create_soil_testing_table_query = """
CREATE TABLE IF NOT EXISTs SoilTesting (
    TestingRecordID INT AUTO_INCREMENT PRIMARY KEY,
    FarmerID INT,
    TestDate DATE,
    SoilQualityParameters VARCHAR(255),
    TestingResults TEXT,
    RelevantInformation TEXT,
    FOREIGN KEY (FarmerID) REFERENCES Farmers(FarmerID)
);
"""


cursor.execute(create_soil_testing_table_query)
connection.commit()


cursor.close()
connection.close()
