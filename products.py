import os #operating system

#讀取檔案
def read_file(filename):
    products = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue #繼續跳到下一回
            #s = line.strip().split(',')#先去掉換行符號、再用逗號分割
            #name = s[0]
            #price = s[1]
            #print(s)
            name, price = line.strip().split(',')
            products.append([name,price])
    return products    

#讓使用者輸入
def user_input(products):
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
    return products

#印出所有商品
def print_products(products):
    for p in products:
        print(p[0], '的價格是', p[1])

#寫入檔案
def write_file(filename, products):
    #with open('product.txt', 'w') as f:
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
    filename = 'product.csv'
    if os.path.isfile(filename): # 檢查檔案在不在
        print('找到檔案了!')
        products = read_file(filename)
    else:
        print('找不到檔案...')

    products = user_input(products)
    print_products(products)
    write_file('product.csv', products)

main()