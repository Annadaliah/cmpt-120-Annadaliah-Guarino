from Product import Product

p1 = Product("Ultra range finder", 2.50, 4)
p2 = Product("Servo motor", 14.99, 10)
p3 = Product("Servo controller", 44.95, 5)
p4 = Product("Microcontroller Board", 34.95, 7)
p5 = Product("Laser Range Finder", 149.99, 2)
p6 = Product("lithium Polymer Battery", 8.99, 8)

products = [p1, p2, p3, p4, p5, p6]


def print_stock():
    print("\nAvailable Products")
    print("------------------")
    for i in range(0, len(products)):
        if products[i].getQuantity() > 0:
            print(str(i) + ")", products[i].getName(),
                  "$", products[i].getPrice())
        print()


def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        print_stock()
        vals = input(
            "Enter product ID and quanity you wish to buy: ").split(" ")
        if vals[0] == "quit":
            break

        prod_id = int(vals[0])
        count = int(vals[1])

        product = products[prod_id]

        if product.checkQuantity(count):
            if cash >= product.totalCost(count):
                cash -= product.totalCost(count)
                print("You purchased", count,
                      product.getName() + ".")
                print("You have $", "{0:.2f}".format(
                    cash), "remaining.")
            else:
                print("Sorry, you cannot afford that product.")
        else:
            print("Sorry, we are sold out of", product.getName())


main()
