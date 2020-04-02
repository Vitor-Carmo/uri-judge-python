alphabet =[ 
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','0'
    ,'P','Q','R','S','T','U','V','W','X','Y','Z'
]

tests = int(input())

for test in range(tests):
    
    code = input()
    key = int(input())

    decode = str()
    if not key == 0:

        for string in code:
            for i in range(len(alphabet)):
                if alphabet[i] == string:
                    if  i - key < 0:
                        pos = i - key
                        pos = len(alphabet) + pos
                    else:
                        pos = i - key
                    
                    decode += alphabet[pos]
    else:
        decode = code
    print(decode)
