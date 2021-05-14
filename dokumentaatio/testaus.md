# Testausdokumentti
Ohjelmaa on testattu automatisoiduilla 
unittest-testeillä, sekä manuaalisesti.

## Sovelluslogiikan testaus
Sovelluslogiikasta vastaavaa luokkaa `AppService` testaan [TestAppService](https://github.com/maizzuu/ot-harjoitustyo/blob/b4659ab513da8f45dc4e8ea61a8cb59f2e41c604/src/tests/app_service_test.py#L64)-luokalla. Pysyväistallennuksen sijaan testeissä hyödynnetään repositorioita esittäviä `FakeMonthRepo` ja `FakeUserRepo`.

## Repositorioiden testaus
Repositorioita `MonthRepository` ja `UserRepository` testataan samassa tietokannassa, jota käytetään muuhun ohjelmaan. Tämän muuttaminen on yksi mahdollisia kehitysideoita. Repositorioita testataan [TestMonthRepository](https://github.com/maizzuu/ot-harjoitustyo/blob/master/src/tests/month_repository_test.py)- ja [TestUserRepository](https://github.com/maizzuu/ot-harjoitustyo/blob/master/src/tests/user_repository_test.py)-luokilla.

## Muu testaus
Luokkaa `Month`, joka kuvaa yksittäistä kuukautta, testaa testiluokka [TestMonth](https://github.com/maizzuu/ot-harjoitustyo/blob/master/src/tests/month_test.py).

## Testikattavuus
Testikattavuus ohjelmalla on 95%, kun käyttöliittymä jätetään kattavuuden ulkopuolelle.  
![coverage-report](https://github.com/maizzuu/ot-harjoitustyo/blob/master/dokumentaatio/images/coverage_report.png)  
Testaamatta jäi muun muassa kuukausien hakeminen kun ei ole kirjauduttu sisään, sekä uuden kuukauden lisääminen menojen kirjaamisen yhteydessä.

## Asennuksen testaus
Asentaminen on testattu manuaalisesti seuraamalla [käyttöohjeen](https://github.com/maizzuu/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md) ohjeita.

## Ongelmat
* Repositorioiden testaaminen vaikuttaa kaikkiin tietokannassa oleviin tiedostoihin.
* Kaikista tilanteista ei tule virheilmoituksia, esimerkiksi kuukauden nimeksi voi antaa minkä vain, samoin vuosiluku voi olla epätodellinen.
