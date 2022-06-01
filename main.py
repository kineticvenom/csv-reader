import csv

def available_for_adoption(user_input) :
    #print(user_input) 
    if user_input.__contains__("cats"):
        with open ('data/cats.csv', 'r' ) as cats_file:
            rows = csv.reader(cats_file, delimiter=',')
            title = next(rows)
            
            data = {}
            cats_list = []
            
            for row in rows:     
               
                data[title[0].replace(" ","")] = row[0]
                data[title[1].replace(" ","")] = row[1].replace(" ","")
                data[title[2].replace(" ","")] = row[2].replace(" ","")
                cats_list.append(f"{data['name']} is a {data['age']} year old {data['breed']}")
        return cats_list
    if user_input.__contains__("dogs") :
       with open ('data/dogs.csv', 'r' ) as dogs_file:
            rows = csv.reader(dogs_file, delimiter=',')
            title = next(rows)
            data = {}
            dogs_list = []
                    
            for row in rows:                  
                data[title[0].replace(" ","")] = row[0]
                data[title[1].replace(" ","")] = row[1].replace(" ","")
                data[title[2].replace(" ","")] = row[2].replace(" ","")
                dogs_list.append(f"{data['name']} is a {data['age']} year old {data['breed']}")
            return dogs_list
    else :
        return (f"Sorry we do not have any {user_input}")     

print(available_for_adoption("Do you have any cats"))
print(available_for_adoption("what dogs do you have"))
print(available_for_adoption("snakes"))

# print(data)
# for item in data:
#     print(item[0])