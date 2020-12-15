Skilltest
==============================

Hva er dette?
-------------

Dette er en Python/Flask webapplikasjon. Du kan søke opp informasjon om ulike bedrifter ved å skrive inn organisasjon nummeret.
Du kan også lagre potensielle kunder, og notere og lagre hva som helst om bedriften.


Hvordan kjører du applikasjonen?
---------------

### Prerequisities


In order to run this container you'll need docker installed.

* [Windows](https://docs.docker.com/windows/started)
* [OS X](https://docs.docker.com/mac/started/)
* [Linux](https://docs.docker.com/linux/started/)

### Hvordan lager du applikasjonen?

Naviger til mappen som inneholder `docker-compose.yml` i terminalen din


Deretter kan du skrive dette i terminalen din
```shell
docker-compose build
```

Hvis du skriver dette vil docker lage en container og starte den automatisk.
```shell
docker-compose up
```

For å se webapplikasjonen trenger du å besøke denne linken
http://localhost:5000/
