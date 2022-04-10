import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def main():

    s = (15,15)
    mat = np.zeros(s)
    mat = mat.astype(int)
    for i in range(15):
        for j in range(15):
            Downward = np.asarray(mat[0:i,j])
            toTheLeft = np.asarray(mat[i,0:j])
            Diagonal = np.diag(mat,k = (j-i))[0:min(i,j)]
            MinimumExclude = np.concatenate((Downward,toTheLeft,Diagonal))
            MinimumExclude = np.sort(MinimumExclude)
            
            runner = 0
            for value in MinimumExclude:
                if runner == value:
                    runner = value + 1
                
                mat[i][j] = runner
    fig, ax = plt.subplots()

    ax.axis('tight')

    df = pd.DataFrame(mat, columns=np.arange(15))

    ax.table(cellText=df.values, colLabels=df.columns, loc='center')

    fig.tight_layout()

    plt.show()

    

    # print(mat)
            
    






if __name__ == '__main__':
    main()

