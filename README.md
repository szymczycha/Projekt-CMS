# Instrukcja
## Aby uruchomić aplikację poraz pierwszy należy: 
1. Klonujemy repozytorium do folderu
```
git clone https://github.com/szymczycha/Projekt-CMS.git
```
3. Po sklonowaniu repozytorium otwieramy w folderze SvelteFrontEnd cmd i wpisujemy następujące komendy:
```
npm install
npm run build
```
3. Uruchamiamy flaskServer.py z folderu flaskServer
 - aplikacja uruchamia się na porcie 5000

### Aplikacja TKinter znajduje się w folderze CMSadminapp pod nazwą app.py

## Informacje o aplikacji

### W aplikacji powstaje domyślnie administrator 
 - Nick: admin
 - Hasło: admin
można to oczywiście zmienić na stronie i w aplikacji

### Administrator może:
 - wszystko to co moderator
 - zarządzać użytkownikami
 - ma dostęp do aplikacji tkinter

### Moderator może: 
 - wszystko to co normalny użytkownik
 - edytować Slider News ContentCards
 - zmieniać motyw strony
 - zmieniać kolejność bloków na stronie

### Zwykły user może: 
 - zostawiać komentarze pod artykułami

### Niezalogowany użytkownik może:
 - jedynie przeglądać stronę


### Autorzy:
 - Antoni Leszczyński
 - Szymon Konieczny
