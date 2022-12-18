#!/usr/bin/env python
# coding: utf-8

# <center> <h1>Universidad Nacional de San Agustín de Arequipa</h1> </center> 
# <center> <h1>Escuela Profesional de Ingeniería de Telecomunicaciones</h1> </center> 
# 
# <center> <h1> </h1> </center> 
# 
# <center><img src="https://www.unsa.edu.pe/wp-content/uploads/sites/3/2018/05/Logo-UNSA.png" width="380" height="4200"></center>
# 

# <center> <h2>Ingeniero Renzo Bolivar - Docente DAIE</h2> </center> 

# <center> <h1>Curso : Computación 1</h1> </center> 

# ![linea 1](https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png)

# <center> <h2>GRUPO A - GRUPO 2</h2> </center> 
# <h2>Alumnos:  </h2>
# <h2>    
# 
#     ABRIL MESTAS RAUL EDILBERTO 
#     ALMIRON PATIÑO ROSA LINDA
#     CCOA CUYO PAULA MARCIA
#     PAREDES MORON ROSARIO ISABEL
# </h2>
# 

# ![linea 1](https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png)

# <center> <h1>INVESTIGACIÓN FORMATIVA</h1> </center> 
# <center> <h1>PROYECTO FINAL</h1> </center> 
# <center> <h1>PYTHON - Inteligencia Artificial</h1> </center> 

# ![linea 1](https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png)

# ## OBJETIVOS

# Los Objetivos de la investigación formativa son:
# 
# - **Competencia Comunicativa** Presentación de sus resultados con lenguaje de programación Python utilizando los archivos Jupyter Notebook.
# - **Competencia Aprendizaje**: con las aptitudes en **Descomposición** (desarticular el problema en pequeñas series de soluciones), **Reconocimiento de Patrones** (encontrar simulitud al momento de resolver problemas), **Abstracción** (omitir información relevante), **Algoritmos** (pasos para resolución de un problema).
# - **Competencia de Trabajo en Equipo**: exige habilidades individuales y grupales orientadas a la cooperación, planificación, coordinación, asignación de tareas, cumplimiento de tareas y solución de conflictos en pro de un trabajo colectivo, utilizando los archivos Jupyter Notebook los cuales se sincronizan en el servidor Gitlab con comandos Git.

# ![linea 1](https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png)

# <center> <h1>Aplicación en IA</h1> </center> 
# <center> <h1>Sistema Recomendador</h1> </center>

# ![linea 2](https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png)

# <div class="alert alert-info">
# El Sistema recomendador deberá encontrar la <strong>compatibilidad o similitud</strong> entre un grupo de personas encuestadas, en las áreas de:
# 
# </div>

# <div class="alert alert-info">
#     
#    -Musica
#    
#    -Peliculas
#     
#    -Comida
#     
#    -Lugares que desean Conocer
#     
#    -Obras de Arte
# 
#     
# 
# 
#     
# </div>

# <div class="alert alert-info">
# 
#     
#    La <strong>compatibilidad o similitud</strong> será encontrada con el algoritmo de <strong>Correlación de Pearson</strong> y será verificada con la <strong>La Matrix de Correlación de Pearson con una librería de Python y utilizando una función personal</strong>
#     
# </div>

# <center> <h1>Base Teórica</h1> </center> 

# ## Análisis de Correlación

# <div class="alert alert-info">
# 
#    A menudo nos interesa observar y medir la <strong>relación entre 2 variables numéricas</strong> mediante el análisis de correlación. 
#    Se trata de una de las *técnicas más habituales en análisis de datos* y el primer paso necesario antes de construir cualquier <strong>modelo explicativo o predictivo más complejo</strong>.
#    Para poder tener el  Datset hay que recolectar información a travez de encuentas.
#     
# </div>

# ### ¿Qué es la correlación?
# 

# La correlación es un tipo de asociación entre dos variables numéricas, específicamente evalúa la **tendencia (creciente o decreciente) en los datos**.
# 
# Dos variables están asociadas cuando una variable nos da información acerca de la otra. Por el contrario, cuando no existe asociación, el aumento o disminución de una variable no nos dice nada sobre el comportamiento de la otra variable.
# 
# Dos variables ***se correlacionan cuando muestran una tendencia creciente o decreciente***.

# ### ¿Cómo se mide la correlación?

