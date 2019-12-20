#重复输入购买过的东西
#while loop (不知道执行几次的情况下使用)

products = []


while True:
	name = input('请输入商品名称:')

	if name == 'q': #输入q，退出循环
		break
	price = input('请输入商品价格:')
	p = [name, price] #大清单里的小清单
	products.append(p) #小清单里有2个元素，把两个元素一起放入大清单（二维清单）
print(products)

#products[0][0]
#products这个清单中，第一个集合里面，第一个位置的数据（清单数据第一个为0，第二个为1）
#products[1][1]，大清单中，第二个位置的第二个数据