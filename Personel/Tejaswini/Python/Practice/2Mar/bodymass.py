
def Bodymass(h,w):
    print("\nYour body mass index is: ", round(w / (h * h), 2))

n=int(input("Enter the value of n"))
for i in range(n):
    print(f"\nFor Calculating Body Mass: {i+1}")
    h = float(input("Enter height in meters: "))  
    w = float(input("Enter weight in kilogram: "))
    Bodymass(h,w)