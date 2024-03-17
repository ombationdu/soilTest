import mysql.connector


connection = mysql.connector.connect(
    host="127.0.0.1",
    user="ombati",
    password="your_password",
    database="soilTest"
)


cursor = connection.cursor()

create_counties_table_query = """
CREATE TABLE IF NOT EXISTS Counties (
    CountyID INT AUTO_INCREMENT PRIMARY KEY,
    CountyName VARCHAR(100) NOT NULL,
    RelevantInformation TEXT
);
"""


cursor.execute(create_counties_table_query)
connection.commit()

cursor.close()
connection.close()
