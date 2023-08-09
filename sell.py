
from clean import clear_screen
from display import display
from read import read_data
from write import stock_change
from write import sell_top_bill,sell_bottom_bill
bill = []

def sell():
    while True:    
        display()  
        Name = input("Enter customer name: ")
        if Name == '':
            print("Please enter customer name and try again.")
        else:
            break
    clear_screen()
    data = read_data()
    sell = True

    while sell:         
        try:
            display()
            print("What would you like to sell?")
            user_input = int(input('Please enter SN from above table to sell: '))

            if user_input == "":
                print("Please enter any number from the table above.")        
            elif user_input <= 0 or user_input > 5:
                print("Please select a valid number from 1 to 5.")
            else:
                Quantity = int(input(f'How many {data[user_input][1]} would you like to sell?: '))
                if int(data[user_input][4]) < Quantity:
                    print("""
                              ▄▀▄ █ █ ▀█▀   ▄▀▄ █▀   ▄▀▀ ▀█▀ ▄▀▄ ▄▀▀ █▄▀
                              ▀▄▀ ▀▄█  █    ▀▄▀ █▀   ▄██  █  ▀▄▀ ▀▄▄ █ █
""")
                    continue
                elif Quantity == 0:
                    print("Please try again. The quantity must be greater than 0.")
                else:
                    print(f"{data[user_input][1]} has been successfully sold.")               
                    rate = int(data[user_input][3].strip().strip("$"))
                    name = data[user_input][1]
                    brand = data[user_input][2]
                    total_Price = rate * Quantity
                    bill.append([name, brand, total_Price, Quantity])
                    sell_top_bill(Name)
                    data[user_input ][4] = str(int(data[user_input ][4]) - Quantity)
                    stock_change(data) 
                while True:
                    user_input = input("Would you like to sell anything else? (Y/N): ").upper()

                    if user_input == "Y":
                        clear_screen()
                        break
                    elif user_input == "N":
                        clear_screen()
                        sell = False
                        Shipping_Charge = int(input(f'Please enter Shipping_charge: '))
                        sell_bottom_bill(Name,bill,Shipping_Charge)
                        break
                    else:
                        print("Please enter Y or N only.")
        except:
            print("only use string")

