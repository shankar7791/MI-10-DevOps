
def main():

   virus = input()
   nu_of_people = int(input())
   user_list = []
   for x in range(nu_of_people):
       user_list.append(input())
   for x in range(nu_of_people):
       print(check_sample(virus, user_list[x]))

def check_sample(virus, blood):
   m = len(virus)
   n = len(blood)
   i = j = 0
   while i < n and j < m:
       if blood[i] == virus[j]:
           i = i + 1
       j = j + 1
   if (n==i):
       return "POSITIVE"
   else:
       return "NEGATIVE"
main()

