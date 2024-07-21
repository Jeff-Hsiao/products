products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	price = int(price)
	#p = []
	#p.append(name)
	#p.append(price)

	#p = [name, price]#等於Line7~9
	#products.append(p)

	products.append([name, price])#等於Line11~12
print(products)

print(products[0][0])

for p in products:
	print(p[0], '的價格是', p[1])

#with open('product.txt', 'w') as f:
with open('product.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')