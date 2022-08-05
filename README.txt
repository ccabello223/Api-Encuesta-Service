1-Se necesita previamente instalar WAMP o XAMPP para esta prueba se utilizo Wampserver64

2 - Introducir en su administrador de base datos el siguiente SQL:

CREATE DATABASE IF NOT EXISTS ptecnica;
use ptecnica;

CREATE TABLE ptecnica_cacs(
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(50) NOT NULL,
  `edades` varchar(10) NOT NULL,
  `sexo` varchar(10) NOT NULL,
  `social_fav` varchar(50) NOT NULL COMMENT 'Red Social Favorita',
  `time_on_fc` int(25) NOT NULL COMMENT 'Tiempo en Facebook',
  `time_on_ws` int(25) NOT NULL COMMENT 'Tiempo en WhatsApp',
  `time_on_tw` int(25) NOT NULL COMMENT 'Tiempo en Twitter',
  `time_on_ig` int(25) NOT NULL COMMENT 'Tiempo en Instagram',
  `time_on_tk` int(25) NOT NULL COMMENT 'Tiempo en Tiktok',
  PRIMARY KEY (`id`)
) ENGINE = InnoDB;

3-  En la carpeta donde se guardo los archivos de API-ENCUESTA-SERVICE del repositorio de GitHub. Se debe abrir una consola con el mismo directorio y ejecutar el siguiente comando (Tener instalado python previamente: https://www.python.org/downloads/ ):

virtualenv -p python3 env

Para generar el entorno virtual y luego entrar en el con el siguiente comando

.\env\Scripts\activate

Ya dentro del entorno virtual se ejecutaran los siguientes comandos

python.exe -m pip install --upgrade pip

pip install -r requirements.txt

python src/app.py

Este ultimo activa el localhost de flask

3- Luego de ejecutar flask, verificar si tiene activo el localhost de XAMPP o WAMP dependiendo el caso.

4- Una vez terminado con flask, ir al repositorio donde se encuentra la aplicacion de angular para probar el API: ENCUESTA-REDES-SOCIALES. En la carpeta donde se guardo los archivos de angular del repositorio de GitHub se debe abrir una consola con el mismo directorio y ejecutar el siguiente comando:

npm install

Este comando para instalar los paquetes

ng serve -o

Este ultimo para abrir la aplicacion

Listo, la aplicacion se estara ejecutando en localhost:4200