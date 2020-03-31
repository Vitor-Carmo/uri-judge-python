# A(xa, ya) B(xb, yb)
# √(xb - xa)² + (yb - ya)² 


def distance_points(xa, ya, xb, yb):
    from math import pow, sqrt
    return sqrt(pow((xb - xa), 2)  + pow((yb - ya), 2))


i = int(input())

for i in range(0, i):
    
    j  = int(input())

    white_ball_pos = input().split()
    xa = int(white_ball_pos[0])
    ya = int(white_ball_pos[1])

    dist_min = 0

    for j in range(1, j + 1):
        randon_ball_pos = input().split()
        xb = int(randon_ball_pos[0])
        yb = int(randon_ball_pos[1])

        distance_to_white_ball = distance_points(xa, ya, xb, yb)
        
        if j == 1:
            ball_number = j
            dist_min = distance_to_white_ball

        if(dist_min > distance_to_white_ball):
            ball_number = j
            dist_min = distance_to_white_ball

    print(ball_number)