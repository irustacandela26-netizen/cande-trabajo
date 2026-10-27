# Galaxy en Django - Clase 12

1. Abrí la carpeta completa `galaxy-django` en Visual Studio Code.
2. Leé `apunte-clase-12.pdf`, que está en esta misma carpeta.
3. En una terminal dentro de la carpeta ejecutá:

```text
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
py manage.py migrate
py manage.py loaddata niveles
py manage.py createsuperuser
py manage.py runserver
```

4. Abrí `http://127.0.0.1:8000/` y recorré las pantallas.
5. Buscá los comentarios `TODO` en estos tres archivos:
   - `juegos/templates/juegos/jugar.html` (TODO 1)
   - `juegos/static/juegos/galaxy/game.js` (TODO 2, 3, 4 y 6)
   - `juegos/views.py` (TODO 5)
6. Completá un paso por vez y probá después de cada cambio (Ctrl+F5 para recargar el juego).
7. Comprobá el servidor con `py manage.py test`.
8. Para entregar, comprimí la carpeta completa `galaxy-django` sin la carpeta `.venv`.

Si algo falla, presioná F12, abrí **Console** y leé el primer mensaje de error.
