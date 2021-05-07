# Edward Daka - Y2 2021 - Rahan seuranta

Tarkoituksenani on toteuttaa ohjelma, joka lukee tilitapahtumat tiedostosta, erottelee tulot ja menot toisistaan sekä tekee selkeän kuvaajan menojen jakautumisesta, esimerkiksi piirakka- tai pylväsdiagrammin.

Mitä ominaisuuksia olet jo toteuttanut projektiisi?
*  Lukee tiedoston "Tilitapahtumat.csv"
*  Luo tapahtumista oliot ja osaa ryhmitellä saman paikan tapahtumat yhteen nimikkeeseen
*  Jaottelee tapahtumat tuloihin, menoihin ja sisäisiin siirtoihin. (Sisäisiä siirtoja ei ole mitenkään vielä implementoitu, jäävät vain pois tuloista)
*  Antaa käyttäjälle mahdollisuuden valita haluaako nähdä tulot vai menot, luo sitten listauksen näistä ja niiden osuuksista.
*  En ole vielä juuri testaillut virheitä yms. 


Tiedoston -ja kansiorakenne
    
*  *Mikä kansio on mikäkin ?*
        code = kansio sisältää ohjelman suorittamiseen tarvittavan koodin. 
        documents = kansio sisältää projektisuunnitelman ja projektidokumentin.
        idea. = Tuli vahingossa aiemman pushin myötä. Ei sisällä ohjelmaan tarvittavaa koodia.
        (Huom. Jouduin checkpointtia varten 26.3 tekemään uuden Gitlab-projektin, koska tiedostojen ajamisessa oli teknisiä vaikeuksia)
        (Aloitin Gitlabin käytön ns. alusta, joten projektisuunnitelma puuttui alustavasti uudesta Gitlabistä, mutta olen näyttänyt sen vanhasta gitlabista mm. suunnitelmademossa.)


Asennusohje
    
*  *Mitä kirjastoja tulisi asentaa ?*
    Ohjelma ei käytä asennettavia kirjastoja, pelkkää Pythonin standard libraryä.
    Olisi hyvä tarkistaa että PyCharmsissa käytettävä tulkitsija lukee oikeaa working directoriä.
    Tämän voi tehdä menemällä *Run > Edit Configurations > Working directory*. Tarkista että lopussa oleva kansio on /code, mikäli *Tilitapahtumat.csv* tiedosto on siellä.

Ohjelman käynnistys ja käyttö
    
*  *Kuinka ohjelma käynnistetään?*
       Valitaan PyCharmista main.py auki, ja suoritetaan "Run".
       1. Syötetään haluttu tiedosto nimi (Tilitapahtumat.csv)
       2. Mikäli tiedosto luetaan onnistuneesti antaa tämä valikon, jossa on vaihtoehtona 5 eri toimintoa.
       3. Näistä toiminnoista voidaan valita haluttu. 