words = {"1":"One", "2":"Two", "3":"Three", "4":"Four", "5":"Five", "6":"Six", "7":"Seven", "8":"Eight", "9":"Nine", "0":"Zero"}
value = input("Enter Number : ")
output = ''
for i in value :
#    print(words[i] + ' ', end='')
    output += words.get(i, '!') + ' '
print(output)