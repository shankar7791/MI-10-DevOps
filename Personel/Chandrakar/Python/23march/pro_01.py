class reverse:
   def rev_sentence(self,sentence):
      words = sentence.split(' ')
      reverse_sentence = ' '.join(reversed(words))  
      print("after the reverce string are : ",reverse_sentence)  
c=reverse()
a = "hello my name is dev"
print("Befor the reverce string are : ",a)
c.rev_sentence(a)