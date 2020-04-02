tests = int(input())

for test in range(tests):

    code = input().upper()
    key = int(input())

    
    decode = str()

    for l in code:
        pos = ord(l)-key

        if(pos < 65):
            decode += chr(91-(65-pos))
        else:
            decode += chr(ord(l)-key)
    print(decode)