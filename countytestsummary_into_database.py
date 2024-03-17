import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="ombati",
    password="your_password",
    database="soilTest"
)

cursor = connection.cursor()

create_summary_table_query = """
CREATE TABLE IF NOT EXISTS CountySoilTestingSummary (
    CountyID INT,
    TotalFarmers INT,
    AverageSoilQualityParameters FLOAT,
    OtherAggregatedData TEXT,
    FOREIGN KEY (CountyID) REFERENCES Counties(CountyID),
    PRIMARY KEY (CountyID)
);
"""

cursor.execute(create_summary_table_query)
connection.commit()
cursor.close()
connection.close()
