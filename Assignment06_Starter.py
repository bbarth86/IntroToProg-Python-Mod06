# ------------------------------------------------------------------------ #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added code to complete assignment 5
# RRoot,1.1.2030,Fixed bug by clearing the list before it was refilled
# Beau Barth,11.12.2019,Modified code to complete assignment 6
# ------------------------------------------------------------------------ #

# Declare variables and constants
strFileName = "ToDoList.txt"  # The name of the data file
objFile = None  # An object that represents a file
lstTable = []  # A dictionary that acts as a 'table' of rows
strChoice = ""  # Capture the user option selection


class FileProcessor:  # includes functions for reading and writing the to-do list data to and from text file

    @staticmethod
    def ReadFileDataToList(file_name, list_of_rows):
        """
        Desc - Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) of tasks in data table, populated by rows in file
        :return (list) of tasks in data table
        """
        file = open(file_name, "r")
        for line in file:
            data = line.split(",")
            row = {"task": data[0].strip(), "priority": data[1].strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows

    @staticmethod
    def WriteListDataToFile(file_name, list_of_rows):
        """
        Desc - Writes data from a list of dictionary rows into a file

        :param list_of_rows: (list) containing dictionary rows:
        :param file_name: (string) with name of file:
        :return nothing
        """
        file = open(file_name, "w")
        for row in list_of_rows:  # use for loop to append each row found in table list to ToDoFile.txt
            file.write(row["task"] + "," + row["priority"] + "\n")
        file.close()

    @staticmethod
    def ReloadFileDataToList(file_name, list_of_rows):
        """
        Desc - Reads data from a file into a list of tasks, replacing any existing data in the list

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) of tasks in data table, populated by rows in file
        :return: (list) of tasks in data table
        """
        list_of_rows.clear()
        file = open(file_name, "r")
        for line in file:  # use for loop to append each row found in ToDoFile.txt to table list
            data = line.split(",")
            row = {"task": data[0].strip(), "priority": data[1].strip()}
            list_of_rows.append(row)
        file.close()
        print("Data successfully reloaded!")
        return list_of_rows


class IO:  # includes functions for add, remove and display of task data, as well as capturing user operation choice

    @staticmethod
    def OutputMenuItems():
        """
        Desc - Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Show current data
        2) Add a new item.
        3) Remove an existing item.
        4) Save Data to File
        5) Reload Data from File
        6) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def InputMenuChoice():
        """
        Desc - Gets the menu choice from a user

        :return: (string) user choice
        """
        choice = str(input("Which option would you like to perform? [1 to 6] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def ShowCurrentItemsInList(list_of_rows):
        """
        Desc - Shows the current tasks in the data table

        :param list_of_rows: (list) of tasks in data table you want to display
        :return: nothing
        """
        print("******* The current items ToDo are: *******")
        for row in list_of_rows:
            print(row["task"] + " (" + row["priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def AddNewItemInList(task, priority, list_of_rows):
        """
        Desc - Adds new task to current data table

        :param list_of_rows: (list) of tasks in data table to which new task will be appended
        :return: (list) of tasks in data table, including new task
        """
        dicrow = {"task": task, "priority": priority}  # assign task, priority values to new dictionary
        list_of_rows.append(dicrow)  # append new dictionary to list
        print("Task added successfully...\n")  # confirm addition
        return list_of_rows

    @staticmethod
    def RemoveItemFromList(task, list_of_rows):
        """
        Desc - Removes a task from the data table based on user input

        :param task: (string) identifying the queried task/item:
        :param list_of_rows: (list) containing dictionary rows:
        :return: list of rows in data table, updated following task removal
        """
        for item in list_of_rows:  # iterate over current list. for each item,
            if item["task"] == task:  # if value of task is equivalent to user input
                list_of_rows.remove(item)  # remove the item dictionary from list
                print("Task successfully removed...")  # confirm removal
        return list_of_rows


# When the program starts, load data from ToDoFile.txt.
FileProcessor.ReadFileDataToList(strFileName, lstTable)  # read file data

# Display a menu of choices to the user
while True:
    IO.OutputMenuItems()  # Shows menu
    strChoice = IO.InputMenuChoice()  # Get menu option

    # Run ShowCurrentItemsInList function if "Show Data" operation selected
    if strChoice.strip() == '1':
        IO.ShowCurrentItemsInList(lstTable)  # Show current data in the list/table
        continue  # to show the menu

    # Run AddNewItemInList function if "Add Item to List" operation selected
    elif strChoice.strip() == '2':

        strTask = str(input("What is the task? ")).strip()  # Get task from user
        strPriority = str(input("What is the priority? [high|low] ")).strip()  # Get priority from user
        IO.AddNewItemInList(strTask, strPriority, lstTable)  # Add task to Data table
        print()  # Add an extra line for looks
        IO.ShowCurrentItemsInList(lstTable)  # Show current data in the list/table
        continue  # to show the menu

    # Run RemoveItemInList function if "Remove Item in List" operation selected
    elif strChoice == '3':
        item_name = str(input("Enter a task to remove: ")).strip()  # Get task from user
        IO.RemoveItemFromList(item_name, lstTable)  # Remove task from Data table
        print()  # Add an extra line for looks
        IO.ShowCurrentItemsInList(lstTable)  # Show current data in the list/table
        continue  # to show the menu

    # Run WriteListDataToFile function if "Save to File" operation selected
    elif strChoice == '4':
        IO.ShowCurrentItemsInList(lstTable)  # Show current data in the list/table
        if "y" == str(input("Save this data to file? (y/n) - ")).strip().lower():  # Double-check with user
            FileProcessor.WriteListDataToFile(strFileName, lstTable)  # Save task data table to file
            input("Data saved to file! Press the [Enter] key to return to menu.")  # Confirm file save
        else:  # Let the user know the data was not saved
            input("New data was NOT Saved, but previous data still exists! Press the [Enter] key to return to menu.")
        continue  # to show the menu

    # Run ReloadFileDataToList function if "Reload Data from File" operation selected
    elif strChoice == '5':
        print("Warning: This will replace all unsaved changes. Data loss may occur!")  # Warn user of data loss
        strYesOrNo = input("Reload file data without saving? [y/n] - ")  # Double-check with user
        if strYesOrNo.lower() == 'y':
            FileProcessor.ReloadFileDataToList(strFileName, lstTable)  # Replace the current list data with file data
            IO.ShowCurrentItemsInList(lstTable)  # Show current data in the list/table
        else:
            input("File data was NOT reloaded! Press the [Enter] key to return to menu.")
            IO.ShowCurrentItemsInList(lstTable)  # Show current data in the list/table
        continue  # to show the menu

    # Break While Loop if "Exit Program" operation selected
    elif strChoice == '6':
        break  # and Exit

