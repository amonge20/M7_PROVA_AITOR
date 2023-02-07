import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def Exercici1():
    df = pd.read_csv("Llistat.csv")

    alumnes = df.array(['Abril','Andres','Bruno','Ivan','Kevin','Marta','Raúl','Roger','Samuel','Sara','Xavier'])
    notes = df.array([9,5,7,6,5,7,5,8,3,6,4])

    print(df.array)
    df.plot.bar()
    plt.show()