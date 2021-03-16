# Print anagrams together in Python using List and Dictionary 

def anagrams(words):  
      
    A = [''.join(sorted(word)) for word in words]

    dict = {}
    for i, e in enumerate(A):
        dict.setdefault(e, []).append(i)

    for index in dict.values():
        print([words[i] for i in index])


words = [
        "CARS", "REPAID", "DUES", "NOSE", "SIGNED", "LANE",
        "PAIRED", "ARCS", "GRAB", "USED", "ONES", "BRAG",
        "SUED", "LEAN", "SCAR", "DESIGN"]
 
anagrams(words)