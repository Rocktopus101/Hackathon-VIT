person1 = [["Milk" , "Eggs" , "Yoghurt" , "Butter"] , ["Milk" , "Cookies" , "Chips" , "Cheese"] , ["Oil" , "Milk" , "Bread" , "Eggs" , "Butter"] , ["Milk" , "Sugar"] , ["Chips" , "Milk" , "Eggs"]]
person2 = [["Bread" , "Milk" , "Yoghurt" , "Cookies" , "Cheese" , "Butter"] , ["Chips" , "Milk" ,  "Cheese" , "Butter" , "Bread"] , ["Bread" , "Cheese" , "Cookies" , "Butter"] , ["Chips" , "Cookies" , "Butter" , "Bread"] , ["Butter" , "Cookies" , "Milk" , "Bread"]]
recommended_list = set()

c=0
for i in range(len(person1)):
    for j in range(len(person1[i])):
        item = person1[i][j]
        for x in range(len(person1)):
            if (x>i) and (item in person1[x]):
                c = c + 1
                print(item)
        if c > 3:
            recommended_list.add(item)

'''c=0
for i in range(len(person2)):
    for j in range(len(person2[i])):
        item = person2[i][j]
        for x in range(len(person2)):
            if x!=i:
                if item in person1[x]:
                    c += 1
                    print(item)
        if c > 3:
            recommended_list.update(item)

'''
print(recommended_list)