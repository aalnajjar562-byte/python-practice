def item_price(item):
    if item == "x":
        price = 8.50

    elif item == "y":
        price = 4

    elif item == "z":
        price = 2

    else:
        price = 0

    return price


def main():
    print("x", "y", "z", sep="|")
    item = input("choose an item: ")
    price = item_price(item)
    if item != "x" and item != "z" and item != "y":
        print("unavilable")

    else:
        print(f"- {item} {price}$")
        print("ced")


main()
