#Lists

players = ["Rohit", "Virat", "Gill", "Dhoni"]
players[2]="surya"
players.append("jadeja")
print(players)
print(len(players))
print(f"the second last player is {players[-2]}")

#Tuples

Laptop_info = ("HP", "16GB", "512GB SSD", 2024, True) 
Laptop_info[0] = "Dell"
#we can't change the values once we assign in the tuple
print(Laptop_info)

elements=Laptop_info[-2:]
print(f"Last two elements (slicing): {elements}")


#Sets

Countries = {"India", "USA", "India", "Canada", "UK", "USA"} 
print(Countries)
#In this set the duplicate is India and USA because they are repeating
Countries.add("Germany")
print(Countries)
Countries.discard("UK")
print(Countries)

#Frozen

Frozen_marks = frozenset([90, 85, 75, 85]) 
Frozen_marks = frozenset.add(65)
Frozen_marks = frozenset.remove(85)
#it was raising an error because frozen don't have attributs like add (or) remove
print(type(Frozen_marks))
print(Frozen_marks)


