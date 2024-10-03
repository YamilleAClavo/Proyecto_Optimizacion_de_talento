Exploración de Datos: Análisis EDA
________________________________________
1. Age 🧑‍💼 (La edad del empleado)
•	Nulos: 0 ☑️
•	Unique: 54
•	Tipo de Dato: object
•	Tipo de Variable: Numérica
•	Transformaciones:
o	Convertir edades en texto (e.g., "veinticinco") a números (int64). ☑️
o	Cambiar tipo de dato de object a int64.☑️

2. Attrition 🏃‍♂️ (Indica si el empleado ha dejado la empresa)
•	Nulos: 0 ☑️
•	Unique: 2
•	Tipo de Dato: object
•	Tipo de Variable: Categórica
•	Transformaciones: Ninguna ☑️

3. BusinessTravel ✈️ (Frecuencia de los viajes relacionados con el trabajo)
•	Nulos: 772❌    "desconocido"
•	Unique: 3
•	Tipo de Dato: object
•	Tipo de Variable: Categórica
•	Transformaciones:
o	Reemplazar '_' por ' '  y capitalizar los valores  ( "travel_rarely" -> "Travel Rarely").❌☑️ 
o	Decidir el tratamiento de los nulos (posible imputación o eliminación).❌

4. DailyRate 💰 (La tarifa diaria del empleado)
•	Nulos: 124❌ MEDIA
•	Unique: 849
•	Tipo de Dato: object
•	Tipo de Variable: Numérica
•	Transformaciones:
o	Eliminar "$" y convertir a int64.☑️
o	Decidir el tratamiento de los nulos (posible imputación o eliminación).❌

5. Department 🏢 (El departamento en el que trabaja el empleado)
•	Nulos: 1312 ❌ "MODA" 
•	Unique: 3
•	Tipo de Dato: object
•	Tipo de Variable: Categórica
•	Transformaciones:
o	Decidir el tratamiento de los valores nulos.❌
    (1 Research & Development: 196, 2 Sales:91,3 Human Resources: 15)
   
6. DistanceFromHome 🚗 (La distancia desde el hogar del empleado hasta su lugar de trabajo)
•	Nulos: 0 ☑️
•	Unique: 69
•	Tipo de Dato: int64
•	Tipo de Variable: Numérica
•	Transformaciones:
o	Convertir valores negativos a positivos.☑️

7. Education 🎓 (Nivel de educación del empleado)
•	Nulos: 0 ☑️
•	Unique: 5
•	Tipo de Dato: int64
•	Tipo de Variable: Categórica
•	Transformaciones:
o	Convertir a categórica con etiquetas descriptivas ( 1."Primary", 2."Secondary", 3."High School", 4. "Bachelor's", 5."Postgraduate")(1: 180, 2: 314, 3: 621, 4: 445, 5: 54).❌☑️
o   Convertir a object.❌☑️
 
8. EducationField 🧑‍🎓 (El campo de educación del empleado)
•	Nulos: 745 ❓ Desconocido - No tiene mucho sentido esta columna y la anterior. ❌ "ELIMINAR COLUMNA "☑️
•	Unique: 6
•	Tipo de Dato: object
•	Tipo de Variable: Categórica
•	Transformaciones:
o	Decidir cómo tratar los valores nulos.❌ 
(1. Life Sciences 349, 2. Medical 276, 3. Marketing 104, 4. Technical Degree 69, 5. Other 59, 6. Human Resources 12)

9. EmployeeCount 📊 (Un contador que generalmente es 1)
•	Nulos: 0 ☑️
•	Unique: 1
•	Tipo de Dato: int64
•	Tipo de Variable: Constante
•	Transformaciones: Eliminar la columna.☑️

10. EmployeeNumber 🆔 (Un número de identificación único para el empleado)
•	Nulos: 431 ❓ "PASAR A DESCONOCIDO"
•	Unique: 1079
•	Tipo de Dato: object
•	Tipo de Variable: Identificador único
•	Transformaciones:
o	Convertir a formato numérico (int64).☑️ "QUITAR PASAR A INT (queda en object)" ☑️
o   Decidir que vamos a hacer con los nulos (lo vamos a dejar asi)❌

