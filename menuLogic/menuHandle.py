from menuLogic.menu import afficher_menu
from colorama import Fore
from menuLogic.newGame import oui
from menuLogic.continueGame import keep_on
from menuLogic.options import show_options


def main(): 
    #choices = [1, 2, 3]




    afficher_menu()

    choice = input("Your choice --> ")

    while choice not in ["1", "2", "3"]:
        print(Fore.RED + "Please select a available option" + Fore.RESET)
        choice = input("Your choice --> ")

    if choice == "1":
        keep_on()
    
    if choice == "2":
        oui()
    
    if choice == "3":
        show_options()