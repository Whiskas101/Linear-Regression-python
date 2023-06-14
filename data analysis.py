import pandas as pd
import matplotlib.pyplot as plt
import random

# Very basic visualisation of how a best fit line is decided for a bunch of data

y_values = []
x_values = []
constant = 3.5
slope = 1.3

#generating the data
for i in range(25):

    x_values.append(i)
    new_y = constant + slope*(i)  + random.randint(-2, 4) + random.randint(-7, 2)
    y_values.append(new_y)


    
    
    
plt.scatter(x_values, y_values)
plt.xlim(0, 25)
plt.ylim(0, 50)

   



#assumed best fit line of the form y = Mx + C

bestfit_slope = 0.0
bestfit_constant = 0.0

# best fit line storage

bf_X_values = []

for i in range(0, 25):
    bf_X_values.append(i)

bf_Y_values = []

#fine tuning

STEPS = 150
LEARNING_RATE = 0.001



for step in range(0, STEPS):
    residual_x = []
    residual_y = []     

    bf_Y_values = []
    for x in range(0, 25):

        #generating the values for the guess lines
        new_bf_y = bestfit_constant + bestfit_slope*(x)
        bf_Y_values.append(new_bf_y)

    #calculating error
    
    deltaSlope = 0
    deltaConstant = 0
    
    for i in range(25):

        temp1 = (bf_Y_values[i] - y_values[i]) * i

        deltaSlope += temp1

        temp2 = (bf_Y_values[i] - y_values[i])

        deltaConstant += temp2

    
    deltaSlope = deltaSlope * (-2/25)
    deltaConstant = deltaConstant * (-2/25)

    

    bestfit_slope = bestfit_slope + (LEARNING_RATE * deltaSlope)
    bestfit_constant = bestfit_constant + (LEARNING_RATE* 20 * deltaConstant)

    
    plt.plot(bf_X_values, bf_Y_values)
    
    plt.pause(0.0000000000001)
    print(f"\n {bestfit_slope} {bestfit_constant} || {slope} {constant}")

plt.clf()
plt.xlim(0, 25)
plt.ylim(0, 50)
plt.scatter(x_values, y_values)

plt.plot(bf_X_values, bf_Y_values)

plt.show()
        
print(f"Best fit line is of the form Y = {bestfit_slope}x + {bestfit_constant}")

