#!/usr/bin/env python3

items = []

#loops to get items found at the dog park
input_item = input('do you need to enter an item found at the dog park? Y/N:  ')
while True:
    if input_item.capitalize() == "Y":
        item = input('enter item')
        items.append(item)
    more = input("do you need to add more items? Y/N?")
    if more.capitalize() == 'N':
        print('Thank you have a good day!!!')
        break

# shows items found at the dog park
for item in items:
    print(f"{item} was found in the dog park")