# Tenemos el coeficiente de **correlación lineal de Pearson** que se *sirve para cuantificar tendencias lineales*, y el **coeficiente de correlación de Spearman** que se utiliza para *tendencias de aumento o disminución, no necesariamente lineales pero sí monótonas*. 

# ### Correlación de Pearson

# <div class="alert alert-info">
# El coeficiente de correlación lineal de Pearson mide una tendencia lineal entre dos variables numéricas.
# </div>

# Es el método de correlación más utilizado, pero asume que:
# 
#  - La tendencia debe ser de tipo lineal.
#  - No existen valores atípicos (outliers).
#  - Las variables deben ser numéricas.
#  - Tenemos suficientes datos (algunos autores recomiendan tener más de 30 puntos u observaciones).
# 
# Los dos primeros supuestos se pueden evaluar simplemente con un diagrama de dispersión, mientras que para los últimos basta con mirar los datos y evaluar el diseño que tenemos.

# ### Cómo se interpreta la correlación

# El signo nos indica la dirección de la relación, como hemos visto en el diagrama de dispersión.
#  - un valor positivo indica una relación directa o positiva,
#  - un valor negativo indica relación indirecta, inversa o negativa,
#  - un valor nulo indica que no existe una tendencia entre ambas variables (puede ocurrir que no exista relación o que la relación sea más compleja que una tendencia, por ejemplo, una relación en forma de U).

# La magnitud nos indica la fuerza de la relación, y toma valores entre  −1  a  1 . Cuanto más cercano sea el valor a los extremos del intervalo ( 1  o  −1 ) más fuerte será la tendencia de las variables, o será menor la dispersión que existe en los puntos alrededor de dicha tendencia. Cuanto más cerca del cero esté el coeficiente de correlación, más débil será la tendencia, es decir, habrá más dispersión en la nube de puntos.
# 
# si la correlación vale  1  o  −1  diremos que la correlación es “perfecta”,
# si la correlación vale  0  diremos que las variables no están correlacionadas.

# <center><img src="https://user-images.githubusercontent.com/25250496/204172549-2ccf3be3-a2b3-4b49-9cd4-adb66e28621d.png" width="700" height="4200"></center>
# 

# <center> <h3>Fórmula Coeficiente de Correlación de Pearson</h3> </center>  
# <center> <h3> </h3> </center> 
# $$ r(x,y)=\frac{\sum_{i=1}^{n}(x_{i}-\overline{x})(y_{i}-\overline{y})}{\sqrt{\sum_{i=1}^{n}(x_{i}-\overline{x})^{2}}\sqrt{\sum_{i=1}^{n}(y_{i}-\overline{y})^{2}}}$$

# **Distancia Euclidiana**: La distancia euclidiana es la generalización del __`teorema de Pitágoras`__.

# $$d_{E}(x,y)=\sqrt{\sum_{i=1}^{n}(x_{i}-y_{i})^{2}}$$

# **Regresión Lineal**: La regresión lineal se usa para encontrar una __`relación lineal entre el objetivo y uno o más predictores`__.

# ![que-es-la-regresion-lineal-y-para-que-sirve](https://user-images.githubusercontent.com/25250496/204172072-0fabbfdf-1c4c-4f9b-8f42-505d98b18b71.png)

# <div class="alert alert-info">
# <strong>MARCO TEÓRICO</strong>
# </div>

# ### ¿Que es machine learning?

# Machine learning: Es una rama de la inteligencia artificial que es autónoma ya que puede realizar predicciones a partir de procesamiento de datos.
# Esta tecnología está presente en un sinfín de aplicaciones como las recomendaciones de Netflix o Spotify, las respuestas inteligentes de Gmail o el habla de Siri y Alexa.
# El ‘machine learning’ es un maestro del reconocimiento de patrones, y es capaz de convertir una muestra de datos en un programa informático capaz de extraer inferencias de nuevos conjuntos de datos para los que no ha sido entrenado previamente
# Aunque ahora esté de moda, gracias a su capacidad para derrotar a jugadores del Go o resolver cubos de Rubik, su origen se remonta al siglo pasado. “La estadística es sin duda la base fundamental del aprendizaje automático, que básicamente consiste en una serie de algoritmos capaces de analizar grandes cantidades de datos para deducir cuál es el resultado más óptimo para un determinado problema”, añade Espinoza.
# 

# <img src="https://www.atriainnovation.com/wp-content/uploads/2021/02/portada.jpg">

