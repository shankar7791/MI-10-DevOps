    
    
    
with open('/home/meerhasan/MI-10-DevOps/Personel/Meerhasan/Project/test.txt') as f: 
    print(sum(1 for c in f.read() if c.isupper())) 