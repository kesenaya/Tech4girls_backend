# Define a tuple containing 5 different elements
my_tuple = (42, 3.14, 'Hello', True, 'World')

# Print the first and last elements of the tuple using indexing
first_element = my_tuple[0]
last_element = my_tuple[-1]

print("First element:", first_element)  
print("Last element:", last_element)    

# Demonstrate the use of count() and index() methods
count_hello = my_tuple.count('Hello')
index_true = my_tuple.index(True)

print("Count of 'Hello':", count_hello) 
print("Index of True:", index_true)       

# Convert an integer to a float
int_value = 10
float_value = float(int_value)
print("Integer to float:", float_value)   

# Convert a float to an integer
float_value = 3.99
int_from_float = int(float_value)
print("Float to integer:", int_from_float)  

# Convert a string representing a number to an integer
string_number = "25"
int_from_string = int(string_number)
print("String to integer:", int_from_string) 

# Join a list of strings into a single string using join()
string_list = ['Python', 'is', 'fun']
joined_string = ' '.join(string_list)
print("Joined string:", joined_string) 