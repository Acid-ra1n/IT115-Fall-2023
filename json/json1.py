# Import json module
import json
#Create data dictionary
data = {
    # Key and value pairs, key is left of colon and value is right of colon
    'name': 'John Doe', 
    'age': 30,
    'city':'New York, NY',
    # string:list values
    'interests': ['sleep', 'green', 'food'],
    # string:boolean values
    'is_student' : True
}

# Create a json file and write inside 
with open('data.json', 'w') as json_file: 
    # Passing array data into json file, file indentation is 4 spaces
    json.dump(data,json_file,indent=4)

# Confirming code works
print('Data has been written to data.json')


# Open json file to read from it
with open('data.json', 'r') as json_file:

    # Create a loaded data object that loads the file
    loaded_data = json.load(json_file)

# Confirming code works
print('Successfully able to read data.json')
# Prints data array from data json file
print(loaded_data)


# Change value of age in dictionary
loaded_data['age'] = 34
# Add item to end of list interests in dictionary
loaded_data['interests'].append('nature')

# Open json file and write in file
with open('data.json', 'w') as json_file:

    # Passing updated object into json file, file indentation is 4 spaces
    json.dump(loaded_data, json_file, indent=4)

# Confirming code works
print('Modified data written to data.json')