
------------

# HENRY LABS

------------

# PROYECTO INDIVIDUAL 01
## DATA ENGINEERING & MACHINE LEARNING
### Alejandro Busquet
------------

------------



# PARTE 1: DATA ENGINEERING

## Temática:

Empecé a trabajar como Data Scientist en una start-up que provee servicios de agregación de plataformas de streaming, para lo cual deberé crear mi primer modelo de ML, que solucione un problema de negocio: un sistema de recomendación que aún no ha sido puesto en marcha!

Voy a los datos y me doy cuenta que la madurez de los mismos es poca. Datos sin transformar, no hay procesos automatizados para la actualización de nuevas películas o series, entre otras cosas...

Debo comenzar desde 0, haciendo un trabajo rápido de Data Engineer y tener un MVP (Minimum Viable Product) para la próxima semana! Mi cabeza va a explotar 🤯, pero al menos sé cual es, conceptualmente, el camino que debo de seguir. Así que trato de espantar los miedos y me pongo manos a la obra 💪

## Herramientas:

Para trabajar cuento con 4 datasets correspondiente a 4 plataformas de streaming: Amazon Prime, Disney Plus, Hulu y Netflix, con variada informacion sobre las películas o temporadas.

Por otro lado cuento con 8 datasets adicionales que contienen información referente a los usuarios y sus preferencias.

## Propuesta de trabajo:

- Generar un campo id: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = **a**s123)

- Reemplazo de nulos: Los valores nulos de la columna "rating" deberán reemplazarse por el string “G” (que corresponde al maturity rating: “general for all audiences”)

- Fechas: De haber fechas, deberán tener el formato AAAA-mm-dd

- Texto: Los campos de texto deberán estar todos en minúsculas, sin excepciones

- Columna "duration": Este campo contiene un número y una unidad de medición. Deberá abrirse en dos campos: "duration_int" y "duration_type". El primero será un integer que contendrá la duración, y el segundo un string que indicará la unidad de medición de esa duración ("min" = minutos o "season" = temporadas)

## Objetivos:

1. En la función de Data Engineer, el Tech Lead solicita realizar un proceso de ETL (extracción, transformación y carga) sobre los cuatro datasets proporcionados. Esto con el objetivo de contar con una base lo mas "limpia" posible, que luego permita extraer información valiosa referente tanto a las plataformas como a los catálogos de películas y series que en ellas se ofrece.

2. Se me encarga elaborar una API, a efectos de disponibilizar todos los datos de manera online. Esta API permitirá que la información de la base de datos pueda ser accedida mediante, en este caso, cuatro consultas predefinidas.

3. Como objetivo final para este módulo, se me encargó documentar todo este proceso, subir los archivos a github y confeccionar un video donde se explicarían los pasos realizados y se mostraría el funcionamiento de los distintos procesos.

## Funcionalidades de la API:

Con el propósito de disponibilizar los datos de la empresa, usando un framework como FastAPI, las consultas que deberá responder son las siguientes:

- Película con mayor duración, con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN (la función debe llamarse "get_max_duration(year, platform, duration_type)")

- Cantidad de películas por plataforma, con un puntaje mayor a XX en determinado año (la función debe llamarse "get_score_count(platform, scored, year")

- Cantidad de películas por plataforma, con filtro de PLATAFORMA. (la función debe llamarse "get_count_platform(platform)")

- Actor que más se repite, según plataforma y año (la función debe llamarse "get_actor(platform, year)")

**Hasta acá traté lo referente a las tareas, las propuestas y los objetivos del trabajo, paso a definir las herramientas utilizadas y los pasos efectuados.
**

------------


## Herramientas utilizadas:

- Python: es el lenguaje de programación utilizado, ya que brinda acceso a las librerías apropiadas para realizar la tarea encomendada, de una manera clara, eficaz y eficiente.

