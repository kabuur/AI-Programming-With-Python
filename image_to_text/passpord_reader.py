import pytesseract 
from PIL import Image
image_path = "./2.jpeg"
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
img = Image.open(image_path)
result = pytesseract.image_to_string(img)
print (result)
result = result.replace('\n',"")
result = result.replace('/' , "")
list1 = result.split(" ")


last_num = list1[len(list1)-1]
# print(last_num)
last_result =""


if(last_num[0] !="P"):
    last_result = last_num[1:]
else:
    last_result = last_num
print(last_result)




def find_nationality(word):
    natinality = word[2:5]
    return natinality

print("Nationality is :",find_nationality(last_result))



def Find_surname(word):
    sur_name = ""
    count_less_then_symbol = 0
    for i in range(len(word)):
        if word[i] == "<":
            count_less_then_symbol += 1
            if count_less_then_symbol == 2:
                sur_name = word[5:i]
            
          
                


    return sur_name
print("SurName is :",Find_surname(last_result))



# hel = ("/Mother's" in list1)
# mother_name = list1.index("/Mother's")
# # if (len(list1[mother_name+1])):
# name = list1[mother_name+1]
# # print(name[6:])
# fridt_name = name.replace("Name", "")
# result_frist_name = fridt_name.replace("\n","")
# second_name = list1[mother_name+2]
# hel_last_name = list1[mother_name+3]
# last_name = hel_last_name[0:5]

# print(result_frist_name,second_name,last_name)

# print(list1[mother_name+2])




