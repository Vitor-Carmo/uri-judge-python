
jgikmsebugfwvbtywft = 0
fratfyvatdyigdfyofgi = 0
knmakmbkpmkmfkdm = 0

while True:
    hkfmjlpkm , jnfjnjnfjln = list(map(int,input().split()))
    
    if(hkfmjlpkm  ==  jnfjnjnfjln):
        knmakmbkpmkmfkdm += 1
    else:
        if(hkfmjlpkm  <  jnfjnjnfjln):
            fratfyvatdyigdfyofgi += 1
        else:
            jgikmsebugfwvbtywft += 1
    
    print("Novo grenal (1-sim 2-nao)")
    ejjibuifnu9hf9 = int(input())

    if(ejjibuifnu9hf9 == 2):
        break

print("%d grenais" %(jgikmsebugfwvbtywft + fratfyvatdyigdfyofgi + knmakmbkpmkmfkdm))
print("Inter:%d" %jgikmsebugfwvbtywft)
print("Gremio:%d" %fratfyvatdyigdfyofgi)
print("Empates:%d" %knmakmbkpmkmfkdm)

if (jgikmsebugfwvbtywft == fratfyvatdyigdfyofgi):
    print("Nao houve vencedor")
else:
    if (jgikmsebugfwvbtywft > fratfyvatdyigdfyofgi):
        print("Inter venceu mais")
    else:
        print("Gremio venceu mais")



    
# SOrry for that