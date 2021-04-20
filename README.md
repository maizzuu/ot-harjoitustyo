# TrackApp

### Dokumentaatio

- [Työaikakirjanpito](https://github.com/maizzuu/ot-harjoitustyo/blob/master/time_management.md)
  
- [Määrittelydokumentti](https://github.com/maizzuu/ot-harjoitustyo/blob/master/dokumentaatio/requirements_specification.md) 

- [Arkkitehtuuri](https://github.com/maizzuu/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

### Asennus
Asenna alkuun riippuvuudet komennolla:
  
` poetry install `

Alusta tietokannat komennolla:  
  
` poetry run invoke initialize `

### Komennot

Ohjelman voi käynnistää komentoriviltä komennolla:  
  
` poetry run invoke start `

Testit voi suorittaa komennolla:  
` poetry run invoke test `
  
Testikattavuusraportin voi luoda komennolla:  
  
` poetry run invoke coverage-report `
  
Pylint-tarkastukset voi suorittaa komennolla:  
  
` poetry run invoke lint `

   
