REM Borrado y Creacion de la base de datos

cd instance

del test.db

cd ..

python3 Creacion_de_la_base_de_datos.py %*

REM Ejecutable para iniciar el servidor en windows
cd .env
cd Scripts
call activate.bat
cd ..
cd ..

start "" "Reset de la base de datos.html"

cls

python app.py

cmd /k