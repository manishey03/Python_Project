import datetime
def stock_change(data):
    file = open("data.txt", "w")
    for i in range(1, len(data)):
        each = data[i]
        file.write(f"{each[1]},{each[2]},{each[3]},{each[4]},{each[5]},{each[6]}\n")
    file.close()

def sell_top_bill(Name):
    file = open("sell_" + Name + ".txt", "w")
    file.write("\t\t\t\tFASTECH\n")
    file.write("Pokhara -25  PHONE NO: 061-400009\n\n")
    file.write("Customer Name: " + Name)
    file.write(f"\nDate & Time: {datetime.datetime.now()}\n")
    file.write('------------------------------------------\n')
    file.close()

def sell_bottom_bill(Name,bill,Shipping_Charge):
        for s in bill:
            file = open("sell_" + Name + ".txt", "a+")
            file.write(f'Laptop Name: {s[0]}\n')
            file.write(f'Brand: {s[1]}\n')
            file.write(f'Net amount: {s[2]}\n')
            file.write(f'Total quantity: {s[3]}\n')
            file.write('------------------------------------------\n')
        total_Price = Shipping_Charge
        for item in bill:
               total_Price += int(item[2])
        final_price = total_Price - Shipping_Charge                  
        final_price = sum(int(_[2]) + Shipping_Charge for _ in bill)                      
        file.write(f"\n Total amount: {total_Price}\n Shipping cost: {Shipping_Charge}  \n Total cost: {final_price}")
        file.close()

def purchase_top_bill(distributor_name):
    file = open("purchased"+ distributor_name+".txt","w")
    file.write("\t\t\t\t\tFASTECH\n")
    file.write("Pokhara-25  PHONE NO: 061-400009\n\n")
    file.write("distributor name:"+distributor_name)
    file.write(f"\ndate & time: {datetime.datetime.now()}\n")
    file.write('------------------------------------------\n')
    file.close()

def purchase_bottom_bill(bill,distributor_name):
    for s in bill:
        file = open("purchased"+ distributor_name+".txt", "a+")
        file.write(f'Laptop Name: {s[0]}\n')
        file.write(f'Brand: {s[1]}\n')
        file.write(f'Net amount: {s[2]}\n')
        file.write(f'Total quantity: {s[3]}\n')
        file.write('------------------------------------------\n')
        file.close()
    money_without_vat = 0
    for i in bill:
        money_without_vat += int(i[2])
    vat_amount = money_without_vat* 0.13
    total_amount = money_without_vat + vat_amount
    file = open("purchased"+ distributor_name+".txt", "a+")
    file.write(f"Total amount without VAT: {money_without_vat}\n")
    file.write(f"VAT amount (13%): {vat_amount}\n")
    file.write(f"Total amount including VAT: {total_amount}\n")
    file.close()