# ### LIBRERIAS PARA CIENCIA DE DATOS:
# 
# Conjuntos de archivos de código que han sido creados para desarrollar software de manera sencilla. Gracias a ellas, los desarrolladores pueden evitar la duplicidad de código y minimizar errores con mayor agilidad .Estas librerías son altamente prácticas a la hora de implementar flujos de Machine Learning. 

# librerías para ciencia de datos:
# Conjuntos de archivos de código que han sido creados para desarrollar software de manera sencilla. Gracias a ellas, los desarrolladores pueden evitar la duplicidad de código y minimizar errores con mayor agilidad .Estas librerías son altamente prácticas a la hora de implementar flujos de Machine Learning. 

# <img src="data:image/jpeg;base64,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">

# #### ¿Que es NUMPY?
# 
# Es una librería de Python especializada en el cálculo numérico y el análisis de datos, especialmente para un gran volumen de datos.Incorpora arrays lo que permite representar colecciones de datos de un mismo tipo en varias dimensiones, y funciones muy eficientes para su manipulación.Además cuenta con múltiples herramientas para manejar matrices de una forma muy eficiente.
# 
# El módulo Numpy introduce en escena un nuevo tipo de objeto, ndarray (n dimensional array), caracterizado por:
#    - Almacenamiento eficiente de colecciones de datos del mismo tipo
#    - Conjunto de métodos que permiten operar de forma vectorizada sobre sus datos
# 
# Las formas más habituales de crear un nuevo array son:
#    - A partir de otras colecciones de datos de Python, como listas o tuplas
#    - Desde cero mediante funciones específicas
#    - Leyendo los datos de un fichero

# <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_VfYfuw4JGQC0QLtbrhWyAQgW9qD9fXanG34lWGAyI1y34PxtAPagPNkCTAoX7_x7sFw&usqp=CAU">

# <img src="https://aprendeconalf.es/docencia/python/manual/img/arrays.png">

# ### ¿Qué es Pandas?
# 
# Pandas es una librería de código abierto que ofrece unas estructuras muy poderosas y flexibles que facilitan la manipulación y tratamiento de datos.Las principales funciones de pandas son :cargar datos, modelar, analizar, manipular y prepararlos.
# 
# ### Estructuras de datos Pandas:
# 
# Cuenta con dos estructuras estas son:
#   - Series: array unidimensional etiquetado capaz de almacenar cualquier tipo de dato.
#   - DataFrame: estructura bidimensional con columnas que pueden ser también de cualquier tipo. Estas columnas son a su vez Series.
# 
# ### ¿Como analizar datos con Pandas?
# 
#    - head(n): Esta función devuelve las primeras n filas de nuestro DataFrame.
#    - tail(n): Devuelve las n últimas filas de nuestro DataFrame.
#    - describe(): Esta función da estadísticas descriptivas incluyendo aquellas que resumen la tendencia central,        dispersión y la forma de la distribución de los datos.

# <img src="data:image/png;base64,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">

# <img src="https://profile.es/wp-content/media/Estructuras-de-datos-en-Pandas-1.png">

# ¿Qué es matplotlib?
# Es una biblioteca para la generación de gráficos en dos dimensiones, a partir de datos contenidos en listas en el lenguaje de programación Python. Permite crear y personalizar los tipos de gráficos más comunes, entre ellos:
# 
#    - Diagramas de barras
#    - Histograma
#    - Diagramas de sectores
#    - Diagramas de caja y bigotes
#    - Diagramas de violín
#    - Diagramas de dispersión o puntos
#    - Diagramas de lineas
#    - Diagramas de areas
#    - Diagramas de contorno
#    - Mapas de color
# Mapas de color y combinaciones de todos ellos.

# <img src="https://matplotlib.org/3.1.1/_static/logo2_compressed.svg">

# <img src="https://miro.medium.com/max/1400/1*JTEqCz-VU16nkkUwzyWp_w.png">

# ## Seaborn:
# Es una librería para Python que permite generar fácilmente gráficos. Seaborn está basada en matplotlib y proporciona una interfaz de alto nivel . Tiene como objetivo convertir la visualización en una parte central de la exploración y comprensión de los datos, generando atractivas gráficas con sencillas funciones que ofrecen una interfaz semejante, facilitando el paso de unas funciones a otras.

# <img src="https://livecodestream.dev/post/how-to-build-beautiful-plots-with-python-and-seaborn/featured.jpg">

