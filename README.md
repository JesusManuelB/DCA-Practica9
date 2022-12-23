# DCA-Practica9

Para esta práctica he usado el código de la práctica 2 de esta asignatura:

1º Hay unos commits de prueba que hice.
2º Hubo un commit en el que introduje un error de compilación y lo solucioné con git bisect:
	- git bisect start -> Comienza el bisect
	- git bisect bad -> Marcamos el commit malo
	- git bisect good "commit" : Marcamos el commit bueno
	- git bisect reset -> Recuperamos el commit bueno
3º En los ficheros pre-commit y post-commit he puesto que se hago push y se ejecute el programa como prueba de archivos Hook.
4º Hay unos alias señalados con el comando: git config --global alias."nombre"
