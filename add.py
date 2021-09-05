import json
f = open('record.json', 'r')
a = f.read()
f.close()
record = json.loads(a)

pId = input('Product ID: ')
pName = input('Name: ')
pType = input('Type: ')
pRating = int(input('Rating: '))
pPrice = int(input('Price: '))
pQty = int(input('Quantity: '))
pDiscount = int(input('Discount: '))
record[pId] = {'name': pName, 'type': pType, 'rating': pRating, 'price': pPrice, 'qty': pQty, 'discount': pDiscount}

a = json.dumps(record, indent = 2)
f = open('record.json', 'w')
f.write(a)
f.close()