11. EnvironmentSatisfaction 🌱 (Nivel de satisfacción del empleado en relación con su entorno de trabajo)
•	Nulos: 0 ☑️
•	Unique: 4
•	Tipo de Dato: int64
•	Tipo de Variable: Categórica
•	Transformaciones:
o	Convertir a categórico con etiquetas ( 1 "Very Dissatisfied", 2 "Dissatisfied", 3 "Satisfied", 4 "Very Satisfied")(1: 298, 2: 297, 3: 459, 4: 460). ❌☑️
o   Convertir a object.❌☑️
o   Datos erroneos: pendiente de decidir si los datos distintos de 0,1,2,3,4 cogemos el primer digito o eliminamos.❌☑️

12. Gender 👨‍👩‍👧‍👦 (El género del empleado)
•	Nulos: 0 ☑️
•	Unique: 2
•	Tipo de Dato: int64
•	Tipo de Variable: Categórica
•	Transformaciones:
o	Convertir a categórico con etiquetas (0 "Male", 1 "Female")(Hombre:971, Mujer 643).❌☑️
o   Convertir a object.❌☑️

13. HourlyRate ⏰ (La tarifa por hora del empleado)
•	Nulos: 84❌ "NO SE QUE HACER" COMO ESTA
•	Unique: 72
•	Tipo de Dato: object
•	Tipo de Variable: Numérica
•	Transformaciones:
o	Convertir a formato numérico (int64).☑️
o   Cambiar el 'not available'por nan☑️
o	Decidir el tratamiento de los nulos (posible imputación o eliminación).❌

14. JobInvolvement 💼 (Nivel de implicación del empleado en su trabajo)
•	Nulos: 0 ☑️
•	Unique: 4
•	Tipo de Dato: int64
•	Tipo de Variable: Categórica
•	Transformaciones:
o	Convertir a categórico con etiquetas descriptivas (e.g., "Very Low", "Low", "Moderate", "High")(1: 89, 2: 406, 3: 955, 4: 164)❌☑️
o   Convertir a object.❌☑️

15. JobLevel 🏢 (Nivel jerárquico del empleado en la empresa)
•	Nulos: 0 ☑️
•	Unique: 5
•	Tipo de Dato: int64
•	Tipo de Variable: Categórica
•	Transformaciones:
o	Convertir a categórico con etiquetas jerárquicas (1 "Entry Level",2 "Assistant",3 "Coordinator",4 "Manager",5 "Director")(1: 586, 2: 597, 3: 242, 4: 113, 5: 76).❌☑️
o   Convertir a object.❌☑️

16. JobRole 🏷️ (El rol o puesto de trabajo del empleado)
•	Nulos: 0 ☑️
•	Unique: 9
•	Tipo de Dato: object
•	Tipo de Variable: Categórica
•	Transformaciones:
o	Unificar la nomenclatura para evitar inconsistencias (e.g., "Manager" vs "manager").❌☑️


17. JobSatisfaction 😊 (Nivel de satisfacción del empleado con su trabajo)
•	Nulos: 0 ☑️
•	Unique: 4
•	Tipo de Dato: int64
•	Tipo de Variable: Categórica
•	Transformaciones:
o	Convertir a categórico con etiquetas (e.g., "Very Dissatisfied", "Dissatisfied", "Satisfied", "Very Satisfied")(1: 317, 2: 302, 3: 481, 4: 514).❌☑️
o   Convertir a object.❌☑️

18. MaritalStatus 💍 (El estado civil del empleado)
•	Nulos: 651 ❓"Desconocido"
•	Unique: 3
•	Tipo de Dato: object
•	Tipo de Variable: Categórica
•	Transformaciones:
o	Corregir errores tipográficos.❌ ☑️
o   Decidir cómo manejar los valores nulos.❌
o   Tenemos que unificar nombres y repetir recuento ( 'Married', 'Divorced', 'Single', 'divorced', 'Marreid') (1 divorced: 11, 2 Marreid: 35, 3 Divorced: 188, 4 Single: 325, 5 Married: 404) ❌☑️

19. MonthlyIncome 💵 (Ingresos mensuales del empleado)
•	Nulos: 843❌CORRELACIONES COMO ESTA
•	Unique: N/A
•	Tipo de Dato: object
•	Tipo de Variable: Numérica
•	Transformaciones:
o	Convertir a formato numérico (int64).☑️
o   Decidir cómo manejar los valores nulos.❌

20. MonthlyRate 💸 (Tasa mensual del empleado)
•	Nulos: 0
•	Unique: 1427
•	Tipo de Dato: int64
•	Tipo de Variable: Numérica
•	Transformaciones: Ninguna☑️

