class Regtangle:
    def insest_value(self):
        self.width = int(input('Enter width: '))
        self.height = int(input('Enter height: '))

    def draw(self):
        for i in range(self.height):
            print('*' * self.width)

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2


regtangle = Regtangle()
regtangle.insest_value()

regtangle.draw()

print(regtangle.area())
print(regtangle.perimeter())
