import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize
import pandas as pd

cases = pd.read_csv(r'time_series_covid19_confirmed_global.csv').values
deaths = pd.read_csv(r'time_series_covid19_deaths_global.csv').values
recovered = pd.read_csv(r'time_series_covid19_recovered_global.csv').values

JC = cases[156][4:]
JD = deaths[156][4:]
JR = recovered[141][4:]

JN = 126300000

Jinfected = JC - JD - JR


Jsusceptible = JN - (JD + JR + Jinfected)


Jremoved = JD + JR



print((Jinfected + Jremoved + Jsusceptible) == JN)


Jinfected = Jinfected / JN
Jsusceptible = Jsusceptible / JN
Jremoved = Jremoved / JN

x = np.linspace(0, 349, 350)


plt.figure(1)
plt.xlabel('Days')
plt.ylabel('Fraction of Population')
plt.plot(x, Jinfected[:350])
plt.plot(x, Jremoved[:350])
plt.legend(['Actual Infected', 'Actual Removed'])



plt.title("Japan Covid-19 data from 1/22/2020")

plt.show()

plt.figure(2)
plt.xlabel('Days')
plt.ylabel('Fraction of Population')
plt.plot(x, Jsusceptible[:350])
plt.legend(['Actual Susceptible'])



plt.title("Japan Covid-19 data from 1/22/2020")

plt.show()

def SIR ( S0, I0, R0 , beta , gamma ):
    
    """
    Discrete SIR model function
    
    Arguments:
    S0 - initial value of susceptible people (fraction of population)
    I0 - initial value of infected people (fraction of population)
    R0 - initial value of removed people (fraction of population)
    beta - transmission rate parameter
    gamma - recovery rate parameter
    
    Output:
    Y - a 3x350 array containing S, I, R values over 350 days
    """
    
    #Initializing an array matrix with 3 rows and all elements are 0
    Y = np.zeros((3,350))
    
    Y[0,0] = S0 #initial value of susceptible people
    Y[1,0] = I0 # initial value of infected people
    Y[2,0] = R0 # initial value of removed people
    
    for n in range(349):
        
        ###### part 3a
        S_n = Y[0, n]
        I_n = Y[1, n]
        R_n = Y[2, n]
        
        ###### part 3b
        S_n_1 = S_n + ((-beta)*S_n*I_n)
        I_n_1 = I_n + ((beta*S_n*I_n) - (gamma*I_n))
        R_n_1 = R_n + gamma*I_n
        
        ###### part 3c
        Y[0, n+ 1] = S_n_1
        Y[1, n+ 1] = I_n_1
        Y[2, n+ 1] = R_n_1
        
        
    return Y

###### part 3d
S0 = (JN -500) / JN
I0 = 500/ JN
R0 = 0
beta = 0.07
gamma = 0.06

Y_test = SIR(S0, I0, R0, beta, gamma)

###### part 3e
plt.figure(3)
plt.xlabel('Days')
plt.ylabel('Fraction of Population')
plt.plot(x, Jinfected[:350])
plt.plot(x, Y_test[1,:350])
plt.plot(x, Jremoved[:350])
plt.plot(x, Y_test[2,:350])
plt.legend(['Actual Infected','Infected' ,'Actual Removed', 'Removed'])

plt.title("Japan Covid-19 data from 1/22/2020")

plt.show()


plt.figure(4)
plt.xlabel('Days')
plt.ylabel('Fraction of Population')
plt.plot(x, Jsusceptible[:350])
plt.plot(x, Y_test[0,:350])
plt.legend(['Actual Susceptible', 'Susceptible'])

plt.title("Japan Covid-19 data from 1/22/2020")

plt.show()





        
    


    








