# flask-mongodb-ms
Microservicio en flask con conexión a base de datos mongo.

## Descarga

`$ git clone https://github.com/samusinho/flask-mongodb-ms.git`

## Instalación y configuración

Una vez clonado el proyecto, acceder al directorio, 
crear el entorno virtual y luego activarlo.

`$ py -3 -m venv venv`

`$ venv\Scripts\activate`

Instalar las librerías del archivo requirements.txt

`$ pip install -r requirements.txt`

Crear nuevo archivo dentro del directorio src con nombre "config.py".  
Copiar el contenido de "config.example.py" y pegarlo en "config.py" 

En la línea 6 del archivo "config.py", pegar la url correspondiente a la url de la
base de datos en mongo atlas, reemplazado `<password>` por la contraseña dada al
momento de la creación de la base de datos.

## Correr proyecto

#### Windows

`$ python .\src\app.py`
