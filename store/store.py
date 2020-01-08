""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    in_menu =  True

    while in_menu:
        ui.print_menu("Store", ["Show Table", "Add", "Remove", "Update", "Get Counts By Manufacturers", "Get Average By Manufacturer"], "Back to Main Menu")
        number_of_menu_options = 6
        user_input = ui.get_input_menu(number_of_menu_options-1) #asks user to select numbered option from the menu
        if user_input == 1:
            show_table(data_manager.get_table_from_file("store/games.csv"))
        elif user_input == 2:
            add(table)
        elif user_input == 3:
            remove(table, id)
        elif user_input == 4:
            update(table, id)
        elif user_input == 5:
            get_counts_by_manufacturers(table, id)
        elif user_input == 6:
            get_average_by_manufacturer(table, id)
        elif user_input == 0:
            in_menu = False #dopóki jest w menu i prosi o input, dopóty nie dostanie 0 pętla się powtarza a jak się przerwie, user wychodzi itd. 
    
    main.main() #exit to the main menu


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    title_list = ["Id", "Title", "Manufacturer", "Price", "In Stock"]
    ui.print_table(table, title_list) #z UI tabelka


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    # your code

    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    # your code

    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    # your code

    return table


# special functions:
# ------------------

def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """

    # your code


def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """

    # your code
