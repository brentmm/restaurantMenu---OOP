class resturantMenu():
  #constructor
  def __init__(self, menuItem, menuDesc, glutenFree, menuPrice):
    self.menuItem = menuItem
    self.menuDesc = menuDesc
    self.glutenFree = glutenFree
    self.menuPrice = menuPrice
  
  #formats theMenu list
  def __str__(self):
    return ("\n\nItem:" + self.menuItem + "\nDescription: " +  self.menuDesc + "\nGluten Friendly: " + str(self.glutenFree) + "\nPrice: $" + str(self.menuPrice))

theMenu = []

#adds all menu items to a list
theMenu.append(resturantMenu("Bresaola and tuna pasta","Fresh egg pasta in a sauce made from bresaola and tuna", False, 10.99))
theMenu.append(resturantMenu("Mangosteen and ezekiel salad", "A crisp salad featuring fresh mangosteen and ezekiel", True, 12.99))
theMenu.append(resturantMenu("Egg and bacon soup", "Free range eggs and streaky bacon combined into creamy soup", False, 6.99))
theMenu.append(resturantMenu("Italian sausage and sweet dessert wine salad", "A crisp salad featuring italian sausage and sweet dessert wine", False, 8.25))
theMenu.append(resturantMenu("Lamb and plantain vindaloo", "Spicy vindaloo made with succulent lamb and fresh plantain" , False, 5.99))
theMenu.append(resturantMenu("Chickpea and celery soup", "Fresh chickpea and celery combined into creamy soup", False, 13.50))
theMenu.append(resturantMenu("Mandarine and cauliflower salad", "A crisp salad featuring fresh mandarine and cauliflower", True, 4.30))
theMenu.append(resturantMenu("Bresaola and opossum salad", "A crisp salad featuring bresaola and opossum", True, 5.20))
theMenu.append(resturantMenu("Mangetout and jalape stir fry", "Crunchy stir fry featuring fresh mangetout and jalape", False, 14.60))
theMenu.append(resturantMenu("Raspberry and haroset salad", "Salad with raspberries and herosets", True, 100.29))

#prints out list
for i in theMenu:
  print(i)

"""
Which approach did you find easier? Why?
  The approach without objects because I didnt have to learn how to use objects

Which approach takes the least amount of initial setup? Explain
  The attempt without objects used way less code to set it up. Because a for loop just iterated through the lists instead of having to append everything into a list.

Which approach would be more efficient if your menu had 100 items? Explain
  Definietly the code that uses objects because it then is basically a fill in the blank

In your own words, explain the difference, advantages and disadvantages of the object-oriented approach compared with the procedural approach.
  Differences would be that it is like a fill in the blank statment and that it is easier if you are trying to code using a certain format. Advantages are that it makes coding with many different items way easier since you are not typing every items statement. Disadvantages is that it, if you are only trying to code a few items then it can be very time consuming and over complicated than other methods. 

"""
