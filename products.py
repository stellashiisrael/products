
#读取档案
products = []
with open ('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		name,price = line.strip().split(',')
		products.append([name, price])
print(products)


#重复输入购买过的东西
#while loop (不知道执行几次的情况下使用)
products = []


while True:
	name = input('请输入商品名称:')

	if name == 'q': #输入q，退出循环
		break
	price = input('请输入商品价格:')
	price = int(price)
	products.append([name, price]) #小清单里有2个元素，把两个元素一起放入大清单（二维清单）
print(products)

#products[0][0]
#products这个清单中，第一个集合里面，第一个位置的数据（清单数据第一个为0，第二个为1）
#products[1][1]，大清单中，第二个位置的第二个数据

for p in products:
	print(p[0], '的价格是',  p[1])
#products 是大清单，所以打印出大清单，就会把里面的东西全部一行展示出来
#p是小清单，所以会打印出小清单里的东西，自动换行显示

#写入/产生档案：
with open('products.csv', 'w', encoding ='utf-8' ) as f:#打开档案；写入模式；utf-8 解决中文乱码问题
#csv电脑储存资料常见的资料格式
#打开products这个文档，如果没有，就会产生这个档案，因为这是w模式。这个档案称为f
	f.write('商品,价格\n')#栏位名称
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')#写入
		#\n=分行

#字串的合并运算:   + 和*

#'abc' + '123' = 'abc123'
#'abc' * 3 = 'abcabcabc'
