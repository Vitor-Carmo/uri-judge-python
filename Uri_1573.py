from math import pow



# parallelepipid volum = a  * b * c
# cube volume = a³
# a³ = a * b * c
# a = ∛(a * b * c)

while True:
    parallelepipid_edges = input().split()
    a = int(parallelepipid_edges[0])
    b = int(parallelepipid_edges[1])
    c = int(parallelepipid_edges[2])
    if(a == b == c ==0):
        break
    
    parallelepipid_volume = a * b * c
    cube_egde = pow(float(parallelepipid_volume), 1 / 3)

    cube_egde = int(cube_egde)

    print(cube_egde)

    

   


