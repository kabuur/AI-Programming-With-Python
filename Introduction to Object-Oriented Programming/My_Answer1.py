


class Pants:
    def __init__(self, color, waist_size, length, price):     
        self.color = color
        self.waist_size = waist_size
        self.length = length
        self.price = price
    
    def change_price(self, new_price):

        self.price = new_price
    
    def discount(self, percentage):
   
        return self.price * (1 - percentage)


class  SalesPerson:
    def __init__(self,first_name,last_name,employee_id,salary,):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.salary = salary
        self.pants_sold = []
        self.total_sales = 0

    def sell_pants(self,pants_object):
        self.pants_sold.append(pants_object)
        return self.pants_sold
    
    def calculate_sales(self):
        total = 0
        for pants in self.pants_sold:
            total += pants.price
            
        self.total_sales = total
        
        return total
    

    def display_sales(self):
        for sales in self.pants_sold:
            print(f"Color: {sales.color} , Price : {sales.price}, waist_size : {sales.waist_size}, Lenght : {sales.length}")


    def calculate_commission(self, percentage):
        sales_total = self.calculate_sales()
       
        return sales_total * percentage 










def check_results():
    pants_one = Pants('red', 35, 36, 15.12)
    pants_two = Pants('blue', 40, 38, 24.12)
    pants_three = Pants('tan', 28, 30, 8.12)
    
    salesperson = SalesPerson('Amy', 'Gonzalez', 2581923, 40000)
    
    assert salesperson.first_name == 'Amy'
    assert salesperson.last_name == 'Gonzalez'
    assert salesperson.employee_id == 2581923
    assert salesperson.salary == 40000
    assert salesperson.pants_sold == []
    assert salesperson.total_sales == 0
    
    salesperson.sell_pants(pants_one)
    salesperson.pants_sold[0] == pants_one.color
    
    salesperson.sell_pants(pants_two)
    salesperson.sell_pants(pants_three)
    
    assert len(salesperson.pants_sold) == 3
    assert round(salesperson.calculate_sales(),2) == 47.36
    assert round(salesperson.calculate_commission(.1),2) == 4.74
    
    print('Great job, you made it to the end of the code checks!')
    
check_results()