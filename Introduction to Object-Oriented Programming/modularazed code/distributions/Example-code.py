# from GaussionDesterbution import Gaussian

from Binomialdistribution import Binomial

# gaussian_one = Gaussian(22, 2)
# print(gaussian_one.mean)

b = Binomial.read_data_file("numbers_binomial.txt")
# c = Binomial(9,4) 
# sum = b+c

# b = Binomial.read_data_file("numbers_binomial.txt")
print(b.calculate_mean())