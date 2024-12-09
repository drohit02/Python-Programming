# 1. String using double quotes
print('"String using double quotes"')
double_quote_str = "String created using the double quotes"
print(double_quote_str)

# 2. String using single quotes
print("'String using single quotes'")
single_quote_str = 'String created using the single quotes'
print(single_quote_str)

# Using strip() function: Remove whitespaces from string
my_string = "    This is a string with whitespaces    "
print("Original string with whitespaces:", repr(my_string))  # Use repr() to show spaces
print("String without whitespaces:", my_string.strip(), sep="")

# Using title() functions : Capatized each word first letter in uppercase
my_string = "string letters and title() method called"
print("Captialized each word first letter:",my_string.title()) 

#Using upper() functions : Transform test into uppercase
my_string="string to be transformed!"
print("upper() function:",my_string.upper())

#Using lower() functions : Transform test into uppercase
my_string="STRING TO BE TRAANSFORMED!"
print("lower() function:",my_string.lower())