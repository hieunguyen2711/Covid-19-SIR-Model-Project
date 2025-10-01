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


    








