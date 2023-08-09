# Import necessary functions from other files
from clean import clear_screen
from display import display
from purchase import purchase
from sell import sell

print("here")
# Define a function called main, which is the entry point of the program
def main():
    # Print a welcome message
    print("""
                ███████╗ █████╗ ███████╗████████╗███████╗ ██████╗██╗  ██╗
                ██╔════╝██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔════╝██║  ██║
                █████╗  ███████║███████╗   ██║   █████╗  ██║     ███████║
                ██╔══╝  ██╔══██║╚════██║   ██║   ██╔══╝  ██║     ██╔══██║
                ██║     ██║  ██║███████║   ██║   ███████╗╚██████╗██║  ██║
                ╚═╝     ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝
    """)

    # Start an infinite loop to keep the program running until the user chooses to exit
    while True:
        try:
            print("""
                    ---------------------------------------
                    |--------|----------------------------|
                    |Option | Description                 |
                    |--------|----------------------------|
                    |        |                            |
                    | 1      | Display Available Products |
                    |        |                            |
                    |--------|----------------------------|
                    |        |                            |
                    | 2      | Buy from Distributer       |
                    |        |                            |
                    |--------|----------------------------|
                    |        |                            |
                    | 3      | Sell to Customer           |
                    |        |                            |
                    |--------|----------------------------|
                    |        |                            |
                    | 999    | EXIT                       |
                    |        |                            |
                    |--------|----------------------------|
                    ---------------------------------------
            """)

            # Get the user's choice as an integer
            choice = int(input("Choose the options given in the screen:"))
            # Based on the user's choice, call the appropriate function from the imported modules
            if choice == 1:
                clear_screen()
                display()
            elif choice == 2:
                clear_screen()
                purchase()
            elif choice == 3:
                clear_screen()
                sell()
            elif choice == 999:
                clear_screen()
                # Print a message to indicate that the program is ending
                print("""                   
                            ░▄▀▀▒██▀▒██▀░░░▀▄▀░▄▀▄░█▒█░░░▄▀▀░▄▀▄░▄▀▄░█▄░█░█
                            ▒▄██░█▄▄░█▄▄▒░░▒█▒░▀▄▀░▀▄█▒░▒▄██░▀▄▀░▀▄▀░█▒▀█░▄
""")
                # Exit the program by breaking out of the infinite loop
                break
            else:
                clear_screen()
                print("Please select a number from given options")
        except ValueError:
            # Handle the case where the user inputs a non-integer value
            print("Please select a number from given options (except)")


# Call the main function to start the program
main()


