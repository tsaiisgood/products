proudcts=[]

while True:
	name = input('請輸入商品名')
	if name == 'q':
		break
	price = input('請輸入商品價格')
	
	#p=[name,price]
	#p.append(name)
	#p.append(price)
	proudcts.append([name,price])

print(proudcts)