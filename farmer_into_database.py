import mysql.connector


connection = mysql.connector.connect(
    host="127.0.0.1",
    user="ombati",
    password="your_password",
    database="soilTest"
)

cursor = connection.cursor()


create_table_query = """
CREATE TABLE IF NOT EXISTS Farmers (
    FarmerID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    ContactInformation VARCHAR(100)
);
"""


cursor.execute(create_table_query)
connection.commit()
cursor.close()
connection.close()


