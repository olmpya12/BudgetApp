from typing import List


class Category:
    def __init__(self, name) -> None:
        self.name = name
        self.ledger = []
        
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        
    def withdraw(self, amount, description=""):
        
        if self.check_funds(amount):
            self.ledger.append({"amount": -1*(amount), "description": description})
            return True
        else:
            return False

    def get_balance(self):
        total = 0
        for a in self.ledger:
            total = total + a["amount"]
        return total
    def transfer(self,transfer_amount:int,target_category):
        
        if self.check_funds(transfer_amount):
            self.ledger.append({"amount": -1*transfer_amount, "description": f"Transfer to {target_category.name}"})
            target_category.ledger.append({"amount": transfer_amount, "description": f"Transfer from {self.name}"})
            return True
        else:
            return False
    def check_funds(self,amount):
        balance = self.get_balance()
        if balance >= amount:
            return True
        else:
            return False
    def __str__(self) -> str:
        len_name = len(self.name)
        l1 = int((30-len_name)/2)*"*"+self.name+int((30-len_name)/2)*"*"
        string = l1 + "\n"
        for a in self.ledger:
            amount = a["amount"]
            if len(a["description"])>=23:
                string = string + a["description"][:23] + " "
                amount_text = str(amount)
                if amount_text.find(".") == -1:
                    amount_text = amount_text + ".00"
                else:
                    if len(amount_text) == amount_text.find(".") + 2:
                        amount_text = amount_text + "0"
                string = string + amount_text +"\n"
            else:
                string = string + a["description"]
                string = string + (23-len(a["description"]))*" " + " "
                amount_text = str(amount)
                if amount_text.find(".") == -1:
                    amount_text = amount_text + ".00"
                else:
                    if len(amount_text) == amount_text.find(".") + 2:
                        amount_text = amount_text + "0"
                string = string + amount_text + "\n"
                
        string = string + f"Total: {self.get_balance()}"
        return string
                

def create_spend_chart(categories:List):
    balance = []
    percentage = []
    string = "Percentage spent by category\n"
    for i in categories:
        balance.append(900-(i.get_balance()))
    total_balence = sum(balance)
    for a in balance:
        percentage.append(round((a*100)/total_balence))
    count = [10,9,8,7,6,5,4,3,2,1,0]
    for i in count: 
        back = 1
        perc = str(i*10)
        if len(perc)<3:
            if len(perc)==1:
                string = string + "  "
            else:
                string = string + " "
        string = string + perc + "|"      
        index = 1
        for a in percentage:
            if a >= i*10:
                string = string + " o "    
            else:
                string = string + "   "
            if len(percentage) == index:
                    string = string + " "
            index = index + 1
        string = string + "\n"
    
    string = string + "    ----------\n"
    long_name = ""
    for a in categories:
        if len(a.name) > len(long_name):
            long_name = a.name
    for i in range(len(long_name)):
        string = string + "    "
        for a in categories:
            try:
                string = string + " " + a.name[i] + " "
            except:
                string = string + "   "
        if i == len(long_name):
            string = string + " "
        else:
            string = string + " \n"
    print(string)
    return string


food = Category("food")
entertainment = Category("entertainment")
business = Category("business")


food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

create_spend_chart([business,food,entertainment])

        
        



