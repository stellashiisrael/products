#重复输入购买过的东西
#while loop (不知道执行几次的情况下使用)

products = []


while True:
	name = input('请输入商品名称:')

	if name == 'q': #输入q，退出循环
		break
	price = input('请输入商品价格:')
	p = [] #大清单里的小清单
	p.append(name)
	p.append(price)
	products.append(p) #小清单里有2个元素，把两个元素一起放入大清单
print(products)