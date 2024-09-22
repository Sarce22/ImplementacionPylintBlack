# ImplementacionPylintBlack
Trabajo en clase de python utilizando Pylint y black

## Requisitos

Asegúrate de tener instalado lo siguiente:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/)
- [Python 3.x](https://www.python.org/downloads/)

## Instrucciones

### 1. Levantar los contenerdores 

estando en el root del directorio del proyecto en nuestro terminal (/PylintTrabajoClase) vamos a correr el domando 

docker compose build 

seguido de :

docker compose up

en este punto nuestros contenedores y nuestra aplicacion deben quedar 100% funcionales

### 1.  Ejecutar Pylint para analizar el código.

Primero otra vez estando en el root del directorio del proyecto en nuestro terminal (/PylintTrabajoClase)

- crearemos un entorno virtual de python

python3 -m venv venv

- lo activamos

source venv/bin/activate

- vamos al directorio de fast api

cd FastAPI/

- instalamos todas nuestras dependencias desde el requirements.txt 

pip3 install -r requirements.txt

- Por ultimo analizamos todo nuestro codigo con pylint con el comando :

pylint app
