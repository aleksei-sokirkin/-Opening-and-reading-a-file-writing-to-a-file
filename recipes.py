import os

with open ('recipes.txt', 'r', encoding='utf8') as recipes:
    cook_book = {}
    for line in recipes:  
        food_name = line.strip()
        cook_book [food_name] = []
        products_count = recipes.readline()
        for i in range(int(products_count)):
            prod = recipes.readline().strip().split(' | ')
            ingredient_name, quantity, measure = prod
            recipe = {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure' : measure.split()}
            cook_book[food_name].append(recipe)
        recipes.readline()  
print(cook_book)


def get_shop_list_by_dishes(dishes, person_count: int):
    shoping_2 = {}
    for dish in dishes:
        if dish in cook_book:
            for consist in cook_book[dish]:
                if consist['ingredient_name'] in shoping_2:
                    shoping_2[consist['ingredient_name']]['quantity'] += int((consist['quantity']) * person_count)
                else:
                    shoping_2[consist['ingredient_name']] = {'measure': consist['measure'], 'quantity':  (int(consist['quantity'])) * person_count}
    print(shoping_2)
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)




cook_book2 = {}


for filename in os.listdir('texts'):
    with open (filename, encoding= 'utf-8') as text_files:
        text_files_list = text_files.readlines()
        number_lines = len(text_files_list)
        cook_book2[filename] = [number_lines, text_files_list]
sort_data = sorted(cook_book2.items(), key=lambda x: x[1])        
sorted_dict = dict(sort_data) 

with open ('unifacation.txt', 'w', encoding= 'utf-8') as new_file:
    text_list = []
    for key, value in sorted_dict.items():
        filename = key.strip()
        number_lines, text_files_list = value
        text_list.append(filename)
        text_list.append(number_lines)
        for text_files in text_files_list:
            text = text_files.strip()
            text_list.append(text)
    for i in text_list:
        new_file.write(f'\n{i}\n')
