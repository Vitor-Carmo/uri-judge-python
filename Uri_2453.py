x = input()
msg = ''

for word in x.split():
    for letra in range(1, len(word), 2):
        msg += word[letra]

    msg += ' '


print(msg[:-1])