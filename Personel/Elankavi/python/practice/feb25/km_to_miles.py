c=int(input("""To covert : 
1)Kilometer to miles
2)Miles to kilometer
choose 1 or 2 :"""))
if(c == 1):
    km=float(input("Enter your kilometer : "))
    m=(km/8)*5
    print(f"The {km} kilometer is equal to {m} miles ")
else:
    m=float(input("ENter your miles : "))
    km=(m/5)*8
    print(f"The {m} miles is equal to {km} kilometers")