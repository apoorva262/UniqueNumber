import pandas as pd
import numpy as np
def UN(X, Y):
    Input = pd.DataFrame({'Num':np.arange(X,Y+1), 'Tracker':('')}).set_index('Num')
    Prime = []
    while len(Input.index)>0:
        Prime.append(Input.index[0]) #this will store all the prime numbers
        for i in Input.index:
            if i % Input.index[0] == 0: #this will divide all the Num cell from the first cell.
                Input.loc[i, 'Tracker'] = '1' #this will update the cell in column Tracker '1' which is divisible by (Input.index[0]) in that run
            else:
                Input.loc[i, 'Tracker'] = '0' #this will update the cell in column Tracker '0' which is divisible by (Input.index[0]) in that run
        Input = (Input.loc[Input['Tracker']=='0']) #this will filter only the one's with '0' and drop '1'. So now Input dataframe has only prime numbers.
    return Prime
