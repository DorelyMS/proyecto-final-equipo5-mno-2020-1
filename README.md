## Proyecto Final del curso MNO-2020-1: Equipo 5 y 9

Este es el repositorio de Proyecto Final para la materia de Métodos Numéricos y Optimización del semestre 2020-1 en la Maestría en Ciencia de Datos, ITAM.

Título del proyecto: `Uso de LIBMF (A LIBrary for large-scale sparse Matrix Factorization) para sistemas de recomendación de películas con una base de datos de usuarios de Netflix`

Objetivo del proyecto: `**Investigación sobre el uso y explotación de la librería LIBMF empleando el lenguaje de programación Python**. El enfoque del proyecto se orienta al estudio de los parámetros y el uso de paralelización en los métodos disponibles para el caso práctico de realizar recomendaciones de películas a usuarios de Netflix a través de métodos basados en reducción de dimensionalidad o modelos de factores latentes, así como su comparación y evaluación de resultados a través de una muestra de prueba y entrenamiento.`

Trabajo escrito (fuera del repo): https://www.overleaf.com/read/ffbjdrrxtmdm

Presentación de Resultados (en el repo): [liga_presentación](https://github.com/DorelyMS/proyecto-final-equipo5-mno-2020-1/tree/master/Resultados)

Implementación (en el repo): [Implementación](https://github.com/DorelyMS/proyecto-final-equipo5-mno-2020-1/tree/master/Implementation) 

## Indice del proyecto

1. [Introducción](https://github.com/DorelyMS/proyecto-final-equipo5-mno-2020-1/blob/master/README.md#introducci%C3%B3n)
3. [Estructura del equipo](https://github.com/DorelyMS/proyecto-final-equipo5-mno-2020-1/blob/master/README.md#estructura-del-equipo)
4. [Organización del Repositorio](https://github.com/DorelyMS/proyecto-final-equipo5-mno-2020-1/blob/master/README.md#organizaci%C3%B3n-del-repositorio)
5. [Requerimientos de infraestructura](https://github.com/DorelyMS/proyecto-final-equipo5-mno-2020-1/blob/master/README.md#requerimientos-de-infraestructura)

## Introducción 

### Sistemas de Recomendación y LIBMF

Los sistemas de recomendación (*recommender systems*) son un conjunto de métodos que sirven como herramienta para predecir la respuesta de personas a estímulos a los que no han sido expuestos, basados en respuesta a otros estímulos de esta y quizá otras personas similares a su perfil. Por ejemplo, si consideramos usuarios de plataformas de ***streaming***: ¿qué tanto le puede gustar al usuario **![i](https://render.githubusercontent.com/render/math?math=i)** la película **![j](https://render.githubusercontent.com/render/math?math=j)**? Usuarios de sitios de ***e-commerce***: Si se les ofrece el artículo **![j](https://render.githubusercontent.com/render/math?math=j)**, ¿qué tan probable es que lo compren? Anteriormente, las recomendaciones de este tipo de plataformas se basaban únicamente en los raitings populares y se asumía que éstos podrían servir para recomendar a cualquiera (sistemas basados en popularidad). 

Los principales enfoques para ofrecer soluciones a los sistemas de recomendación son:  

+ Aquellos principalmente basados en contenido: En función de características de los estímulos, canciones o películas (por ejemplo, género, actores, país de origen, año, etc.) intentamos predecir el gusto por el estímulo. En este caso, se construyen variables derivadas del contenido de los artículos (por ejemplo: qué actores salen, año, etc. o en textos palabras que aparecen), e intentamos predecir el gusto a partir de esas características. Ejemplo: Si me gustó *Toy Story* entonces el sistema recomienda otras infantiles+animadas como *Monsters Inc*.
+ El enfoque colaborativo busca además “perfilar al usuario” para hacer recomendaciones, tomando como referencia a otros con características similares. Ejemplo: Si a un usuario le gustó *Piratas del Caribe y Alicia en el país de las maravillas*, vemos que a varios otros usuarios a los que también les gustaron otras películas de Johnny Depp, recomendamos “*Charlie y la fábrica de chocolate*”.

Por otra parte, este tipo de sistemas se clasifican en dos tipos basados en la recolección de datos: El explícito, donde el usuario brinda la calificación directamente y el implícito en el que se deriva de la actividad de los usuarios. 

A través de *machine learning*, apoyándose de métodos numéricos para encontrar soluciones a problemas de minimización no convexos, los sistemas de recomendación bajo enfoque colaborativo y datos explícitos han logrado tener una mejora notable en las recomendaciones. Esto se debe al uso de métodos basados en reducción de dimensionalidad o modelos de factores latentes: los cuales se basan en encontrar **![k](https://render.githubusercontent.com/render/math?math=k)** factores latentes (no observados) que describan películas con “contenido implícito similar”, y usuarios según su interés en esa dimensión.  

El presente proyecto utiliza el enfoque colaborativo en sistemas de recomendación de películas para el estudio, dominio y explotación de la librería **LIBMF** (*A LIBrary for large-scale sparse Matrix Factorization*), usando el método de descenso en gradiente para la predicción de calificaciones que dará un usuario a las películas en una muestra de validación a partir de la factorización de la matriz de entrenamiento *R* con las calificaciones observadas por *m* usuarios y **![n](https://render.githubusercontent.com/render/math?math=n)** películas en términos de 2 matrices ![P \in \mathbb {R}^{kxm}](https://render.githubusercontent.com/render/math?math=P%20%5Cin%20%5Cmathbb%20%7BR%7D%5E%7Bkxm%7D) y ![Q \in \mathbb {R}^{kxn}](https://render.githubusercontent.com/render/math?math=Q%20%5Cin%20%5Cmathbb%20%7BR%7D%5E%7Bkxn%7D). En específico, el producto a evaluar a través de sistemas de recomendación son películas con ratings explícitos y se usará una base de datos de *Netflix* para sugerir ver aquella película con calificación más alta.

LIBMF provee un método eficiente de programación en paralelo para encontrar la factorización de matrices de diferentes tipos. Su uso está disponible en C/C++, R, Python y puede ser compilado en Unix, Cygwin, Windows o en MacOS. Las pruebas en este caso se realizaron en Pyhton y Bash a través de la imagen de Docker usada en el curso de MNO 2020 (palmoreck/jupyterlab\_numerical:1.1.0) y una instancia EC2 en AWS para poder realizar cómputo en la nube para poder trabajar con la muestra de datos de Netflix y la base completa del concurso **Netflix Prize**

Para problemas en general, la factorización de matrices busca descomponer una matriz *R* de dimensiones **![m \times n](https://render.githubusercontent.com/render/math?math=m%20%5Ctimes%20n)** en dos matrices: ![P \in \mathbb {R}^{kxm}](https://render.githubusercontent.com/render/math?math=P%20%5Cin%20%5Cmathbb%20%7BR%7D%5E%7Bkxm%7D) y ![Q \in \mathbb {R}^{kxn}](https://render.githubusercontent.com/render/math?math=Q%20%5Cin%20%5Cmathbb%20%7BR%7D%5E%7Bkxn%7D). La importancia de la descomposición de matrices se debe a que se busca aprender de la matriz *R* de tal forma en la que el producto de matrices ![P^{\rm T}Q](https://render.githubusercontent.com/render/math?math=P%5E%7B%5Crm%20T%7DQ) consiga reducir la dimensionalidad de los datos y hacer más eficiente la predicción de nuevos datos. En este tipo de representación, las entradas de las matrices ![r_i_j](https://render.githubusercontent.com/render/math?math=r_i_j) indican para nuestro problema práctico la calificación que el usuario **![i](https://render.githubusercontent.com/render/math?math=i)** le dio a la película **![j](https://render.githubusercontent.com/render/math?math=j)**. El uso de la representación de este problema a través de matrices, con lleva al uso de dimensiones grandes, además de que éstas puedan ser singulares y suelen tener demasiadas entradas con ceros (ralas). Esto sucede porque prácticamente nadie ve todas las películas.

### Base de Datos *Netflix*

Para probar la librería primero utilizamos un extracto de la base de datos original que proviene del concurso de *Netflix* o *Netflix Price* que se llevó a cabo en 2009 y fue tomada de la clase de Métodos Analíticos del ITAM impartida por el profesor Felipe González. Como un ejercicio complementario, también se consiguió utilizar LIBMF sobre la base de datos completa del concurso que contiene más de *100* millones de calificaciones de *480,189* usuarios de la plataforma seleccionados aleatoriamente y más de *17,770* títulos de películas. Las calificaciones obtenidas van en una escala del 1 al 5 y las evaluaciones fueron entre Octubre 1998 a Diciembre 2005.

La base extracto contaba con sólo *100,000* usuarios y las *17,770* películas. Las únicas columnas disponibles son el ID de usuario y película, ID de usuario asignado respecto al renglón **![i](https://render.githubusercontent.com/render/math?math=i)**, calificación de la película y fecha con formato YYYY-MM-DD. Para esta base de datos se tiene un total de 20,968,941 entradas ya que no todos los usuarios califican todas las películas. Las entradas de esta base se muestras a continuación:

![Ejemplo_Matriz_Original0.1\textwidth](https://github.com/DorelyMS/proyecto-final-equipo5-mno-2020-1/blob/master/Imagenes/Ejemplo_Matriz_Original.png)

El dataset completo del concurso se extrajo de Kaggle y está compuesto de 4 archivos de texto (.txt), cada archivo contiene más de 20 millones de filas, que en conjunto generan alrededor de 100 Millones de líneas. Cada uno contiene las siguientes columnas:

+ ID de película (como la primera linea de cada registro y marcado con un numero seguido de :)
+ ID del cliente
+ Calificación (escala del 1 al 5)
+ Fecha de la calificación

En seguida, se muestra el head del archivo 1 de 4 del concurso:

![Ejemplo_Head_Original0.1\textwidth](https://github.com/DorelyMS/proyecto-final-equipo5-mno-2020-1/blob/master/Imagenes/6_Head_Archivo1_txt_Netflix.png)

## Estructura del equipo

Para el desarrollo del proyecto, la división de los integrantes considera una distribución adaptada a su porcentaje de avance, por lo que de manera inicial, se decidió dividir al equipo en 2 partes: el primero y más grande, encargado de la implementación del uso de libmf para resolver nuestro caso práctico (**Equipo de Programación, o P-Team**) y el segundo, encargado de la documentación, revisión de los reportes de resultados para su presentación y trabajo escrito (**Equipo de Revisión, o R-Team**). Finalmente, ambos grupos fueron coordinados por un project manager (**PM**)

La estructura del equipo a lo largo del proyecto se resume en la siguiente tabla:

| #    | Rol                                       | Persona      | Github    |
| ---- | ------------------------ | ------------ | --------- |
| 1    | Programación & documentación              |  Alfie       | gonzalezalfie     |
| 2    | Programación & documentación              |  Guillermo   | gzarazua          |
| 3    | Programación & documentación              |  Javier      | valencig          |
| 4    | Programación, Revisión & documentación    |  Maggie      | maggiemusa        |
| 5    | Investigación, Revisión & documentación   |  Oscar       | oaguilarca        |
| 6    | Project Manager, Revisión & documentación | Dorely       | DorelyMS          |

## Organización del Repositorio

La organización del repositorio se realizó a través una serie de carpetas, las cuales se describen a continuación:

+ **Referencias:** En el apartado de [Referencias](https://github.com/DorelyMS/proyecto-final-equipo5-mno-2020-1/tree/master/Referencias) se añaden todos los textos que se consultaron para la realización de este trabajo.
+ **Implementación:** [Código y Notebooks de implementación](https://github.com/DorelyMS/proyecto-final-equipo5-mno-2020-1/tree/master/Implementation) del uso de libmf para pruebas con diferentes muestras y parámetros. 
+ **Avances:** Contiene un resumen de los [avances de proyecto final](https://github.com/DorelyMS/proyecto-final-equipo5-mno-2020-1/tree/master/Avances) detallado por **PM** y complementado por **P&R Teams** para efecto de reportar al profesor los avances en el desarrollo del proyecto, así como las nuevas tareas a realizar.
+ **Resultados**: Incluye la [Presentación de resultados](https://github.com/DorelyMS/proyecto-final-equipo5-mno-2020-1/tree/master/Resultados) obtenido con la implementación para nuestro sistema de recomendación generado a partir de una instancia de AWS aplicando paralelización con una imagen de Docker.

En complemento, se presenta una versión esquemática de la organización de repositorio del proyecto:

```bash
├── README.md                      <- Archivo readme del proyecto
│
├── Referencias                    <- Carpeta de referencias y materiales usados en el proyecto
│   ├── Google News Personalization_Das etal.pdf              <- Referencias OCMF y BMF
│   ├── One-Class Collaborative Filtering_Pan Rong_etal.pdf   <- Referencias OCMF y BMF
│   ├── README.md                                             <- Archivo readme con links a referencias fuera del repo
│
├── Imagenes                       <- Carpeta de imágenes para readme
│
├── Avances                        <- Carpeta Reporte de de implementación desarrollada por E-Prog
│   └── Avance1                                               <- Reporte de avances al 9 de Mayo de 2020
│   └── Avance2                                               <- Reporte de avances al 16 de Mayo de 2020
│
├── Implementation                 <- Carpeta de reporte de ejercicios de implementación de libmf y libmf python
│   ├──Codigo_Implementacion_Final <- Carpeta con reporte de implementación de libmf bash con base muestra y Completa de Netflix en formato .py
│   ├──REAME.md
│       ├── 0_Ejercicio_libmf      <- Carpeta con reporte de ejercicio inicial sobre uso de libmf bash sobre datos demo
│           ├── Resultados_Ejercicio
│           ├── output_demo_libmf.txt
│           ├── README.md
│       ├── 1_Ejercicio_libmf_demo <- Carpeta con reporte de ejercicio con uso de libmf bash sobre datos demo
│       ├── 2_Ejemplo_libmf_python_matrices_aleatorias <- Carpeta con reporte de ejercicio de libmf python con matrices aleatorias
│       ├── 3_BaseMuestra_Netflix  <- Carpeta con reporte de implementación de libmf bash con base muestra de Netflix
│           ├── README.md
│           ├── Paso1_SeparaBaseMuestraNetflix.ipynb
│           ├── Paso2_Implementacion.ipynb
│           ├── Insumos_LIBMF_Bash    <- Carpeta donde se colocan los archivos demo.sh modificados para correr los modelos de Netflix en libmf bash.
│               ├── demo.sh
│               ├── netflixdemo.sh
│           ├── Resultados_LIBMF_Bash <- Carpeta donde se colocan las salidas de los modelos en libmf bash sobre la base muestra de Netflix con fines ilustrativos.
│               ├── DesempeñoModelo_BaseMuestra_.txt
│               ├── ocmf_model
│           ├── Reference_Files    <- Carpeta donde se colocan los archivos para descargar base muestra de películas de Netflix.
│               ├── README.md
│               ├── README_bajar_datos.md
│               ├── movies_title_fix.csv
│       ├── 4_BaseCompleta_Netflix <- Carpeta con reporte de implementación de python-libmf con base completa de Netflix
│           ├── README.md
│           ├── Paso1_CargaDatos.ipynb
│           ├── Paso2_Prune_ncreate_train_test.ipynb
│           ├── Adicional_BaseCompletaNetflix_libmf_python.ipynb
│
└── Resultados                     <- Carpeta con Presentación de Resultados del Proyecto

```

## Requerimientos de infraestructura
Con el propósito de reproducibilidad del proyecto y para que todos los equipos (**P-Team**, **R-Team** y **PM**) tuvieran un entorno común de trabajo, se empleó la imagen de docker basada en Python del curso MNO 2020 (palmoreck/jupyterlab_numerical:1.1.0) así como una instancia de AWS. A continuación, se describen los pasos utilizados para la creación de la instancia en AWS para poder trabajar de manera más rápida y eficiente. 

### Crear la maquina EC2
Se utilizó una cuenta de AWS Educate lo cual limitó un poco las opciones a elegir de máquinas EC2.

**Paso 1**: Se lanzó una instancia de AWS de tipo EC2, la Amazon Machine Image (AMI) que se eligió fue una del tipo  **ubuntu/images/hvm-ssd/ubuntu-bionic-18.04-amd64-server-20200408**  


![AMI](Imagenes/AMI.png)


**Paso 2**: El tipo de instancia que se eligió fue una t2.2xlarge que cuenta con 8 VCPUs y tiene 32 GB de memoria RAM y 32GB de memoria en disco duro, originalmente habíamos elegido usar una máquina de tipo p2.xlarge que cuenta con GPUs disponibles pero debido a las restricciones de la cuenta AWS Educate no fue posible.

![InstanceType](Imagenes/instance-type.png)

```
Infraestructura: AWS 

+ AMI: ubuntu/images/hvm-ssd/ubuntu-bionic-18.04-amd64-server-20200408 (ami-085925f297f89fce1)
+ EC2 instance:
  + GPU: 1
  + vCPU: 8
  + RAM: 32 GB
  + OS: Linux AMI 2018.03.0
  + Storage: 32 GB
```
**Paso 3**: Se configuró la instancia siguiendo los pasos de la wiki de AWS del curso de MNO situados la liga web: https://github.com/ITAM-DS/analisis-numerico-computo-cientifico/wiki/1.1.Configuracion-de-servicios-basicos-para-uso-de-AWS.
En resumen, se tuvo que configurar una VPC, una subnet pública, un grupo de seguridad y una IP elástica para no tener que cambiar el comando de conexión cada vez que quisiéramos conectarnos a la EC2.

**Grupo de seguridad**
Se hicieron algunas modificaciones al grupo de seguridad estándar para permitir que todos los miembros del equipo se pudieran conectar de manera fácil al servidor de la EC2  


![AMI](Imagenes/securitygroup.png)
![AMI](Imagenes/inboundrules.png)


**Paso 4**: Se creó un key-pair llamado "key-mno-2020.pem":  


![AMI](Imagenes/keypair.png)


El resultado final fue la siguiente EC2:  


![AMI](Imagenes/ec2.png)


### Instalación de herramientas de trabajo en la EC2

Se decidió trabajar con un contenedor de Docker sobre la instancia que contiene todos los requerimientos necesarios para ejecutar el código del proyecto.
Se corrió un bash script que estaba en la wiki de AWS del repositorio de MNO para instalar git y docker   


![AMI](Imagenes/bash-docker.png)


Se descargó y utilizó la imagen de docker jupyter_numerical para correr nuestro proyecto.  


![AMI](Imagenes/docker-image.png)


El comando usado para correr la imagen fue el siguiente
Correr docker imagen jupyter_numerical

```bash
sudo docker run --rm -v /home/ubuntu:/datos --name jupyterlab_numerical -p 8888:8888 -d palmoreck/jupyterlab_numerical:1.1.0 --ip=0.0.0.0 --no-browser
```
### Conexión a la EC2 y al servidor de Jupyter Lab

Para conectarse a la EC2 se usó el siguiente comando en la dirección donde estaba la llave.pem:
```bash
ssh -i key-mno-2020.pem ubuntu@18.205.126.183
```
Al inicio del proyecto, antes de configurar correctamente el security group, fue necesario usar un comando para hacer portforwarding de la EC2 a nuestra computadora y así visualizar el puerto con el Jupyter Notebook:
```bash
ssh -i "key-mno-2020.pem" -NL localhost:5555:localhost:8888 ubuntu@18.205.126.183
```

Finalmente una vez configurado el security group fue posible conectarse al servidor de Jupyter Lab usando la dirección IP http://18.205.126.183:8888/ e introduciendo el password: querty.

![AMI](Imagenes/login.png)
![AMI](Imagenes/jupyterlab.png)


