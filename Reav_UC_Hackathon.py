import mysql.connector

# Establishing connection to MySQL server
cnx = mysql.connector.connect(user='ast', password='root', host='localhost')
mycursor = cnx.cursor()

# Getting the name for the new database from user input
''name = input("Enter the name for the database: ")

# Creating the database
mycursor.execute("CREATE DATABASE {}".format(name))
cnx.commit()

# Reconnect to the newly created database
'''
'''mycursor.execute("USE aon")'''

'''# Getting the number of columns for the new table from user input
column_count = int(input("Enter the number of columns for the table: "))

# Creating the table with user-defined columns and types
columns = []
for i in range(column_count):
    column_name = input("Enter name for column {}: ".format(i+1))
    column_type = input("Enter type for column {} (e.g., VARCHAR(255), INT, etc.): ".format(i+1))
    columns.append((column_name, column_type))

# Constructing the CREATE TABLE query
create_table_query = "CREATE TABLE {} (".format(name)
for column_name, column_type in columns:
    create_table_query = create_table_query + "{} {}, ".format(column_name, column_type)
create_table_query = create_table_query[:-2] + ")"  # Remove the last comma and space

# Debugging: print out the final query
print("CREATE TABLE query: ", create_table_query)

# Executing the CREATE TABLE query
mycursor.execute(create_table_query)'''

def where():
   # mycursor.execute("USE aon;")
    z = input("Enter the database in which to search: ")
    x = input("Enter the column in which to search: ")
    y = input("Enter the element to search: ")
    mycursor.execute("SELECT * FROM {} WHERE {} ={}".format(z, x,y))

# Closing cursor and connection
mycursor.close()
cnx.close()
