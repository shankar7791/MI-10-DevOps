
class TeamMember(object):                   
   def __init__(self, name, uid): 
      self.name = name 
      self.uid = uid 
  

class Worker(object):                 
   def __init__(self, pay, jobtitle): 
      self.pay = pay 
      self.jobtitle = jobtitle 
  
class TeamLeader(TeamMember, Worker):         
    def __init__(self, name, uid, pay, jobtitle, exp): 
        self.exp = exp 
        TeamMember.__init__(self, name, uid) 
        Worker.__init__(self, pay, jobtitle)
    def Team(self):
        print("Name: {}, \nPay: {}, \nExp: {}".format(self.name, self.pay, self.exp))

TL = TeamLeader('Teju', 10001, 250000, 'Xanthrons', 1)
TL.Team()