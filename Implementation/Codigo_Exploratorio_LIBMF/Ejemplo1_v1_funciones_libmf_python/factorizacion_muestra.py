import os
import numpy as np
import pandas as pd
from libmf import mf


directorio = '/home/alfie-gonzalez/Documentos/Maestría/Segundo Semestre/Métodos Numéricos y Optimización'
os.chdir(directorio)

datos_ent = pd.read_csv('muestra_entrena.csv')
datos_ent
datos_val = pd.read_csv('muestra_valida.csv')
datos_val


X = np.array(datos_ent)
Y = np.array(datos_val)

n = len(np.unique(datos_ent['usuario_id']))
p = len(np.unique(datos_ent['peli_id']))
k = 2
eta = 0.1
nr_iters = 10

engine = mf.MF(fun = 0, k = k, eta = eta, nr_iters = nr_iters, quiet = False, 
               lambda_p2 = 0, lambda_q2 = 0)
engine.fit(X)
engine.predict(Y[:,:2])

