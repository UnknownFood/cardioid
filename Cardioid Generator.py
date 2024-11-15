import numpy as np
import matplotlib.pyplot as plt


def main():
    N = input("Enter the number of points to place around the shape: ")
    while N.strip().isdigit() == 0:
        N = input("Enter a number: ")
    print("Number = ",N)          # getting # of points before options
    N = int(N)
    menu(N)

def menu(N):
    a = int(input("1: Circle as outer shape, 2i mod N\n2: Change Number\n3: N-gon Cardiod\nType your choice: "))
    if a == 1:
        cardiod_gen(N)
    elif a == 2:
        pick_num(N)
    elif a == 3:
        ngon_gen_new(N)
    else:
        menu(N)
    

def cardiod_gen(N):      # function to generate cardiods
    points = []
    for i in range(N):
        point = (np.cos(i*2*np.pi/N), np.sin(i*2*np.pi/N))
        points.append(point)

    for i in range(N):
        j = (2*i) % N
        x = [points[i][0],points[j][0]]
        y = [points[i][1],points[j][1]]
        plt.plot(x, y)
        plt.title('Cardiod!')
        plt.xlabel('X axis')
        plt.ylabel('Y axis')

    plt.show()
    menu(N)

def ngon_gen(N):      # function to generate cardiods
    K = int(input("Enter the number of sides you want your shape to have: "))
    theta_pi = (2 / K)
    stop = 0
    section = 0
    vertices = []
    for i in range(K + 1):
        if i != 0:
            angle = theta_pi * (i - (1/2)) * np.pi
        else:
            angle = 0
        if i == 0 or i == K:
            stop += (N / ( 2 * K))
        else:
            stop += (N / K)    
        if i == 0:
            ratio = 1
        else:
            ratio = 1 / np.sin((theta_pi / 2) * np.pi)
        vertice = (ratio * np.cos(angle),ratio * np.sin(angle), i, stop)
        vertices.append(vertice)
        if i == K:
            vertices.append(vertices[0])

    for i in range(N):
        point_i = vertices[2][section]
        point_j = vertices[2][section + 1]
        
        
        # vertices[2] refers to the segment currently being reffered to
        # increment vertice to track which segment the dot you're referring to is on
        # divide side length by N /2K or N/K then just use length of vector to determine points distance from veertice

def ngon_gen_new(N):
    vertices = []
    K = int(input("Enter the number of sides you want your shape to have: "))
    vertice = (np.cos(0), np.sin(0), 0)
    vertices.append(vertice)
    for i in range(K + 1):
        if i == K:
            vertice = (np.cos(i*2*np.pi/K), np.sin(i*2*np.pi/K))
            vertices.append(vertice)
        else:
            vertice = (np.cos((i*2+1)/K*np.pi), np.sin((i*2+1)/K*np.pi))
            vertices.append(vertice)
    n = 0
    stop = 0
    points = []
    vertice_x = 1
    vertice_y = 0
    
    for i in range(K + 1):
        x1 = vertices[i][0]
        x2 = vertices[i + 1][0] 
        y1 = vertices[i][1]
        y2 = vertices[i + 1][1]
        
        if i == 0 or i == K:
            num = N / (2*K)
        else:
            num = N/K
        
        length_x = (x2 - x1)/(num)
        length_y = (y2 - y1)/(num)

        if i == K:
            stop_1 = (N / K) * ((i - 1) + .5)
            stop_2 = N
        elif i == 0:
            stop_1 = 0
            stop_2 = (N / K) * (i + .5)
        else:
            stop_1 = (N / K) * ((i - 1) + .5)
            stop_2 = (N / K) * (i + .5)
        
        while n < stop_2:
            vertice_x += (n - stop_1) * length_x  
            vertice_y += (n - stop_1) * length_y
            point = (vertice_x, vertice_y)
            points.append(point)
            
            n += 1

    print(points)


def pick_num(N):    # function to allow user to change their number
    print("Current number is ",N,"\n")
    N = input("Enter a number: ")
    if N.strip().isdigit() == 0:
        input("Enter a number: ", N)
    N = int(N)
    menu(N)

main()