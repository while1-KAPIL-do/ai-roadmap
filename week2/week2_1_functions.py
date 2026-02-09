def greet():
    print("Hello, welcome to Week 2")
greet()


def sayHi(name):
    print("Hi", name)
sayHi("kapil")
sayHi("AI Engineer")


def add(a, b):
    return a+b
print(add(10, 20))


def isEven(num):
    return num % 2 == 0
print(isEven(21))


def checkStock(in_stock = False):
    return in_stock
print(checkStock())
print(checkStock(True))

def getPrice(product):
    return product.get("price", "unknown")

myProduct = {
    "id"        : 1,
    "name"      : "Protine Powder",
    "price"     : 5400,
    "in_stock"  : True
}
myProduct2 = {}
print(getPrice(myProduct))
print(getPrice(myProduct2))