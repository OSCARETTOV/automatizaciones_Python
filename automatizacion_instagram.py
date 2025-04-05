
from instagrapi import Client
from instagrapi.exceptions import ClientError, BadPassword, ChallengeRequired
import time
import random

# Configuración inicial
cuentas = [
    {"usuario": "coloca tu usuario", "contraseña": "coloca tu contraseña"},
    
    
    
]

personas_a_seguir = ["desdeelcamerino.podcast", "neuromodernos"]  # Cuentas a seguir
comentarios_predeterminados = ["¡Gran contenido!", "Excelente", "Contenido de valor"]  # Comentarios predeterminados

# Función para generar tiempos aleatorios
def tiempo_aleatorio(min_segundos, max_segundos):
    return random.uniform(min_segundos, max_segundos)

# Función para simular comportamiento humano
def comportamiento_humano():
    time.sleep(tiempo_aleatorio(1, 3))  # Pausa aleatoria entre acciones
    if random.random() < 0.1:  # 10% de probabilidad de una pausa más larga
        time.sleep(tiempo_aleatorio(5, 10))

# Función para manejar el desafío de seguridad
def manejar_desafio(cliente, usuario):
    try:
        # Solicitar el código de verificación al usuario
        codigo = input(f"Ingresa el código de 6 dígitos enviado a {usuario} (correo/SMS): ")
        cliente.challenge_code_handler(codigo)
        print("Desafío de seguridad resuelto.")
    except Exception as e:
        print(f"Error al manejar el desafío de seguridad: {e}")

# Función para iniciar sesión
def iniciar_sesion(cliente, usuario, contraseña):
    try:
        cliente.login(usuario, contraseña)
        print(f"Inicio de sesión exitoso en la cuenta: {usuario}")
    except ChallengeRequired:
        print(f"Instagram solicitó un desafío de seguridad para la cuenta {usuario}.")
        manejar_desafio(cliente, usuario)
    except BadPassword:
        print(f"Error: Contraseña incorrecta para la cuenta {usuario}.")
    except ClientError as e:
        print(f"Error al iniciar sesión en la cuenta {usuario}: {e}")

# Función para seguir a una persona
def seguir_persona(cliente, usuario):
    try:
        user_id = cliente.user_id_from_username(usuario)
        cliente.user_follow(user_id)
        print(f"Siguiendo a: {usuario}")
        comportamiento_humano()  # Simular comportamiento humano
    except ClientError as e:
        print(f"No se pudo seguir a {usuario}: {e}")

# Función para comentar en una publicación
def comentar_publicacion(cliente, url_publicacion, comentario):
    try:
        media_id = cliente.media_pk_from_url(url_publicacion)
        for letra in comentario:  # Escribir el comentario letra por letra
            time.sleep(tiempo_aleatorio(0.1, 0.3))  # Simular escritura humana
        cliente.media_comment(media_id, comentario)
        print(f"Comentario publicado: {comentario}")
        comportamiento_humano()  # Simular comportamiento humano
    except ClientError as e:
        print(f"No se pudo comentar en la publicación: {e}")

# Función para dar "me gusta" a una publicación
def dar_me_gusta(cliente, url_publicacion):
    try:
        media_id = cliente.media_pk_from_url(url_publicacion)
        cliente.media_like(media_id)
        print(f"Me gusta dado a la publicación: {url_publicacion}")
        comportamiento_humano()  # Simular comportamiento humano
    except ClientError as e:
        print(f"No se pudo dar me gusta a la publicación: {e}")

# Función para explorar publicaciones aleatorias
def explorar_publicaciones(cliente):
    try:
        explorar = cliente.feed_timeline()  # Obtener publicaciones recientes
        for publicacion in explorar[:3]:  # Interactuar con las primeras 3 publicaciones
            if random.random() < 0.5:  # 50% de probabilidad de dar me gusta
                dar_me_gusta(cliente, publicacion.pk)
            if random.random() < 0.3:  # 30% de probabilidad de comentar
                comentario = random.choice(comentarios_predeterminados)
                comentar_publicacion(cliente, publicacion.pk, comentario)
            comportamiento_humano()  # Simular comportamiento humano
    except ClientError as e:
        print(f"Error al explorar publicaciones: {e}")

# Configuración del cliente de Instagrapi
cliente = Client()

try:
    for cuenta in cuentas:
        # Iniciar sesión
        print(f"Iniciando sesión en la cuenta: {cuenta['usuario']}")
        iniciar_sesion(cliente, cuenta["usuario"], cuenta["contraseña"])

        # Seguir a las personas
        for persona in personas_a_seguir:
            print(f"Intentando seguir a: {persona}")
            seguir_persona(cliente, persona)

        # Comentar en publicaciones (necesitas la URL de la publicación)
        for comentario in comentarios_predeterminados:
            print(f"Intentando comentar: {comentario}")
            comentar_publicacion(cliente, "https://www.instagram.com/p/URL_DE_LA_PUBLICACION/", comentario)

        # Dar "me gusta" a una publicación
        print("Intentando dar me gusta a una publicación...")
        dar_me_gusta(cliente, "https://www.instagram.com/p/URL_DE_LA_PUBLICACION/")

        # Explorar publicaciones aleatorias
        print("Explorando publicaciones...")
        explorar_publicaciones(cliente)

        # Cerrar sesión (opcional)
        print("Cerrando sesión...")
        cliente.logout()
        time.sleep(tiempo_aleatorio(3, 5))

except Exception as e:
    print(f"Error inesperado: {e}")
finally:
    print("Proceso finalizado.")
