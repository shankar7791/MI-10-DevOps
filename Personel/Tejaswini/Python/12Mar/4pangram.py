#Python set to check string is pangram or not

def pangram(s):
    s = s.lower()
    s = set(s)
    char = [ch for ch in s if ord(ch) in range(ord('a'), ord('z')+1)]
    if len(char) == 26:
        print("String is Pangram")
    else:
        print("String is not Pamgram")

s = input("Enter string : ")
pangram(s)
