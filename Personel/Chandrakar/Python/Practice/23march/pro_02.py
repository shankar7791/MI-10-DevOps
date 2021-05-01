#reverce string are upper case
class reverse:
   def rev_sentence(self,sentence):
      words = sentence.split(' ')
      reverse_sentence = ' '.join(reversed(words))  
      print("after the reverce string in upper case are : ",reverse_sentence.upper())  
c=reverse()
a = "hello my name is dev"
print("Befor the reverce string are : ",a)
c.rev_sentence(a)