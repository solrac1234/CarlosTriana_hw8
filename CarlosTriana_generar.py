import numpy as np
import matplotlib.pyplot as plt 

#genera y retorna numeros aleatorios siguiendo la distribucion discreta de probabilidad

def sample_1(N):
	num = np.random.rand(N)
	return num

#retorna N numero aleatorios siguiendo la funcion de probabilidad exponencial 
def sample_2(N):
	beta = 0.5
	pexp = np.random.exponential(beta,N)
	return pexp

# genera y retorna M promedios(Sn) dada la funcion de sampleo 

def get_mean(samplin_fun,N,M):
	mean_1 = []
	for i in range(M):
		promedios = mean_1.append(np.mean(samplin_fun(N+i)))
		i = i+1
	return promedios 

get_mean(samplin_fun,N,M)
print get_mean(sample_1,20,5)
