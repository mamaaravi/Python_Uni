# 12. Дано послідовність слів, відокремлених пропусками, в кінці крапка. 
# В словах з непарною кількістю символів вилучити середню літеру.

sentence=input("Enter sentence: ").split(' ')
sentence[len(sentence)-1]=sentence[len(sentence)-1].replace('.', '')
for word in sentence:
    if not len(word)%2==0:
        word=word[:len(word)//2]+word[len(word)//2+1:]
    print(word)

# OUTPUT SAMPLE:
# Enter sentence: Nan huh baba aba jklkj.
# Nn
# hh
# baba
# aa
# jkkj