# ### ¿Qué es la escala Likert?
# 
# Se utiliza para medir qué tan de acuerdo están los encuestados con una variedad de afirmaciones.Esta es ideal para medir reacciones, actitudes y comportamientos de una persona.
# A diferencia de una simple pregunta de “sí” / “no”, la escala de Likert permite a los encuestados calificar sus respuestas.
# 
# La escala de Likert es uno de los tipos de escalas de medición utilizados principalmente en la investigación de mercados para la comprensión de las opiniones y actitudes de un consumidor hacia una marca, producto o mercado meta. Nos sirve principalmente para realizar mediciones y conocer sobre el grado de conformidad de una persona o encuestado hacia determinada oración afirmativa o negativa.
# 
# Las respuestas pueden ser ofrecidas en diferentes niveles de medición, permitiendo escalas de 5, 7 y 9 elementos configurados previamente. Siempre se debe tener un elemento neutral para aquellos usuarios que ni de acuerdo ni en desacuerdo.

# <img src="https://www.questionpro.com/blog/wp-content/uploads/2018/06/LIKERT-OKOK-768x512.jpg">

# ### CSV (Valores Separados por Comas):
# 
# Es el formato más común de importación y exportación de hojas de cálculo y bases de datos. Es cualquier archivo de texto en el cual los caracteres están separados por comas, haciendo una especie de tabla en filas y columnas. Las columnas quedan definidas por cada punto y coma (;), mientras que cada fila se define mediante una línea adicional en el texto. De esta manera, se pueden crear archivos CSV con gran facilidad.
# 
# ### ¿Para qué sirve un archivo CSV?
# 
# Los archivos CSV sirven para manejar una gran cantidad de datos en formato tabla, sin que ello conlleve sobrecoste computacional alguno. Es tremendamente sencillo generar una tabla a partir de un documento de texto, con tan solo delimitar cada celda requerida con un punto y coma o con una coma). 

# <img src="https://acf.geeknetic.es/imgri/imagenes/tutoriales/definiciones/2020/6/Archivo-CSV-qrdy.jpg?f=webp">

# ## Gráfica de calor
# Un gráfico de calor se usa para visualizar la relación numérica existente entre dos variables de categorías.Esta consiste en una cuadrícula rectangular compuesta de dos variables de categorías,cada celda de la cuadrícula se simboliza con un valor numérico.
# tiene limitaciones?
# Las variables de un gráfico de calor no pueden tener más de 3.000 valores únicos por eje. Si una de las variables o ambas exceden el límite de 3.000 valores, puede usarse un filtro, por ejemplo, un filtro predefinido, para reducir el tamaño del dataset.
# 
# ## Matriz de correlación:
# Es una tabla que indica los coeficientes de conexión entre los factores,se utiliza para bosquejar información, como contribución a una investigación más desarrollada. Normalmente, un marco de relación es “cuadrado”, con factores similares que aparecieron en las líneas y secciones.
# Aplicaciones de una matriz de correlación
# medición de la relación
# La mayoría de los marcos de relación utilizan la Conexión de Minuto de Artículo de Pearson (r). 
# Codificación de los factores
# En el caso de que también tengas información de un resumen, tendrás que elegir cómo codificar la información antes de procesar las conexiones.
# Tratamiento de las cualidades que faltan
# La información que utilizamos para procesar las conexiones a menudo contiene cualidades que faltan. Esto puede deberse a que no hemos recogido esta información o a que no tenemos la menor idea de las reacciones. Existen diferentes procedimientos para manejar las cualidades perdidas cuando se procesan las redes de conexión. La mejor práctica es, en su mayor parte, utilizar numerosas atribuciones.
# 
# ## Ques es un Dashboard?
# Es una herramienta personalizable de visualización de datos, que te ayuda a conectar tus archivos, servicios, API o archivos adjuntos, y muestra estos datos como tablas, tipos de gráficas u otras visualizaciones de datos al espectador y reduce el esfuerzo manual.
# tipos de dashboard
# 

# ### ¿Cómo funcionan los dashboards?
# 
# Los dashboards responden a preguntas importantes sobre tu negocio. A diferencia de las herramientas avanzadas de inteligencia empresarial, los dashboards están diseñados para el análisis rápido y el conocimiento de la información. El enfoque más común para diseñar un dashboard es construirlo utilizando un formato de pregunta-respuesta.

