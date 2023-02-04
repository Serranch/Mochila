def knapSack(W, wt, val, n):
    
    matriz = ['' for i in range(W+1)]  # se crea la matriz
    #print('array inicial: ',matriz)
    for i in range(1, n+1):  
        for w in range(W, 0, -1):  
            #print(w)
            #print('peso ',wt[i-1], w)
            if wt[i-1] <= w:
                matriz[w] = max(matriz[w], matriz[w-wt[i-1]]+' '+val[i-1])
       
    return matriz[W]  

val = ['items 1','items 2','item 3']
wt = [10, 2, 3]
W = 6
n = len(wt)

print('Items totales ',knapSack(W, wt, val, n))