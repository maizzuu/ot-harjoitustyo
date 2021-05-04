# TrackApp
### Tämän hetkinen tilanne
Tekstikäyttöliittymässä on kaikki toiminnallisuudet käytössä. Graafinen käyttöliittymä ei ole vielä käyttökunnossa, mutta tulossa! Testit eivät myöskään vielä testaa services-hakemiston sovelluslogiikkaa.

### Dokumentaatio

- [Työaikakirjanpito](https://github.com/maizzuu/ot-harjoitustyo/blob/master/time_management.md)
  
- [Määrittelydokumentti](https://github.com/maizzuu/ot-harjoitustyo/blob/master/dokumentaatio/requirements_specification.md) 

- [Arkkitehtuuri](https://github.com/maizzuu/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

### Release  
  
- [Release](https://github.com/maizzuu/ot-harjoitustyo/releases/tag/viikko5)

### Asennus
Asenna alkuun riippuvuudet komennolla:
  
` poetry install `

Alusta tietokannat komennolla:  
  
` poetry run invoke build `

### Komennot

Ohjelman voi käynnistää komentoriviltä komennolla:  
  
` poetry run invoke start `

Testit voi suorittaa komennolla:  
` poetry run invoke test `
  
Testikattavuusraportin voi luoda komennolla:  
  
` poetry run invoke coverage-report `
  
Pylint-tarkastukset voi suorittaa komennolla:  
  
` poetry run invoke lint `

   
