# ------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# TQuintana, 2020-Feb-23, Modified #1, and #TODO Functionilating of loading data
# TQuintana, 2020-Feb-24, Modified #3 to print return
# ------------------------------------------#

# Declare variables

strChoice = ''  # User input
lstTbl = []  # list of lists to hold data
dict_row = {"id": '', "CD Title": "", "Artist": ""}  # list of data row (Changed to a Dict)
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n'
          '[a] Add CD\n'
          '[i] Display Current Inventory\n'
          '[d] delete CD from Inventory\n'
          '[s] Save Inventory to file\n'
          '[x] exit')

    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        print("Now Exiting...")
        break

    if strChoice == 'l':
        # TODO Add the functionality of loading existing data
        objFile = open(strFileName, 'r')

        keys = []
        values = []
        items = dict_row.items()
        for items in objFile:
            print("keys : ", str(keys))
            print("values : ", str(values))

        pass

    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dict_row = {"Id": intID, "CD Title": strTitle, "Artist": strArtist}
        lstTbl.append(dict_row)


    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(row, sep=" ")
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(",")
            dict_row ={"ID": int(lstRow[0]), "Title":lstRow[1],"Artist":lstRow[2]}
            lstTbl.append(dict_row)
            objFile.close()

    elif strChoice == 'd':
        del_choice = input("Input number you would like to delete")
        del_num = int(del_choice)
        if del_num in dict_row:
            del dict_row[del_num]
            print("\n Okay, its been deleted")
        else:
            print("\n That is not a valid choice. Goodbye")

        # TODO Add functionality of deleting an entry

        pass

    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            strRow = ''
            for item in row:
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()

    else:
        print('Please choose either l, a, i, d, s or x!')
