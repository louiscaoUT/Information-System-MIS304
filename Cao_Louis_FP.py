# Program header
# Author: Louis Cao, Ema Zoronjic
# Final Project
# November 27, 2022
#
# program stores and manages existing inventory, and allows customers to purchase or return
# bakery supplies

# import
import Inventory, TransactionItem

# constants
main_prompt = "Please input the item id you wish to purchase/return: "
finish_prompt = "Enter 0 when finished."
thank_you_prompt = "Thank you for visiting!"
quantity_prompt = "Please enter the desired quantity (negative quantity for return): "
input_error = "Input was invalid."
stock_error = "Sorry, we do not have enough stock."

# functions
def process_inventory(inFile):
    read = open(inFile, 'r')
    inventory_list = {}

    id = read.readline().strip()

    while id:
        
        inventory_list[int(id)] = Inventory.Inventory(int(id), read.readline().strip(), int(read.readline().strip()), float(read.readline().strip()))

        id = read.readline().strip()


    read.close()

    return inventory_list

        
def print_inventory(d):

    # heading
    print()
    print("ID\tItem\t\t\t Price\t\tStock")

    # body
    for i in d:
        print(d[i])

    # end 
    print()
    print(finish_prompt)
    print()


def get_item_id(d):

    while True:
        try:

            id = int(input(main_prompt))

            while id not in d and id != 0:
                print(input_error)
                print()
                id = int(input(main_prompt))

            return id

        except:
            print(input_error)
            print()
            
def qty_logic(id, inventory_dict, transaction_list):
    
    # quantity input
    print()
    qty = int(input(quantity_prompt))
    
    # purchase logic
    if qty > 0:
        if not(inventory_dict[id].purchase(qty)):
            print(stock_error)
        else:
            # adding transaction
            transaction = TransactionItem.TransactionItem()
            transaction.set_id(id)
            transaction.set_name(inventory_dict[id].get_name())
            transaction.set_qty(qty)
            transaction.set_price(inventory_dict[id].get_price())

            transaction_list.append(transaction)

    # restock logic
    else:
        if not(inventory_dict[id].restock(qty)):
            print(input_error)
        else:
            # adding transaction
            transaction = TransactionItem.TransactionItem()
            transaction.set_id(id)
            transaction.set_name(inventory_dict[id].get_name())
            transaction.set_qty(qty)
            transaction.set_price(inventory_dict[id].get_price())

            transaction_list.append(transaction)


def write_updated_inventory(outFile, d):

    output = open(outFile, 'w')

    for i in d:
        output.write(str(d[i].get_id()) + '\n')
        output.write(str(d[i].get_name()) + '\n')
        output.write(str(d[i].get_price()) + '\n')
        output.write(str(d[i].get_stock()) + '\n') 

    output.close()


def print_invoice(lis):

    # variables for output
    h1, h2, h3 = "Price:", "Tax:", "Total:"
    price = tax = total = 0


    # header
    print()
    print("ID\tItem\t\t\tQty\t Price\t\t\tTotal")

    # body
    for i in lis:
        price += float(i.calc_cost())
        print(i)

    # calculation
    tax = price * .085
    total = price + tax

    # formatting
    price = format(price, '.2f')
    tax = format(tax, '.2f')
    total = format(total, '.2f')

    # end 
    print()
    print(f"{h1:<6} ${price}", f"{h2:<6} ${tax}", f"{h3:<6} ${total}", sep = '\n')
    print()



def main():

    # transaction object
    transaction_list = []

    # display starting inventory 
    inventory_dict = process_inventory("Inventory.txt")
    print_inventory(inventory_dict)

    # program
    id = get_item_id(inventory_dict)

    while id:        
       # quantity logic
        qty_logic(id, inventory_dict, transaction_list)

        # display inventory after each trabsaction failed or valid
        print_inventory(inventory_dict)

        # getting another id
        id = get_item_id(inventory_dict)


    # output
    if not(transaction_list):
        print()
        print(thank_you_prompt)
        print()
    else:
        print_invoice(transaction_list)
        write_updated_inventory("UpdatedInventory.txt", inventory_dict)




if __name__ == "__main__":
    main()