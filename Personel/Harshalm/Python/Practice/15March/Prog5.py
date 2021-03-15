#Remove all duplicates words from a given sentence


sents = input("Enter the sentence :-")
l = sents.split()
k = []
for i in l :
    if (sents.count(i) > 1 and (i not in k) or sents.count(i) == 1) :
        k.append(i)
print(" ".join(k))


