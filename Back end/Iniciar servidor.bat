REM Ejecutable para iniciar el servidor en windows

cd .env

cd Scripts

call activate.bat

cd ..

cd ..

start "" "URL del servidor (localhost).html"

cls

python app.py

cmd /k