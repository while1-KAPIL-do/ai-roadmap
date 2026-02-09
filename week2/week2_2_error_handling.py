try:
    number = int("abc")
    print(number)
except:
    print("Conversion failed!")


try:
    number = int("abc")
except ValueError:
    print("Invalid number format")


def safeDivide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Cannot divide by zero"
print(safeDivide(20,2))
print(safeDivide(2,0))


def getStock(product):
    try:
        return product['price']
    except KeyError:
        return False
myProduct = {
    "id"        : 1,
    "name"      : "Protine Powder",
    "price"     : 5400,
    "in_stock"  : True
}
myProduct2 = {}
print(getStock(myProduct))
print(getStock(myProduct2))