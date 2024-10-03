#%%
import pandas as pd
import numpy as np
from IPython.display import display
from itertools import combinations
from scipy.stats import kstest, spearmanr, pearsonr

from src import soporte_eda as eda
from src import soporte_bbdd as bbdd
from src import soporte_transformacion as st

# %%
autoEda = eda.AutoEDA()
df = autoEda.read_file("data/HR RAW DATA.csv")
autoEda.explo_df(df)
# %%
limpieza = st.LimpiarDatos()
limpieza.cambiar_nombres_columnas()
limpieza.eliminar_columnas()
limpieza.cambiar_a_numerico()
limpieza.cambiar_a_categorica()
limpieza.guardar_archivo()
# %%
transformacion = st.LimpiarDatosBBDD()
transformacion.cambiar_nombres_columnas()
transformacion.eliminar_columnas()
transformacion.cambiar_a_numerico()
transformacion.cambiar_a_categorica()
transformacion.guardar_archivo()
# %%
bbdd.crear_bbdd()
bbdd.crear_tablas()
df_bbdd = pd.read_csv("./data/hr_raw_data_limpio_BBDD.csv")
bbdd.insert_employees(df_bbdd)
# %%
