import os
import numpy as np
import pandas as pd

directorio = '/home/alfie-gonzalez/Documentos/Maestría/Segundo Semestre/Métodos Numéricos y Optimización'
os.chdir(directorio)

pelis_nombres = pd.read_csv('movies_title_fix.csv', header = 0, 
                            na_values = ["", "NA", "NULL"]) 

pelis_nombres.columns = ['peli_id', 'año', 'nombre']

dat_netflix = pd.read_csv('dat_muestra_nflix.csv') \
    .drop(columns = ['usuario_id_orig'])

np.random.seed(28882)
usuarios = dat_netflix.loc[:,'usuario_id'].unique()
valida_usuarios = pd.Series(usuarios).sample(frac = 0.02)
peliculas = dat_netflix.loc[:,'peli_id'].unique()
valida_pelis = pd.Series(peliculas).sample(frac = 0.02)

from dplython import DplyFrame, X, select, sift, mutate, group_by, arrange, summarize
from dplython import semi_join, anti_join, count, head, tail

dat_netflix = DplyFrame(dat_netflix)
usuarios = DplyFrame(usuarios)
usuarios.columns = ['usuario_id']
valida_usuarios = DplyFrame(valida_usuarios)
valida_usuarios.columns = ['usuario_id']
peliculas = DplyFrame(peliculas)
peliculas.columns = ['peli_id']
valida_pelis = DplyFrame(valida_pelis)
valida_pelis.columns = ['peli_id']

dat_valida = dat_netflix >> semi_join(valida_usuarios)

dat_entrena = dat_netflix >> anti_join(dat_valida)

dat_entrena_c = (dat_entrena >> 
                 group_by(X.usuario_id) >> 
                 mutate(calif_c = X.calif - np.mean(X.calif))

                 )
dat_entrena_c.head(10)

