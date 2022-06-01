import csv

def available_for_adoption(user_input) :
    #print(user_input) 
    if user_input == "cats" :
        with open ('data/cats.csv', 'r' ) as cats_file:
            rows = csv.reader(cats_file, delimiter=',')
            title = next(rows)
            data = {}
            cats_list = []
            
            
            for row in rows:     
                data[title[0]] = row[0]
                data[title[1]] = row[1]
                data[title[2]] = row[2]
                cats_list.append(f"{data['name']} is a {data[' age']} year old {data[' breed']}")

            for cat in cats_list :        
                cat = cat.replace("  ", " ")
                cats_list.append(cat) 
        return cats_list
    elif user_input == "dogs" :
       with open ('data/dogs.csv', 'r' ) as dogs_file:
            rows = csv.reader(dogs_file, delimiter=',')
            title = next(rows)
            data = {}
            
            
            for row in rows:  
                
                data[title[0]] = row[0]
                data[title[1]] = row[1]
                data[title[2]] = row[2]
                print (f"{data['name']} is a {data[' age']} year old {data[' breed']}")
    else :
        return (f"Sorry we do not have any {user_input}")     

print(available_for_adoption("cats"))

# print(data)
# for item in data:
#     print(item[0])