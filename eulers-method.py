#Calculated for theta = 0.01, 0.1, 0.5, 1, 1.5, 2, 2.5, 3.1


#package imports for graphing and computing sine/pi
import matplotlib.pyplot as plt # matplotlib must be installed, NumPy >= 1.15 also required
import math

#constants
gravity = 10
length = 0.1
step = 0.000001
initialAngle = <initial angle>
angularVelocity = 0 #initial condition for angular velocity

GbyL = gravity/length #computed once and saved instead of computing each time

time = 0 #initial time set to zero
theta = initialAngle #initialize the angle to the original angle

previousValues = [theta+1, theta-1] #initialize this with arbitrary values that don't trigger the check, logic explained on line 27

angles = [] #an array to store the angles to graph later

while 1: #loop until we reach a maximum, after which we break out of the loop

    acceleration = -GbyL * math.sin(theta) #calculating the acceleration
    time += step
    angularVelocity += step * acceleration
    theta += angularVelocity*step

    #logic to check whether it has reached a maximum: in loop n, if the (n-1)th value is greater than the (n-2)th value and greater than the nth value, it is a maximum and we can quit the calculation without saving this round.
    if previousValues[0] < previousValues[1] and previousValues[1] > theta and time > 0.01:
        break
    previousValues[0] = previousValues[1]
    previousValues[1] = theta

    angles.append(theta) #if we're still in the first oscillation, keep the value for graphing

xValues = [i*step for i in range(len(angles))] #Creates an array of timestep values in order, with the same length as the array of angles.

plt.scatter(xValues, angles, color='#000000', marker="o", s=0.1) #scatterplot the time and angle.

linearPrediction = [initialAngle*math.cos(i * math.sqrt(GbyL)) for i in xValues] #create an array of what the linear approximation (SHM pendulum) predicts.

plt.scatter(xValues, linearPrediction, color='#0000FF', marker="o", s=0.1) #scatterplot the time and prediction.
approximatePeriod = 2*math.pi*math.sqrt(length/gravity) #calculate the approximate period
plt.title(r"$\theta_0 = " + str(initialAngle) + r"$" + "\n Real period = "+ str(round(time, 7)) + ", Approximated period = " + str(round(approximatePeriod, 7))) #mark the title
plt.xlabel("Time") #Label the X axis
plt.ylabel("Angular Displacement") #Label the Y axis

plt.show() #show the graph

