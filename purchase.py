import json
f = open('record.json', 'r')
a = f.read()
f.close()
record = json.loads(a)
print(record)
try:
	f = open('sales.json', 'r')
	a = f.read()
	f.close()
	sales = json.loads(a)
	sId = len(sales) + 1
except:
	sales = {}
	sId = 1

pId = input('Enter the product ID: ')
pQty = int(input('Enter the quantity: '))

if pId not in record:
	print('Product not found')
else:
	p = record[pId]
	if p['qty'] < pQty:
		print('Not enough items on stock')
	else:
		price = (p['price'] - p['discount']) * pQty
		print('Product: ', p['name'])
		print('Price: ', p['price'])
		print('Total: ', price)
		record[pId]['qty'] -= pQty
		sales[sId] = {'name': p['name'], 'quantity': pQty, 'amount': price};
		a = json.dumps(record, indent = 2)
		f = open('record.json', 'w')
		f.write(a)
		f.close()
		a = json.dumps(sales, indent = 2)
		f = open('sales.json', 'w')
		f.write(a)
		f.close()
