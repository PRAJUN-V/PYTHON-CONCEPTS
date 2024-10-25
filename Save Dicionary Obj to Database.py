import sqlite3

user = {
    1: {
        'name': 'Prajun V',
        'age': 23,
        'place': 'Thalassery',
        'email': 'prajunvelandi@gmail.com'
    },
    2: {
        'name': 'Alex',
        'age': 24,
        'place': 'Kannur',
        'email': None
    },
}

# Creates or Opens a Database File:
#   If the file user.db exists in the same directory, it opens the existing database.
#   If the file does not exist, it creates a new SQLite database file named user.db.
connection = sqlite3.connect('user.db')

curser = connection.cursor() # To establish connection between database.
curser.execute(
    #  Write sql queries here.
    'CREATE TABLE IF NOT EXISTS user(id int primary key, name varchar(100) not null, age int not null, place varchar(100) not null, email varchar(100))'
)

# curser.execute("INSERT INTO user (id, name, age, place, email) values (1, 'anu', 23, 'Thalassey', 'anu@gmail.com')")

curser.execute("SELECT * FROM user")
rows = curser.fetchall()
print(rows)

connection.commit()  # Save the changes
connection.close() # Close the connection
