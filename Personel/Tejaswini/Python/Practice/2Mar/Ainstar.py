def Alpha(n):
    for i in range(n): 
        for j in range((n // 2) + 1): 
            if ((j == 0 or j == n // 2) and i != 0 or     #for cecking first and last column
                i == 0 and j != 0 and j != n // 2 or      #for cheking first line
                i == n // 2):                             #for checking middle line
                print("*", end = "") 
            else:                                         #others lines making blank
                print(" ", end = "") 
        print()      

Alpha(10)