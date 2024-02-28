
StdId = input("enter Your ID:")
Name = input("enter Your Name:")
hall = input("enter Your Class:")
html = int(input("Enter HTML marks:"))
Python = int(input("Enter Python marks:"))
Math = int(input("Enter Math marks:"))
total = Python+Math+html
average = float(total/3)
print("\nID\tName\tClass\tPython\tHtml\tMath\tTotal\tAverage")
print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(StdId,Name,hall,Python,html,Math,total,average))