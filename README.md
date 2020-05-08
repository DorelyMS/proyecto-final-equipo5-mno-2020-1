## Proyecto Final del curso MNO-2020-1: Equipo 5 y 9

Este es el repositorio de Proyecto Final para la materia de Materia de Métodos Numéricos y Optimización del semestre 2020-1 en la Maestría en Ciencia de Datos, ITAM.

Título del proyecto: `Uso de LIBMF (A LIBrary for large-scale sparse Matrix Factorization) para sistemas de recomendación de películas con una base de datos de usuarios de Netflix`

Objetivo del proyecto: `$Investigación sobre el uso y explotación de la librería LIBMF empleando el lenguaje de programación Python$. El enfoque del estudio, se orienta al estudio de los parámetros y uso de paralelización en los métodos disponibles para el caso práctico de realizar recomendaciones de películas a usuarios de Netflix a través de métodos basados en reducción de dimensionalidad o modelos de factores latentes, así como su comparación y evaluación de resultados a través de una muestra de prueba y entrenamiento.`

Trabajo escrito (fuera del repo): https://www.overleaf.com/read/ffbjdrrxtmdm

Presentación de Resultados (en el repo): [liga_presentación]()

Implementación (en el repo): [Implementación](https://github.com/DorelyMS/proyecto-final-equipo5-mno-2020-1/tree/master/Implementaci%C3%B3n) 

## Indice del proyecto

1. [Introducción]()
2. [Planteamiento del Problema]()
3. [Estructura del equipo]()
4. [Organización del Repositorio]()
5. [Requerimientos de infraestructura]()

## Introducción 

## Planteamiento del problema de sistemas de recomendación

## Estructura del equipo

Para el desarrollo del proyecto, la división de los integrantes considera una distribución adaptada a su porcentaje de avance, por lo que de manera inicial, se dicidió dividir al equipo en 2 partes: el primero y más grande, encargado de la implementación del uso de libmf para resolver nuestro caso práctico (**Equipo de Programación, o P-Team**) y el segundo, encargado de la documentación, revisión de los reportes de resultados para su presentación y trabajo escrito (**Equipo de Revisión, o R-Team**). Finalmente, ambos grupos fueron coordinador por un project manager (**PM**)

La anterior estructura vigente hasta el 10 de mayo, se puede resumir mediante la siguiente tabla:

| #    | Rol                                      | Persona      | Github    |
| ---- | ------------------------ | ------------ | --------- |
| 1    | Programación                             |  Alfie       | gonzalezalfie     |
| 2    | Programación                             |  Guillermo   | gzarazua          |
| 3    | Programación                             |  Javier      | valencig          |
| 4    | Programación                             |  Maggie      | maggiemusa        |
| 5    |Investigación, Revisión & documentación   |  Oscar       | oaguilarca        |
| 6    | Project Manager                          | Dorely       | DorelyMS          |

## Organización del Repositorio

La organización del repositorio se realizó a través una serie de carpetas, las cuales se describen a continuación

+ **Diseño de Muestra:** [obtención de muestra](liga) en esta carpeta se desarrollará el código para la obtención de las muestras de entrenamiento y validación para la base de datos de Netflix que se usará para el reporte de resultados.
+ **Implementación:** [reporte de implementación](liga) del uso de libmf para pruebas con diferentes muestras y parámetros. 
+ **Acances:** contiene un resumen de los [avances de proyecto final](liga) detallado por **PM** y complementado por **P&R Teams** para efecto de reportar al prof los avances en el desarrollo del proyecto, así como las nuevas tareas a realizar.
+ **Resultados**: incluirá el [reporte ejecutivo de resultados](liga) obtenido con la implementación del resultado final sobre nuestra base final depurada sobre nuestro caso práctico generado a partir de una instancia de AWS aplicando paralelización con una imagen de Docker.

## Requerimientos de infraestructura

Con el propósito de reproducibilidad del proyecto y para que todos los equipos (**P-Team**, **R-Team** y **PM**) tuvieran un entorno común de trabajo, se empleó la imagen de docker basada en Python del curso MNO 2020 (palmoreck/jupyterlab_r_kernel:1.1.0) así como una intancia de AWS con las siguientes características.

```bash
docker run --rm -v <ruta a mi directorio>:/datos --name jupyterlab_numerical
-p 8888:8888 -d palmoreck/jupyterlab_numerical:1.1.0
```
Documentación de la imagen de docker palmoreck/jupyterlab_numerical:1.1.0 en [liga](https://github.com/palmoreck/dockerfiles/tree/master/jupyterlab/numerical)

```
Infraestructura: AWS (ESTE SOLO ES UN EJEMPLO)

+ AMI: ami-0915e09cc7ceee3ab, Amazon Linux AMI 2018.03.0 (HVM)
+ EC2 instance:
  + GPU: 1
  + vCPU: 1
  + RAM: 1 GB
+ OS: Linux AMI 2018.03.0
+ Volumes: 1
  + Type: gp2
  + Size: 16 GB
+ RDS: PostgreSQL
  + Engine: PostgreSQL
  + Engine version: 10.6
  + Instance: db.t2.micro
  + vCPU: 1
  + RAM: 1 GB
  + Storage: 80 GB
```
Con ello se habilitó la posibilidad de realizar el trabajo mediante sucesivos *Jupyter Notebooks*.
