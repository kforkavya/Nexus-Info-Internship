import numpy as np

text = "In a land far away, there lived a wise old owl. The owl loved to share stories. These stories were not just any tales; they were reflections of the wisdom the owl had gained over the years. Every evening, creatures from all around the land would gather to listen to the owl's tales. The tales spoke of adventures, lessons, and the mysteries of the land. Among the listeners were a curious rabbit, a brave fox, and a cautious deer. The rabbit, known for its endless curiosity, would always ask questions about the tales. The fox, brave and cunning, would ponder how to use the lessons in life. The deer, cautious and gentle, would reflect on the morals of the stories. Together, they learned much from the wise old owl and looked forward to each new tale with great anticipation."
words = text.split(' ')
for i in range(len(words)):
    last_char = words[i][-1]
    if not(last_char>='a' and last_char<='z' or last_char>='A' and last_char<='Z'):
        words[i] = words[i][:len(words[i])-1]
    words[i] = words[i].lower()

words_list = []
for word in words:
    if word not in words_list:
        words_list.append(word)

table = np.zeros([len(words_list), len(words_list)])

def index(s):
    i = 0
    while words_list[i]!=s:
        i+=1
    return i

for i in range(len(words)-1):
    table[index(words[i])][index(words[i+1])]+=1
table[index(words[-1])][index(words[0])]+=1

for i in range(len(words_list)):
    sum=0
    for j in range(len(words_list)):
        sum+=table[i][j]
    for j in range(len(words_list)):
        table[i][j]/=sum

for word in words_list:
    print(",",end='')
    print(word,end='')
print("")
for i in range(len(words_list)):
    print(words_list[i],end='')
    for j in range(len(words_list)):
        print(",",end='')
        print(table[i][j],end='')
    print("")
