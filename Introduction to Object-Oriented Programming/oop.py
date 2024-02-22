


class Shirt:
    def __init__(self,Shirt_color, shirt_size, shirt_style,shirt_price):
        self.color = Shirt_color
        self.size = shirt_size
        self.style = shirt_style
        self.price =shirt_price
    

    def change_price(self, new_price):
        self.price = new_price
    
    def change_color(self, new_color):
        self.color = new_color

    def change_size(self, new_size):
        self.size = new_size

    def change_style(self, new_style):
        self.style = new_style







new_shirt =  Shirt("black","m","short sveez",12)

print("old shirt price is ",new_shirt.price)
print("old shirt size is ",new_shirt.size)

new_shirt.change_price(16)
new_shirt.change_size("s")

print("changed shirt price is ", new_shirt.price)
print("changed shirt size is ",new_shirt.size)



