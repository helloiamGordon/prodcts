prodcts = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q' :
		break
	price = input('請輸入商品價格: ')
	prodcts.append([name ,price])
print(prodcts)	

for p in prodcts:
	print(p[0], '的價格是',p[1])
with open ('products.txt', 'w') as f:
	for p in prodcts :
		f.write(p[0]+','+p[1]+'\n')