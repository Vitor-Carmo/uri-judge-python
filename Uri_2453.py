x = input()
msg = ''

for word in x.split():
    for letter in range(1, len(word), 2):
        msg += word[letter]

    msg += ' '


print(msg[:-1])