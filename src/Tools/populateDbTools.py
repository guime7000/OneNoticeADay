from dotenv import dotenv_values
import glob
import mysql.connector

# Getting COnfig environement variables
directoriesConfig = dotenv_values("../Config/.env.dir_config")

# Getting user and passwd for DB management
dbManagement = dotenv_values(directoriesConfig["DB_PASSWORD_FILE_PATH"])

dbUser = dbManagement["USER"]
dbPassword = dbManagement["PASSWORD"]

tableName = "numpy"

dbName = mysql.connector.connect(
    host="localhost", user=dbUser, password=dbPassword, database="onenotice"
)
cursor = dbName.cursor()
cursor.execute(
    f"CREATE TABLE IF NOT EXISTS {tableName} (id INT NOT NULL AUTO_INCREMENT, filename VARCHAR(255) NOT NULL, PRIMARY KEY (id)) ENGINE=InnoDB DEFAULT CHARSET=utf8;"
)

filePattern = directoriesConfig["PROCESSED_FILES_DIRECTORY_SAVE"] + "*.html"
for idx, file in enumerate(glob.glob(filePattern)):
    cursor.execute(
        f"INSERT INTO {tableName}(id, filename) VALUES (%s, %s)", (idx + 1, file)
    )
dbName.commit()
