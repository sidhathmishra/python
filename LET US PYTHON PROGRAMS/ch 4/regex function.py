import re #regular expressions module
word = "javascript"
print(re.search("java",word))#searching for "java" in word
print(re.search("z",word))#searching for "z" in word
#use of [] in regular expression,used in set of characters
print(re.search('[ac]plication','application'))
#use of - in regular expressions,used in range
print(re.search('["a-z"]',"anything"))
#use of . in RE
print(re.search('[a.x]',word))