21. NumCompaniesWorked 🏢 (Número de compañías en las que el empleado ha trabajado)
•	Nulos: 0
•	Unique: 10
•	Tipo de Dato: int64
•	Tipo de Variable: Numérica
•	Transformaciones: Cambiar el nombre de la columna NumCompaniesWorked ☑️
(0: 226, 1: 573, 2: 156, 3: 169, 4: 157, 5: 66, 6: 73, 7: 84, 8: 51,9: 59)

22. Over18 ✔️ (Indica si el empleado es mayor de 18 años)
•	Nulos: 901
•	Unique: 1
•	Tipo de Dato: object
•	Tipo de Variable: Categórica
•	Transformaciones: Eliminar la columna.☑️

23. OverTime ⏱️ (Indica si el empleado trabaja horas extras)
•	Nulos: 676❌ "MODA"
•	Unique: 2
•	Tipo de Dato: object
•	Tipo de Variable: Categórica
•	Transformaciones:
o	Tratar los valores nulos y asegurarse de que los datos sean categóricos y consistentes.❌

24. PercentSalaryHike 📈 (El porcentaje de aumento salarial del empleado)
•	Nulos: 0 ☑️
•	Unique: 15
•	Tipo de Dato: int64
•	Tipo de Variable: Numérica
•	Transformaciones: Ninguna

25. PerformanceRating ⭐ (Calificación de rendimiento del empleado)
•	Nulos: 195 ❌ "MODA"
•	Unique: 2
•	Tipo de Dato: object
•	Tipo de Variable: Categórica
•	Transformaciones:
o	Convertir a categórico con etiquetas (1 "Poor", 2 "Average", 3 "Good", 4 "Excellent").❌☑️
o   Decidir cómo manejar los valores nulos.❌

26. RelationshipSatisfaction ❤️ (Nivel de satisfacción en las relaciones interpersonales)
•	Nulos: 0 ☑️
•	Unique: 4
•	Tipo de Dato: int64
•	Tipo de Variable: Categórica
•	Transformaciones:
o	Convertir a categórico con etiquetas (1 "Very Dissatisfied",2 "Dissatisfied", 3 "Satisfied",4 "Very Satisfied").❌☑️

27. StandardHours ⏲️ (Las horas estándar de trabajo)
•	Nulos: 1195 ❓ Desconocido - Mucha diferencia de salarios independientemente del rol. Mucha diferencia de sueldo dentro del mismo rol. ❌
•	Unique: 1
•	Tipo de Dato: object
•	Tipo de Variable: Constante
•	Transformaciones: Considerar si eliminar o mantener la columna, verificar coherencia.❌
o   Decidir cómo manejar los valores nulos.❌nulos a 160??
o   Cambiar a int64 ☑️
•	Transformaciones: Eliminar la columna. "ELIMINAR COLUMNA" ☑️

28. StockOptionLevel 📈 (Nivel de opciones de compra de acciones del empleado)
•	Nulos: 687 ❌ ESTA EN EL CERO "NONE" "NO HAY NULOS" ☑️
•	Unique: 4
•	Tipo de Dato: int64
•	Tipo de Variable: Categórica
•	Transformaciones:
o	Convertir a categórico con etiquetas (0 "ZERO" (CAMBIAR)☑️, 1 "Low", 2 "Medium", 3"High").❌☑️
o   Decidir cómo manejar los valores nulos.❌ ☑️

29. TotalWorkingYears 👔 (Total de años de experiencia laboral del empleado)
•	Nulos: 526❌ "ITERATIVE"
•	Unique: 40
•	Tipo de Dato: object
•	Tipo de Variable: Numérica
•	Transformaciones:
o	Convertir a formato numérico (int64).☑️
o	Tratar los valores nulos.❌

30. TrainingTimesLastYear 🎓 (Número de veces que el empleado recibió capacitación el año pasado)
•	Nulos: 0 ☑️
•	Unique: 7
•	Tipo de Dato: int64
•	Tipo de Variable: Numérica
•	Valor más frecuente: 2
•	Transformaciones: Ninguna ☑️

31. WorkLifeBalance ⚖️ (Equilibrio entre trabajo y vida personal del empleado)
•	Nulos: 108❌ "MODA"
•	Unique: 4
•	Tipo de Dato: object
•	Tipo de Variable: Categórica
•	Transformaciones:
o	Convertir a categórico con etiquetas descriptivas (1"Bad", 2"Good", 3"Better", 4"Best").❌☑️
o	Tratar los valores nulos.❌

