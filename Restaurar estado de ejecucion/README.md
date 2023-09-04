![cerberus](https://github.com/AndreaGasparMiramontes/Toleranteafallas/assets/142550697/ce7694d4-2c7f-4448-9ac8-ce7bc1278f06)# Pickle para restaurar estado de un formulario

**Pickle** es un módulo de Python que permite serializar y deserializar objetos de Python, es decir, convertirlos en una secuencia de bytes y viceversa.

Esto es útil para almacenar, transferir o copiar objetos de forma eficiente y segura

Por ejemplo, si tienes una lista de números en Python, puedes usar pickle para guardarla en un archivo o enviarla por una red, y luego recuperarla con pickle en otro programa o máquina. Así puedes preservar el estado y la estructura de los objetos sin tener que reconstruirlos manualmente.


## Como restaurar el estado de un formulario
Pickle se puede usar para mantener el estado de un formulario en caso de que este se cierre repentinamente y se quiera evitar volver a llenar lo que ya se había llenado antes

## Ejemplo
- Python

En el codigo save.py podras encontrar un ejemplo muy simple de como esto puede funcionar, en primer lugar se revisa si ya existe un archivo ".pickle" si es que ya existe carga todos los datos y uno por uno se comprueba si estos tenian datos guardados o si estaban vacios, en caso de que ya tuvieran datos no se necesita guardar de nuevo la informacion asi que solo se imprime como si el mismo usuario hubiera guardado la informacion anteriormente

P.D: para que te sea más facil ver el funcionamiento te recomiendo dar ENTER sin llenar unos campos, asi despues podras ver como te los pide pero los que hayas llenado no lo pedirá
![image](https://github.com/AndreaGasparMiramontes/Toleranteafallas/assets/142550697/66e0c05d-7ebb-4c44-ab29-2b796777e884)



