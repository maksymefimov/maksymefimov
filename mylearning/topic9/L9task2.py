##Створіть словник, ключами якого є країни, а значеннями – список великих міст цієї країни
##На запит міста, що введений користувачем, програма повинна вивести країну, в якій воно
##знаходиться.
print()
counter = []
country = {"Germany":["Munchen","Berlin"],"Russia":["Moscow","Sochi"],\
           "Ukraine":["Kiyv","Harkyv"]}
print("Dictinary country: ",country)
country_inp = input("input the town of country: ")
for key in country:
    counter = country[key]
    if country_inp in counter:
        print("Country: ",key)
