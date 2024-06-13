import mysql.connector

hostname = "85.215.139.196"
username = "dbeaver_user"
password = "1234"

try:
  # Connect to the MySQL server
  connection = mysql.connector.connect(
      host=hostname,
      user=username,
      password=password,
  )
  # Print a success message if connected
  print("Connection to MySQL server successful!")

except mysql.connector.Error as err:
  # Print an error message if connection fails
  print("Connection failed:", err)

