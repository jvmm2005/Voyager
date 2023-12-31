"""
En este programa, se encuentran los contextos históricos de las voyagers, las constantes de velocidad, fórmulas de cálculo cinemático cómo las del recorrido
o del año luz.
"""
#Introducción
print ("""Hola, para explicarte lo que voy a contarte en unos instantes vamos a hacer un pequeño experimento. Estás delante de un balón de futbol y le das una patada, ignorando
 las leyes de atracción, el balón se va a ir alejando rápidamente sin parar. Vamos a comprobarlo, suponiendo que has hecho un buen tiro, la velocidad del balón es de más o menos
unos 20m/s, veamos cuanto espacio recorre en el tiempo que tú me digas y en un año.""")


#Velocidad del golpe

VelocidadB = 20


#Definimos una función para calcular el espacio recorrido en un periodo de tiempo general
def recorrido(velocidad,tiempo):
    recorrido = (velocidad*tiempo)
    return recorrido
tiempo = float(input("El tiempo en días:"))


#Creamos variables con la función y con fórmulas físicas
segundos = (tiempo*24*3600)
bolea = recorrido(VelocidadB, segundos)
bolea1 = recorrido(VelocidadB, 31536000)
print ("La pelota ha recorrido" , (bolea/100) , "km en" , tiempo , "días y" , bolea1 , "km en un año")


#Velocidades de las Voyager en metros segundo. para que no haya error de cálculo se utiliza el sistema internacional de medidas (S.I.)

velocidadV1 = 16944.444
velocidadV2 = 16080.556


#Contexto

print ("""¿Sorprendente no? Probablemente haya sido el peor penalti de la historia. Bien, ahora te voy a contar una cosa curiosa. Las Voyager fuéron unos satélites que 
se lanzaron en 1977 con el objetivo de descubrir nuevas cosas en planetas cómo Júpiter, Saturno y otros que no están en nuestro sistema solar (También tenían unos discos 
de oro con el título de canciones de la tierra).
 En su misión, la que ahora es la Voyager 2 (ya que la adelantó su hermana) se paró en la órbita de Júpiter, Saturno, Urano y Neptuno, cosa que la atrasó y permitió
 el avanze de su hermana que solo se paró en Júpiter y en Saturno, actualmente la Voyager 1 es el satélite más alejado de la tierra hasta la fecha a una distancia de 23,3
 miles de millones de kilometros de distancia y se aleja a una velocidad de 61 miles de km/h. Su hermana en cambio va a una velocidad de 57,89 miles de km/h, por lo que 
nunca la alcanzará y se encuentra 19,9 miles de millones de kilometros.\n Ahora toca pensar en futuro, tu solo me tienes que decir un tiempo y yo te diré la distancia a la que
 se encontrarán las Voyager. \n LETS GO BACK TO THE FUTURE""")
años = float(input("El tiempo transcurrido es de (años):"))


#Conversor de unidades de años a segundos segun S.I.

segundos2 = (((años*365)*24)*3600)


#Utilizamos la función para obtener el espacio recorrido específico de cada Voyager y también lo pasamos a años luz

recorrido1 = float(recorrido(velocidadV1,segundos))
recorrido2 = float(recorrido(velocidadV2,segundos))
añoluz1 = (recorrido1/(300000*3600*365*24))
añoluz2 = (recorrido2/(300000*3600*365*24))
print ("En ese periodo de tiempo la voyager1 ha recorrido un total de", (recorrido1/1000), "km y la voyager 2 un total de",(recorrido2/1000), "km divagando por el espacio ")
print ("Debido a estos números tan grandes, utilizamos otraunidad de medida, el año luz, que es el recorrido que hace la luz en un año, que es de unos 300.000 km")
print ("Haciendo los cálculos la voyager 1 ha recorrido", (añoluz1) , "años luz y la voyager 2" , (añoluz2) , "años luz.")