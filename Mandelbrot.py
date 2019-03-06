#mandelbrot set
#weston Harby, dec, 16, 2018

#import nessisary libraries
import matplotlib.pyplot as plt
import math as m
import cmath as cm
import numpy as np

#univeral vars
divisions = 1
interations = 1
#np array of points to test
test = np.array([])
#np array of points in the set
Set_real = np.array([])
Set_imag = np.array([])
#np array of points that leave the set 
leave = np.array([])
#np array of the number of iterations it takes to leave the circle of radius 2


def find_points():
    global test
    divisions = eval(input("Enter a of divisions: "))
    
    step = 4/divisions
    count_real = -2.00 
    count_imag = -2.00
    
    #loops to populate array
    while count_real <= 2.00:
        while count_imag <= 2.00:
            #use dummy var to throw numbers into a numpy array
            temp = complex(count_real, count_imag)
            test = np.append(test, temp)
            count_imag = count_imag + step
               
        count_real = count_real + step               
        count_imag = -2.00
    
    print(test.shape)    
    print(test)
    
def mandelbrot_set():
    #get points
    global Set_real, Set_imag
    find_points()
    iterations = eval(input("Enter the amount of iterations: "))

    n1 = list(test.shape)
    n1 = int(n1[0])
    
    z = 0
    c_for = 0
    c_while = 0
    r = 1
    #iterate over the set
    for i in range(n1):
        while c_while < iterations:
            #actaul math
            z = complex((m.pow(z, 2)) + test[c_for])

            #radius check   
            r = float(m.sqrt((m.pow(z.real, 2)) + (m.pow(z.imag, 2))))

            #break while loop
            if r > 2.00:
                print(r > 2.00)
                print(c_while)
                c_while = iterations + 1
                
            #add point to the Set array  
            elif c_while == (iterations - 1):
                Set_real = np.append(Set_real, test[c_for].real)
                Set_imag = np.append(Set_imag, test[c_for].imag)
                c_while = iterations + 1

            #proigate the loop    
            else:
                c_while = c_while + 1
                

        print(c_for)
        c_for = c_for + 1
        c_while = 0

    area = 4
    plt.scatter(Set_real, Set_imag,s=area, alpha=1)
    plt.xlabel('real')
    plt.ylabel('imag')
    plt.show()


mandelbrot_set()
