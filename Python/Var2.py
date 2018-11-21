from Funcs import *

smth = [
    {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964,
        "owners": {
                "Bob",
                "Boba"
                  }
    },
    {
        "brand": "Mers",
        "model": "C500",
        "year": 2000,
        "owners": {
                "Bob",
                  }
    },
    {
        "brand": "Wolksvagen",
        "model": "Polo",
        "year": 2002,
        "owners": set()


    }
]




c=addOwner(smth,"Mers","Bodya")
d=addOwner(smth,"Mers","Sanya")
b=addOwner(smth,"Wolksvagen","Anton")
print(getBrand(smth))
print("====================================")
print(getNames_cars(smth))

for i in smth:
    for a in i:
        print(a,i[a])