import mysql.connector
from mysql.connector import errorcode
import pandas as pd
import numpy as np

# Esta función crea el BDD. Se conecta al servidor y si funciona lo crea, si falla te dice el fallo.
def crear_bbdd():
    cnx = mysql.connector.connect(user='root', password='AlumnaAdalab', host='127.0.0.1')
    mycursor = cnx.cursor()

    try:
        mycursor.execute("CREATE DATABASE ABC_Corporation") # Aquí, el nombre de la base de datos se indica después del operador CREATE DATABASE.
        print("DATABASE CREATED UNDER THE NAME: ABC_Corporation 🆗")
    except mysql.connector.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)
    finally:
        cnx.commit()
        mycursor.close()
        cnx.close()

# Esta función crea las tablas. Se conecta al servidor y si funciona lo crea, si falla te dice el fallo.
def crear_tablas():
    cnx = mysql.connector.connect(user='root', password='AlumnaAdalab', host='127.0.0.1', database='ABC_Corporation')
    mycursor = cnx.cursor()

 # Lista de consultas donde se crean todas las tablas.
    queries = [
        """CREATE TABLE Employee (
    ID INT PRIMARY KEY,
    Age INT,
    Attrition VARCHAR(5),
    BusinessTravel VARCHAR(50),
    DailyRate DECIMAL(10, 2),
    Department VARCHAR(50),
    DistanceFromHome INT,
    Education VARCHAR(50),
    EducationField VARCHAR(50),
    EmployeeNumber INT UNIQUE,
    EnvironmentSatisfaction VARCHAR(50),
    Gender VARCHAR(10),
    HourlyRate DECIMAL(10, 2),
    JobInvolvement VARCHAR(50),
    JobLevel VARCHAR(50),
    JobRole VARCHAR(50),
    JobSatisfaction VARCHAR(50),
    MaritalStatus VARCHAR(50),
    MonthlyIncome DECIMAL(10, 2),
    MonthlyRate DECIMAL(10, 2),
    NumCompaniesWorked INT,
    OverTime VARCHAR(5),
    PercentSalaryHike DECIMAL(5, 2),
    PerformanceRating VARCHAR(50),
    RelationshipSatisfaction VARCHAR(50),
    StandardHours INT DEFAULT 40,
    StockOptionLevel VARCHAR(50),
    TotalWorkingYears INT,
    TrainingTimesLastYear INT,
    WorkLifeBalance VARCHAR(50),
    YearsAtCompany INT,
    YearsInCurrentRole DECIMAL(5, 2),
    YearsSinceLastPromotion INT,
    YearsWithCurrManager INT,
    DateBirth YEAR,
    RemoteWork VARCHAR(5)
);""",]

    
# Hemos creado esta lista de nombres de tablas para poder iterar sobre ella e imprimirá sus nombres apropiadamente a medida que los cree.
    nombre_tablas = [
        'employees',
        ]

   # El zip es una función que agrupa listas que tienen múltiples elementos en tuplas. 
    # Esto luego le permite iterar a través de los nombres en la impresión.
    for query, nombre_tablas in zip(queries, nombre_tablas):
        try:
            mycursor.execute(query) 
            print(f"TABLA CREADA CON EL NOMBRE: {nombre_tablas} 🆗")
        
        except mysql.connector.Error as err:
            print(err)
            print("Código de error:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("mensaje", err.msg)

    cnx.commit()
    mycursor.close()
    cnx.close()

def insert_employees(df):
    # Conectar a la base de datos
    cnx = mysql.connector.connect(
        user='root', 
        password='AlumnaAdalab', 
        host='127.0.0.1', 
        database='ABC_Corporation'
    )
    mycursor = cnx.cursor()

    try:
        sql_insert_query = """ 
        INSERT INTO Employee (
            ID, Age, Attrition, BusinessTravel, DailyRate, Department,
            DistanceFromHome, Education, EducationField, EmployeeNumber,
            EnvironmentSatisfaction, Gender, HourlyRate, JobInvolvement, JobLevel,
            JobRole, JobSatisfaction, MaritalStatus, MonthlyIncome, MonthlyRate,
            NumCompaniesWorked, OverTime, PercentSalaryHike, PerformanceRating,
            RelationshipSatisfaction, StandardHours, StockOptionLevel, TotalWorkingYears,
            TrainingTimesLastYear, WorkLifeBalance, YearsAtCompany, YearsInCurrentRole,
            YearsSinceLastPromotion, YearsWithCurrManager, DateBirth, RemoteWork
        ) VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s
        )
        ON DUPLICATE KEY UPDATE
            Age = VALUES(Age),
            Attrition = VALUES(Attrition),
            BusinessTravel = VALUES(BusinessTravel),
            DailyRate = VALUES(DailyRate),
            Department = VALUES(Department),
            DistanceFromHome = VALUES(DistanceFromHome),
            Education = VALUES(Education),
            EducationField = VALUES(EducationField),
            EmployeeNumber = VALUES(EmployeeNumber),
            EnvironmentSatisfaction = VALUES(EnvironmentSatisfaction),
            Gender = VALUES(Gender),
            HourlyRate = VALUES(HourlyRate),
            JobInvolvement = VALUES(JobInvolvement),
            JobLevel = VALUES(JobLevel),
            JobRole = VALUES(JobRole),
            JobSatisfaction = VALUES(JobSatisfaction),
            MaritalStatus = VALUES(MaritalStatus),
            MonthlyIncome = VALUES(MonthlyIncome),
            MonthlyRate = VALUES(MonthlyRate),
            NumCompaniesWorked = VALUES(NumCompaniesWorked),
            OverTime = VALUES(OverTime),
            PercentSalaryHike = VALUES(PercentSalaryHike),
            PerformanceRating = VALUES(PerformanceRating),
            RelationshipSatisfaction = VALUES(RelationshipSatisfaction),
            StandardHours = VALUES(StandardHours),
            StockOptionLevel = VALUES(StockOptionLevel),
            TotalWorkingYears = VALUES(TotalWorkingYears),
            TrainingTimesLastYear = VALUES(TrainingTimesLastYear),
            WorkLifeBalance = VALUES(WorkLifeBalance),
            YearsAtCompany = VALUES(YearsAtCompany),
            YearsInCurrentRole = VALUES(YearsInCurrentRole),
            YearsSinceLastPromotion = VALUES(YearsSinceLastPromotion),
            YearsWithCurrManager = VALUES(YearsWithCurrManager),
            DateBirth = VALUES(DateBirth),
            RemoteWork = VALUES(RemoteWork)
        """

        for index, row in df.iterrows():
            # Limpiar los datos de la fila
            cleaned_row = clean_data(row)
            
            # Ejecutar la consulta SQL
            mycursor.execute(sql_insert_query, (
                cleaned_row['ID'],
                cleaned_row['Age'],
                cleaned_row['Attrition'],
                cleaned_row['BusinessTravel'],
                cleaned_row['DailyRate'],
                cleaned_row['Department'],
                cleaned_row['DistanceFromHome'],
                cleaned_row['Education'],
                cleaned_row['EducationField'],
                cleaned_row['EmployeeNumber'],
                cleaned_row['EnvironmentSatisfaction'],
                cleaned_row['Gender'],
                cleaned_row['HourlyRate'],
                cleaned_row['JobInvolvement'],
                cleaned_row['JobLevel'],
                cleaned_row['JobRole'],
                cleaned_row['JobSatisfaction'],
                cleaned_row['MaritalStatus'],
                cleaned_row['MonthlyIncome'],
                cleaned_row['MonthlyRate'],
                cleaned_row['NumCompaniesWorked'],
                cleaned_row['OverTime'],
                cleaned_row['PercentSalaryHike'],
                cleaned_row['PerformanceRating'],
                cleaned_row['RelationshipSatisfaction'],
                cleaned_row['StandardHours'],
                cleaned_row['StockOptionLevel'],
                cleaned_row['TotalWorkingYears'],
                cleaned_row['TrainingTimesLastYear'],
                cleaned_row['WorkLifeBalance'],
                cleaned_row['YearsAtCompany'],
                cleaned_row['YearsInCurrentRole'],
                cleaned_row['YearsSinceLastPromotion'],
                cleaned_row['YearsWithCurrManager'],
                cleaned_row['DateBirth'],
                cleaned_row['RemoteWork']
            ))

        # Confirmar la transacción
        cnx.commit()
        print("Datos insertados correctamente.")

    except mysql.connector.Error as err:
        print(f"Error al insertar en la base de datos: {err}")

    finally:
        if cnx.is_connected():
            mycursor.close()
            cnx.close()
            print("Conexión a la base de datos cerrada.")
