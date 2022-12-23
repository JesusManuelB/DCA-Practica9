import sqlite3


        conexion = sqlite3.connect("database.sqlite3")
        cursor = conexion.cursor()
except Exception as ex:
        print(ex)

def creaDB():
        cursor.execute("CREATE TABLE IF NOT EXISTS USUARIO (USERNAME TEXT NOT NULL, PASSWORD TEXT NOT NULL,CONSTRAINT PK_USUARIO PRIMARY KEY (USERNAME))")
        cursor.execute("CREATE TABLE IF NOT EXISTS PROBLEMA (DESCRIPCION TEXT NOT NULL, USUARIO TEXT NOT NULL, ESTADO TEXT NOT NULL, CONSTRAINT PK_PROBLEMA PRIMARY KEY (DESCRIPCION), CONSTRAINT PK_PROBLEMA FOREIGN KEY (USUARIO) REFERENCES USUARIO(USERNAME))")
        cursor.execute("CREATE TABLE IF NOT EXISTS COMENTARIO (CONTENIDO TEXT NOT NULL, PROBLEMA TEXT NOT NULL, CONSTRAINT PK_COMENTARIO PRIMARY KEY (CONTENIDO), CONSTRAINT PK_COMENTARIO FOREIGN KEY (PROBLEMA) REFERENCES PROBLEMA(DESCRIPCION))")
    except Exception as ex:
        print("Error al crear la Base de Datos.")


def insertarUsuario(username, passw):
        sentencia = "INSERT INTO USUARIO('USERNAME', 'PASSWORD') VALUES(?, ?)"
        cursor.execute(sentencia,(username, passw))
        print("Usuario registrado correctamente.")
        conexion.commit()
    except Exception as ex:
        print(ex)

def comprobarAutenticacion(username, passw):
    t
        sentencia = "SELECT * FROM USUARIO WHERE USERNAME = ? AND PASSWORD = ?"
        cursor.execute(sentencia,(username, passw))
        if(len(cursor.fetchall())==0):
            print("Usuario no encontrado.")
            conexion.commit()
            return 0
        else:
            print("Usuario autenticado.")
            conexion.commit()
            return 1
    except Exception as ex:
        print(ex)
        return 0


def insertaIssue(username, nombreIssue):
    try:
        estado = 1
        sentencia = "INSERT INTO PROBLEMA('DESCRIPCION', 'USUARIO', 'ESTADO') VALUES (?, ?, ?)"
        cursor.execute(sentencia, (nombreIssue, username, estado))
        print("Problema registrado correctamente.")
        conexion.commit()
    except Exception as ex:
        print(ex)

def cierraIssue(username, nombreIssue):
    try:
        sentencia = "UPDATE PROBLEMA SET ESTADO = 0 WHERE DESCRIPCION = ? AND USUARIO = ?"
        cursor.execute(sentencia, (nombreIssue, username))
        print("Problema cerrado.")
        conexion.commit()
    except Exception as ex:
        print(ex)

def reabreIssue(username, nombreIssue):
    try:
        sentencia = "UPDATE PROBLEMA SET ESTADO = 1 WHERE DESCRIPCION = ? AND USUARIO = ?"
        cursor.execute(sentencia, (nombreIssue, username))
        print("Problema reabierto.")
        conexion.commit()
    except Exception as ex:
        print(ex)

def listarIssues(username):
    try:
        sentencia = "SELECT * FROM PROBLEMA WHERE USUARIO = ? AND ESTADO = 1"
        cursor.execute(sentencia, (username,))
        rows = cursor.fetchall()
        print("listado de Problemas:")
        valor = [row[0] for row in rows]
        print(valor)
        conexion.commit()
    except Exception as ex:
        print(ex)

def verHistorialIssue(nombre, username):
    try:
        sentencia = "SELECT * FROM PROBLEMA WHERE DESCRIPCION = ? AND USUARIO = ? AND ESTADO = 1"
        cursor.execute(sentencia, (nombre, username))
        if(len(cursor.fetchall())==0):
            print("Problema cerrado o no registrado.")
            conexion.commit()
        else:
            sentencia = "SELECT * FROM COMENTARIO WHERE PROBLEMA = ?"
            cursor.execute(sentencia, (nombre,))
            rows = cursor.fetchall()
            valor = [row[0] for row in rows]
            print("Histórico de comentarios:")
            for i in range(len(valor)):
                print(valor[i])
            conexion.commit()
    except Exception as ex:
        print(ex)

def insertarComentario(comentario, nombre):
    try:
        sentencia = "INSERT INTO COMENTARIO('CONTENIDO', 'PROBLEMA') VALUES(?, ?)"
        cursor.execute(sentencia,(comentario, nombre))
        print("Comentario registrado correctamente.")
        conexion.commit()
    except Exception as ex:
        print(ex)

creaDB()
print("Bienvenido a GitBit, seleccione la acción a realizar: ")
print("1 - Registro")
print("2 - Inicio de sesión: ")
entrada = int(input())
activo = 1
if(entrada == 1):
    print("Introduzca el username ")
    username = input()
    print("Ahora introduzca la contraseña: ")
    passw = input()
    insertarUsuario(username, passw)
if(entrada == 2):
    print("Introduzca el username ")
    username = input()
    print("Ahora introduzca la contraseña: ")
    passw = input()
if(comprobarAutenticacion(username, passw) == 1):
    activo = 1
else:
    activo = 0
while activo == 1:
    print("1 - Crear issue")
    print("2 - Comentar issue: ")
    print("3 - Ver historial de la issue: ")
    print("4 - Cerrar issue.")
    print("5 - Reabrir issue.")
    print("6 - Salir.")
    entrada = int(input())
    if(entrada == 1):
        print("Nombre de la issue: ")
        nombreIssue = input()
        insertaIssue(username, nombreIssue)
    if(entrada == 2):
        print("Introduzca el nombre de la issue que desea comentar: ")
        nombre = input()
        print("Ahora introduzca el comentario: ")
        comentario = input()
        insertarComentario(comentario,nombre)
    if(entrada == 3):
        print("Los problemas actuales, son: ")
        listarIssues(username)
        print("Introduzca el nombre de la issue: ")
        nombre = input()
        verHistorialIssue(nombre, username)
    if(entrada == 4):
        print("Introduzca el nombre de la issue que desea cerrar: ")
        nombre = input()
        cierraIssue(username, nombre)
    if(entrada == 5):
        print("Introduzca el nombre de la issue que desea reabrir: ")
        nombre = input()
        reabreIssue(username, nombre)
    if(entrada == 6):
        print("Salió de la aplicación. Buen día!")
        activo = 0
