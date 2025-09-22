#Dictionaries: 

car_info = { 
             "brand": "Tesla", 
             "model": "Model S", 
              "price": "1.5Cr", 
             "features": ["Autopilot", "Electric", "Sunroof"] 
            } 
car_info["color"] = "white"
print(car_info)
car_info["price"] = "1.7Cr"
print(car_info)
car_info["Insurance"] = {"provider": "HDFC", "valid_till": "2026"}
print(car_info)


#List of Dictionaries: 

books = [ {"title": "Atomic Habits", "author": "James Clear"}, 
          {"title": "Ikigai", "author": "Héctor García"}, 
          {"title": "Zero to One", "author": "Peter Thiel"} 
        ] 
new_book = {"title": "Deep Work", "author": "Cal Newport"}
books.append(new_book)
print(books)
for i in books:
   if i["author"] == "Peter Thiel":
      print(i["title"])

#Nested Dictionary Print: 

laptop = { 
"brand": "Apple", 
"specs": {"ram": "16GB", "storage": "1TB SSD", "chip": "M2"}, 
"price": "2L" 
       } 
print(laptop["specs"]["chip"])
print(f"{laptop["brand"]} laptop comes with {laptop["specs"]["chip"]} chip and costs {laptop["price"]}")


#� Challenge Tasks 
ott_data = [ 
{"platform": "Netflix", "shows": ["Stranger Things", "Wednesday"]}, 
{"platform": "Prime", "shows": ["Mirzapur", "Farzi"]}, 
{"platform": "Hotstar", "shows": ["Special Ops", "The Freelancer"]} 
]
print("all shows in ",Netflix)

 #Add a new show to Prime. 
for platform_data in ott_data:
    if platform_data["platform"]=="prime":
        platform_data["shows"].append("Kingdom")
        print(platform_data["shows"])

for platform_data in ott_data:
    if platform_data["platform"] == "Netflix":
        print(platform_data["shows"])
        break 