32. YearsAtCompany 🏢 (Años que el empleado ha trabajado en la empresa actual)
•	Nulos: 0 ☑️
•	Unique: 37
•	Tipo de Dato: int64
•	Tipo de Variable: Numérica
•	Transformaciones: Ninguna☑️

33. YearsInCurrentRole 📅 (Años que el empleado ha estado en su puesto actual)
•	Nulos: 1580
•	Unique: 10
•	Tipo de Dato: object
•	Tipo de Variable: Numérica
•	Transformaciones:
o	Convertir a formato numérico (int64).☑️
o	Decidir cómo manejar los valores nulos.
o   Eliminar columna "HAY QUE ELIMINARLA" ☑️


34. YearsSinceLastPromotion 🚀 (Años desde la última promoción del empleado)
•	Nulos: 0 ☑️
•	Unique: 16
•	Duplicados: No
•	Tipo de Dato: int64
•	Tipo de Variable: Numérica
•	Transformaciones: Ninguna☑️

35. YearsWithCurrManager 👔 (Años que el empleado ha estado bajo la supervisión del actual gerente)
•	Nulos: 0 ☑️
•	Unique: 18
•	Tipo de Dato: int64
•	Tipo de Variable: Numérica
•	Transformaciones: Ninguna☑️

36. SameAsMonthlyIncome 💵 (Ingresos mensuales del empleado)
•	Observación: Columna duplicada con MonthlyIncome.
•	Transformaciones: Eliminar la columna.☑️

37. DateBirth 🎂 (Año de nacimiento del empleado)
•	Nulos: 0 ☑️
•	Unique: 43
•	Tipo de Dato: int64
•	Tipo de Variable: Fecha
•	Transformaciones:
o	Mantener como int64 si solo se requiere el año, o convertir a datetime si se desea análisis temporal más detallado. Mantener esta columna para la bbdd pero crear una nueva con el calculo de la edad? ❌ SE QUEDA EN INT

38. Salary 💸 (Salario de los empleados)
•	Nulos: 0 ☑️
•	Unique: N/A
•	Tipo de Dato: object
•	Tipo de Variable: Numérica
•	Transformaciones:
o	Eliminar columna☑️

39. RoleDepartament 🏢 (El departamento y el rol del empleado)
•	Nulos: 1312 ❌ 
•	Unique: 301
•	Tipo de Dato: object
•	Tipo de Variable: Categórica
•	Transformaciones:
o	Normalizar nombres (minusculas, capitalize) ☑️y decidir cómo manejar los valores nulos.❌
o	Eliminar columna "HAY QUE ELIMINAR"☑️

40. NumberChildren 👶 (Número de hijos de los empleados)
•	Nulos: 1614
•	Unique: 0
•	Tipo de Dato: float64
•	Tipo de Variable: No aplicable
•	Transformaciones: Eliminar la columna.☑️

41. RemoteWork 🏠 (Si el empleado puede teletrabajar o no)
•	Nulos: 0 ☑️
•	Unique: 5
•	Tipo de Dato: object
•	Tipo de Variable: Categórica
•	Transformaciones:
o	Unificar los valores a "Yes" y "No" para mayor consistencia.❌☑️

## Pendiente

Próximos Pasos 🚀
1. Limpieza Adicional de Datos 🧼
Revisar y corregir valores faltantes en columnas.
Verificar y ajustar tipos de datos restantes.

2. Gestión de Valores Nulos 🛠️
Identificar todas las columnas con valores nulos.
Decidir la estrategia para gestionar nulos (eliminación, imputación con media/mediana/moda, etc.).
Implementar la estrategia de gestión de nulos en el notebook de EDA.

3. Análisis Exploratorio de Datos Continuo 📊
Generar más visualizaciones para identificar patrones y tendencias.
Realizar análisis estadísticos adicionales para descubrir relaciones entre variables.
Documentar los hallazgos en el notebook.

4. Diseño de la Base de Datos 🗂️
Definir la estructura de la base de datos (tablas, relaciones, claves primarias y foráneas).☑️
Crear scripts SQL para la creación de la base de datos y tablas.

5. Inserción de Datos en la Base de Datos 📝
Escribir scripts para cargar los datos transformados en la base de datos.

6. Preparación para el Experimento A/B 🔬

7. Automatización con ETL 🤖

8. Creación del Informe Final 📈
Actualizar el informe con nuevas visualizaciones y análisis.
Redactar secciones adicionales del informe, incluyendo recomendaciones basadas en el análisis de datos.
Preparar una presentación final con los resultados y recomendaciones para ABC Corporation.