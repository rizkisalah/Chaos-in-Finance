import wolf_test
from kv_neuralnetwork import *
from numpy import *
from numpy import linalg as la
M = 16
A = weights_first_layer.T
C = weights_second_layer.T
def lyap(serie,M,A,C):
  t = 0
  somme = 0
  # Création de la matrice jacobienne avec initialisation par 0 de la dernière ligne
  D=[[0 for i in range(M)] for u in range(M)]
  for i in range(0,M-1):
      D[i][i+1]=1
      i+=1
  # La boucle dans laquelle on calculera notre exposant
  Xprm=0
  alpha=[0 for i in range(M)]
  for t in range(len(serie)-M+1):
    X = serie[t:t + M ]
    L = []
    for k in range(M):
      for h in range(3):
        for m in range (M):
          Xprm+=A[h][m]*X[m]
          m+=1
        alpha[k]=C[0][h]*A[h][k]*(exp(Xprm)/(exp(Xprm)+1)**2)
        h+=1
      L += [alpha[k] - X[k]]
      k+=1
    D[M-1]=alpha
    u=dot(array(L),D)
    somme+=log(la.norm(u)/la.norm(array(L)))
    t+=1
  somme=somme/len(serie)
  return somme

print("L'exposant de Lyapunov vaut : ",lyap(wolf_test.bdserie,M,A,C))
