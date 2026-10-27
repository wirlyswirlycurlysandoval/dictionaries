from pyscript import document, display

#DICTIONARY
#UNIQUE KEYS; Values can have duplicates
#[0,1]is it indexed? Nah, but it is KEYED (use key to get value inside data)
#set1 = {'sample1': 'sample2'}
grades =  {"math":97,
           "science":90,
           "ss":91, 
           "p.e.":97 }
#dictionary is mutable
#adding of values - .add

del grades['p.e.'] #deletes key and value
#display(type(set1))
display(grades)

#dictionary = {key: value}

a = ["ab", "xy"]
display(dict(a))

keys = ["firstname", "lastname", "jerseynumber"]
values = ["Eldon", "Linsangan", "15"]

Brotherhood_member = dict(zip(keys, values))
display(Brotherhood_member)


squishy1 = {"Cheese":"Vaseline", "Watermelon": "Slushy", "Butter": "Crunchy", "Ball": "Coconut"}

display(len(squishy1))
display(squishy1.get("Cheese"))
display(squishy1["Butter"])