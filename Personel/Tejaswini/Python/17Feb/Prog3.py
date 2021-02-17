n1 = float(input("Enter the Side1:"))
n2 = float(input("Enter the Side2:"))
n3 = float(input("Enter the Side2:"))
semi= (n1 + n2 + n2) / 2           #Find Semi Perimeter
area = (semi * (semi - n1) * (semi - n2) * (semi - n3)) ** 0.5
print("Area Of Triangle=%0.2f"%area)