# Arkkitehtuurikuvaus

## Rakenne
Koodin pakkausrakenne on seuraava:  
![rakenne](https://github.com/maizzuu/ot-harjoitustyo/blob/master/dokumentaatio/images/rakenne.png)  

## Sovelluslogiikka
Sovelluksen looginen tietomalli koostuu luokista User ja Month. User kuvaa yksittäistä käyttäjää, Month käyttäjälle kuuluvaa kuukautta.  
  
![class_diagram](https://github.com/maizzuu/ot-harjoitustyo/blob/master/dokumentaatio/images/class_diagram.png)  
Sovelluksen toiminnallisuuksista huolehtii tiedosto
[app_service.py](https://github.com/maizzuu/ot-harjoitustyo/blob/master/src/services/app_service.py).
Kaikille toiminnallisuuksille on omat metodinsa.

## Päätoiminnallisuudet
Tällä hetkellä tekstikäyttöliittymässä menojen kirjaaminen näyttää seuraavalta sekvenssikaaviona:  
![sequence_graph](https://github.com/maizzuu/ot-harjoitustyo/blob/master/dokumentaatio/images/sekvenssikaavio.png)  
Sekvenssikaavio tulee vielä muuttumaan kun graafinen käyttöliittymä valmistuu.
