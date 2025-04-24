

# Indice di qualità dell'aria Via Home Assistant 


![HomeAssistant](https://github.com/kapkirk/Indice-di-qualita-dell-aria-via-Home-Assistant/blob/main/images/HA%20logo2.png)
---   


Una utility [Home Assistant](https://home-assistant.io/) che ti aiuta a visualizzare il dato di qualità dell'aria, ed i singoli dati dei principali inquinanti ambientali, pubblicati da [I.S.P.R.A.](https://www.isprambiente.gov.it/it/) (**Istituto Superiore per la Protezione e la Ricerca Ambientale**) utilizzando i dati forniti dalle Regioni italiane in ["quasi tempo reale"](https://www.isprambiente.gov.it/it/attivita/aria-1/qualita-dellaria/dati-in-tempo-quasi-reale).

Come è possibile leggere nella pagine dell'Istituto italiano i dati in “tempo quasi reale”, sono dati raccolti e trasmessi da parte delle Regioni e Province Autonome, trasmessi quotidianamente dall’ ISPRA alla Commissione Europea. Essi sono caratterizzati da un livello minimo di validazione ovvero che non sono stati sottoposti ai processi di filtrazione previsti successivamente alla loro acquisizione.

I dati disponibili nella dashboard dell'Istituto è possiible conoscere quelli relativi ai seguenti inquinanti: **NO2, O3, PM10, PM2,5, C6H6, CO e SO2.**



<br>

## Indice

Il seguente progetto è così articolato:

1. **Descrizione del progetto**

2. **Caratteristiche principali**

3. **Descrizione del funzionamento**

4. **Installazione**
   1. **Prerequisiti**
   1. **Configurazione dei dati da acquisire**
   1. **Configurazione di Node-RED**
   1. **Gestione della Lovelace**
   1. **Configurazione Sensore di Qualità dell'Aria**
 
<br>


## Descrizione del progetto

Scopo principale di questo progetto  è quello di automatizzare l`acquisizione "_in quasi tempo reale_" di un indice di qualità dell'aria utilizzando i dati ambientali pubblicati tramite _API_ dall'ISPRA a cui pervengono dalle diverse Agenzie Regionali di Protezione e Prevenzione Ambientale sparse su tutto il territorio nazionale, la loro elaborazione e la successiva integrazione in Home Assistant per la successiva visualizzazione.

Tutte le info sono disponibili sul sito dell'Istituto traime il [S.I.N.A.](https://sinacloud.isprambiente.it/portal/apps/experiencebuilder/experience/?draft=true&id=df677d20871d4383b34ce355e24f0598&page=page_38) (**Sistema Unformativo Nazionale Ambientale**) secondo la [mappa](https://sinacloud.isprambiente.it/portal/apps/experiencebuilder/experience/?draft=true&id=df677d20871d4383b34ce355e24f0598&page=page_62) dove i dati sono disponbili per il [download](https://sinacloud.isprambiente.it/portal/apps/experiencebuilder/experience/?draft=true&id=df677d20871d4383b34ce355e24f0598&page=page_74). 

---

## Caratteristiche principali

- **API Integration**: Collegamento diretto alle API di ISPRA per il prelievo di dei seguenti parametri ambientali:
     1.  **PM10** (Polveri inalabili. Insieme di sostanze solide e liquide con diametro inferiore a 10 micron. Derivano  da emissioni di autoveicoli, processi industriali, fenomeni naturali)
     1.  **PM2.5** (Polveri respirabili. Insieme di sostanze solide e liquide con diametro inferiore a 2.5 micron. Derivano  da processi industriali, processi di combustione, emissioni di autoveicoli, fenomeni naturali)
     3.  **NO2** (Biossido di azoto. Gas tossico che si forma nelle combustioni ad alta temperatura. Sue principali sorgenti sono i motori a scoppio, gli impianti termici, le centrali termoelettriche)
     4.  **SO2** (Biossido di zolfo. Gas irritante, si forma soprattutto in seguito all`utilizzo di combustibili (carbone, petrolio, gasolio) contenenti impurezze di zolfo)
     5.  **CO** (Monossido di Carbonio. Sostanza gassosa, si forma per combustione incompleta di materiale organico, ad esempio nei motori degli autoveicoli e nei processi industriali)
     6.  **C6H6** (Benzene. Liquido volatile e dall`odore dolciastro. Deriva dalla combustione incompleta del carbone e del petrolio, dai gas esausti dei veicoli a motore, dal fumo di tabacco)
     7.  **O3** (Ozono. Sostanza non emessa direttamente in atmosfera, si forma per reazione tra altri inquinanti, principalmente NO2 e idrocarburi, in presenza di radiazione solare)
    

## Descrizione del Funzionamento

1. **Acquisizione Dati**:  
   Ogni ora Home Assistant, mediante una interrogazione acquisisce i dati aggiornati, li filtra e restituisce il valore aggiornato del singolo inquinante.

2. **Elaborazione**:  
   I dati vengono analizzati e restituiti sia singolarmente che in modo aggregato fornendo un giudizio di qualità dell'aria. 

3. **Invio a Home Assistant**:  
   Tutti i dati acquisiti sono pubblicati come elementi dei singoli sensori direttamente esposti in HA.

5. **Visualizzazione**:  
   I dati dati così ottenuti sono graficamente esposti.

---

## Installazione

### 1 - Prerequisiti

- Abilitazione dei  **`packages`** e degli **`scripts python`**:
   - in HA aprire il file **`configuration.yaml`** mediante un editor di testo:   
      - inserire il seguente codice se già non presente:
      
      codice:
      ```
      homeassistant:
        packages: !include_dir_named packages
      
      python_script: 
      ```

- HACS installato e configurato con i seguenti pacchetti installati:
  - la custom  `flex-table-card` (Se volete utilizzare la tabella di visualizzazione come ho fatto io).



### 2 - Configurazione dei dati da acquisire

1.Come già anticipato i dati sono acquisiti tramite le API pubbliche messe a disposizione dall`ARPA. Le centraline disponibili (dato aggiornato al 9/4/2025) sono le seguenti:

|Regione|             Inquinante                                     |  
| -------- | -------------------------------------------------------- | 
ABRUZZO|Sulphur dioxide (air)|ABRUZZO - Sulphur dioxide (air)
ABRUZZO|Carbon monoxide (air)|ABRUZZO - Carbon monoxide (air)
ABRUZZO|Benzene (air)|ABRUZZO - Benzene (air)
ABRUZZO|Particulate matter < 10 µm (aerosol)|ABRUZZO - Particulate matter < 10 µm (aerosol)
ABRUZZO|Particulate matter < 2.5 µm (aerosol)|ABRUZZO - Particulate matter < 2.5 µm (aerosol)
ABRUZZO|Ozone (air)|ABRUZZO - Ozone (air)
ABRUZZO|Nitrogen dioxide (air)|ABRUZZO - Nitrogen dioxide (air)
BASILICATA|Sulphur dioxide (air)|BASILICATA - Sulphur dioxide (air)
BASILICATA|Carbon monoxide (air)|BASILICATA - Carbon monoxide (air)
BASILICATA|Benzene (air)|BASILICATA - Benzene (air)
BASILICATA|Particulate matter < 10 µm (aerosol)|BASILICATA - Particulate matter < 10 µm (aerosol)
BASILICATA|Particulate matter < 2.5 µm (aerosol)|BASILICATA - Particulate matter < 2.5 µm (aerosol)
BASILICATA|Ozone (air)|BASILICATA - Ozone (air)
BASILICATA|Nitrogen dioxide (air)|BASILICATA - Nitrogen dioxide (air)
CALABRIA|Sulphur dioxide (air)|CALABRIA - Sulphur dioxide (air)
CALABRIA|Carbon monoxide (air)|CALABRIA - Carbon monoxide (air)
CALABRIA|Benzene (air)|CALABRIA - Benzene (air)
CALABRIA|Particulate matter < 10 µm (aerosol)|CALABRIA - Particulate matter < 10 µm (aerosol)
CALABRIA|Particulate matter < 2.5 µm (aerosol)|CALABRIA - Particulate matter < 2.5 µm (aerosol)
CALABRIA|Ozone (air)|CALABRIA - Ozone (air)
CALABRIA|Nitrogen dioxide (air)|CALABRIA - Nitrogen dioxide (air)
CAMPANIA|Sulphur dioxide (air)|CAMPANIA - Sulphur dioxide (air)
CAMPANIA|Carbon monoxide (air)|CAMPANIA - Carbon monoxide (air)
CAMPANIA|Benzene (air)|CAMPANIA - Benzene (air)
CAMPANIA|Particulate matter < 10 µm (aerosol)|CAMPANIA - Particulate matter < 10 µm (aerosol)
CAMPANIA|Particulate matter < 2.5 µm (aerosol)|CAMPANIA - Particulate matter < 2.5 µm (aerosol)
CAMPANIA|Ozone (air)|CAMPANIA - Ozone (air)
CAMPANIA|Nitrogen dioxide (air)|CAMPANIA - Nitrogen dioxide (air)
EMILIA ROMAGNA|Sulphur dioxide (air)|EMILIA_ROMAGNA - Sulphur dioxide (air)
EMILIA ROMAGNA|Carbon monoxide (air)|EMILIA_ROMAGNA - Carbon monoxide (air)
EMILIA ROMAGNA|Benzene (air)|EMILIA_ROMAGNA - Benzene (air)
EMILIA ROMAGNA|Particulate matter < 10 µm (aerosol)|EMILIA_ROMAGNA - Particulate matter < 10 µm (aerosol)
EMILIA ROMAGNA|Particulate matter < 2.5 µm (aerosol)|EMILIA_ROMAGNA - Particulate matter < 2.5 µm (aerosol)
EMILIA ROMAGNA|Ozone (air)|EMILIA_ROMAGNA - Ozone (air)
EMILIA ROMAGNA|Nitrogen dioxide (air)|EMILIA_ROMAGNA - Nitrogen dioxide (air)
FRIULI VENEZIA GIULIA|Sulphur dioxide (air)|FRIULI_VENEZIA_GIULIA - Sulphur dioxide (air)
FRIULI VENEZIA GIULIA|Carbon monoxide (air)|FRIULI_VENEZIA_GIULIA - Carbon monoxide (air)
FRIULI VENEZIA GIULIA|Benzene (air)|FRIULI_VENEZIA_GIULIA - Benzene (air)
FRIULI VENEZIA GIULIA|Particulate matter < 10 µm (aerosol)|FRIULI_VENEZIA_GIULIA - Particulate matter < 10 µm (aerosol)
FRIULI VENEZIA GIULIA|Particulate matter < 2.5 µm (aerosol)|FRIULI_VENEZIA_GIULIA - Particulate matter < 2.5 µm (aerosol)
FRIULI VENEZIA GIULIA|Ozone (air)|FRIULI_VENEZIA_GIULIA - Ozone (air)
FRIULI VENEZIA GIULIA|Nitrogen dioxide (air)|FRIULI_VENEZIA_GIULIA - Nitrogen dioxide (air)
LAZIO|Sulphur dioxide (air)|LAZIO - Sulphur dioxide (air)
LAZIO|Carbon monoxide (air)|LAZIO - Carbon monoxide (air)
LAZIO|Benzene (air)|LAZIO - Benzene (air)
LAZIO|Particulate matter < 10 µm (aerosol)|LAZIO - Particulate matter < 10 µm (aerosol)
LAZIO|Particulate matter < 2.5 µm (aerosol)|LAZIO - Particulate matter < 2.5 µm (aerosol)
LAZIO|Ozone (air)|LAZIO - Ozone (air)
LAZIO|Nitrogen dioxide (air)|LAZIO - Nitrogen dioxide (air)
LIGURIA|Sulphur dioxide (air)|LIGURIA - Sulphur dioxide (air)
LIGURIA|Carbon monoxide (air)|LIGURIA - Carbon monoxide (air)
LIGURIA|Benzene (air)|LIGURIA - Benzene (air)
LIGURIA|Particulate matter < 10 µm (aerosol)|LIGURIA - Particulate matter < 10 µm (aerosol)
LIGURIA|Particulate matter < 2.5 µm (aerosol)|LIGURIA - Particulate matter < 2.5 µm (aerosol)
LIGURIA|Ozone (air)|LIGURIA - Ozone (air)
LIGURIA|Nitrogen dioxide (air)|LIGURIA - Nitrogen dioxide (air)
LOMBARDIA|Sulphur dioxide (air)|LOMBARDIA - Sulphur dioxide (air)
LOMBARDIA|Carbon monoxide (air)|LOMBARDIA - Carbon monoxide (air)
LOMBARDIA|Benzene (air)|LOMBARDIA - Benzene (air)
LOMBARDIA|Particulate matter < 10 µm (aerosol)|LOMBARDIA - Particulate matter < 10 µm (aerosol)
LOMBARDIA|Particulate matter < 2.5 µm (aerosol)|LOMBARDIA - Particulate matter < 2.5 µm (aerosol)
LOMBARDIA|Ozone (air)|LOMBARDIA - Ozone (air)
LOMBARDIA|Nitrogen dioxide (air)|LOMBARDIA - Nitrogen dioxide (air)
MARCHE|Sulphur dioxide (air)|MARCHE - Sulphur dioxide (air)
MARCHE|Carbon monoxide (air)|MARCHE - Carbon monoxide (air)
MARCHE|Benzene (air)|MARCHE - Benzene (air)
MARCHE|Particulate matter < 10 µm (aerosol)|MARCHE - Particulate matter < 10 µm (aerosol)
MARCHE|Particulate matter < 2.5 µm (aerosol)|MARCHE - Particulate matter < 2.5 µm (aerosol)
MARCHE|Ozone (air)|MARCHE - Ozone (air)
MARCHE|Nitrogen dioxide (air)|MARCHE - Nitrogen dioxide (air)
MOLISE|Sulphur dioxide (air)|MOLISE - Sulphur dioxide (air)
MOLISE|Carbon monoxide (air)|MOLISE - Carbon monoxide (air)
MOLISE|Benzene (air)|MOLISE - Benzene (air)
MOLISE|Particulate matter < 10 µm (aerosol)|MOLISE - Particulate matter < 10 µm (aerosol)
MOLISE|Particulate matter < 2.5 µm (aerosol)|MOLISE - Particulate matter < 2.5 µm (aerosol)
MOLISE|Ozone (air)|MOLISE - Ozone (air)
MOLISE|Nitrogen dioxide (air)|MOLISE - Nitrogen dioxide (air)
PIEMONTE|Sulphur dioxide (air)|PIEMONTE - Sulphur dioxide (air)
PIEMONTE|Carbon monoxide (air)|PIEMONTE - Carbon monoxide (air)
PIEMONTE|Benzene (air)|PIEMONTE - Benzene (air)
PIEMONTE|Particulate matter < 10 µm (aerosol)|PIEMONTE - Particulate matter < 10 µm (aerosol)
PIEMONTE|Particulate matter < 2.5 µm (aerosol)|PIEMONTE - Particulate matter < 2.5 µm (aerosol)
PIEMONTE|Ozone (air)|PIEMONTE - Ozone (air)
PIEMONTE|Nitrogen dioxide (air)|PIEMONTE - Nitrogen dioxide (air)
PUGLIA|Sulphur dioxide (air)|PUGLIA - Sulphur dioxide (air)
PUGLIA|Carbon monoxide (air)|PUGLIA - Carbon monoxide (air)
PUGLIA|Benzene (air)|PUGLIA - Benzene (air)
PUGLIA|Particulate matter < 10 µm (aerosol)|PUGLIA - Particulate matter < 10 µm (aerosol)
PUGLIA|Particulate matter < 2.5 µm (aerosol)|PUGLIA - Particulate matter < 2.5 µm (aerosol)
PUGLIA|Ozone (air)|PUGLIA - Ozone (air)
PUGLIA|Nitrogen dioxide (air)|PUGLIA - Nitrogen dioxide (air)
SARDEGNA|Sulphur dioxide (air)|SARDEGNA - Sulphur dioxide (air)
SARDEGNA|Carbon monoxide (air)|SARDEGNA - Carbon monoxide (air)
SARDEGNA|Benzene (air)|SARDEGNA - Benzene (air)
SARDEGNA|Particulate matter < 10 µm (aerosol)|SARDEGNA - Particulate matter < 10 µm (aerosol)
SARDEGNA|Particulate matter < 2.5 µm (aerosol)|SARDEGNA - Particulate matter < 2.5 µm (aerosol)
SARDEGNA|Ozone (air)|SARDEGNA - Ozone (air)
SARDEGNA|Nitrogen dioxide (air)|SARDEGNA - Nitrogen dioxide (air)
SICILIA|Sulphur dioxide (air)|SICILIA - Sulphur dioxide (air)
SICILIA|Carbon monoxide (air)|SICILIA - Carbon monoxide (air)
SICILIA|Benzene (air)|SICILIA - Benzene (air)
SICILIA|Particulate matter < 10 µm (aerosol)|SICILIA - Particulate matter < 10 µm (aerosol)
SICILIA|Particulate matter < 2.5 µm (aerosol)|SICILIA - Particulate matter < 2.5 µm (aerosol)
SICILIA|Ozone (air)|SICILIA - Ozone (air)
SICILIA|Nitrogen dioxide (air)|SICILIA - Nitrogen dioxide (air)
TOSCANA|Sulphur dioxide (air)|TOSCANA - Sulphur dioxide (air)
TOSCANA|Carbon monoxide (air)|TOSCANA - Carbon monoxide (air)
TOSCANA|Benzene (air)|TOSCANA - Benzene (air)
TOSCANA|Particulate matter < 10 µm (aerosol)|TOSCANA - Particulate matter < 10 µm (aerosol)
TOSCANA|Particulate matter < 2.5 µm (aerosol)|TOSCANA - Particulate matter < 2.5 µm (aerosol)
TOSCANA|Ozone (air)|TOSCANA - Ozone (air)
TOSCANA|Nitrogen dioxide (air)|TOSCANA - Nitrogen dioxide (air)
UMBRIA|Sulphur dioxide (air)|UMBRIA - Sulphur dioxide (air)
UMBRIA|Carbon monoxide (air)|UMBRIA - Carbon monoxide (air)
UMBRIA|Benzene (air)|UMBRIA - Benzene (air)
UMBRIA|Particulate matter < 10 µm (aerosol)|UMBRIA - Particulate matter < 10 µm (aerosol)
UMBRIA|Particulate matter < 2.5 µm (aerosol)|UMBRIA - Particulate matter < 2.5 µm (aerosol)
UMBRIA|Ozone (air)|UMBRIA - Ozone (air)
UMBRIA|Nitrogen dioxide (air)|UMBRIA - Nitrogen dioxide (air)
VALLE AOSTA|Benzene (air)|VALLE_AOSTA - Benzene (air)
VALLE AOSTA|Particulate matter < 10 µm (aerosol)|VALLE_AOSTA - Particulate matter < 10 µm (aerosol)
VALLE AOSTA|Particulate matter < 2.5 µm (aerosol)|VALLE_AOSTA - Particulate matter < 2.5 µm (aerosol)
VALLE AOSTA|Ozone (air)|VALLE_AOSTA - Ozone (air)
VALLE AOSTA|Nitrogen dioxide (air)|VALLE_AOSTA - Nitrogen dioxide (air)
VENETO|Sulphur dioxide (air)|VENETO - Sulphur dioxide (air)
VENETO|Carbon monoxide (air)|VENETO - Carbon monoxide (air)
VENETO|Benzene (air)|VENETO - Benzene (air)
VENETO|Particulate matter < 10 µm (aerosol)|VENETO - Particulate matter < 10 µm (aerosol)
VENETO|Particulate matter < 2.5 µm (aerosol)|VENETO - Particulate matter < 2.5 µm (aerosol)
VENETO|Ozone (air)|VENETO - Ozone (air)
VENETO|Nitrogen dioxide (air)|VENETO - Nitrogen dioxide (air)


Oltre che le Provincie Autonome:

|Regione|             Inquinante                                     |  
| -------- | -------------------------------------------------------- | 
BOLZANO|Sulphur dioxide (air)|PA_BOLZANO - Sulphur dioxide (air)
BOLZANO|Carbon monoxide (air)|PA_BOLZANO - Carbon monoxide (air)
BOLZANO|Benzene (air)|PA_BOLZANO - Benzene (air)
BOLZANO|Particulate matter < 10 µm (aerosol)|PA_BOLZANO - Particulate matter < 10 µm (aerosol)
BOLZANO|Particulate matter < 2.5 µm (aerosol)|PA_BOLZANO - Particulate matter < 2.5 µm (aerosol)
BOLZANO|Ozone (air)|PA_BOLZANO - Ozone (air)
BOLZANO|Nitrogen dioxide (air)|PA_BOLZANO - Nitrogen dioxide (air)
TRENTO|Sulphur dioxide (air)|PA_TRENTO - Sulphur dioxide (air)
TRENTO|Carbon monoxide (air)|PA_TRENTO - Carbon monoxide (air)
TRENTO|Benzene (air)|PA_TRENTO - Benzene (air)
TRENTO|Particulate matter < 10 µm (aerosol)|PA_TRENTO - Particulate matter < 10 µm (aerosol)
TRENTO|Particulate matter < 2.5 µm (aerosol)|PA_TRENTO - Particulate matter < 2.5 µm (aerosol)
TRENTO|Ozone (air)|PA_TRENTO - Ozone (air)
TRENTO|Nitrogen dioxide (air)|PA_TRENTO - Nitrogen dioxide (air)


1. La procedura da seguire per individuare il dato è la seguente:
- Accedere alla pagine del [download](https://sinacloud.isprambiente.it/portal/apps/experiencebuilder/experience/?data_id=dataSource_137-infoariadowload_7094-infoariadowload%3A127&draft=true&id=df677d20871d4383b34ce355e24f0598&page=page_74)
- Selezionare la Regione della quale si vuole acquisire il dato inquinante ed individuare il rigo dell'inquinante. Il terzo campo della tabella conterrà il link per il download che bisognerà copiare per inserirlo nel flusso di Node-RED.
  
  Ad esempio, volendo conoscere il dato di SO2 per la Regione Abruzzo, otterremo il seguente link:

    `https://sdi.isprambiente.it/geoserver/infoaria/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=infoaria%3Adati_nrt_informambiente_mv&CQL_FILTER=region_name=%27ABRUZZO%27+AND+pollutant_id=%271%27&maxFeatures=10000&outputFormat=csv `

   può essere utilizzato anche nel normale browser. La sua consultazione genererà il download di un file che potrete leggere ed apprezzare soprattutto perchè per la centralina che avrete individuato, vi consentirà di sapere quali sono i dati pubblicati da ISPRA.

  Ma quale è la centralina che ci interessa? Le soluzioni sono due:
1. individuarla tramite la [mappa](https://sinacloud.isprambiente.it/portal/apps/experiencebuilder/experience/?draft=true&id=df677d20871d4383b34ce355e24f0598&page=page_62):
     - ci colleghiamo al sito ISPRA
     - selezioniamo l`inquinante che ci interessa
     - clicchiamo sulla casella dati orari e vedremo comparire tutte le centraline che esopngono il dato
     - cliccandoci sopra vedremo come primo dato il codice europeo, proprio quello che ci serve (es: IT1659A), prendetene nota!
       
2. Individuarla tramite il file csv:
     - scaricate il file csv come spiegato al precedente punto 1
     - aprite Excel
     - nella scheda del menu `dati` selezionate `txt\csv`
     - selezionate il file, cliccate sempre continua ed importate i dati
     - cercate la centralina che vi interessa tramite l`indirizzo o le coordinate
     - individuate il dato riportato nella colonna campo `station_eu_code`  (es: IT1659A), prendetene nota!
       
    
### 3 - Configurazione in Node-RED

1. Creare i sensori:
- Editare i singoli `sensor node` creando una nuona configurazione per ogni sensore. In pratica:
- selezionare tra le `home assistant entities` il nodo `sensor` e trasportarlo nel flusso;
- editate il nodo `sensor`;
- cliccare su `+` dopo la voce `Entity config`;
- inserire il nome del sensore nel campo `nome`;
- cliccare su `+` dopo la voce `Device` e nella successva maschera inserire ad esempio `Node-RED`;
- nel campo `type` inserire la voce `sensor`;
- nel campo `Friendly name` il nome del sensore, ad esempio `CO Orario`;
- nel campo `Unit of measurement` l'unità di misura, ad esempio `mg/m³`;
- in alto cliccare su `Add`. Il programma tornerà alla schermata precedente di configurazione del sensore, ottenendo la seguente configurazione:

![sensore](https://github.com/kapkirk/Indice-di-qualita-dell-aria-via-Home-Assistant/blob/main/images/Sensore.png)

  
- inserire un nome da attribuire al `sensor`, ad esempio `CO Orario`;
- nel campo `Entity config` avremo il nome del sensore creato in precedenza;
- nel campo `state` inserire `payload.data_record_value`, dopo `msg.`;
- cliccare su `+ add attribute` ed aggiungere i seguenti campi:

|Attributo |           Msg da inserire |
| -------- | -------------------------------------------------------- | 
luogo |msg.payload.municipality_name
indirizzo |msg.payload.station_municipality
codice_europeo |msg.payload.station_eu_code
inquinante_sigla |msg.payload.pollutant_notation
inquinante_descrizione |msg.payload.pollutant_label
data_rilevazione |msg.payload.data_record_end_time
unita_misura |msg.payload.observation_unit_notation
livello_inquinante |msg.payload.pollutant_level
posizione_stazione |msg.payload.station_position
limite | 10 mg/m3 ogni 8 ore

- i sensori da configurare sono quelli relativi ad ogni singolo inquinante, quindi CO, SO2, C6H6, PM10, PM2.5, O3 ed NO2. Il risultato finale dovrebbe essere questo:


![sensore1](https://github.com/kapkirk/Indice-di-qualita-dell-aria-via-Home-Assistant/blob/main/images/Sensore_nodo.jpg)

L`unica cosa che cambierà nella configurazione dei sensori sarà il limite che dovrete impostare come segue:
- CO: 10 mg/m3 ogni 8 ore
- SO2: 350 µg/m3 al giorno
- C6H6: 5 µg/m3 all'anno
- PM10: 50 µg/m3 al giorno per non più di 35 volte in un anno
- PM2.5: 25 µg/m3 al giorno
- O3: 180 µg/m3 per ora
- NO2: 180 µg/m3 per ora

A questo punto possiamo acquisire il codice in Node-RED, lo trovate nel file `flusso Node-Red.json`, oppure da copiare ed incollare:

![Node-red1](https://github.com/kapkirk/Indice-di-qualita-dell-aria-via-Home-Assistant/blob/main/images/Flusso_Node-Red.jpg)



codice:
```yaml
[{"id":"9341e81a2672a77b","type":"tab","label":"Dari Orari ISPRA","disabled":false,"info":"","env":[]},{"id":"86a27412fd248875","type":"http request","z":"9341e81a2672a77b","name":"","method":"GET","ret":"txt","paytoqs":"ignore","url":"https://sdi.isprambiente.it/geoserver/infoaria/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=infoaria%3Adati_nrt_informambiente_mv&CQL_FILTER=region_name=%27PUGLIA%27+AND+pollutant_id=%2710%27&maxFeatures=10000&outputFormat=csv","tls":"","persist":true,"proxy":"","insecureHTTPParser":true,"authType":"","senderr":false,"headers":[],"x":490,"y":200,"wires":[["129a117ec0480da4"]]},{"id":"129a117ec0480da4","type":"csv","z":"9341e81a2672a77b","name":"","spec":"rfc","sep":",","hdrin":true,"hdrout":"none","multi":"one","ret":"\\r\\n","temp":"","skip":"0","strings":true,"include_empty_strings":true,"include_null_values":true,"x":630,"y":200,"wires":[["0f80c4ac185f9d2b"]]},{"id":"d4c2feeff75e09fc","type":"http request","z":"9341e81a2672a77b","name":"","method":"GET","ret":"txt","paytoqs":"ignore","url":"https://sdi.isprambiente.it/geoserver/infoaria/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=infoaria%3Adati_nrt_informambiente_mv&CQL_FILTER=region_name=%27PUGLIA%27+AND+pollutant_id=%2720%27&maxFeatures=10000&outputFormat=csv","tls":"","persist":true,"proxy":"","insecureHTTPParser":false,"authType":"","senderr":false,"headers":[],"x":490,"y":320,"wires":[["6039f795bf127e3a"]]},{"id":"aa59fbdcd1545be8","type":"http request","z":"9341e81a2672a77b","name":"","method":"GET","ret":"txt","paytoqs":"ignore","url":"https://sdi.isprambiente.it/geoserver/infoaria/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=infoaria%3Adati_nrt_informambiente_mv&CQL_FILTER=region_name=%27PUGLIA%27+AND+pollutant_id=%275%27&maxFeatures=10000&outputFormat=csv","tls":"","persist":true,"proxy":"","insecureHTTPParser":false,"authType":"","senderr":false,"headers":[],"x":490,"y":380,"wires":[["10e322bfb597f397"]]},{"id":"d2e0462a8bfc7fc4","type":"http request","z":"9341e81a2672a77b","name":"","method":"GET","ret":"txt","paytoqs":"ignore","url":"https://sdi.isprambiente.it/geoserver/infoaria/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=infoaria%3Adati_nrt_informambiente_mv&CQL_FILTER=region_name=%27PUGLIA%27+AND+pollutant_id=%276001%27&maxFeatures=10000&outputFormat=csv","tls":"","persist":true,"proxy":"","insecureHTTPParser":false,"authType":"","senderr":false,"headers":[],"x":490,"y":440,"wires":[["a1f4b7fdd094dac2"]]},{"id":"d91e018119691670","type":"http request","z":"9341e81a2672a77b","name":"","method":"GET","ret":"txt","paytoqs":"ignore","url":"https://sdi.isprambiente.it/geoserver/infoaria/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=infoaria%3Adati_nrt_informambiente_mv&CQL_FILTER=region_name=%27PUGLIA%27+AND+pollutant_id=%277%27&maxFeatures=10000&outputFormat=csv","tls":"","persist":true,"proxy":"","insecureHTTPParser":false,"authType":"","senderr":false,"headers":[],"x":490,"y":500,"wires":[["2f140e806700e380"]]},{"id":"bc4ecc4da286b3c8","type":"http request","z":"9341e81a2672a77b","name":"","method":"GET","ret":"txt","paytoqs":"ignore","url":"https://sdi.isprambiente.it/geoserver/infoaria/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=infoaria%3Adati_nrt_informambiente_mv&CQL_FILTER=region_name=%27PUGLIA%27+AND+pollutant_id=%278%27&maxFeatures=10000&outputFormat=csv","tls":"","persist":true,"proxy":"","insecureHTTPParser":false,"authType":"","senderr":false,"headers":[],"x":490,"y":560,"wires":[["193995d8afc547b0"]]},{"id":"a76b8be52e38c6df","type":"csv","z":"9341e81a2672a77b","name":"","spec":"rfc","sep":",","hdrin":true,"hdrout":"none","multi":"one","ret":"\\r\\n","temp":"","skip":"0","strings":true,"include_empty_strings":true,"include_null_values":true,"x":630,"y":260,"wires":[["caa73170cbae11e6"]]},{"id":"6039f795bf127e3a","type":"csv","z":"9341e81a2672a77b","name":"","spec":"rfc","sep":",","hdrin":true,"hdrout":"none","multi":"one","ret":"\\r\\n","temp":"","skip":"0","strings":true,"include_empty_strings":true,"include_null_values":true,"x":630,"y":320,"wires":[["260a26186db8e11c"]]},{"id":"10e322bfb597f397","type":"csv","z":"9341e81a2672a77b","name":"","spec":"rfc","sep":",","hdrin":true,"hdrout":"none","multi":"one","ret":"\\r\\n","temp":"","skip":"0","strings":true,"include_empty_strings":true,"include_null_values":true,"x":630,"y":380,"wires":[["0efe1d45b2822b0a"]]},{"id":"a1f4b7fdd094dac2","type":"csv","z":"9341e81a2672a77b","name":"","spec":"rfc","sep":",","hdrin":true,"hdrout":"none","multi":"one","ret":"\\r\\n","temp":"","skip":"0","strings":true,"include_empty_strings":true,"include_null_values":true,"x":630,"y":440,"wires":[["d5b73c602d374caa"]]},{"id":"2f140e806700e380","type":"csv","z":"9341e81a2672a77b","name":"","spec":"rfc","sep":",","hdrin":true,"hdrout":"none","multi":"one","ret":"\\r\\n","temp":"","skip":"0","strings":true,"include_empty_strings":true,"include_null_values":true,"x":630,"y":500,"wires":[["5bcf5b37d42bdfee"]]},{"id":"193995d8afc547b0","type":"csv","z":"9341e81a2672a77b","name":"","spec":"rfc","sep":",","hdrin":true,"hdrout":"none","multi":"one","ret":"\\r\\n","temp":"","skip":"0","strings":true,"include_empty_strings":true,"include_null_values":true,"x":630,"y":560,"wires":[["65f747768b243167"]]},{"id":"3d80e107b51013e6","type":"http request","z":"9341e81a2672a77b","name":"","method":"GET","ret":"txt","paytoqs":"ignore","url":"https://sdi.isprambiente.it/geoserver/infoaria/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=infoaria%3Adati_nrt_informambiente_mv&CQL_FILTER=region_name=%27PUGLIA%27+AND+pollutant_id=%271%27&maxFeatures=10000&outputFormat=csv","tls":"","persist":true,"proxy":"","insecureHTTPParser":false,"authType":"","senderr":false,"headers":[],"x":490,"y":260,"wires":[["a76b8be52e38c6df"]]},{"id":"0f80c4ac185f9d2b","type":"switch","z":"9341e81a2672a77b","name":"","property":"payload.station_eu_code","propertyType":"msg","rules":[{"t":"eq","v":"IT1658A","vt":"str"},{"t":"else"}],"checkall":"true","repair":false,"outputs":2,"x":810,"y":200,"wires":[["bf84667c52653692"],[]]},{"id":"70c367d7c81694b0","type":"ha-sensor","z":"9341e81a2672a77b","name":"CO Orario","entityConfig":"018d9c5d8af3c28a","version":0,"state":"payload.data_record_value","stateType":"msg","attributes":[{"property":"luogo","value":"payload.municipality_name","valueType":"msg"},{"property":"indirizzo","value":"payload.station_municipality","valueType":"msg"},{"property":"codice_europeo","value":"payload.station_eu_code","valueType":"msg"},{"property":"inquinante_sigla","value":"payload.pollutant_notation","valueType":"msg"},{"property":"inquinante_descrizione","value":"payload.pollutant_label","valueType":"msg"},{"property":"data_rilevazione","value":"payload.data_record_end_time","valueType":"msg"},{"property":"unita_misura","value":"payload.observation_unit_notation","valueType":"msg"},{"property":"livello_inquinante","value":"payload.pollutant_level","valueType":"msg"},{"property":"posizione_stazione","value":"payload.station_position","valueType":"msg"},{"property":"limite","value":"10 mg/m3 ogni 8 ore","valueType":"str"}],"inputOverride":"allow","outputProperties":[],"x":1130,"y":200,"wires":[[]]},{"id":"0efe1d45b2822b0a","type":"switch","z":"9341e81a2672a77b","name":"","property":"payload.station_eu_code","propertyType":"msg","rules":[{"t":"eq","v":"IT1658A","vt":"str"},{"t":"else"}],"checkall":"true","repair":false,"outputs":2,"x":810,"y":380,"wires":[["a7f2dabdfa56f504"],[]]},{"id":"d5b73c602d374caa","type":"switch","z":"9341e81a2672a77b","name":"","property":"payload.station_eu_code","propertyType":"msg","rules":[{"t":"eq","v":"IT1658A","vt":"str"},{"t":"else"}],"checkall":"true","repair":false,"outputs":2,"x":810,"y":440,"wires":[["b8d2af647cf08a5a"],[]]},{"id":"5bcf5b37d42bdfee","type":"switch","z":"9341e81a2672a77b","name":"","property":"payload.station_eu_code","propertyType":"msg","rules":[{"t":"eq","v":"IT2139A","vt":"str"},{"t":"else"}],"checkall":"true","repair":false,"outputs":2,"x":810,"y":500,"wires":[["cd5c61642abc1632"],[]]},{"id":"65f747768b243167","type":"switch","z":"9341e81a2672a77b","name":"","property":"payload.station_eu_code","propertyType":"msg","rules":[{"t":"eq","v":"IT1657A","vt":"str"},{"t":"else"}],"checkall":"true","repair":false,"outputs":2,"x":810,"y":560,"wires":[["7db8532370fd384d"],[]]},{"id":"caa73170cbae11e6","type":"switch","z":"9341e81a2672a77b","name":"","property":"payload.station_eu_code","propertyType":"msg","rules":[{"t":"eq","v":"IT1658A","vt":"str"},{"t":"else"}],"checkall":"true","repair":false,"outputs":2,"x":810,"y":260,"wires":[["494566f4d1175bf5"],[]]},{"id":"f359e094c2916855","type":"ha-sensor","z":"9341e81a2672a77b","name":"SO2 Orario","entityConfig":"d164653373b81866","version":0,"state":"payload.data_record_value","stateType":"msg","attributes":[{"property":"luogo","value":"payload.municipality_name","valueType":"msg"},{"property":"indirizzo","value":"payload.station_municipality","valueType":"msg"},{"property":"codice_europeo","value":"payload.station_eu_code","valueType":"msg"},{"property":"inquinante_sigla","value":"payload.pollutant_notation","valueType":"msg"},{"property":"inquinante_descrizione","value":"payload.pollutant_label","valueType":"msg"},{"property":"data_rilevazione","value":"payload.data_record_end_time","valueType":"msg"},{"property":"unita_misura","value":"payload.observation_unit_notation","valueType":"msg"},{"property":"livello_inquinante","value":"payload.pollutant_level","valueType":"msg"},{"property":"posizione_stazione","value":"payload.station_position","valueType":"msg"},{"property":"limite","value":"350  µg/m3 al giorno","valueType":"str"}],"inputOverride":"allow","outputProperties":[],"x":1130,"y":260,"wires":[[]]},{"id":"be1140aedd07108f","type":"ha-sensor","z":"9341e81a2672a77b","name":"C6H6 Orario","entityConfig":"ea9fa5358962befe","version":0,"state":"payload.data_record_value","stateType":"msg","attributes":[{"property":"luogo","value":"payload.municipality_name","valueType":"msg"},{"property":"indirizzo","value":"payload.station_municipality","valueType":"msg"},{"property":"codice_europeo","value":"payload.station_eu_code","valueType":"msg"},{"property":"inquinante_sigla","value":"payload.pollutant_notation","valueType":"msg"},{"property":"inquinante_descrizione","value":"payload.pollutant_label","valueType":"msg"},{"property":"data_rilevazione","value":"payload.data_record_end_time","valueType":"msg"},{"property":"unita_misura","value":"payload.observation_unit_notation","valueType":"msg"},{"property":"livello_inquinante","value":"payload.pollutant_level","valueType":"msg"},{"property":"posizione_stazione","value":"payload.station_position","valueType":"msg"},{"property":"limite","value":"5 µg/m3 all'anno","valueType":"str"}],"inputOverride":"allow","outputProperties":[],"x":1130,"y":320,"wires":[[]]},{"id":"122187a9ccb9da0e","type":"ha-sensor","z":"9341e81a2672a77b","name":"PM10 Orario","entityConfig":"2b73079bc1f934e1","version":0,"state":"payload.data_record_value","stateType":"msg","attributes":[{"property":"luogo","value":"payload.municipality_name","valueType":"msg"},{"property":"indirizzo","value":"payload.station_municipality","valueType":"msg"},{"property":"codice_europeo","value":"payload.station_eu_code","valueType":"msg"},{"property":"inquinante_sigla","value":"payload.pollutant_notation","valueType":"msg"},{"property":"inquinante_descrizione","value":"payload.pollutant_label","valueType":"msg"},{"property":"data_rilevazione","value":"payload.data_record_end_time","valueType":"msg"},{"property":"unita_misura","value":"payload.observation_unit_notation","valueType":"msg"},{"property":"livello_inquinante","value":"payload.pollutant_level","valueType":"msg"},{"property":"posizione_stazione","value":"payload.station_position","valueType":"msg"},{"property":"limite","value":"50 µg/m3 al giorno per non più di 35 volte in un anno","valueType":"str"}],"inputOverride":"allow","outputProperties":[],"x":1130,"y":380,"wires":[[]]},{"id":"f8c4f7e6629310cb","type":"ha-sensor","z":"9341e81a2672a77b","name":"PM25 Orario","entityConfig":"e913556f2e570def","version":0,"state":"payload.data_record_value","stateType":"msg","attributes":[{"property":"luogo","value":"payload.municipality_name","valueType":"msg"},{"property":"indirizzo","value":"payload.station_municipality","valueType":"msg"},{"property":"codice_europeo","value":"payload.station_eu_code","valueType":"msg"},{"property":"inquinante_sigla","value":"payload.pollutant_notation","valueType":"msg"},{"property":"inquinante_descrizione","value":"payload.pollutant_label","valueType":"msg"},{"property":"data_rilevazione","value":"payload.data_record_end_time","valueType":"msg"},{"property":"unita_misura","value":"payload.observation_unit_notation","valueType":"msg"},{"property":"livello_inquinante","value":"payload.pollutant_level","valueType":"msg"},{"property":"posizione_stazione","value":"payload.station_position","valueType":"msg"},{"property":"limite","value":"25 µg/m3 al giorno","valueType":"str"}],"inputOverride":"allow","outputProperties":[],"x":1130,"y":440,"wires":[[]]},{"id":"9cace0e7d80f0fec","type":"ha-sensor","z":"9341e81a2672a77b","name":"O3 Orario","entityConfig":"8b9bc702715f3b15","version":0,"state":"payload.data_record_value","stateType":"msg","attributes":[{"property":"luogo","value":"payload.municipality_name","valueType":"msg"},{"property":"indirizzo","value":"payload.station_municipality","valueType":"msg"},{"property":"codice_europeo","value":"payload.station_eu_code","valueType":"msg"},{"property":"inquinante_sigla","value":"payload.pollutant_notation","valueType":"msg"},{"property":"inquinante_descrizione","value":"payload.pollutant_label","valueType":"msg"},{"property":"data_rilevazione","value":"payload.data_record_end_time","valueType":"msg"},{"property":"unita_misura","value":"payload.observation_unit_notation","valueType":"msg"},{"property":"livello_inquinante","value":"payload.pollutant_level","valueType":"msg"},{"property":"posizione_stazione","value":"payload.station_position","valueType":"msg"},{"property":"limite","value":"180 µg/m3 per ora","valueType":"str"}],"inputOverride":"allow","outputProperties":[],"x":1120,"y":500,"wires":[[]]},{"id":"b3e7f7b6d745543b","type":"ha-sensor","z":"9341e81a2672a77b","name":"NO2 Orario","entityConfig":"136a6476a7590443","version":0,"state":"payload.data_record_value","stateType":"msg","attributes":[{"property":"luogo","value":"payload.municipality_name","valueType":"msg"},{"property":"indirizzo","value":"payload.station_municipality","valueType":"msg"},{"property":"codice_europeo","value":"payload.station_eu_code","valueType":"msg"},{"property":"inquinante_sigla","value":"payload.pollutant_notation","valueType":"msg"},{"property":"inquinante_descrizione","value":"payload.pollutant_label","valueType":"msg"},{"property":"data_rilevazione","value":"payload.data_record_end_time","valueType":"msg"},{"property":"unita_misura","value":"payload.observation_unit_notation","valueType":"msg"},{"property":"livello_inquinante","value":"payload.pollutant_level","valueType":"msg"},{"property":"posizione_stazione","value":"payload.station_position","valueType":"msg"},{"property":"limite","value":"200 µg/m3 al giorno per non più di 18 volte in un anno","valueType":"str"}],"inputOverride":"allow","outputProperties":[],"x":1130,"y":560,"wires":[[]]},{"id":"d17996519aae5d44","type":"ha-button","z":"9341e81a2672a77b","name":"","version":0,"debugenabled":false,"outputs":1,"entityConfig":"09fe098a6e9c3183","outputProperties":[{"property":"payload","propertyType":"msg","value":"","valueType":"entityState"},{"property":"topic","propertyType":"msg","value":"","valueType":"triggerId"},{"property":"data","propertyType":"msg","value":"","valueType":"entity"}],"x":150,"y":40,"wires":[["ab8c3c44fbcf8ab6"]]},{"id":"45f7384ded2e44b5","type":"inject","z":"9341e81a2672a77b","name":"","props":[{"p":"payload"},{"p":"topic","vt":"str"}],"repeat":"3600","crontab":"","once":true,"onceDelay":0.1,"topic":"","payload":"","payloadType":"date","x":190,"y":120,"wires":[["ab8c3c44fbcf8ab6"]]},{"id":"ab8c3c44fbcf8ab6","type":"link out","z":"9341e81a2672a77b","name":"link out 123","mode":"link","links":["93bab1ec2d64d3a7"],"x":345,"y":120,"wires":[]},{"id":"93bab1ec2d64d3a7","type":"link in","z":"9341e81a2672a77b","name":"link in 65","links":["ab8c3c44fbcf8ab6"],"x":315,"y":380,"wires":[["86a27412fd248875","3d80e107b51013e6","d4c2feeff75e09fc","aa59fbdcd1545be8","d2e0462a8bfc7fc4","d91e018119691670","bc4ecc4da286b3c8"]]},{"id":"260a26186db8e11c","type":"switch","z":"9341e81a2672a77b","name":"","property":"payload.station_eu_code","propertyType":"msg","rules":[{"t":"eq","v":"IT1658A","vt":"str"},{"t":"else"}],"checkall":"true","repair":false,"outputs":2,"x":810,"y":320,"wires":[["136098c27cd667eb"],[]]},{"id":"c409f470e25feae8","type":"comment","z":"9341e81a2672a77b","name":"Carbon monoxide (air)","info":"","x":1320,"y":200,"wires":[]},{"id":"2fc04ecdb49a76e2","type":"comment","z":"9341e81a2672a77b","name":" Sulphur dioxide (air)","info":"","x":1310,"y":260,"wires":[]},{"id":"21a4b5e2da677ee2","type":"comment","z":"9341e81a2672a77b","name":"Benzene (air)","info":"","x":1290,"y":320,"wires":[]},{"id":"26eb8d5360629947","type":"comment","z":"9341e81a2672a77b","name":"PM10","info":"","x":1270,"y":380,"wires":[]},{"id":"347f978804fde924","type":"comment","z":"9341e81a2672a77b","name":"PM 2.5","info":"","x":1270,"y":440,"wires":[]},{"id":"3e96d213d91d31d6","type":"comment","z":"9341e81a2672a77b","name":"Ozone (air)","info":"","x":1280,"y":500,"wires":[]},{"id":"a1d1d746f606c99d","type":"comment","z":"9341e81a2672a77b","name":"Nitrogen dioxide (air)","info":"","x":1310,"y":560,"wires":[]},{"id":"bf84667c52653692","type":"switch","z":"9341e81a2672a77b","name":"","property":"payload.data_record_end_time","propertyType":"msg","rules":[{"t":"gt","v":"","vt":"prev"},{"t":"else"}],"checkall":"true","repair":false,"outputs":2,"x":950,"y":200,"wires":[["70c367d7c81694b0"],[]]},{"id":"494566f4d1175bf5","type":"switch","z":"9341e81a2672a77b","name":"","property":"payload.data_record_end_time","propertyType":"msg","rules":[{"t":"gt","v":"","vt":"prev"},{"t":"else"}],"checkall":"true","repair":false,"outputs":2,"x":950,"y":260,"wires":[["f359e094c2916855"],[]]},{"id":"136098c27cd667eb","type":"switch","z":"9341e81a2672a77b","name":"","property":"payload.data_record_end_time","propertyType":"msg","rules":[{"t":"gt","v":"","vt":"prev"},{"t":"else"}],"checkall":"true","repair":false,"outputs":2,"x":950,"y":320,"wires":[["be1140aedd07108f"],[]]},{"id":"a7f2dabdfa56f504","type":"switch","z":"9341e81a2672a77b","name":"","property":"payload.data_record_end_time","propertyType":"msg","rules":[{"t":"gt","v":"","vt":"prev"},{"t":"else"}],"checkall":"true","repair":false,"outputs":2,"x":950,"y":380,"wires":[["122187a9ccb9da0e"],[]]},{"id":"b8d2af647cf08a5a","type":"switch","z":"9341e81a2672a77b","name":"","property":"payload.data_record_end_time","propertyType":"msg","rules":[{"t":"gt","v":"","vt":"prev"},{"t":"else"}],"checkall":"true","repair":false,"outputs":2,"x":950,"y":440,"wires":[["f8c4f7e6629310cb"],[]]},{"id":"cd5c61642abc1632","type":"switch","z":"9341e81a2672a77b","name":"","property":"payload.data_record_end_time","propertyType":"msg","rules":[{"t":"gt","v":"","vt":"prev"},{"t":"else"}],"checkall":"true","repair":false,"outputs":2,"x":950,"y":500,"wires":[["9cace0e7d80f0fec"],[]]},{"id":"7db8532370fd384d","type":"switch","z":"9341e81a2672a77b","name":"","property":"payload.data_record_end_time","propertyType":"msg","rules":[{"t":"gt","v":"","vt":"prev"},{"t":"else"}],"checkall":"true","repair":false,"outputs":2,"x":950,"y":560,"wires":[["b3e7f7b6d745543b"],[]]},{"id":"018d9c5d8af3c28a","type":"ha-entity-config","server":"5d1c0eb6.fa674","deviceConfig":"502c0a918e764ed3","name":"CO Orario","version":6,"entityType":"sensor","haConfig":[{"property":"name","value":"CO Orario"},{"property":"icon","value":""},{"property":"entity_picture","value":""},{"property":"entity_category","value":""},{"property":"device_class","value":""},{"property":"unit_of_measurement","value":"mg/m³"},{"property":"state_class","value":""}],"resend":false,"debugEnabled":false},{"id":"d164653373b81866","type":"ha-entity-config","server":"5d1c0eb6.fa674","deviceConfig":"502c0a918e764ed3","name":"SO2 Orario","version":6,"entityType":"sensor","haConfig":[{"property":"name","value":"SO2 Orario"},{"property":"icon","value":""},{"property":"entity_picture","value":""},{"property":"entity_category","value":""},{"property":"device_class","value":"sulphur_dioxide"},{"property":"unit_of_measurement","value":"µg/m³"},{"property":"state_class","value":"measurement"}],"resend":false,"debugEnabled":false},{"id":"ea9fa5358962befe","type":"ha-entity-config","server":"5d1c0eb6.fa674","deviceConfig":"502c0a918e764ed3","name":"C6H6 Orario","version":6,"entityType":"sensor","haConfig":[{"property":"name","value":"C6H6 Orario"},{"property":"icon","value":""},{"property":"entity_picture","value":""},{"property":"entity_category","value":""},{"property":"device_class","value":"pm10"},{"property":"unit_of_measurement","value":"µg/m³"},{"property":"state_class","value":"measurement"}],"resend":false,"debugEnabled":false},{"id":"2b73079bc1f934e1","type":"ha-entity-config","server":"5d1c0eb6.fa674","deviceConfig":"502c0a918e764ed3","name":"PM10 Orario","version":6,"entityType":"sensor","haConfig":[{"property":"name","value":"PM10 Orario"},{"property":"icon","value":""},{"property":"entity_picture","value":""},{"property":"entity_category","value":""},{"property":"device_class","value":"pm10"},{"property":"unit_of_measurement","value":"µg/m³"},{"property":"state_class","value":"measurement"}],"resend":false,"debugEnabled":false},{"id":"e913556f2e570def","type":"ha-entity-config","server":"5d1c0eb6.fa674","deviceConfig":"502c0a918e764ed3","name":"PM25 Orario","version":6,"entityType":"sensor","haConfig":[{"property":"name","value":"PM25 Orario"},{"property":"icon","value":""},{"property":"entity_picture","value":""},{"property":"entity_category","value":""},{"property":"device_class","value":"pm25"},{"property":"unit_of_measurement","value":"µg/m³"},{"property":"state_class","value":"measurement"}],"resend":false,"debugEnabled":false},{"id":"8b9bc702715f3b15","type":"ha-entity-config","server":"5d1c0eb6.fa674","deviceConfig":"502c0a918e764ed3","name":"O3 Orario","version":6,"entityType":"sensor","haConfig":[{"property":"name","value":"O3 Orario"},{"property":"icon","value":""},{"property":"entity_picture","value":""},{"property":"entity_category","value":""},{"property":"device_class","value":"ozone"},{"property":"unit_of_measurement","value":"µg/m³"},{"property":"state_class","value":"measurement"}],"resend":false,"debugEnabled":false},{"id":"136a6476a7590443","type":"ha-entity-config","server":"5d1c0eb6.fa674","deviceConfig":"502c0a918e764ed3","name":"NO2 Orario","version":6,"entityType":"sensor","haConfig":[{"property":"name","value":"NO2 Orario"},{"property":"icon","value":""},{"property":"entity_picture","value":""},{"property":"entity_category","value":""},{"property":"device_class","value":"sulphur_dioxide"},{"property":"unit_of_measurement","value":"µg/m³"},{"property":"state_class","value":"measurement"}],"resend":false,"debugEnabled":false},{"id":"09fe098a6e9c3183","type":"ha-entity-config","server":"5d1c0eb6.fa674","deviceConfig":"502c0a918e764ed3","name":"Aggiorna_dati_ISPRA","version":6,"entityType":"button","haConfig":[{"property":"name","value":"Aggiorna dati ISPRA"},{"property":"icon","value":""},{"property":"entity_picture","value":""},{"property":"entity_category","value":""},{"property":"device_class","value":""}],"resend":false,"debugEnabled":false},{"id":"5d1c0eb6.fa674","type":"server","name":"Home Assistant","addon":true,"rejectUnauthorizedCerts":true,"ha_boolean":"","connectionDelay":false,"cacheJson":true,"heartbeat":false,"heartbeatInterval":"","areaSelector":"id","deviceSelector":"id","entitySelector":"id","statusSeparator":"","enableGlobalContextStore":true},{"id":"502c0a918e764ed3","type":"ha-device-config","name":"Node-RED","hwVersion":"","manufacturer":"Node-RED","model":"","swVersion":""}]
```

Il codice sopra indicato prevede anche la creazione di un pulsante in Home Assistant così da poter richiarmare l'aggiornamento manualmente quando si vuole. Non è necessario e può essere eliminato perchè l'aggiornamento avviene ciclicamente ogni ora mediante il tasto `inject` per l'aggiornamento orario che, alla sua sinistra, presenta anche il tastino per l'attivazione manuale.

Dobbiamo però personalizzare il codice:
1. inserire le stringhe per il download dei dati. Come si è avuto modo di notare il download è singolo per ogni inquinante, pertanto, individuata la stringa come indicato sopra bisognerà aprire il nodo `http request` e nel campo `URL` inserire la stringa di download per ogni singolo inquinante relativamente ad ogni singola centralina che si vuole conoscere.
2. Inserire il codice della Stazione nel primo dei due campi `switch`.
3. Non toccate altro.
4. Eseguite un `Deploy`
5. Cliccate sulla casellina del  nodo `inject`. Se tutto è andato a buon fine vedrete comparire sotto il nodo `http request` un indicatore blu con la scritta `requesting`, mentre, sotto il sensore vedrete comparire un indicatore verde con un numero che indicherà proprio il valore dell`inquinante.

Terminata questa configuazione in Node-RED, vediamo cosa succede in Home Assistant:

Se abbiamo rispettato tutti i prerequisiti, tra i `Device` delle impostazioni troveremo `Node-Red Companion`. Al suo interno risulteranno configurati uno o più dispositivi, tra i quali, se avete seguito la mia configurazione, quello denominato `Node-RED`. All'interno di esso saranno presenti e configurati tutti i sensori ed il pulsante creato. In particolare, cliccando sui sensori e visualizzando gli attributi, vedremo la seguente configurazione (dopo il primo aggiornamento):

![HA1](https://github.com/kapkirk/Indice-di-qualita-dell-aria-via-Home-Assistant/blob/main/images/Sensore_HA.jpg)


### 4 - Configurazione Lovelace di Home Assistant

I sensori sono stati creati e possiamo dunque configurare la scheda Lovelace per la sua visualizzazione. Io ho scelto quella indicata nei prerequisiti anche perchè consente, cliccando sulle intestazioni, di visualizzare i dati secondo l'ordine preferito.

- Nella _Dashbord_ della _lovelace_, dove preferite, aprite una nuova scheda ed incollate il codice del file `HA lovelace.txt` ed il risultato sarà questo:

![lovelace](https://github.com/kapkirk/Indice-di-qualita-dell-aria-via-Home-Assistant/blob/main/images/HA_lovelace.jpg)

codice:
```yaml
type: custom:flex-table-card
title: Dati in quasi tempo reale
entities:
  include:
    - sensor.pm10_orario_2
    - sensor.pm25_orario_2
    - sensor.no2_orario_2
    - sensor.co_orario_2
    - sensor.o3_orario_2
    - sensor.c6h6_orario_2
  sort_by: name
columns:
  - name: Inquin.
    data: inquinante_sigla
  - name: Val.
    data: state
  - name: Unità misura
    data: unita_misura
  - name: Livello Inq.
    data: livello_inquinante
  - name: Ultima rilevazione
    data: data_rilevazione
grid_options:
  columns: 15
  rows: 6
```

Notate che, avendo eseguito diverse prove, i miei sensori in `Home Assistant` hanno il suffisso `_2`, eventualmente rimuovetelo.


### 5 - Configurazione Sensore di Qualità dell'Aria


- Terminata questa fase l'ultimo step è quello di creare il sensore di qualità dell'aria basato su questi dati. La sua configurazione è un template che va configurtato come segue e restituirà il valore più basso tra quelli dei singoli sensori espresso sotto forma di giudizio sintetico:

codice:
```yaml
    - name: "AQI"
      unique_id: qualita_aria
      state: >
          {% set sensori = [
            'sensor.pm10_orario_2',
            'sensor.pm25_orario_2',
            'sensor.no2_orario_2',
            'sensor.so2_orario_2',
            'sensor.co_orario_2',
            'sensor.o3_orario_2',
            'sensor.c6h6_orario_2'
          ] %}
          
          {% set classi = {
            6: 'ottima',
            5: 'buona',
            4: 'discreta',
            3: 'sufficiente',
            2: 'scarsa'
          } %}
          
          {% set valori_numerici = [
            state_attr('sensor.pm10_orario_2', 'livello_inquinante'),
            state_attr('sensor.pm25_orario_2', 'livello_inquinante'),
            state_attr('sensor.no2_orario_2', 'livello_inquinante'),
            state_attr('sensor.so2_orario_2', 'livello_inquinante'),
            state_attr('sensor.co_orario_2', 'livello_inquinante'),
            state_attr('sensor.o3_orario_2', 'livello_inquinante'),
            state_attr('sensor.c6h6_orario_2', 'livello_inquinante')
          ] | select('!=', None) | list %}
          
          {% if valori_numerici %}
            {% set valore_peggiore = valori_numerici | min %}
            {{ classi[valore_peggiore] }}
          {% else %}
            non disponibile
          {% endif %}
```

anche questo potrà essere viasualizzato nella Lovelace come meglio credete. Io l'ho esposto nella dashboard cellulare:

![lovelace2](https://github.com/kapkirk/Indice-di-qualita-dell-aria-via-Home-Assistant/blob/main/images/HA_lovelace2.jpg)


e nella scheda dedicata:

![lovelace3](https://github.com/kapkirk/Indice-di-qualita-dell-aria-via-Home-Assistant/blob/main/images/HA_lovelace3.jpg)


Il pulsante che vedete con l'etichetta (Aggiornamento dati ISPRA) è quello reso disponibile da Node-RED nella configurazione sopra esposta che utilizzo per l'aggiornamento manuale dei dati.

La seconda parte che vedete nella foto, invece, è quella dedicata ai dati ambientali provenienti direttamente da ARPA Puglia. In questo caso, però, i dati sono acquisiti, filtrati e validati dall'Ente che li pubblica con cadenza giornaliera, essi sono riferiti al giorno precedente. 
Se a qualcuno dovessero interessare, questi sono i link ai due progetti:

- [Implementazione in Home Assistant tramite Node-RED](https://github.com/kapkirk/Dati-ambientali-ARPA-Puglia-via-Home-Assistant-e-NodeRED)
- [Implementazione in Home Assistant tramite Node-RED ed MQTT](https://github.com/kapkirk/Dati-ambientali-ARPA-Puglia-via-Home-Assistant)
  

Lavoro finito e buon divertimento!

