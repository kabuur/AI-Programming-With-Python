
Flower_dic  = {}

def get_flower ():

    with open("flower .txt",'r') as flower:
        for line in flower:
            word = line.strip()
            Flower_dic[word[0]] = word[3:]
            
    

get_flower()


def grt_frist_later ():

    full_name = input(str("Unique flower name with the first letter:"))

    for k ,v in Flower_dic.items():
    
        if k == full_name[0]:
            print(f"your name is {full_name} and flowr name is {v}")
            break

grt_frist_later ()