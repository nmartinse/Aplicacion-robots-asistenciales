REM Ejecutable para activar el entorno en terminal de windows

cd .env

cd Scripts

call activate.bat

cd ..

cd ..

start "" "URL del servidor (localhost).html"

cls

python app.py

cmd /k