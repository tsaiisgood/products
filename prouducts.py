proudcts=[]

while True:
	name = input('請輸入商品名')
	if name == 'q':
		break
	price = input('請輸入商品價格')

	price= int(price)
	
	#p=[name,price]
	#p.append(name)
	#p.append(price)
	proudcts.append([name,price])

print(proudcts)

for p in proudcts:
	print(p[0],'的價格是',p[1])

with open('products.csv','w',encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in proudcts:
		f.write(p[0] + ',' + str(p[1]) + '\n')