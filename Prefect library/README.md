
# Prefect - Una libreria de python para el manejo de errores

Prefect es una herramienta de orquestación de flujo de trabajo para flujos de datos intensivos basada en Python. Con Prefect, puede transformar cualquier función de Python en una unidad de trabajo que se puede observar y orquestar. Puede construir flujos de trabajo dinámicos y resistentes que reaccionan al mundo que los rodea y se recuperan de cambios inesperados

## Como instalar Prefect

En la propia pagina de prefect se nos recomienda instalar la librería usando un ambiente virtual, por lo que debemos hacer para empezar a instalar es crear este ambiente

En mi caso use virtualenv/venv que se puede instalar en Python directamente por el pip con el comando:

`py -m pip install --user virtualenv`

Una vez instalado debemos crear el ambiente virtual, para hacer esto tenemos que situarnos en la carpeta donde deseamos crear el ambiente virtual y correr el siguiente comando:

`py -m venv <nombre>`

Esto nos creara el ambiente y ahora lo único que tenemos que hacer es activarlo con la siguiente instrucción:

`.\env\Scripts\activate`

Nota: si se tiene un error similar al siguiente:

>imagen<
 
Lo que debes hacer es correr el powershell como administrador, para hacer esto ejecuta el comando:

`Set-ExecutionPolicy Unrestricted`

Y vuelve a abrir la terminal, ya debería permitirte activar el ambiente 

Una vez hecho esto instala la librería de prefect por medio del pip (esta se instalará en el ambiente virtual porque ya lo activamos)

`pip install -U prefect`

Y ahora si se puede hacer uso de prefect



## Ejemplo

Para el ejemplo de uso de prefect decidí enfocarme en el uso del "timeout" o ahora usado como "wait"

Esta instruccion esta hecha para prevenir tiempos de espera inintencionales demasiado largos y se indica por medio de segundos 

```python
@flow
def my_flow():
    final_state = wait_task.submit().wait(2)
```

Como se ve en mi ejemplo lo que yo hago es mandar a llamar a mi task e indicarle que tiene 2 segundos de espera, si no se acaba la funcion en esos dos segundos esta no acaba

```python
@task
def wait_task():
    num = random.randint(0,3)
    sleep(num)
    return 1
```

En el task lo que hago es esperar un numero random de segundos para simular los diferentes tiempos que pudo tardar, en algunos casos funcionará y terminará regresando un 1 y en otros casos no terminará 

```python
@task
    logger = get_run_logger()
    if final_state:
        logger.info("The task is done")

    else:
        logger.info("The task is canceled because it takes too long to run")
```

Finalmente haciendo uso de looger guardamos el estado de la tarea, si es que termino correctamente o si es que fue cancelada por ser demasiado larga, esto se sabe que sucedio por el retorno que deberia dar de 1, si es que no existe es que fue cancelada

>Imagen<

Después de varios intentos se puede ver como algunos si acaban con exito y otros son cancelados por la larga duración


