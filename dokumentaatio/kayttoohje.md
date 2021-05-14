# Käyttöohje
## Asentaminen
Lataa uusin release, linkki siihen löytyy [README](https://github.com/maizzuu/ot-harjoitustyo/blob/master/README.md)
:sta
  
## Käynnistäminen
Ensimmäisellä käyttökerralla asenna riippuvuudet komennolla  
  
`poetry install `  
  
Seuraavaksi alusta ohjelma komennolla  
  
`poetry run invoke build`
  
Nyt ohjelman voi käynnistää komennolla  
  
`poetry run invoke start`  

## Kirjautuminen 
Sovellus avaa ensimmäisenä kirjautumisikkunan.
Kirjautuminen onnistuu kirjoittamalla käyttäjätunnus ja salasana niille tarkoitettuihin kenttiin, ja painamalla "Login"-nappia.  
!!!KUVA!!!
  
## Käyttäjän luominen 
Uuden käyttäjän pääsee luomaan kirjautumisikkunan kohdasta "Create". Avautuvaan ikkunaan syötetään haluttu käyttäjänimi ja salasana, ja käyttäjä luodaan klikkaamalla "Create".  
!!!KUVA!!!  
Jos valitsemasi käyttäjätunnus on jo käytössä, huomauttaa sovellus tästä, ja sinun tarvitsee valita uusi tunnus.

## Menojen kirjaaminen
Aluksi käyttäjän näkymä sisäänkirjautumisen jälkeen on tämä:  
!!!KUVA!!!  
Uuden kuukauden voi lisätä kenttiin "Month" ja "Year". Jos haluat vain luoda uuden kuukauden, jätä kaksi viimeistä kenttää tyhjiksi, mutta halutessasi voit samalla kirjata menoja kuukaudelle jonka luot.  
  
Menoja voi kirjata syöttämällä sopiviin kenttiin kuukauden, vuoden ja kategorian, sekä määrän jonka on käyttänyt. Kategorioita ovat:  
* Ruoka ja muut pakolliset
* Asuminen
* Harrastukset
* Kulkuneuvot
* Kulttuuri ja ravintolat
* Muu
  
Klikkaamalla kohtaa "Log", määrä kirjautuu, ja se ilmestyy näkyviin sen kuukauden kohdalle listaan.  
!!!KUVA!!!
Uloskirjautuminen tapahtuu klikkaamalla oikean yläkulman painiketta "Log out".