- Pandas: framework que representa el complemento perfecto para Python, ya que permite acceder a los archivos csv provistos, su conversión a dataframes, el proceso. de transformación de los datos y la posterior exportación de los mismos a un único archivo, el cual luego será utilizado por la API para disponibilizar los datos.

- Pandasql: librería utilizada en el back, que nos permitió efectuar consultas con lenguaje SQL, sobre los Dataframes de Pandas.

- FastApi: framework para la construcción de la API basada en Python.

- Uvicorn: permite efectuar tests para controlar el funciomaniento de la API de manera local, previo a su despliegue en Render. Maneja también la actualización automática de los archivos de uso, cuando estos son modificados por correcciones, permitiendo una continuidad en dichas pruebas.

- Render: plataforma online y gratuita que permite, mediante una dirección web, disponibilizar tanto la API como los datos, para que puedan ser accedidos y consultados por el usuario mediante su software. Aquí el [link](https://render.com/docs/free#free-web-services "link") y el [tutorial](https://github.com/HX-FNegrete/render-fastapi-tutorial "tutorial").

## Pasos efectuados:

Descargue los cuatro datasets originales y realicé una previsualización de los datos.
Utilizando el Jupyter notebook, importé las librerías necesarias para desempeñar los pasos.

Comencé a trabajar en el ETL, enfocado principalmente en la "Propuesta de trabajo" (detallada arriba), pero también en otros puntos adicionales como la verificación de filas repetidas, eliminación de datos nulos, corrección de datos en campos de texto y demás.

Una vez que tuve disponible una base de datos "limpia", encaré la tarea de las Funciones para la API, creando el archivo "main.py" y realizando las pruebas de manera local mediante las herramientas FastAPI y Uvicorn.

Una vez realizadas algunas tareas extra, y ya depurados los procesos que permitían realizar las consultas encomendadas, subí los archivos y las bibliotecas a Github.

Pasé entonces al proceso del deploy de la API por medio de Render, para lo que tuve que poner a punto algunas cuestiones técnicas, hasta que pude acceder a un dominio y experimentar con diferentes consultas.

## PARTE 2: MACHINE LEARNING

Una vez que los datos son consumibles desde la API y la misma se encuentra lista para ser accedida por los departamentos de Analytics y de Machine Learning, y tenemos un EDA bien realizado, es hora de entrenar nuestro modelo de Machine Learning para que sea capaz de armar un sistema de recomendación de películas para usuarios, por el cual dado un id de usuario y una película, el modelo nos diga si la recomienda o no para dicho usuario.

De ser posible, este sistema de recomendación debe ser deployado para tener una interfaz gráfica amigable para ser utilizada, usando para su deployment "Gradio" o alguna solución como "Streamlit" u otra similar en local (lograr el deployment del sistema de recomendación o una interfaz gráfica son un plus al proyecto).

Para esta etapa dispuse del archivo ya depurado en la primera parte, por lo que procedí a encarar el EDA, correlaciones y outliers.

Luego, utilizando la librería "Surprise", especializada en este arte, pude proporcionarle (mediante el "reader" y "data") los datos que extraje de los 8 datasets, con información valiosa de los usuarios, para que mediante un modelo SVD (Singular Value Decomposition) me devuelva una estimación sobre la recomendación o no de determinada película a ese usuario.

Para medir la validez de esa estimación, utilicé las métricas del RMSE (Root Mean Square Error), MAE (Mean Absolute Error) y las de Precisión, Recall y F1-score.

## Conclusión:

Por último pasé a grabar, editar y publicar el video, en el cual se muestra a la API en funcionamiento, efectuando algunas consultas de muestra. Se accede mediante este [link al video](https://youtu.be/f0zM91a6HRM "link al video").

Para terminar, documenté todos los pasos realizados en este Readme.md, para disponibilidad pública.

Muchas gracias!

##### Autor: Alejandro Busquet
##### Correo: abusquet@hotmail.com / algabu00@gmail.com

