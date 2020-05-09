## Proyecto Final del curso MNO-2020-1: Equipo 5 y 9

Este es el repositorio de Proyecto Final para la materia de Métodos Numéricos y Optimización del semestre 2020-1 en la Maestría en Ciencia de Datos, ITAM.

Título del proyecto: `Uso de LIBMF (A LIBrary for large-scale sparse Matrix Factorization) para sistemas de recomendación de películas con una base de datos de usuarios de Netflix`

Objetivo del proyecto: `**Investigación sobre el uso y explotación de la librería LIBMF empleando el lenguaje de programación Python**. El enfoque del proyecto se orienta al estudio de los parámetros y el uso de paralelización en los métodos disponibles para el caso práctico de realizar recomendaciones de películas a usuarios de Netflix a través de métodos basados en reducción de dimensionalidad o modelos de factores latentes, así como su comparación y evaluación de resultados a través de una muestra de prueba y entrenamiento.`

Trabajo escrito (fuera del repo): https://www.overleaf.com/read/ffbjdrrxtmdm

Presentación de Resultados (en el repo): [liga_presentación]()

Implementación (en el repo): [Implementación](https://github.com/DorelyMS/proyecto-final-equipo5-mno-2020-1/tree/master/Implementaci%C3%B3n) 

## Indice del proyecto

1. [Introducción](https://github.com/DorelyMS/proyecto-final-equipo5-mno-2020-1/blob/master/README.md#introducci%C3%B3n)
2. [Planteamiento del Problema](https://github.com/DorelyMS/proyecto-final-equipo5-mno-2020-1/blob/master/README.md#planteamiento-del-problema-de-sistemas-de-recomendaci%C3%B3n)
3. [Estructura del equipo](https://github.com/DorelyMS/proyecto-final-equipo5-mno-2020-1/blob/master/README.md#estructura-del-equipo)
4. [Organización del Repositorio](https://github.com/DorelyMS/proyecto-final-equipo5-mno-2020-1/blob/master/README.md#organizaci%C3%B3n-del-repositorio)
5. [Requerimientos de infraestructura](https://github.com/DorelyMS/proyecto-final-equipo5-mno-2020-1/blob/master/README.md#requerimientos-de-infraestructura)

## Introducción 

## Planteamiento del problema de sistemas de recomendación

## Estructura del equipo

Para el desarrollo del proyecto, la división de los integrantes considera una distribución adaptada a su porcentaje de avance, por lo que de manera inicial, se decidió dividir al equipo en 2 partes: el primero y más grande, encargado de la implementación del uso de libmf para resolver nuestro caso práctico (**Equipo de Programación, o P-Team**) y el segundo, encargado de la documentación, revisión de los reportes de resultados para su presentación y trabajo escrito (**Equipo de Revisión, o R-Team**). Finalmente, ambos grupos fueron coordinados por un project manager (**PM**)

La anterior estructura vigente hasta el 10 de mayo, se resume en la siguiente tabla:

| #    | Rol                                      | Persona      | Github    |
| ---- | ------------------------ | ------------ | --------- |
| 1    | Programación                             |  Alfie       | gonzalezalfie     |
| 2    | Programación                             |  Guillermo   | gzarazua          |
| 3    | Programación                             |  Javier      | valencig          |
| 4    | Programación                             |  Maggie      | maggiemusa        |
| 5    |Investigación, Revisión & documentación   |  Oscar       | oaguilarca        |
| 6    | Project Manager                          | Dorely       | DorelyMS          |

## Organización del Repositorio

La organización del repositorio se realizó a través una serie de carpetas, las cuales se describen a continuación:

+ **Diseño de Muestra:** En la carpeta [obtención de muestra](liga) se desarrollará el código para la obtención de las muestras de entrenamiento y validación para la base de datos de Netflix que se usará para el reporte de resultados.
+ **Implementación:** [Reporte de implementación](liga) del uso de libmf para pruebas con diferentes muestras y parámetros. 
+ **Avances:** Contiene un resumen de los [avances de proyecto final](liga) detallado por **PM** y complementado por **P&R Teams** para efecto de reportar al profesor los avances en el desarrollo del proyecto, así como las nuevas tareas a realizar.
+ **Resultados**: Incluirá el [Reporte ejecutivo de resultados](liga) obtenido con la implementación del resultado final sobre nuestra base final depurada sobre nuestro caso práctico y generado a partir de una instancia de AWS aplicando paralelización con una imagen de Docker.

## Requerimientos de infraestructura

Con el propósito de reproducibilidad del proyecto y para que todos los equipos (**P-Team**, **R-Team** y **PM**) tuvieran un entorno común de trabajo, se empleó la imagen de docker basada en Python del curso MNO 2020 (palmoreck/jupyterlab_r_kernel:1.1.0) así como una instancia de AWS con las siguientes características:

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
