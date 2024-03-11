import psycopg2

# Connect to the PostgreSQL database
connection = psycopg2.connect(
    database="connect_with",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)
#
# cursor = connection.cursor()
#
# try:
#     # Execute SQL statements within the transaction
#     cursor.execute("delete from table1 where name = 'Alen'")
#
#     # Commit the transaction
#     connection.commit()
# except Exception as e:
#     # Rollback the transaction if an error occurs
#     connection.rollback()
#     print(f"Error: {e}")
# finally:
#     # Close the cursor
#     cursor.close()

cursor = connection.cursor()

# Execute a SELECT query
cursor.execute("SELECT * FROM table1")

# Fetch the results
results = cursor.fetchall()
print(results)

# Close the cursor
cursor.close()
