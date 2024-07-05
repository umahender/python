import re
text="my name is nagendra and my age is 25"
k=re.sub("[aeiou AEIOU]","#",text)
print(k)
