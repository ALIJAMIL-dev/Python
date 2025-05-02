import sqlite3

connection = sqlite3.connect('D:/Python/Databasing/chinook.db')
cursor = connection.cursor()

sql = "INSERT INTO genres (Name) VALUES ('Amazing')"
cursor.execute(sql)
connection.commit()
# cursor.execute('SELECT * FROM customers where city="Oslo"')  # Corrected table name
# result = cursor.fetchall()

# for customer in result:
#     print(customer[1])


connection.close()
print("Database connection established successfully.")
