import sqlite3

def createTable(connection):
    """Creates a table named inventory to save the data
    and the table is not created if it already exists
    
    Parameters
        connection: database connection object"""
    #Created a try-except block to manage a possible sqlite exception
    try:
        #This command will create a table named INVENTORY if the table does not exist in the database
        connection.execute('''CREATE TABLE if not exists INVENTORY (ID INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL, QUANTITY INT NOT NULL,PRICE REAL NOT NULL);''')
    except sqlite3.Error as e:
        print(e)

def addItem(connection):
    """Adds an item to the Inventory database

    Parameters:
        connection: database connection object """
    #Created a try-except block to manage a possible sqlite exception or a value error
    #in case the user does not type the correct data type.
    try:
        #Asks the user the ID, Name, Quantity and Price of the item to add in the database
        id = input("Please write the ID of the item: ")
        name = input("Please write the name of the item: ")
        quantity = input("Please write the initial quantity of the item: ")
        price = input("Please write the price of the item: ")
        
        #After asking the data, the function will execute an Insert query to add the item
        #to the database
        connection.execute(f"INSERT INTO INVENTORY (ID,NAME,QUANTITY,PRICE) \
        VALUES ({id}, '{name}', {quantity}, {price})")
        connection.commit()

        #If the operation is successfull the program will print this line
        print("Item added successfully")
    except sqlite3.Error as e:
        print(e)
    except ValueError as e:
        print(e)

def removeItem(connection):
    """Removes an item from the database where the ID
       is equal to the one provided by the user
       
       Parameters:
            connection: database connection object
            id: id to be deleted    """
    #Created a try-except block to manage a possible sqlite exception
    try:
        #Calls the displayItems function to show the user the current items in the database
        displayItems(connection)

        #Asks the user which item they would like to remove from the database
        id = input("Please select the ID of the item you would like to delete: ")

        #After getting the ID from the user the function will execute a delete query
        #and will delete the selected item from the database
        connection.execute(f"DELETE from INVENTORY where ID = {id}")
        connection.commit()
        #If the operation is successfull the program will print this line
        print("Item removed successfully")
    except sqlite3.Error as e:
        print(e)


def displayItems(connection):
    """Displays all the items in the Inventory table
    
    Parameters
        connection: database connection object"""
    #Created a try-except block to manage a possible sqlite exception
    try:
        #This function will create a cursor with the result of the Select From query
        #then it will use a for loop to show each item retrieved from the query
        cursor = connection.execute("SELECT ID,NAME,QUANTITY,PRICE from INVENTORY")
        for row in cursor:
            print(f"ID = {row[0]}, Name = {row[1]}, Quantity = {row[2]}, Price = ${row[3]:.2f}")
    except sqlite3.Error as e:
        print(e)

def sellItem(connection):
    """This function will reduce the quantity of the
    item selected in the database, and will show the 
    total amount of money made from the sale.
    
    Parameters
        connection: database connection object"""
    #Created a try-except block to manage a possible sqlite exception
    try:
        #Prints a blank line
        print()

        #Calls the displayItems function to show the current items to the user
        #so they can select which item they have sold.
        displayItems(connection)

        #Asks the user the ID of the item they sold
        id = input("Please write the ID of the item you would like to sell: ") 

        #The function will then execute a Select From Query to get the data of the item sold
        cursor = connection.execute(f"SELECT NAME, QUANTITY, PRICE from INVENTORY where ID = {id}")
        #The data function will save the data got from the query as an array
        data = cursor.fetchone()
        #The following 3 variables are created using the data from the query
        name = data[0]
        currentQuantity = int(data[1])
        price = float(data[2])

        #The function asks the user the amount of items they sold of the item selected
        quantityToSell = int(input("Please write the amount you would like to sell: "))

        #Then it calculates the revenue by multiplying the quantity to sell with the price
        revenue = float(quantityToSell * price)

        #The program then saves the new quantity in a new variable by substracting the currentQuantity
        #with the quantityToSell
        newQuantity = currentQuantity - quantityToSell

        #Then the function executes an update query to set the quantity in the database to the newQuantity
        connection.execute(f"UPDATE INVENTORY set QUANTITY = {newQuantity} where ID = {id}")
        connection.commit()

        #Finally if this is successful, the program will show the revenue got from the sale and the new quantity
        #of the item.
        print(f"You have earned ${revenue:.2f} for the sale and the new amount of {name} is now {newQuantity}")

    except sqlite3.Error as e:
        print(e)

def restockItem(connection):
    """This function will increase the quantity of the
    item selected in the database according to the ID
    selected by the user.
    
    Parameters
        connection: database connection object"""
    
    #Created a try-except block to manage a possible sqlite exception
    try:
        #Prints a blank line
        print()
        #Calls the displayItems function to show the current items to the user
        #so they can select which item they want to restock.
        displayItems(connection)

        #Asks the ID of the restocked item and the quantity of items restocked
        id = input("Please write the ID of the restocked item: ")
        quantityToAdd = int(input("Please write the quantity of items you restocked: "))

        #Creates a cursor with the data of the Select from query from the database
        cursor = connection.execute(f"SELECT QUANTITY from INVENTORY where ID = {id}")
        #Gets the quantity data of the cursor
        currentQuantity = int(cursor.fetchone()[0])

        #Adds the current quantity of the database with the quantity of items restocked
        newQuantity = currentQuantity + quantityToAdd

        #The function then executes an update query and updates the quanity to the new
        #quantity previously calculated
        connection.execute(f"UPDATE INVENTORY set QUANTITY = {newQuantity} where ID = {id}")
        connection.commit()
        #If the operation is successful this will print a message with the new quantity
        print(f"Operation done successfully the new quantity for the item is now {newQuantity}")

    except sqlite3.Error as e:
        print(e)

def main():
    #This is the main function of the program, this will show a
    #menu to the user and will use the functions according
    #to the user choice.

    #First we use sqlite3.connect function this 
    #will connect or create a database
    #named inventory if it does not exist
    try:   
        connection = sqlite3.connect('Inventory.db')
    except sqlite3.Error as e:
        print(e)
    
    #Then we call the createTable function, this will create a
    #table named Inventory if it does not exist   
    createTable(connection)

    print("Welcome to the Inventory Management System")
    menuOption = 0

    #This while loop shows a menu until the user selects the option
    #to exit the program, each menu option runs one of the functions created
    #above using the database connection object to query.
    while(menuOption != 6):
        print("What would you like to do?")
        print("1. Add an item")
        print("2. Delete an item")
        print("3. Display items")
        print("4. Sell an item")
        print("5. Restock an item")
        print("6. Exit")
        menuOption = int(input("Please select an option from the menu: "))

        if(menuOption == 1):
            addItem(connection)
        elif(menuOption == 2):
            removeItem(connection)
        elif(menuOption == 3):
            displayItems(connection)
        elif(menuOption == 4):
            sellItem(connection)
        elif(menuOption == 5):
            restockItem(connection)
        elif(menuOption > 6 or menuOption < 1):
            print("Please select a valid option")
    
    #Finally after the user exits the program, the connection with the database is closed
    connection.close()

main()
