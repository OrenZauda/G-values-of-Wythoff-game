import numpy as np

def main():
    
    mat = np.zeros((16,16,16))
    mat = mat.astype(int)

    for rows in range(16):
          for columns in range(rows,16):
                for height in range(columns,16):

                    Downward = np.asarray(mat[0:rows,columns,height])
                    toTheLeft = np.asarray(mat[rows,0:columns,height])
                    toDeeperLayer = np.asarray(mat[rows,columns,0:height])
                    NimSumZero = []

                    maxBorAorC = max(columns,rows,height)
                    for d in range(0, maxBorAorC + 1):
                        for e in range(d, maxBorAorC + 1):
                            f = d ^ e                   
                            if d != 0 or e != 0 or f != 0: 
                                g = max(f,e)
                                h = min(f,e) 
                                if (rows - d) >= 0 and (columns - h) >= 0 and (height - g) >= 0 and  mat[rows - d, columns - h, height - g] >= 0:
                                    
                                    NimSumZero.append(mat[rows - d, columns - h, height - g]) 
                                
                    NimSumZero = np.asarray(NimSumZero)
                    MinExclude = np.concatenate((Downward,toTheLeft,toDeeperLayer,NimSumZero))
                    MinExclude = np.unique(MinExclude)
                    MinExclude = np.sort(MinExclude)

                    MinExclude = MinExclude.astype(int)
                                                
                    gValue = 0
                    for value in MinExclude:
                        if gValue == value:
                            gValue = value + 1
                
                    mat[rows][columns][height] = gValue
                    mat[rows][height][columns] = gValue
                    mat[columns][rows][height] = gValue
                    mat[columns][height][rows] = gValue
                    mat[height][columns][rows] = gValue
                    mat[height][rows][columns] = gValue


    print(mat[0, 0:16,0:16])






if __name__ == '__main__':
    main()
