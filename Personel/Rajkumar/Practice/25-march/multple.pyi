class CementDealer:
    def getCementCost(self, quantity):
        return quantity * 300
 
class IronDealer:
    def getlronCost(self, quantity):
        return quantity * 4500
 
class Builder(CementDealer, IronDealer):
    def getTotalCost(self, cQ, iQ):
        c_cost = self.getCementCost(cQ)
        i_cost = self.getlronCost(iQ)
        totalCost = c_cost +i_cost
        return totalCost
 
cement = int(input("Enter Cement Quantity : "))
iron = int(input("Enter Iron Quantity : "))
 
b = Builder()
 
total_cost = b.getTotalCost(cement, iron)
print("TOTAL COST :", total_cost)