# # DATOS FALTANTES
# 
# 
# 
# Son aquellos que no constan debido a cualquier acontecimiento, como por ejemplo errores en la transcripción de los datos o la ausencia de disposición a responder a ciertas cuestiones de una encuesta. Los datos pueden faltar de manera aleatoria o no aleatoria.
# 
# 
# Los datos faltantes aleatorios pueden perturbar el análisis de datos dado que disminuyen el tamaño de las muestras y en consecuencia la potencia de las pruebas de contraste de hipótesis. Los datos faltantes no aleatorios ocasionan, además, disminución de la representatividad de la muestra.
# 
# 
# Tratamiento
# 
# 
# # De casos completos o eliminación por lista
# 
# 
# Este procedimiento consiste en incluir en el análisis los casos que presentan observaciones completas en todas las variables. Este método solo debe utilizarse cuando el proceso de recogida de datos es aleatorio, porque en otro caso introduce sesgo. Otro inconveniente es que el tamaño muestral puede llegar a sufrir una gran reducción y afectar a la representatividad de la muestra.
# 
# 
# Selección por variables
# 
# 
# Se mantienen en la base de datos los casos con tal que tengan datos en las variables que van a ser utilizadas para el análisis. Este procedimiento tiene el inconveniente de generar muestras heterogéneas.
# 
# 
# # Métodos de imputación
# 
# 
# Los métodos de imputación consisten en estimar los valores ausentes en base a los valores válidos de otras variables y/o casos de la muestra. La estimación se puede hacer a partir de la información del conjunto completo de variables o bien de algunas variables especialmente seleccionadas. Usualmente los métodos de imputación se utilizan con variables métricas (de intervalo o de razón), y deben aplicarse con gran precaución porque pueden introducir relaciones inexistentes en los datos realas.
# 
# 
# ## Principales procedimientos:
# 
# 
# # Sustitución por la Media. Consiste en sustituir el valor ausente por la Media de los valores válidos. Este procedimiento plantea inconvenientes como:
# 
# Dificulta la estimación de la Variáncia.
# 
# Distorsiona la verdadera distribución de la variable,
# 
# Distorsiona la correlación entre variables dado que añade valores constantes.
# 
# 
# Sustitución por constante. Consiste en sustituir los valores ausentes por constantes cuyo valor viene determinado por razones teóricas o relacionadas con la investigación previa. Presenta los mismos inconvenientes que la sustitución por la Media, y solo debe ser utilizado si hay razones para suponer que es más adecuado que el método de la media.
# 
# 
# Imputación por regresión. Este método consiste en estimar los valores ausentes en base a su relación con otros variables mediante Análisis de Regresión.
# 
# 
# Inconvenientes:
# 
# 
# - Incrementa artificialmente las relaciones entre variables.
# 
# - Hace que se subestime la Variáncia de las distribuciones.
# 
# - Asume que las variables con datos ausentes tienen relación de alta magnitud con las otras variables.

# # ¿Qué es un framework?
# Es una especie de plantilla, un esquema conceptual, que simplifica la elaboración de una tarea, ya que solo es necesario complementarlo de acuerdo a lo que se quiere realizar.

# ![linea 2](https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png)

# <center> <h1>Propuesta</h1> </center> 

# ![linea 2](https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png)

# ## 1.- Dataset

# #### Formulario de Google (Preguntas)

# - Por Ustedes 
# - ME VAS A EXTRAÑAR
# - TE VI VENIR 
# - MARC ANTHONY -VIVIR MI VIDA
# - LOS 4 FT LOS BARRAZA - ESE HOMBRE
# - IMAGINE DRAGONS - BELIEVER 
# - ED SHEERAN - SHAPE OF YOU
# - AVICII - WAKE ME UP 
# - ROMEO SANTOS - PROPUESTA INDECENTE
# - LADY GAGA - BLOODY MARY
# - SODA STEREO - DE MUSICA LIGERA
# - LUIS FONSI -  NO ME DOY POR VENCIDO
# - HARRY STYLES - SIGN OF THE TIMES 
# - COLDPLAY - YELLOW
# - BOM JOVI- IT'S MY LIFE 
# - FOUDEQUSH  CON LA BRISA 
# - TAYLOR SWIFT - SHAKE IT OFF 
# - VICTOR MANUEL - MALA TU
# - GIAN MARCO GRUPO 5 - EL RITMO DE MI CORAZON
# - DON OMAR - LOS BANDOLEROS
# - LOS DAVALOS - MONTONERO AREQUIPEÑO
# - EVA AYLLON - SACA LAS MANOS
# - OCOBAMBA -MATADOR
# - WILLIAN LUNA - NIÑACHAY
# - LOS KJARKAS - LLORANDO SE FUE
# - BAD BUNNY- UN VERANO SIN TI
# - J BALVIN Y MARIA BECERRA - QUE MAS PUES 
# - ROSALIA - DESPECHÁ
# - DON OMAR - DANZA KUDURO
# - OZUNA - HEY MOR
# - BECKY G , CAROL G - MAMIII
# - RIO ROMA - MI PERSONA FAVORITA
# - CARLOS BAUTE - COLGANDO EN TUS MANOS
# - HA ASH - PERDON
# - JESSE Y JOY - CORRE
# - REIK - CREO EN TI

