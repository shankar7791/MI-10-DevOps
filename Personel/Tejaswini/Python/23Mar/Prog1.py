#Write a Python class to reverse a string word by word.
#Input string : 'hello my name is dev'
#Expected Output : '.dev is name my hello'

def rev_sentence(sentence):  
  
    # first split the string into words  
    words = sentence.split(' ')  
  
    # then reverse the split string list and join using space  
    reverse_sentence = ' '.join(reversed(words))  
  
    # finally return the joined string  
    return reverse_sentence  
  
if __name__ == "__main__":  
    inp = input("Enter sentence: ")
    print (f".{rev_sentence(inp)}") 