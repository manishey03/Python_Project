# Import necessary Functions
from clean import clear_screen
from display import display
from read import read_data
from write import stock_change,purchase_bottom_bill,purchase_top_bill

bill = []

def purchase():
    while True:    
        display()  
        distributor_name = input("Enter distributor name: ")
        if distributor_name == '':
            print("Please enter distributor name and try again.")
        else:
            break

    clear_screen()
    data = read_data()
    purchase = True

    while purchase: 
              
        try:
            display()
            print("what you want to purchase?")
            user_input  = int(input('Please enter SN from above table to purchase: '))

            if user_input  == "":
                print("please enter any number from above table")
            elif  user_input  <= 0 or user_input  > 5:
                print("Please! Select valid number from 1 to 5")
            else:
                Quantity = int(input(f'How many {data[user_input ][1]} are you going to purchase at the moment?: '))                
                if Quantity <= 0:
                    print("Please try again, the quantity must be greater than 0 ")
                else:
                    print(f" {data[user_input ][1]}is succesfully purchased.")               
                    rate = int(data[user_input ][3].strip().strip("$"))
                    name = data[user_input ][1]
                    brand = data[user_input ][2]
                    total_Price = (rate*Quantity)            
                    bill.append([name, brand, total_Price, Quantity])
                    purchase_top_bill(distributor_name)
                    data[user_input ][4] = str(int(data[user_input ][4])+Quantity)
                    stock_change(data)                
                while True:
                    user_input = input(f"Would you like to purchase anything else? (Y/N): ").upper()
                    if user_input == "Y":
                        clear_screen()
                        break
                    elif user_input == "N":
                        clear_screen()
                        purchase = False
                        purchase_bottom_bill(bill,distributor_name)
                        break
                    else:
                        print("Please enter Y or N only.")
        except:
            print("you have entered wrong number")