# #### Formulario de Google (Imagenes)

# <img src="https://z-p3-scontent.flim4-3.fna.fbcdn.net/v/t39.30808-6/317694224_674692240897506_910912979828170038_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=730e14&_nc_eui2=AeFgGMz-M4_Pw_LSIwWFHFChxp3mv3BnjurGnea_cGeO6m7y9aNskPGgsou1EaeiYLyKhSWH4HbYO4pyo7sf2xqR&_nc_ohc=OyYqST3sJ2QAX939fR9&_nc_zt=23&_nc_ht=z-p3-scontent.flim4-3.fna&oh=00_AfDuP86VJJdb3AowWnc-CysrBun6Iz5JE-Mh3gIWzbEdLA&oe=6390D67C">

# <img src="https://z-p3-scontent.flim4-2.fna.fbcdn.net/v/t39.30808-6/317843467_674692367564160_2795522244153562413_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=730e14&_nc_eui2=AeHOjHYYkjm6gJtHcWDJ-hCOiDfuSwKyGquIN-5LArIaqxvHXeMUjMYssJEfEu2pMlk1YhTZ2z0W60QiaOCSjAeB&_nc_ohc=NMBTf6Tg9LAAX80G2n0&_nc_zt=23&_nc_ht=z-p3-scontent.flim4-2.fna&oh=00_AfDp8trj1-cbEIyC1wWZHipcxoTCVHUHT1HJEdFYPUJlQg&oe=639109A3">

# <img src="https://z-p3-scontent.flim4-3.fna.fbcdn.net/v/t39.30808-6/317483153_674692574230806_5594513295833318242_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=730e14&_nc_eui2=AeHZsX8HZ2O5I9zv3apOR_yT6947wX8Ogk7r3jvBfw6CTr1uACq6SZwJ2v5EdnZcf1bu78Ytj88DHVwCEvcwj9G4&_nc_ohc=Yb28KXU6cv0AX_zcBGz&_nc_zt=23&_nc_ht=z-p3-scontent.flim4-3.fna&oh=00_AfBz95U-vnytIG06_aoWiXzcC4o3AjdLG9l2GxRs1LaC1g&oe=6390DED9">

# #### Formulario de Google (Preprocesamiento)

# <img src="https://lh5.googleusercontent.com/4TxVanCwusmM0iQJ-1MSWnLnuA86TrqFLcV7i8lQrdT8QSxLR6dumcXVeTtpdcLadFHTEX8Paeb_OI6Om5pgiJ2OQFN8eFEYUwj4edtdEyh9NRYXwDQGGEd339I59mzIFSLH3skS3TfRFjgsbdgPVw">

# <img src="https://lh3.googleusercontent.com/NgHLwBMshmFIWxXx2nzNFzclrCRGhqe8f36IAQDQPrY6jXWhOx4URiCd8OaYRKtu2YQgQhKzIxO2zZODseM9gtSIsg6Gt_SK4GUBRQyECkdy8_BY6t09WBCH_0GPeN8EJbArGZWWZ8ty3GBGZ8uWKg">

# <img src="https://lh3.googleusercontent.com/CJBueIa7aNHpzyE0LhHvYTdFnjNqQ5F90gSOwYT0n_f8BUsFXcsEfAp3MJHrqiqamNCD2qaU69IhhNlH_WjP3LEc8BzL1RfZ0tMUQoRcY3oieQmRkhC8QMqf2vUbuNFxkBrJY2zwraxj9Zb_V2s0zg">

# <img src="https://lh5.googleusercontent.com/ipbTYAbUz0rsV7JUzwzlZ8AeOgrxGhWWDaL9qrQcq1c4rrJFpzxlxFwzDO2_e_U6Ln5HOjbarC8twdlsWWkoL6ypO-whGQbadWedQyhF_hp-qlEhX5way0RCNx5sLtl7CpocJtwnMs2bbJn4Pbw5LQ">

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
datos=pd.read_csv("ENCUESTA.csv")
datos


