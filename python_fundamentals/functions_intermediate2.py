x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
z = [ {'x': 10, 'y': 20} ]

def iterateDictionary(list):
    for student in list:
        names = ""
        for key,val in student.items():
            names += key + ' - ' + val + ', '
        print(names.rstrip(', '))

def iterateDictionary2(key, dicts):
    for dict in dicts:
        print(dict[key])

def iterateDictionary3(dict):
    for key,val in dict.items():
        print(len(val), key.upper())
        for item in val:
            print(item)
        print('\n')
        
iterateDictionary3(dojo)