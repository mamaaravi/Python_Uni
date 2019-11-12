words=input("Enter string:").split(' ')
substring_twice=set([]) #because set keeps only unique elements!
for word in words:
    if words.count(word)==2:
        substring_twice.add(word)
print(substring_twice)



# output sample:
# Enter string:ff dd ss gg gg ff
# {'gg', 'ff'}