# In[2]:


datos.shape


# In[3]:


datos.isnull().sum()


# In[4]:


datos.dtypes


# # IMPUTACION 

# In[5]:


datos.describe()


# In[6]:


ndatos=datos.fillna({"POR USTEDES":4,"PROPUESTA INDECENTE":4,"SIGN OF THE TIMES ":4,"BLOODY MARY":4,"MY LIFE ":4,"CON LA BRISA ":3,"MALA TU":3,"MONTONERO AREQUIPENO":4,"MATADOR":3,"NINACHAY":5,"UN VERANO SIN TI":3,"QUE MAS PUES ":3,"DESPECHA":3,"DANZA KUDURO":4,"HEY MOR":3,"MAMIII":3,"COLGANDO EN TUS MANOS":4,"CREO EN TI":4})
ndatos


# In[7]:


ndatos.isnull().sum()


# # CORRELACION DE PEARSON

# In[8]:


n = datos[datos.columns[1:]].to_numpy()
m = datos[datos.columns[0]].to_numpy()
print(n)
print(m)


# # CORRELACION PANDAS

# In[9]:


n.T


# In[11]:


df=pd.DataFrame(n.T, columns = m)
df


# In[12]:


m_corr=df.corr()
m_corr


# # MATRIX DE CORRELACION

# In[13]:


m_corr_d = np.round(m_corr, 
                       decimals = 2)  
  
m_corr_d 


# In[14]:


m_corr_d 


# # GRAFICA DE CALOR

# In[15]:


sns.heatmap(m_corr_d)


# # Propuesta

# In[16]:


n1 = ndatos[ndatos.columns[1:]].to_numpy()
m1 = ndatos[ndatos.columns[0]].to_numpy()
print(n1)
print(m1)


# """
# El coeficiente de correlación viene dado por:
# 
#               (â.T)b̂
#             -----------
#             ||â||.||b̂||
# donde â y b̂ son 
#   â = a - mean(a)*1
#   b̂ = b - mean(b)*1
# Donde â.T es la transpuesta de â
# """
# 
# 
# 
# 

# In[54]:


calculo_pearson=[]
def correlax_pearson(x,y):
    mx=x.mean()
    my=y.mean()
    num=np.sum((x-mx)*(y-my))
    den=np.sqrt(np.sum((x-mx)**2)*np.sum((y-my)**2))
    return num / den
for i in range(len(m1)):
    for j in range(len(m1)):
        caln=ndatos.loc[[i,j],:]
        ndt=caln[caln.columns[1:]].to_numpy()
        calculo_pearson.append(correlax_pearson(ndt[0],ndt[1]))
rpearson=np.array(calculo_pearson).reshape(len(m1),len(m1))
mostrar=pd.DataFrame(rpearson,m1,m1)
mostrar


# In[55]:



corf=pd.DataFrame(n1.T, columns = m1)
corf


# In[56]:


corrmusica=corf.corr()
corrmusica


# In[85]:


corrmusica_= np.round(corf, 
                       decimals = 4)  
  
corrmusica_ 


# In[86]:


corrmusica_


# In[95]:


def correx(corr_mat):
    '''
    Función para convertir una matriz de correlación de pandas en formato tidy.
    '''
    corr_mat = corr_mat.stack().reset_index()
    corr_mat.columns = ['Nombres1','Nombres2','r']
    corr_mat = corr_mat.loc[corr_mat['Nombres1'] != corr_mat['Nombres2'], :]
    corr_mat['abs_r'] = np.abs(corr_mat['r'])
    corr_mat = corr_mat.sort_values('abs_r', ascending=False)
    
    return(corr_mat)

correx(corrmusica).head()


# In[91]:


import pingouin as pg
ncor=pg.pairwise_corr(corrmusica,method='spearman')
ncor.sort_values(by=['p-unc'])[['X','Y','n','r','p-unc']]


# In[93]:


import pingouin as pg
ncor=pg.pairwise_corr(corrmusica,method='pearson')
ncor.sort_values(by=['p-unc'])[['X','Y','n','r','p-unc']]


# In[57]:


corrmusica_spearman=corf.corr(method="spearman")
corrmusica_spearman


# # resultados automaticos con funcion de busqueda de 2 valores maximos

# In[ ]:





