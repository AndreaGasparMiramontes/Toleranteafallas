
# Servicios de windows

En windows los servicios son una serie de aplicaciones que se ejecutan en segundo plano y que permiten que el sistema operativo funcione correctamente. Estos servicios se pueden iniciar automáticamente al arrancar el equipo, se pueden pausar y reiniciar, y no muestran ninguna interfaz de usuario.
(En linux se les conoce por el nombre de *Deamons*)

En este programa se muestra un breve ejemplo de como se puede crear un servicio de windows por medio de python 

## Librerias

Para correr este proyecto necesitaras las siguientes librerias de python, asegurate de descargarlas por medio de *pip* o por algun otro medio

`psutil`

`subprocess`


## Explicacion

Ignorando funciones base para obtener parametros y comprobar que estos no estén vacios el corazon del programa es la siguiente funcion:

```python
def on(target):
	for proc in psutil.process_iter():
		if proc.name().lower() == target.lower():
			return True
	return False
```

En esta funcion estamos recorriendo los procesos en busca de un proceso en particular (el cual indicamos con los parametros al iniciar este programa) si encuentra el proceso regresa un "true" para indicar que el proceso se encuentra ejecutandose y si la busqueda termino y nunca se cumplio esto se retorna un "false"

```python
while True:
	for target in targets:
		if(not on(target)):
			sub.call(f'START {target}',shell=True)
```

En el "main" captaremos esa señal que nos regreso la funcion y si es que nos regresa "false" se llama a una instruccion de linea de comandos para abrir el programa indicado


## Correr el ejemplo

Para probar el codigo situate en la carpeta donde se encuentra el codigo por linea de comandos y escribe lo siguiente:

```bash
  python ejemplo.py spotify.exe
```

*Nota: si tu computadora no tiene spotify puedes tratar con algúna otra aplicación*

Una vez lo corras puedes intentar cerrar spotify tantas veces como quieras pero esta continuará abriendose 


## Screenshots

![](https://github.com/AndreaGasparMiramontes/Toleranteafallas/blob/main/Estado/gif_deamon.gif)
