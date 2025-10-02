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



###### part 3e


def lsquare(x, args):
    beta, gamma = x
    S0, I0,R0, Jsusceptible, Jinfected, Jremoved = args
    Y = SIR(S0, I0,R0, beta, gamma)
    
    S = Y[0, :]
    I = Y[1, :]
    R = Y[2, :]
    
    T = 350 
    ls = (np.linalg.norm(S - Jsusceptible[0:T]) + 
          np.linalg.norm(I - Jinfected[0:T]) + 
          np.linalg.norm(R - Jremoved[0:T]))
    
    return ls

initial_guess = [0.1,0.05]
args = [S0, I0, R0, Jsusceptible, Jinfected, Jremoved]
result = optimize.minimize(lsquare ,initial_guess, args)
optimal = result.x
beta = optimal[0]
gamma = optimal[1]


Y_test = SIR(S0, I0, R0, beta, gamma)

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



R_0 = beta / gamma
print("This is the value of R_0:", R_0)

avg_recovered = 1 / gamma
print(avg_recovered)
########## Part 5: Final question:

    # a) What is the value of R0?
       # The value of R0 is 1.1398935681411384
       
       
    # b) What does the model predict about the spread of Covid-19 in Japan?
        # The model predicts that over the course of one year, a lot of people 
        # in Japan were still susceptible, slightly drop from 100% to 99.8%. Also
        # The percentage of people who either died or recovered were increasing 
        # at a higher rate that the newly infected people. Therefore, we can conclude
        # that Covid - 19 was really limited in Japan from 1/22/2020.
    
    # c) How long was the average infection (in days)?
        # Since gamma represents the rate of how many people recover each day, then
        # the average infection days will be 1 / gamm = 11.868291076156606 days.
    





        
    


    








