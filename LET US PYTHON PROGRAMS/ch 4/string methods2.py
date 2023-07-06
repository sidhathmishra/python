string = str(" programming with python ")
print(string)
#content test functions
print(str.isalpha(string))
print(str.isdigit(string))
print(str.isalnum(string))
print(str.islower(string))
print(str.isupper(string))
print(string.startswith('p'))
print(string.endswith('o'))
#search and replace
print(string.find('r'))
print(string.replace('r',''))
print(str.lstrip(string))
print(str.rstrip(string))
print(str.strip(string))
#split and partition 
print(string.split("with"))
print(string.partition("with"))
#join
string2 = "java".join(string)
print(string2)