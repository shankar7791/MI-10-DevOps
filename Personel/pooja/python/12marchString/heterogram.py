def heterogram(input):

    alphabets = [ch for ch in input if (
        ord(ch) >= ord('a') and ord(ch) <= ord('z'))]

    if len(set(alphabets)) == len(alphabets):
        print('Yes it is herogram')
    else:
        print('No it is not heterogram')


input = input("enter string ")
heterogram(input)