# In[59]:


maximos=resultado.unstack()
print(maximos.sort_values(ascending=False)[range(len(n1),((len(n1)+12)))])


# In[34]:


corrmusica.max().idxmax()


# # PRIMER MAXIMO

# In[128]:


corrmusica[corrmusica==1]=0
primermaximo=corrmusica.max()
primermaximo.max()


# In[129]:


primermaximo


# # SEGUNDO MAXIMO

# In[130]:


corrmusica[corrmusica==0.9211637210055882]=0
segundomaximo=corrmusica.max()
segundomaximo.max()


# In[131]:


segundomaximo


# In[135]:


print(corrmusica.corr())(ascending=True)


# In[65]:


sns.heatmap(resultado,cmap="hot")


# In[92]:


from scipy.spatial.distance import euclidean
Z=int(len(m1))
L=np.zeros((Z,Z))
for i in range (Z):
    for j in range(Z):
        print("\nEntre",m1[i],'y' ,n1[j],'\ntenemos: ')
        dist=euclidean(n1[i],n1[j])
        print('\tDistancia = ',dist)
        simil=1/(1+dist)
        L[i,j]=simil
        print('\tSimlitud = ',simil)


# # INDICE MAS ALTO

# In[93]:


t=L[L<1].max()
r=np.max(t)
print("el indice mas alto es: ",r)


# # CASO NETFLIX

# In[96]:


datos.loc[[0,1],["POR USTEDES"]]


# In[97]:


ndatos.loc[[0,1],["POR USTEDES"]]


# In[98]:


ndatos.loc[[0,1],["POR USTEDES","ME VAS A EXTRANAR"]]


# ## 5.- RESULTADOS 

#  1. _noeliaparedesgu@gmail.com	_ y _gparedesg@unsa.edu.pe_  obtienen el **PRIMER** indice mas alto de similitud 
#  
#  2. _noeliaparedesgu@gmail.com_ y _elhuamani@unsa.edu.pe_ obtienen el **SEGUNDO** indice mas alto de similitud 

# In[99]:


plt.scatter(mostrar["noeliaparedesgu@gmail.com"],mostrar["gparedesg@unsa.edu.pe"])
plt.xlabel("noeliaparedesgu@gmail.com")
plt.ylabel("gparedesg@unsa.edu.pe")
plt.title("Relacion entre noeliaparedesgu@gmail.com y gparedesg@unsa.edu.pe")
plt.show


# In[103]:


plt.scatter(mostrar["noeliaparedesgu@gmail.com"],mostrar["elhuamani@unsa.edu.pe"])
plt.xlabel("noeliaparedesgu@gmail.com")
plt.ylabel("elhuamani@unsa.edu.pe")
plt.title("Relacion entre noeliaparedesgu@gmail.com y  elhuamani@unsa.edu.pe ")
plt.show


# <center> <h1>Conclusiones</h1> </center> 

# # Se importo los datos obtenidos del formulario mediante el formato csv el cual nos permitio la lectura de datos del formulario delimitado por comas 
# # Se imputo los datos Nah los cuales no permitian que el algoritmo funcione correctamente
# # El metodo de imputacion de datos es mediante la media, luego de obtener los datos con la funcion describe() se pueden observar valores excatos los cuales nos ayudan a una imputacion
# # La necesidad de librerias como el pandas y el numpy nos ayudan a la lectura de datos y a mostrar los graficos 
# # Se delimito la importancia de imputacion de datos  y la distancia euclidiana 

# ![linea 1](https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png)

# # REFERENCIAS

# - __Profesor de Matematicas__: `John Gabriel Muñoz Cruz`
# https://www.linkedin.com/in/jgmc

# ![linea 1](https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png)

# BIBLIOGRAFÍA 
# 
# https://aprendeconalf.es/docencia/python/manual/numpy/#:~:text=NumPy%20es%20una%20librer%C3%ADa%20de,un%20gran%20volumen%20de%20datos. 
# 
# 
# 
# https://doc.arcgis.com/es/insights/latest/create/heat-chart.htm 
# 
# https://datascience.eu/es/matematica-y-estadistica/que-es-una-matriz-de-correlacion/ 
# 
# https://www.lifeder.com/distancia-euclidiana/ 
# 
# https://tudashboard.com/que-es-un-dashboard/ 
# 
# https://www.cursosgis.com/que-es-streamlit/ 
# 
# https://rockcontent.com/es/blog/framework/ 
