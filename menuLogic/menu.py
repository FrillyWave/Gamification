from colorama import Fore

def afficher_menu():
    print(Fore.GREEN + "Welcome" + Fore.RESET)
    print(Fore.BLUE + "Choose an option: " + Fore.RESET)
    print(Fore.WHITE + "1. Continue \n"
                       "2. New Game \n"
                       "3. Options" + Fore.RESET)