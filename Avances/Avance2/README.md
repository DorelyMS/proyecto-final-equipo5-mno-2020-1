# Avance 2

## Integrantes:

* Dorely Morales Santiago

* Margarita M. Muñoz Sancén

* Guillermo Zarazúa Cruz

* Alfie S. Gonzalez Salcedo

* Javier Valencia Goujon

* Oscar A. Aguilar Castillo

## Trabajo: 

### Resumen

El 9 de mayo tuvimos reunión con Erick y se agregan objetivos al proyecto como el uso de factorización matrices No-Negativas y ejemplos donde se usan las matrices One-Class y Binarias. Se decide además crear un Milestone relativo al diseño de las muestras que serán utilizadas para correr libmf con entrenamiento y validación.

El 13 de mayo nos reunimos para discutir avances individuales en el proyecto, así como asignar tareas nuevas. Javier realizó una prueba exitosa levantando una instancia EC2 en AWS, además se verificó que tanto Maggie, como Dorely pudieron conectarse a dicha instancia. Además, se acordó que para garantizar cumplir con el 90% del trabajo el viernes 22 de mayo, el objetivo será utilizar un extracto de la base original para la implementación y presentación de resultados. En caso de lograr los avances y el reporte satisfactoriamente anterior a lo previsto, se buscará correr la base completa del *Netflix price*.


Los avances logrados sobre los equipos se describen a continuación:

### Project Manager

Avanzamos en el *milestone* de **Implementación** relacionado con los issues #14 #15 #16 y #22 logrando pruebas existosas con bases de datos pequeñas y levantar una instancia en AWS. En el *milestone* de **Trabajo Escrito** avanzamos con los issues  #19 #20 #30 y #32 respecto a la la Introducción del trabajo escrito y parámetros de la librería, así como algunos métodos disponibles. En general, encargada de dar seguimiento y revisión de ambos milestones.

### Equipo de programación

Respecto a los issues #14 #15 #16 y #22 relacionados con el *milestone* de **Implementación** se realizaron los siguientes avances:

+ Javier realizó la lectura y pruebas exitosas para la manipulación de la base completa del concurso de Netflix sobre una instancia de AWS. Agrega ejemplos prácticos de matrices Binarias y One-Class.
+ Maggie genera el código para la lectura de la base de *Netflix price* y la separación en *train* y *test*, así como revisión y notas a la Introducción del trabajo escrito.
+ Alfie realizó códigos en formato .py para la lectura y centralización de las calificaciones de la base muestra de *Netflix*.
+ Guillermo generó códigos de ejemplo con el uso de funciones de libmf sobre Python con matrices aleatorias.


### Investigación, Revisión y Documentación

Se realiza la Introducción del trabajo escrito en el [overleaf](https://www.overleaf.com/project/5e9a6dd6cbcf62000110548a). Se crea una tabla para indicar los parámetros de la librería LIBMF y las entradas para utilizar distintos métodos. Se describen dichos métodos de manera general y se proporcionan ejemplos básicos de dichas matrices. Después de las revisiones de Maggie y Dorely, se agrega la introducción al [README del proyecto](https://github.com/DorelyMS/proyecto-final-equipo5-mno-2020-1). Se agregan referencias y se realizan primeras revisiones a documentación de los códigos.

## Tareas (o *milestone* o trabajo) que continúa


+ Correr RVMF y NPF en libmf con base chica Netflix modificando todos los parámetros sobre instancia de AWS con Docker de jupyterlab_numerical
+ Documentación de pruebas con libmf, agregar aprendizajes sobre cómo cambia el desempeño cuando se modifica cada parámetro
+ Reporte ejecutivo de resultados en Notebook con parámetros finales que obtuvieron mejor desempeño en factorizaciones RVMF y NPF y reportar en el trabajo escrito
+ Comparació
+ Reporte ejecutivo de resultados en Notebook con parámetros finales que obtuvieron mejor desempeño en factorizaciones RVMF y NPF y reportar en el trabajo escrito.
+ Comparación de desempeño del modelo implementado en libmf con la referencia base y tomar ejemplos particulares de recomendaciones para evaluar si las recomendaciones tienen sentido.

En caso de lograr los avances en un tiempo menor a lo previsto:

+ Utilizar el código trabajado para intentar correr libmf con la base completa de *Netflix*. En caso de éxito, agregar los resultados obtenidos.







