import warnings
warnings.simplefilter(action='ignore', category=FutureWarning) # elimina los errres de que van a cambiar

# importamos las librerías que necesitamos
# Tratamiento de datos
# -----------------------------------------------------------------------
import pandas as pd
import numpy as np

# Imputación de nulos usando métodos avanzados estadísticos
# -----------------------------------------------------------------------
from sklearn.impute import SimpleImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.impute import KNNImputer

# Librerías de visualización
# -----------------------------------------------------------------------
import seaborn as sns
import matplotlib.pyplot as plt
# Configuración
# -----------------------------------------------------------------------
pd.set_option('display.max_columns', None) # para poder visualizar todas las columnas de los DataFrames

from word2number import w2n

class LimpiarDatos:
    def __init__(self):
        self.df = pd.read_csv("data/HR RAW DATA.csv", index_col=0)
    def cambiar_nombres_columnas (self):
        nombres_columnas = {"employeecount":"EmployeeCount",
                     "employeenumber" :"EmployeeNumber",
                     "NUMCOMPANIESWORKED" : "NumCompaniesWorked",
                     "TOTALWORKINGYEARS" :"TotalWorkingYears",
                     "WORKLIFEBALANCE" : "WorkLifeBalance",
                     "YEARSWITHCURRMANAGER" : "YearsWithCurrManager",
                     "NUMBERCHILDREN" : "NumberChildren"}
        self.df.rename(columns=nombres_columnas, inplace=True)
    def eliminar_columnas (self):
        columnas_eliminar = ["EmployeeCount", "Salary", "NumberChildren", "SameAsMonthlyIncome", "DateBirth", "YearsInCurrentRole", "Over18", "EducationField", "StandardHours", "RoleDepartament"]
        self.df.drop(columns=columnas_eliminar, inplace=True)
    def cambiar_a_numerico (self):
        # convertir la edad str en número:
        def convertir_edad(value):
            try:
                return w2n.word_to_num(value)
            except ValueError:
                return value  # Devolver el valor original si no puede ser convertido
        self.df["Age"] = self.df["Age"].apply(convertir_edad)
        # quitar simbolo $
        self.df["DailyRate"] = self.df["DailyRate"].str.replace("$", "")
        # Convertir la distancia al trabajo en positivo
        self.df["DistanceFromHome"] = self.df["DistanceFromHome"].abs()
        # columnas a convertir a numerico
        columnas_a_convertir = ["DailyRate", "MonthlyIncome", "TotalWorkingYears", "Age", "HourlyRate"]
        for col in columnas_a_convertir:
            if self.df[col].dtype == 'object':
                # Verificar si la columna contiene comas antes de intentar reemplazarlas
                if self.df[col].str.contains(",").any():
                    self.df[col] = self.df[col].str.replace(",", ".")
            # Convertir la columna a formato numérico
                try:
                    self.df[col] = pd.to_numeric(self.df[col], errors='coerce')
                except:
                    self.df[col] = np.nan
    def cambiar_a_categorica (self):
        # if self.df.select_dtypes(include = "object")
        # Comprobar las columnas que tiene guion y quitarlo
        columnas_guion = [col for col in self.df.select_dtypes(include = "object").columns if self.df[col].str.contains('-|_', regex=True).any()]
        for col in columnas_guion:
            self.df[col] = self.df[col].apply(lambda val: val.replace("_", " ").replace("-", " ") if pd.notna(val) else val)
        # convertimos los nombres a minusculas y luego ponemos la primera letra en mayusculas
        columnas_objetivo = self.df.select_dtypes(include="object").columns
        for col in columnas_objetivo:
            self.df[col] = self.df[col].str.lower().str.title()
        # Quitamos el segundo digito del valor. Deberian de ser valores del 1 al 4 y este patron se repite solo en el primer digito, eliminamos el segundo.
        self.df['EnvironmentSatisfaction'] = self.df['EnvironmentSatisfaction'].apply(lambda num: num if num < 10 else num // 10 )
        # Poner nombres descriptivos
        self.df["Education"].replace(to_replace= [1, 2, 3, 4, 5], value=["Primary", "Secondary", "High School", "Bachelor's", "Postgraduate"], inplace=True)
        self.df["JobLevel"].replace(to_replace= [1, 2, 3, 4, 5], value=["Entry Level", "Assistant", "Coordinator", "Manager", "Director"], inplace=True)
        self.df["Gender"].replace(to_replace= [0, 1], value=["Male", "Female"], inplace=True)
        self.df["RemoteWork"].replace(to_replace= ["0", "1", "True", "False"], value=["No", "Yes", "Yes", "No"], inplace=True)
        self.df["StockOptionLevel"].replace(to_replace= [0, 1, 2, 3], value=["Zero", "Low", "Medium", "High"], inplace=True)
        self.df["MaritalStatus"].replace(to_replace= "Marreid", value= "Married", inplace=True)
        satisfaccion = ["JobInvolvement", "EnvironmentSatisfaction", "JobSatisfaction", "RelationshipSatisfaction", "WorkLifeBalance"]
        for col in satisfaccion:
            self.df[col].replace(to_replace= [1, 2, 3, 4], value=["Very Low", "Low", "Medium", "High"], inplace=True)
    def guardar_archivo (self):
        # Save into a .csv file
        self.df.to_csv("./data/hr_raw_data_limpio_.csv")


class LimpiarDatosBBDD:
    def __init__(self):
        self.df = pd.read_csv("data/HR RAW DATA.csv")
    
    def cambiar_nombres_columnas (self):
        nombres_columnas = {"employeecount":"EmployeeCount",
                     "employeenumber" :"EmployeeNumber",
                     "NUMCOMPANIESWORKED" : "NumCompaniesWorked",
                     "TOTALWORKINGYEARS" :"TotalWorkingYears",
                     "WORKLIFEBALANCE" : "WorkLifeBalance",
                     "YEARSWITHCURRMANAGER" : "YearsWithCurrManager",
                     "NUMBERCHILDREN" : "NumberChildren", "Unnamed: 0": "ID"}
        self.df.rename(columns=nombres_columnas, inplace=True)
    
    def eliminar_columnas (self):
        columnas_eliminar = ["EmployeeCount", "Salary", "NumberChildren", "SameAsMonthlyIncome", "Over18", "RoleDepartament"]
        self.df.drop(columns=columnas_eliminar, inplace=True)

    def cambiar_a_numerico (self):
        # convertir la edad str en número:
        def convertir_edad(value):
            try:
                return w2n.word_to_num(value)
            except ValueError:
                return value  # Devolver el valor original si no puede ser convertido
        self.df["Age"] = self.df["Age"].apply(convertir_edad)
        
        # quitar simbolo $
        self.df["DailyRate"] = self.df["DailyRate"].str.replace("$", "")

        # Convertir la distancia al trabajo en positivo
        self.df["DistanceFromHome"] = self.df["DistanceFromHome"].abs()
            
        # columnas a convertir a numerico
        columnas_a_convertir = ["DailyRate", "EmployeeNumber", "MonthlyIncome", "TotalWorkingYears", "Age", "HourlyRate", "StandardHours"]
        for col in columnas_a_convertir:
            if self.df[col].dtype == 'object':
                # Verificar si la columna contiene comas antes de intentar reemplazarlas
                if self.df[col].str.contains(",").any():
                    self.df[col] = self.df[col].str.replace(",", ".")
            # Convertir la columna a formato numérico
                try:
                    self.df[col] = pd.to_numeric(self.df[col], errors='coerce')
                except:
                    self.df[col] = np.nan           
        
            
    def cambiar_a_categorica (self):
        # if self.df.select_dtypes(include = "object")
        # Comprobar las columnas que tiene guion y quitarlo
        columnas_guion = [col for col in self.df.select_dtypes(include = "object").columns if self.df[col].str.contains('-|_', regex=True).any()]        
        for col in columnas_guion:
            self.df[col] = self.df[col].apply(lambda val: val.replace("_", " ").replace("-", " ") if pd.notna(val) else val)

        # convertimos los nombres a minusculas y luego ponemos la primera letra en mayusculas
        columnas_objetivo = self.df.select_dtypes(include="object").columns
        for col in columnas_objetivo:
            self.df[col] = self.df[col].str.lower().str.title()

        # Quitamos el segundo digito del valor. Deberian de ser valores del 1 al 4 y este patron se repite solo en el primer digito, eliminamos el segundo.
        self.df['EnvironmentSatisfaction'] = self.df['EnvironmentSatisfaction'].apply(lambda num: num if num < 10 else num // 10 )

        # Poner nombres descriptivos               
        self.df["Education"].replace(to_replace= [1, 2, 3, 4, 5], value=["Primary", "Secondary", "High School", "Bachelor's", "Postgraduate"], inplace=True)
        self.df["JobLevel"].replace(to_replace= [1, 2, 3, 4, 5], value=["Entry Level", "Assistant", "Coordinator", "Manager", "Director"], inplace=True)
        self.df["Gender"].replace(to_replace= [0, 1], value=["Male", "Female"], inplace=True)
        self.df["RemoteWork"].replace(to_replace= ["0", "1", "True", "False"], value=["No", "Yes", "Yes", "No"], inplace=True)
        self.df["StockOptionLevel"].replace(to_replace= [0, 1, 2, 3], value=["None", "Low", "Medium", "High"], inplace=True)
        self.df["MaritalStatus"].replace(to_replace= "Marreid", value= "Married", inplace=True)
        
        satisfaccion = ["JobInvolvement", "EnvironmentSatisfaction", "JobSatisfaction", "RelationshipSatisfaction", "WorkLifeBalance"]
        for col in satisfaccion:
            self.df[col].replace(to_replace= [1, 2, 3, 4], value=["Very Low", "Low", "Medium", "High"], inplace=True)
    

    def guardar_archivo (self):
        # Save into a .csv file
        self.df.to_csv(f"./data/hr_raw_data_limpio_BBDD.csv")
       
           