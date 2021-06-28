groceries = {"chicken": 1.59 , "beef": 1.99, "cheese": 1.00, "milk": 2.50 }

def total_price(item1,item2):
    total=groceries[item1]+groceries[item2]
    print("The total price of "+ item1 " and " + item2 " is " + total ".")

def price_difference(item1,item2):
    diff=groceries[item1]-groceries[item2]
    print("“The difference between " + item1 " and " + item2 " is " + diff + ".")
# step V
def All(food):
    groceries[food].clear

shoe = {"Jordon 13": 1, "Yeezy": 8, "Foamposite": 10, "Air Max": 5, "SB Dunk": 20}

def restock(item,multiplier):
    times=shoe[item]*multiplier
    shoe[item]=times
    return shoe

def clearence(item,divider):
    amount=shoe[item]/divider
    shoe[item]=amount
    return shoe















Menu = {"Fried Chicken": 5.99, "Fries": 2.99, "Soda": 1.99}
def foodSum(item1,item2):
    sum - item1 + item2
    print("The total price of your order of " + item1 +"and" + item2 + "is" + str(sum))

foodSum("Fried Chicken", "Fries")

listPlayers = [1,2,3,4,5,6,7]
for i in range(length):
    length = len(listPlayers)
    randomNumber = rand.randint(0,length-1)
    listPlayers.pop(randomNumber)
    print(listPlayers)
 

listNumbers = []
size = 5
for i in range(size):
    listNumbers.append(10*np.random.random())



