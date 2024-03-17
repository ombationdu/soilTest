import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="ombati",
    password="your_password",
    database="soilTest"
)

cursor = connection.cursor()

create_relationship_table_query = """
CREATE TABLE IF NOT EXISTS CountyFarmerRelationship (
    FarmerID INT,
    CountyID INT,
    RelationshipMetadata TEXT,
    FOREIGN KEY (FarmerID) REFERENCES Farmers(FarmerID),
    FOREIGN KEY (CountyID) REFERENCES Counties(CountyID),
    PRIMARY KEY (FarmerID, CountyID)
);
"""


cursor.execute(create_relationship_table_query)
connection.commit()
cursor.close()
connection.close()
