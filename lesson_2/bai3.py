class Good:
    def inseft_good(self):
        self.ID = int(input('Enter goods ID: '))
        self.name = input('Enter goods name: ')
        self.price = float(input('Enter goods price: '))
        self.quantity = int(input('Enter goods quantity: '))

    def goods_info(self):
        return {
            'ID': self.ID,
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity
        }


amount_of_goods = int(input('Enter amount of goods: '))
total_price = 0

for i in range(amount_of_goods):
    good = Good()
    print(f"----------Good {i + 1}----------")
    good.inseft_good()
    total_price += good.price * good.quantity
    print(good.goods_info())

print(f"Total price: {total_price}")
