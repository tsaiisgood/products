products = []

# 從 CSV 檔案讀取商品
with open('products.csv', 'r', encoding='utf-8') as f:
    for line in f:
        if '商品,價格' in line:
            continue  # 跳過標題行
        name, price = line.strip().split(',')
        products.append([name, price])

print(products)

# 輸入新的商品
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
    price = int(price)
    products.append([name, price])

print(products)

# 印出所有商品及其價格
for p in products:
    print(p[0], '的價格是', p[1])

# 將更新的商品列表寫回 CSV 檔案
with open('products.csv', 'w', encoding='utf-8') as f:
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')
