# Indice di qualità dell'aria Via Home Assistant

| [italiano](https://github.com/kapkirk/Indice-di-qualita-dell-aria-via-Home-Assistant#acquisizione-dati-inquinanti-ambientali-arpa-puglia-in-home-assistant) | [inglese](https://github.com/kapkirk/Indice-di-qualita-dell-aria-via-Home-Assistant#arpa-puglia-environmental-pollutant-data-acquisition-in-home-assistant) |

![](https://github.com/kapkirk/Indice-di-qualita-dell-aria-via-Home-Assistant/blob/main/images/HA%20logo2.png)  ` ` ![](https://github.com/kapkirk/Indice-di-qualita-dell-aria-via-Home-Assistant/blob/main/images/Node-RED%20logo.jpg)            `  `
---   
# Acquisizione dati inquinanti ambientali ARPA Puglia in Home Assistant

Una utility [Home Assistant](https://home-assistant.io/) che ti aiuta a visualizzare la qualità dell'aria ed i singoli dati dei principali inquinanti ambientali pubblicati da [I.S.P.R.A.](https://www.isprambiente.gov.it/it/) (**Istituto Superiore per la Protezione e la Ricerca Ambientale**) utilizzando i dati forniti dalle Regioni italiane in ["quasi tempo reale"](https://www.isprambiente.gov.it/it/attivita/aria-1/qualita-dellaria/dati-in-tempo-quasi-reale).

Come è possibile leggere nella pagine dell'Istituto italiano:

      `I dati in “tempo quasi reale”, sono raccolti e trasmessi da parte delle Regioni e Province Autonome, ossia con un minimo 
       fisiologico ritardo (di qualche ora), vengono trasmessi quotidianamente dall’ ISPRA alla Commissione Europea. 
       Si tratta di dati caratterizzati da un livello minimo di validazione ovvero che non sono stati sottoposti ai processi 
       di validazione previsti successivamente all’acquisizione della misura ed è quindi possibile che in un secondo momento 
       vengano corretti.
       
       Nella dashboard qui pubblicata è possibile consultare i dati in tempo quasi reale relativi agli inquinanti 
       NO2, O3, PM10, PM2,5, C6H6, CO e SO2.`



<br>

## Tavola dei Contenuti

1. **[Descrizione del progetto](https://github.com/kapkirk/Indice-di-qualita-dell-aria-via-Home-Assistant#descrizione-del-progetto)**

2. **[Caratteristiche principali](https://github.com/kapkirk/Indice-di-qualita-dell-aria-via-Home-Assistant#caratteristiche-principali)**

3. **[Descrizione del funzionamento](https://github.com/kapkirk/Indice-di-qualita-dell-aria-via-Home-Assistant#descrizione-del-funzionamento)**

4. **[Installazione](https://github.com/kapkirk/Indice-di-qualita-dell-aria-via-Home-Assistant#installazione)**
   1. **[Prerequisiti](https://github.com/kapkirk/Indice-di-qualita-dell-aria-via-Home-Assistant#1---prerequisiti)**
   1. **[Configurazione dei dati da acquisire](https://github.com/kapkirk/Indice-di-qualita-dell-aria-via-Home-Assistant#2---configurazione-dei-dati-da-acquisire)**
   1. **[Configurazione Home Assistant](https://github.com/kapkirk/Indice-di-qualita-dell-aria-via-Home-Assistant#3---configurazione-home-assistant)**
   2. **[Configurazione di Node-RED](https://github.com/kapkirk/Indice-di-qualita-dell-aria-via-Home-Assistant#4---configurazione-di-node-red)**

5. **[Personalizzazione dei flussi di NodeRed](https://github.com/kapkirk/Indice-di-qualita-dell-aria-via-Home-Assistant#personalizzazione-ed-analisi-dei-flussi-nodered)**

6. **[Commento del codice](https://github.com/kapkirk/Indice-di-qualita-dell-aria-via-Home-Assistant#commentiamolo)**  
 

 
<br>

## Descrizione del progetto

Scopo principale di questo progetto  è quello di automatizzare l`acquisizione "in quasi tempo reale" di un indice di qualità dell'aria acquisendo i dati ambientali pubblicati tramite API dall'ISPRA che li acquisisce della diverse Agenzie Regionali di Protezione e Prevenzione Ambientale sparse su tutto il territorio nazionale, la loro elaborazione tramite Node-RED e la successiva integrazione in Home Assistant per la successiva visualizzazione.

Tutte le info sono disponibili sul sito dell'Istituto traime il [S.I.N.A.](https://sinacloud.isprambiente.it/portal/apps/experiencebuilder/experience/?draft=true&id=df677d20871d4383b34ce355e24f0598&page=page_38) (**Sistema Unformativo Nazionale Ambientale**) secondo la [mappa](https://dati.arpa.puglia.it/qaria?footer=false%EF%BB%BF) dove i dati sono disponbili per il [download](https://sinacloud.isprambiente.it/portal/apps/experiencebuilder/experience/?draft=true&id=df677d20871d4383b34ce355e24f0598&page=page_74). 

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
   Node-RED effettua chiamate API ogni ora, filtra i dati e restituisce il singolo valore aggiornato.

2. **Elaborazione**:  
   I dati vengono analizzati e restituiti sian singolarmente che in modo aggregato fornendo il singolo valore di qualità dell'aria. 

3. **Invio a Home Assistant**:  
   I payload sono pubblicati in sensori direttamente esposti in HA.

5. **Visualizzazione**:  
   I dati dati così ottenuti sono graficamente esposti.

---

## Installazione

### 1 - Prerequisiti

- Node-RED installato e configurato con nodi:
  - `node-red-contrib-http-request`
- HACS installata e configurata con:
  - la custom `flex-table-card` (Se volete utilizzare la tabella di visualizzazione come ho fatto io).
  - `Node-RED Companion` per l'interfaccia dei sensori.


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


1. La procedura da seuigre per individuare il dato è la seguente:
- Accedere alla pagine del [download](https://sinacloud.isprambiente.it/portal/apps/experiencebuilder/experience/?data_id=dataSource_137-infoariadowload_7094-infoariadowload%3A127&draft=true&id=df677d20871d4383b34ce355e24f0598&page=page_74)
- Selezionare la Regione della quale si vuole acquisire il dato inquinante ed individuare il rigo dell'inquinante. Il terzo campo della tabella conterrà il link per il download che bisognerà copiare per inserirlo nel flusso di Node-RED.
  
  Ad esempio, volendo conoscere il dato di SO2 per la Regione Abruzzo, otterremo il seguente link:

    `https://sdi.isprambiente.it/geoserver/infoaria/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=infoaria%3Adati_nrt_informambiente_mv&CQL_FILTER=region_name=%27ABRUZZO%27+AND+pollutant_id=%271%27&maxFeatures=10000&outputFormat=csv `

   può essere utilizzare anche nel normale browser. La sua consultazione genererà il download di un file che potrete leggere ed apprezzare soprattutto perchè per la centralina che avrete individuato, vi consentirà di sapere quali sono i dati pubblicati da ISPRA.

    
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
- in alto cliccare su `Add`. Il rpogramma tornerà alla schermata precedente di configurazione del sensore, ottenendo la seguente configurazione:

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


- a questo punto possiamo acquisire il codice in Node-RED, lo trovate nel file `flusso Node-Red.json`, oppure da copiare ed incollare:

![Node-red1](https://github.com/kapkirk/Indice-di-qualita-dell-aria-via-Home-Assistant/blob/main/images/Flusso_Node-Red.jpg)



codice:
```yaml
[{"id":"9341e81a2672a77b","type":"tab","label":"Dari Orari ISPRA","disabled":false,"info":"","env":[]},{"id":"86a27412fd248875","type":"http request","z":"9341e81a2672a77b","name":"","method":"GET","ret":"txt","paytoqs":"ignore","url":"https://sdi.isprambiente.it/geoserver/infoaria/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=infoaria%3Adati_nrt_informambiente_mv&CQL_FILTER=region_name=%27PUGLIA%27+AND+pollutant_id=%2710%27&maxFeatures=10000&outputFormat=csv","tls":"","persist":true,"proxy":"","insecureHTTPParser":true,"authType":"","senderr":false,"headers":[],"x":490,"y":200,"wires":[["129a117ec0480da4"]]},{"id":"129a117ec0480da4","type":"csv","z":"9341e81a2672a77b","name":"","spec":"rfc","sep":",","hdrin":true,"hdrout":"none","multi":"one","ret":"\\r\\n","temp":"","skip":"0","strings":true,"include_empty_strings":true,"include_null_values":true,"x":630,"y":200,"wires":[["0f80c4ac185f9d2b"]]},{"id":"d4c2feeff75e09fc","type":"http request","z":"9341e81a2672a77b","name":"","method":"GET","ret":"txt","paytoqs":"ignore","url":"https://sdi.isprambiente.it/geoserver/infoaria/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=infoaria%3Adati_nrt_informambiente_mv&CQL_FILTER=region_name=%27PUGLIA%27+AND+pollutant_id=%2720%27&maxFeatures=10000&outputFormat=csv","tls":"","persist":true,"proxy":"","insecureHTTPParser":false,"authType":"","senderr":false,"headers":[],"x":490,"y":320,"wires":[["6039f795bf127e3a"]]},{"id":"aa59fbdcd1545be8","type":"http request","z":"9341e81a2672a77b","name":"","method":"GET","ret":"txt","paytoqs":"ignore","url":"https://sdi.isprambiente.it/geoserver/infoaria/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=infoaria%3Adati_nrt_informambiente_mv&CQL_FILTER=region_name=%27PUGLIA%27+AND+pollutant_id=%275%27&maxFeatures=10000&outputFormat=csv","tls":"","persist":true,"proxy":"","insecureHTTPParser":false,"authType":"","senderr":false,"headers":[],"x":490,"y":380,"wires":[["10e322bfb597f397"]]},{"id":"d2e0462a8bfc7fc4","type":"http request","z":"9341e81a2672a77b","name":"","method":"GET","ret":"txt","paytoqs":"ignore","url":"https://sdi.isprambiente.it/geoserver/infoaria/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=infoaria%3Adati_nrt_informambiente_mv&CQL_FILTER=region_name=%27PUGLIA%27+AND+pollutant_id=%276001%27&maxFeatures=10000&outputFormat=csv","tls":"","persist":true,"proxy":"","insecureHTTPParser":false,"authType":"","senderr":false,"headers":[],"x":490,"y":440,"wires":[["a1f4b7fdd094dac2"]]},{"id":"d91e018119691670","type":"http request","z":"9341e81a2672a77b","name":"","method":"GET","ret":"txt","paytoqs":"ignore","url":"https://sdi.isprambiente.it/geoserver/infoaria/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=infoaria%3Adati_nrt_informambiente_mv&CQL_FILTER=region_name=%27PUGLIA%27+AND+pollutant_id=%277%27&maxFeatures=10000&outputFormat=csv","tls":"","persist":true,"proxy":"","insecureHTTPParser":false,"authType":"","senderr":false,"headers":[],"x":490,"y":500,"wires":[["2f140e806700e380"]]},{"id":"bc4ecc4da286b3c8","type":"http request","z":"9341e81a2672a77b","name":"","method":"GET","ret":"txt","paytoqs":"ignore","url":"https://sdi.isprambiente.it/geoserver/infoaria/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=infoaria%3Adati_nrt_informambiente_mv&CQL_FILTER=region_name=%27PUGLIA%27+AND+pollutant_id=%278%27&maxFeatures=10000&outputFormat=csv","tls":"","persist":true,"proxy":"","insecureHTTPParser":false,"authType":"","senderr":false,"headers":[],"x":490,"y":560,"wires":[["193995d8afc547b0"]]},{"id":"a76b8be52e38c6df","type":"csv","z":"9341e81a2672a77b","name":"","spec":"rfc","sep":",","hdrin":true,"hdrout":"none","multi":"one","ret":"\\r\\n","temp":"","skip":"0","strings":true,"include_empty_strings":true,"include_null_values":true,"x":630,"y":260,"wires":[["caa73170cbae11e6"]]},{"id":"6039f795bf127e3a","type":"csv","z":"9341e81a2672a77b","name":"","spec":"rfc","sep":",","hdrin":true,"hdrout":"none","multi":"one","ret":"\\r\\n","temp":"","skip":"0","strings":true,"include_empty_strings":true,"include_null_values":true,"x":630,"y":320,"wires":[["260a26186db8e11c"]]},{"id":"10e322bfb597f397","type":"csv","z":"9341e81a2672a77b","name":"","spec":"rfc","sep":",","hdrin":true,"hdrout":"none","multi":"one","ret":"\\r\\n","temp":"","skip":"0","strings":true,"include_empty_strings":true,"include_null_values":true,"x":630,"y":380,"wires":[["0efe1d45b2822b0a"]]},{"id":"a1f4b7fdd094dac2","type":"csv","z":"9341e81a2672a77b","name":"","spec":"rfc","sep":",","hdrin":true,"hdrout":"none","multi":"one","ret":"\\r\\n","temp":"","skip":"0","strings":true,"include_empty_strings":true,"include_null_values":true,"x":630,"y":440,"wires":[["d5b73c602d374caa"]]},{"id":"2f140e806700e380","type":"csv","z":"9341e81a2672a77b","name":"","spec":"rfc","sep":",","hdrin":true,"hdrout":"none","multi":"one","ret":"\\r\\n","temp":"","skip":"0","strings":true,"include_empty_strings":true,"include_null_values":true,"x":630,"y":500,"wires":[["5bcf5b37d42bdfee"]]},{"id":"193995d8afc547b0","type":"csv","z":"9341e81a2672a77b","name":"","spec":"rfc","sep":",","hdrin":true,"hdrout":"none","multi":"one","ret":"\\r\\n","temp":"","skip":"0","strings":true,"include_empty_strings":true,"include_null_values":true,"x":630,"y":560,"wires":[["65f747768b243167"]]},{"id":"3d80e107b51013e6","type":"http request","z":"9341e81a2672a77b","name":"","method":"GET","ret":"txt","paytoqs":"ignore","url":"https://sdi.isprambiente.it/geoserver/infoaria/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=infoaria%3Adati_nrt_informambiente_mv&CQL_FILTER=region_name=%27PUGLIA%27+AND+pollutant_id=%271%27&maxFeatures=10000&outputFormat=csv","tls":"","persist":true,"proxy":"","insecureHTTPParser":false,"authType":"","senderr":false,"headers":[],"x":490,"y":260,"wires":[["a76b8be52e38c6df"]]},{"id":"0f80c4ac185f9d2b","type":"switch","z":"9341e81a2672a77b","name":"","property":"payload.station_eu_code","propertyType":"msg","rules":[{"t":"eq","v":"IT1658A","vt":"str"},{"t":"else"}],"checkall":"true","repair":false,"outputs":2,"x":810,"y":200,"wires":[["bf84667c52653692"],[]]},{"id":"70c367d7c81694b0","type":"ha-sensor","z":"9341e81a2672a77b","name":"CO Orario","entityConfig":"018d9c5d8af3c28a","version":0,"state":"payload.data_record_value","stateType":"msg","attributes":[{"property":"luogo","value":"payload.municipality_name","valueType":"msg"},{"property":"indirizzo","value":"payload.station_municipality","valueType":"msg"},{"property":"codice_europeo","value":"payload.station_eu_code","valueType":"msg"},{"property":"inquinante_sigla","value":"payload.pollutant_notation","valueType":"msg"},{"property":"inquinante_descrizione","value":"payload.pollutant_label","valueType":"msg"},{"property":"data_rilevazione","value":"payload.data_record_end_time","valueType":"msg"},{"property":"unita_misura","value":"payload.observation_unit_notation","valueType":"msg"},{"property":"livello_inquinante","value":"payload.pollutant_level","valueType":"msg"},{"property":"posizione_stazione","value":"payload.station_position","valueType":"msg"},{"property":"limite","value":"10 mg/m3 ogni 8 ore","valueType":"str"}],"inputOverride":"allow","outputProperties":[],"x":1130,"y":200,"wires":[[]]},{"id":"0efe1d45b2822b0a","type":"switch","z":"9341e81a2672a77b","name":"","property":"payload.station_eu_code","propertyType":"msg","rules":[{"t":"eq","v":"IT1658A","vt":"str"},{"t":"else"}],"checkall":"true","repair":false,"outputs":2,"x":810,"y":380,"wires":[["a7f2dabdfa56f504"],[]]},{"id":"d5b73c602d374caa","type":"switch","z":"9341e81a2672a77b","name":"","property":"payload.station_eu_code","propertyType":"msg","rules":[{"t":"eq","v":"IT1658A","vt":"str"},{"t":"else"}],"checkall":"true","repair":false,"outputs":2,"x":810,"y":440,"wires":[["b8d2af647cf08a5a"],[]]},{"id":"5bcf5b37d42bdfee","type":"switch","z":"9341e81a2672a77b","name":"","property":"payload.station_eu_code","propertyType":"msg","rules":[{"t":"eq","v":"IT2139A","vt":"str"},{"t":"else"}],"checkall":"true","repair":false,"outputs":2,"x":810,"y":500,"wires":[["cd5c61642abc1632"],[]]},{"id":"65f747768b243167","type":"switch","z":"9341e81a2672a77b","name":"","property":"payload.station_eu_code","propertyType":"msg","rules":[{"t":"eq","v":"IT1657A","vt":"str"},{"t":"else"}],"checkall":"true","repair":false,"outputs":2,"x":810,"y":560,"wires":[["7db8532370fd384d"],[]]},{"id":"caa73170cbae11e6","type":"switch","z":"9341e81a2672a77b","name":"","property":"payload.station_eu_code","propertyType":"msg","rules":[{"t":"eq","v":"IT1658A","vt":"str"},{"t":"else"}],"checkall":"true","repair":false,"outputs":2,"x":810,"y":260,"wires":[["494566f4d1175bf5"],[]]},{"id":"f359e094c2916855","type":"ha-sensor","z":"9341e81a2672a77b","name":"SO2 Orario","entityConfig":"d164653373b81866","version":0,"state":"payload.data_record_value","stateType":"msg","attributes":[{"property":"luogo","value":"payload.municipality_name","valueType":"msg"},{"property":"indirizzo","value":"payload.station_municipality","valueType":"msg"},{"property":"codice_europeo","value":"payload.station_eu_code","valueType":"msg"},{"property":"inquinante_sigla","value":"payload.pollutant_notation","valueType":"msg"},{"property":"inquinante_descrizione","value":"payload.pollutant_label","valueType":"msg"},{"property":"data_rilevazione","value":"payload.data_record_end_time","valueType":"msg"},{"property":"unita_misura","value":"payload.observation_unit_notation","valueType":"msg"},{"property":"livello_inquinante","value":"payload.pollutant_level","valueType":"msg"},{"property":"posizione_stazione","value":"payload.station_position","valueType":"msg"},{"property":"limite","value":"350  µg/m3 al giorno","valueType":"str"}],"inputOverride":"allow","outputProperties":[],"x":1130,"y":260,"wires":[[]]},{"id":"be1140aedd07108f","type":"ha-sensor","z":"9341e81a2672a77b","name":"C6H6 Orario","entityConfig":"ea9fa5358962befe","version":0,"state":"payload.data_record_value","stateType":"msg","attributes":[{"property":"luogo","value":"payload.municipality_name","valueType":"msg"},{"property":"indirizzo","value":"payload.station_municipality","valueType":"msg"},{"property":"codice_europeo","value":"payload.station_eu_code","valueType":"msg"},{"property":"inquinante_sigla","value":"payload.pollutant_notation","valueType":"msg"},{"property":"inquinante_descrizione","value":"payload.pollutant_label","valueType":"msg"},{"property":"data_rilevazione","value":"payload.data_record_end_time","valueType":"msg"},{"property":"unita_misura","value":"payload.observation_unit_notation","valueType":"msg"},{"property":"livello_inquinante","value":"payload.pollutant_level","valueType":"msg"},{"property":"posizione_stazione","value":"payload.station_position","valueType":"msg"},{"property":"limite","value":"5 µg/m3 all'anno","valueType":"str"}],"inputOverride":"allow","outputProperties":[],"x":1130,"y":320,"wires":[[]]},{"id":"122187a9ccb9da0e","type":"ha-sensor","z":"9341e81a2672a77b","name":"PM10 Orario","entityConfig":"2b73079bc1f934e1","version":0,"state":"payload.data_record_value","stateType":"msg","attributes":[{"property":"luogo","value":"payload.municipality_name","valueType":"msg"},{"property":"indirizzo","value":"payload.station_municipality","valueType":"msg"},{"property":"codice_europeo","value":"payload.station_eu_code","valueType":"msg"},{"property":"inquinante_sigla","value":"payload.pollutant_notation","valueType":"msg"},{"property":"inquinante_descrizione","value":"payload.pollutant_label","valueType":"msg"},{"property":"data_rilevazione","value":"payload.data_record_end_time","valueType":"msg"},{"property":"unita_misura","value":"payload.observation_unit_notation","valueType":"msg"},{"property":"livello_inquinante","value":"payload.pollutant_level","valueType":"msg"},{"property":"posizione_stazione","value":"payload.station_position","valueType":"msg"},{"property":"limite","value":"50 µg/m3 al giorno per non più di 35 volte in un anno","valueType":"str"}],"inputOverride":"allow","outputProperties":[],"x":1130,"y":380,"wires":[[]]},{"id":"f8c4f7e6629310cb","type":"ha-sensor","z":"9341e81a2672a77b","name":"PM25 Orario","entityConfig":"e913556f2e570def","version":0,"state":"payload.data_record_value","stateType":"msg","attributes":[{"property":"luogo","value":"payload.municipality_name","valueType":"msg"},{"property":"indirizzo","value":"payload.station_municipality","valueType":"msg"},{"property":"codice_europeo","value":"payload.station_eu_code","valueType":"msg"},{"property":"inquinante_sigla","value":"payload.pollutant_notation","valueType":"msg"},{"property":"inquinante_descrizione","value":"payload.pollutant_label","valueType":"msg"},{"property":"data_rilevazione","value":"payload.data_record_end_time","valueType":"msg"},{"property":"unita_misura","value":"payload.observation_unit_notation","valueType":"msg"},{"property":"livello_inquinante","value":"payload.pollutant_level","valueType":"msg"},{"property":"posizione_stazione","value":"payload.station_position","valueType":"msg"},{"property":"limite","value":"25 µg/m3 al giorno","valueType":"str"}],"inputOverride":"allow","outputProperties":[],"x":1130,"y":440,"wires":[[]]},{"id":"9cace0e7d80f0fec","type":"ha-sensor","z":"9341e81a2672a77b","name":"O3 Orario","entityConfig":"8b9bc702715f3b15","version":0,"state":"payload.data_record_value","stateType":"msg","attributes":[{"property":"luogo","value":"payload.municipality_name","valueType":"msg"},{"property":"indirizzo","value":"payload.station_municipality","valueType":"msg"},{"property":"codice_europeo","value":"payload.station_eu_code","valueType":"msg"},{"property":"inquinante_sigla","value":"payload.pollutant_notation","valueType":"msg"},{"property":"inquinante_descrizione","value":"payload.pollutant_label","valueType":"msg"},{"property":"data_rilevazione","value":"payload.data_record_end_time","valueType":"msg"},{"property":"unita_misura","value":"payload.observation_unit_notation","valueType":"msg"},{"property":"livello_inquinante","value":"payload.pollutant_level","valueType":"msg"},{"property":"posizione_stazione","value":"payload.station_position","valueType":"msg"},{"property":"limite","value":"180 µg/m3 per ora","valueType":"str"}],"inputOverride":"allow","outputProperties":[],"x":1120,"y":500,"wires":[[]]},{"id":"b3e7f7b6d745543b","type":"ha-sensor","z":"9341e81a2672a77b","name":"NO2 Orario","entityConfig":"136a6476a7590443","version":0,"state":"payload.data_record_value","stateType":"msg","attributes":[{"property":"luogo","value":"payload.municipality_name","valueType":"msg"},{"property":"indirizzo","value":"payload.station_municipality","valueType":"msg"},{"property":"codice_europeo","value":"payload.station_eu_code","valueType":"msg"},{"property":"inquinante_sigla","value":"payload.pollutant_notation","valueType":"msg"},{"property":"inquinante_descrizione","value":"payload.pollutant_label","valueType":"msg"},{"property":"data_rilevazione","value":"payload.data_record_end_time","valueType":"msg"},{"property":"unita_misura","value":"payload.observation_unit_notation","valueType":"msg"},{"property":"livello_inquinante","value":"payload.pollutant_level","valueType":"msg"},{"property":"posizione_stazione","value":"payload.station_position","valueType":"msg"},{"property":"limite","value":"200 µg/m3 al giorno per non più di 18 volte in un anno","valueType":"str"}],"inputOverride":"allow","outputProperties":[],"x":1130,"y":560,"wires":[[]]},{"id":"d17996519aae5d44","type":"ha-button","z":"9341e81a2672a77b","name":"","version":0,"debugenabled":false,"outputs":1,"entityConfig":"09fe098a6e9c3183","outputProperties":[{"property":"payload","propertyType":"msg","value":"","valueType":"entityState"},{"property":"topic","propertyType":"msg","value":"","valueType":"triggerId"},{"property":"data","propertyType":"msg","value":"","valueType":"entity"}],"x":150,"y":40,"wires":[["ab8c3c44fbcf8ab6"]]},{"id":"45f7384ded2e44b5","type":"inject","z":"9341e81a2672a77b","name":"","props":[{"p":"payload"},{"p":"topic","vt":"str"}],"repeat":"3600","crontab":"","once":true,"onceDelay":0.1,"topic":"","payload":"","payloadType":"date","x":190,"y":120,"wires":[["ab8c3c44fbcf8ab6"]]},{"id":"ab8c3c44fbcf8ab6","type":"link out","z":"9341e81a2672a77b","name":"link out 123","mode":"link","links":["93bab1ec2d64d3a7"],"x":345,"y":120,"wires":[]},{"id":"93bab1ec2d64d3a7","type":"link in","z":"9341e81a2672a77b","name":"link in 65","links":["ab8c3c44fbcf8ab6"],"x":315,"y":380,"wires":[["86a27412fd248875","3d80e107b51013e6","d4c2feeff75e09fc","aa59fbdcd1545be8","d2e0462a8bfc7fc4","d91e018119691670","bc4ecc4da286b3c8"]]},{"id":"260a26186db8e11c","type":"switch","z":"9341e81a2672a77b","name":"","property":"payload.station_eu_code","propertyType":"msg","rules":[{"t":"eq","v":"IT1658A","vt":"str"},{"t":"else"}],"checkall":"true","repair":false,"outputs":2,"x":810,"y":320,"wires":[["136098c27cd667eb"],[]]},{"id":"c409f470e25feae8","type":"comment","z":"9341e81a2672a77b","name":"Carbon monoxide (air)","info":"","x":1320,"y":200,"wires":[]},{"id":"2fc04ecdb49a76e2","type":"comment","z":"9341e81a2672a77b","name":" Sulphur dioxide (air)","info":"","x":1310,"y":260,"wires":[]},{"id":"21a4b5e2da677ee2","type":"comment","z":"9341e81a2672a77b","name":"Benzene (air)","info":"","x":1290,"y":320,"wires":[]},{"id":"26eb8d5360629947","type":"comment","z":"9341e81a2672a77b","name":"PM10","info":"","x":1270,"y":380,"wires":[]},{"id":"347f978804fde924","type":"comment","z":"9341e81a2672a77b","name":"PM 2.5","info":"","x":1270,"y":440,"wires":[]},{"id":"3e96d213d91d31d6","type":"comment","z":"9341e81a2672a77b","name":"Ozone (air)","info":"","x":1280,"y":500,"wires":[]},{"id":"a1d1d746f606c99d","type":"comment","z":"9341e81a2672a77b","name":"Nitrogen dioxide (air)","info":"","x":1310,"y":560,"wires":[]},{"id":"bf84667c52653692","type":"switch","z":"9341e81a2672a77b","name":"","property":"payload.data_record_end_time","propertyType":"msg","rules":[{"t":"gt","v":"","vt":"prev"},{"t":"else"}],"checkall":"true","repair":false,"outputs":2,"x":950,"y":200,"wires":[["70c367d7c81694b0"],[]]},{"id":"494566f4d1175bf5","type":"switch","z":"9341e81a2672a77b","name":"","property":"payload.data_record_end_time","propertyType":"msg","rules":[{"t":"gt","v":"","vt":"prev"},{"t":"else"}],"checkall":"true","repair":false,"outputs":2,"x":950,"y":260,"wires":[["f359e094c2916855"],[]]},{"id":"136098c27cd667eb","type":"switch","z":"9341e81a2672a77b","name":"","property":"payload.data_record_end_time","propertyType":"msg","rules":[{"t":"gt","v":"","vt":"prev"},{"t":"else"}],"checkall":"true","repair":false,"outputs":2,"x":950,"y":320,"wires":[["be1140aedd07108f"],[]]},{"id":"a7f2dabdfa56f504","type":"switch","z":"9341e81a2672a77b","name":"","property":"payload.data_record_end_time","propertyType":"msg","rules":[{"t":"gt","v":"","vt":"prev"},{"t":"else"}],"checkall":"true","repair":false,"outputs":2,"x":950,"y":380,"wires":[["122187a9ccb9da0e"],[]]},{"id":"b8d2af647cf08a5a","type":"switch","z":"9341e81a2672a77b","name":"","property":"payload.data_record_end_time","propertyType":"msg","rules":[{"t":"gt","v":"","vt":"prev"},{"t":"else"}],"checkall":"true","repair":false,"outputs":2,"x":950,"y":440,"wires":[["f8c4f7e6629310cb"],[]]},{"id":"cd5c61642abc1632","type":"switch","z":"9341e81a2672a77b","name":"","property":"payload.data_record_end_time","propertyType":"msg","rules":[{"t":"gt","v":"","vt":"prev"},{"t":"else"}],"checkall":"true","repair":false,"outputs":2,"x":950,"y":500,"wires":[["9cace0e7d80f0fec"],[]]},{"id":"7db8532370fd384d","type":"switch","z":"9341e81a2672a77b","name":"","property":"payload.data_record_end_time","propertyType":"msg","rules":[{"t":"gt","v":"","vt":"prev"},{"t":"else"}],"checkall":"true","repair":false,"outputs":2,"x":950,"y":560,"wires":[["b3e7f7b6d745543b"],[]]},{"id":"018d9c5d8af3c28a","type":"ha-entity-config","server":"5d1c0eb6.fa674","deviceConfig":"502c0a918e764ed3","name":"CO Orario","version":6,"entityType":"sensor","haConfig":[{"property":"name","value":"CO Orario"},{"property":"icon","value":""},{"property":"entity_picture","value":""},{"property":"entity_category","value":""},{"property":"device_class","value":""},{"property":"unit_of_measurement","value":"mg/m³"},{"property":"state_class","value":""}],"resend":false,"debugEnabled":false},{"id":"d164653373b81866","type":"ha-entity-config","server":"5d1c0eb6.fa674","deviceConfig":"502c0a918e764ed3","name":"SO2 Orario","version":6,"entityType":"sensor","haConfig":[{"property":"name","value":"SO2 Orario"},{"property":"icon","value":""},{"property":"entity_picture","value":""},{"property":"entity_category","value":""},{"property":"device_class","value":"sulphur_dioxide"},{"property":"unit_of_measurement","value":"µg/m³"},{"property":"state_class","value":"measurement"}],"resend":false,"debugEnabled":false},{"id":"ea9fa5358962befe","type":"ha-entity-config","server":"5d1c0eb6.fa674","deviceConfig":"502c0a918e764ed3","name":"C6H6 Orario","version":6,"entityType":"sensor","haConfig":[{"property":"name","value":"C6H6 Orario"},{"property":"icon","value":""},{"property":"entity_picture","value":""},{"property":"entity_category","value":""},{"property":"device_class","value":"pm10"},{"property":"unit_of_measurement","value":"µg/m³"},{"property":"state_class","value":"measurement"}],"resend":false,"debugEnabled":false},{"id":"2b73079bc1f934e1","type":"ha-entity-config","server":"5d1c0eb6.fa674","deviceConfig":"502c0a918e764ed3","name":"PM10 Orario","version":6,"entityType":"sensor","haConfig":[{"property":"name","value":"PM10 Orario"},{"property":"icon","value":""},{"property":"entity_picture","value":""},{"property":"entity_category","value":""},{"property":"device_class","value":"pm10"},{"property":"unit_of_measurement","value":"µg/m³"},{"property":"state_class","value":"measurement"}],"resend":false,"debugEnabled":false},{"id":"e913556f2e570def","type":"ha-entity-config","server":"5d1c0eb6.fa674","deviceConfig":"502c0a918e764ed3","name":"PM25 Orario","version":6,"entityType":"sensor","haConfig":[{"property":"name","value":"PM25 Orario"},{"property":"icon","value":""},{"property":"entity_picture","value":""},{"property":"entity_category","value":""},{"property":"device_class","value":"pm25"},{"property":"unit_of_measurement","value":"µg/m³"},{"property":"state_class","value":"measurement"}],"resend":false,"debugEnabled":false},{"id":"8b9bc702715f3b15","type":"ha-entity-config","server":"5d1c0eb6.fa674","deviceConfig":"502c0a918e764ed3","name":"O3 Orario","version":6,"entityType":"sensor","haConfig":[{"property":"name","value":"O3 Orario"},{"property":"icon","value":""},{"property":"entity_picture","value":""},{"property":"entity_category","value":""},{"property":"device_class","value":"ozone"},{"property":"unit_of_measurement","value":"µg/m³"},{"property":"state_class","value":"measurement"}],"resend":false,"debugEnabled":false},{"id":"136a6476a7590443","type":"ha-entity-config","server":"5d1c0eb6.fa674","deviceConfig":"502c0a918e764ed3","name":"NO2 Orario","version":6,"entityType":"sensor","haConfig":[{"property":"name","value":"NO2 Orario"},{"property":"icon","value":""},{"property":"entity_picture","value":""},{"property":"entity_category","value":""},{"property":"device_class","value":"sulphur_dioxide"},{"property":"unit_of_measurement","value":"µg/m³"},{"property":"state_class","value":"measurement"}],"resend":false,"debugEnabled":false},{"id":"09fe098a6e9c3183","type":"ha-entity-config","server":"5d1c0eb6.fa674","deviceConfig":"502c0a918e764ed3","name":"Aggiorna_dati_ISPRA","version":6,"entityType":"button","haConfig":[{"property":"name","value":"Aggiorna dati ISPRA"},{"property":"icon","value":""},{"property":"entity_picture","value":""},{"property":"entity_category","value":""},{"property":"device_class","value":""}],"resend":false,"debugEnabled":false},{"id":"5d1c0eb6.fa674","type":"server","name":"Home Assistant","addon":true,"rejectUnauthorizedCerts":true,"ha_boolean":"","connectionDelay":false,"cacheJson":true,"heartbeat":false,"heartbeatInterval":"","areaSelector":"id","deviceSelector":"id","entitySelector":"id","statusSeparator":"","enableGlobalContextStore":true},{"id":"502c0a918e764ed3","type":"ha-device-config","name":"Node-RED","hwVersion":"","manufacturer":"Node-RED","model":"","swVersion":""}]
```

Il codice sopra indicato prevede anche la creazione di un pulsante in Home Assistant così da poter richiarmare l'aggiornamento manualmente quando si vuole. Non è necessario e può essere eliminato perchè l'aggiornamento avviene ciclicamente ogni ora.

Dobbiamo però personalizzare il codice. 
L'unica cosa da eseguire è l'inserimento delle stringhe per il download dei dati. Come si è avuto modo di notare il download è singolo per ogni inquinante, pertanto, individuata la stringa come indicato sopra bisognerà aprire il nodo `http request` e nel campo `URL` inserire la stringa di download per ogni singolo inquinante relativamente ad ogni singola centralina che si vuole conoscere. 

Terminata questa configuazione in Node-RED, vediamo cosa succede in Home Assistant:

Se abbiamo rispettiato tutti i prerequisiti, nei `Device` troveremo `Node-Red Companion`. Al suo interno risulterà configurato uno o più dispositivi, tra i quali, se avete seguito la mia configurazione quello denominato `Node-RED`. All'interno di esso saranno presenti e configurati tutti i sensori ed il pulsante creato. In particolare, cliccando sui sensori e visualizzando gli attributi, vedremo la seguente configurazione (dopo il primo aggiornamento):

![HA1](https://github.com/kapkirk/Indice-di-qualita-dell-aria-via-Home-Assistant/blob/main/images/Sensore_HA.jpg)


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

anche questo potrà essere viasualizzato nella Lovelace come meglio credete. Iol l'ho esposto sulla dashboard cellulare:

![lovelace2](https://github.com/kapkirk/Indice-di-qualita-dell-aria-via-Home-Assistant/blob/main/images/HA_lovelace2.jpg)


che nella scheda dedicata:

![lovelace3](https://github.com/kapkirk/Indice-di-qualita-dell-aria-via-Home-Assistant/blob/main/images/HA_lovelace3.jpg)


La seconda parte che vedete nella foto è quella dedicata ai dati ambientali proveniente da ARPA Puglia. In questo caso i dati sono pubblicati giornaliermente ma riferiti al giorno precedente e normalizzati dall'Ente. Se a qualcuno dovesse interessare questi sono i link al progetto:

- [Implementazione in Home Assistant tramite Node-RED](https://github.com/kapkirk/Dati-ambientali-ARPA-Puglia-via-Home-Assistant-e-NodeRED)
- [Implementazione in Home Assistant tramite Node-RED ed MQTT](https://github.com/kapkirk/Dati-ambientali-ARPA-Puglia-via-Home-Assistant)
  
















      
  


### 4 - Configurazione di Node-RED

1. Copiate ed incollate il contenuto del file `Flusso Node-RED singola centralina.json` oppure `Flusso Node-RED più centralina.json` in un foglio di NodeRED:

`Flusso Node-RED singola centralina.json`:

![nodered1](https://github.com/kapkirk/Indice-di-qualita-dell-aria-via-Home-Assistant/blob/main/images/Flusso%20Node-RED.jpg)


codice:
```json
[{"id":"0fc96737abf2fa25","type":"http request","z":"ffcf04d739843cc8","name":"","method":"GET","ret":"txt","paytoqs":"ignore","url":"https://dati.arpa.puglia.it/api/v1/measurements?language=ITA&format=CSV&network=RRQA&id_station=26&debugMode=false","tls":"","persist":false,"proxy":"","insecureHTTPParser":false,"authType":"","senderr":false,"headers":[],"x":130,"y":240,"wires":[["45d325f5c135d59b"]]},{"id":"be3859fca160266f","type":"inject","z":"ffcf04d739843cc8","name":"08.00","props":[{"p":"payload"},{"p":"topic","vt":"str"}],"repeat":"","crontab":"00 08 * * *","once":false,"onceDelay":0.1,"topic":"","payload":"","payloadType":"date","x":150,"y":80,"wires":[["0fc96737abf2fa25","7a2723b5493def9c","8d78bf9f78453e8c"]]},{"id":"45d325f5c135d59b","type":"csv","z":"ffcf04d739843cc8","name":"","spec":"rfc","sep":",","hdrin":true,"hdrout":"none","multi":"mult","ret":"\\r\\n","temp":"","skip":"0","strings":true,"include_empty_strings":"","include_---_values":"","x":270,"y":240,"wires":[["1dc499b20f7cf18e"]]},{"id":"1dc499b20f7cf18e","type":"function","z":"ffcf04d739843cc8","name":"Estrae i dati delle misurazioni","func":"// Ottieni l`array dal payload\nlet misurazioni = msg.payload;\n\n// Crea un array per memorizzare i risultati\nlet risultati = [];\n\n// Itera su ogni oggetto nell`array\nmisurazioni.forEach((misurazione, index) => {\n    // Estrai i campi che ti interessano\n    let risultato = {\n        data: misurazione.data_di_misurazione,\n        inquinante: misurazione.inquinante_misurato,\n        valore: misurazione.valore_inquinante_misurato,\n        limite: misurazione.limite,\n        unita: misurazione.unita_misura,\n        indice_qualita: misurazione.indice_qualita,\n        classe_qualita: misurazione.classe_qualita,\n        superamenti:misurazione.superamenti\n    };\n\n    // Aggiungi il risultato all`array\n    risultati.push(risultato);\n});\n\n// Imposta il nuovo payload con i risultati\nmsg.payload = risultati;\n\n// Restituisci il messaggio\nreturn msg;","outputs":1,"timeout":0,"noerr":0,"initialize":"","finalize":"","libs":[],"x":460,"y":240,"wires":[["f8fbe8a712bda9dd"]]},{"id":"f8fbe8a712bda9dd","type":"function","z":"ffcf04d739843cc8","name":"divide i messaggi per ogni inquinante","func":"// Ottieni l`array dal payload\nlet misurazioni = msg.payload;\n\n// Verifica che ci siano almeno due elementi nell`array\nif (misurazioni.length >= 2) {\n    // Crea due messaggi separati\n    let msg1 = { payload: misurazioni[0] }; // Primo oggetto\n    let msg2 = { payload: misurazioni[1] }; // Secondo oggetto\n\n    // Restituisci entrambi i messaggi\n    return [msg1, msg2];\n} else {\n    // Se non ci sono abbastanza elementi, restituisci un messaggio di errore\n    msg.payload = \"Errore: Il payload non contiene abbastanza elementi.\";\n    return msg;\n}","outputs":2,"timeout":0,"noerr":0,"initialize":"","finalize":"","libs":[],"x":750,"y":240,"wires":[["68f810c0b9e6c963"],["e0d2781f9f37aec6"]],"info":"### ## # "},{"id":"782ec5001a0c31e9","type":"mqtt out","z":"ffcf04d739843cc8","name":"NO2","topic":"sensors/no2","qos":"","retain":"","respTopic":"","contentType":"","userProps":"","correl":"","expiry":"","broker":"374295b309ce444f","x":1330,"y":280,"wires":[]},{"id":"377b5abe289f8a25","type":"mqtt out","z":"ffcf04d739843cc8","name":"PM10","topic":"sensors/pm10","qos":"","retain":"","respTopic":"","contentType":"","userProps":"","correl":"","expiry":"","broker":"374295b309ce444f","x":1330,"y":200,"wires":[]},{"id":"68f810c0b9e6c963","type":"function","z":"ffcf04d739843cc8","name":"formatta in valore \"valore\" in caso di errore","func":"\n    if (msg.payload.valore === \"---\") \n{\n    msg.payload.valore = \"0\";\n}\n\nif (msg.payload.indice_qualita === \"---\") \n{\n    msg.payload.indice_qualita = \"0\";\n}\n\nif (msg.payload.classe_qualita === \"---\") \n{\n    msg.payload.classe_qualita = \"0\";\n}\n\nif (msg.payload.superamenti === \"---\") \n{\n    msg.payload.superamenti = \"0\";\n}\n\nif (msg.payload.limite === \"---\") \n{\n    msg.payload.limite = \"0\";\n}\nreturn msg;","outputs":1,"timeout":0,"noerr":0,"initialize":"","finalize":"","libs":[],"x":1090,"y":200,"wires":[["377b5abe289f8a25"]]},{"id":"e0d2781f9f37aec6","type":"function","z":"ffcf04d739843cc8","name":"formatta in valore \"valore\" in caso di errore","func":"\n    if (msg.payload.valore === \"---\") \n{\n    msg.payload.valore = \"0\";\n}\n\nif (msg.payload.indice_qualita === \"---\") \n{\n    msg.payload.indice_qualita = \"0\";\n}\n\nif (msg.payload.classe_qualita === \"---\") \n{\n    msg.payload.classe_qualita = \"0\";\n}\n\nif (msg.payload.superamenti === \"---\") \n{\n    msg.payload.superamenti = \"0\";\n}\n\nif (msg.payload.limite === \"---\") \n{\n    msg.payload.limite = \"0\";\n}\nreturn msg;","outputs":1,"timeout":0,"noerr":0,"initialize":"","finalize":"","libs":[],"x":1090,"y":280,"wires":[["782ec5001a0c31e9"]]},{"id":"374295b309ce444f","type":"mqtt-broker","name":"HA MQTT","broker":"192.168.31.160","port":"1883","clientid":"","autoConnect":true,"usetls":false,"protocolVersion":"4","keepalive":"60","cleansession":true,"autoUnsubscribe":true,"birthTopic":"","birthQos":"0","birthRetain":"false","birthPayload":"","birthMsg":{},"closeTopic":"","closeQos":"0","closeRetain":"false","closePayload":"","closeMsg":{},"willTopic":"","willQos":"0","willRetain":"false","willPayload":"","willMsg":{},"userProps":"","sessionExpiry":""}]
```

oppure `Flusso Node-RED più centralina.json`:

![nodered2](https://github.com/kapkirk/Indice-di-qualita-dell-aria-via-Home-Assistant/blob/main/images/Flusso%20Node-RED%20pi%C3%B9%20centraline.jpg)

codice:
```json
[{"id":"2a235b7b433bbb28","type":"http request","z":"7e71bf58d0d8df1b","name":"","method":"GET","ret":"txt","paytoqs":"ignore","url":"https://dati.arpa.puglia.it/api/v1/measurements?language=ITA&format=CSV&network=RRQA&id_station=26&debugMode=false","tls":"","persist":false,"proxy":"","insecureHTTPParser":false,"authType":"","senderr":false,"headers":[],"x":250,"y":260,"wires":[["9eab0eaff1ec6956"]]},{"id":"daf9aeb5ce35cda6","type":"inject","z":"7e71bf58d0d8df1b","name":"08.00","props":[{"p":"payload"},{"p":"topic","vt":"str"}],"repeat":"","crontab":"00 08 * * *","once":false,"onceDelay":0.1,"topic":"","payload":"","payloadType":"date","x":270,"y":100,"wires":[["2a235b7b433bbb28","34ab8ce6de39ed9f","17b49fe2099cae18"]]},{"id":"9eab0eaff1ec6956","type":"csv","z":"7e71bf58d0d8df1b","name":"","spec":"rfc","sep":",","hdrin":true,"hdrout":"none","multi":"mult","ret":"\\r\\n","temp":"","skip":"0","strings":true,"include_empty_strings":"","include_---_values":"","x":390,"y":260,"wires":[["bc1b63ee1e8f0f29"]]},{"id":"bc1b63ee1e8f0f29","type":"function","z":"7e71bf58d0d8df1b","name":"Estrae i dati delle misurazioni","func":"// Ottieni l`array dal payload\nlet misurazioni = msg.payload;\n\n// Crea un array per memorizzare i risultati\nlet risultati = [];\n\n// Itera su ogni oggetto nell`array\nmisurazioni.forEach((misurazione, index) => {\n    // Estrai i campi che ti interessano\n    let risultato = {\n        data: misurazione.data_di_misurazione,\n        inquinante: misurazione.inquinante_misurato,\n        valore: misurazione.valore_inquinante_misurato,\n        limite: misurazione.limite,\n        unita: misurazione.unita_misura,\n        indice_qualita: misurazione.indice_qualita,\n        classe_qualita: misurazione.classe_qualita,\n        superamenti:misurazione.superamenti\n    };\n\n    // Aggiungi il risultato all`array\n    risultati.push(risultato);\n});\n\n// Imposta il nuovo payload con i risultati\nmsg.payload = risultati;\n\n// Restituisci il messaggio\nreturn msg;","outputs":1,"timeout":0,"noerr":0,"initialize":"","finalize":"","libs":[],"x":580,"y":260,"wires":[["c179c0eb7be60c8b"]]},{"id":"c179c0eb7be60c8b","type":"function","z":"7e71bf58d0d8df1b","name":"divide i messaggi per ogni inquinante","func":"// Ottieni l`array dal payload\nlet misurazioni = msg.payload;\n\n// Verifica che ci siano almeno due elementi nell`array\nif (misurazioni.length >= 2) {\n    // Crea due messaggi separati\n    let msg1 = { payload: misurazioni[0] }; // Primo oggetto\n    let msg2 = { payload: misurazioni[1] }; // Secondo oggetto\n\n    // Restituisci entrambi i messaggi\n    return [msg1, msg2];\n} else {\n    // Se non ci sono abbastanza elementi, restituisci un messaggio di errore\n    msg.payload = \"Errore: Il payload non contiene abbastanza elementi.\";\n    return msg;\n}","outputs":2,"timeout":0,"noerr":0,"initialize":"","finalize":"","libs":[],"x":870,"y":260,"wires":[["ae96a5ccee3735fd"],["d61ca08685d2e68f"]],"info":"### ## # "},{"id":"61e79e4d18ac53ff","type":"mqtt out","z":"7e71bf58d0d8df1b","name":"NO2","topic":"sensors/no2","qos":"","retain":"","respTopic":"","contentType":"","userProps":"","correl":"","expiry":"","broker":"374295b309ce444f","x":1450,"y":300,"wires":[]},{"id":"e3b8e52970320c3d","type":"mqtt out","z":"7e71bf58d0d8df1b","name":"PM10","topic":"sensors/pm10","qos":"","retain":"","respTopic":"","contentType":"","userProps":"","correl":"","expiry":"","broker":"374295b309ce444f","x":1450,"y":220,"wires":[]},{"id":"ae96a5ccee3735fd","type":"function","z":"7e71bf58d0d8df1b","name":"formatta in valore \"valore\" in caso di errore","func":"\n    if (msg.payload.valore === \"---\") \n{\n    msg.payload.valore = \"0\";\n}\n\nif (msg.payload.indice_qualita === \"---\") \n{\n    msg.payload.indice_qualita = \"0\";\n}\n\nif (msg.payload.classe_qualita === \"---\") \n{\n    msg.payload.classe_qualita = \"0\";\n}\n\nif (msg.payload.superamenti === \"---\") \n{\n    msg.payload.superamenti = \"0\";\n}\n\nif (msg.payload.limite === \"---\") \n{\n    msg.payload.limite = \"0\";\n}\nreturn msg;","outputs":1,"timeout":0,"noerr":0,"initialize":"","finalize":"","libs":[],"x":1210,"y":220,"wires":[["e3b8e52970320c3d"]]},{"id":"640e1cd659bc8bcc","type":"http request","z":"7e71bf58d0d8df1b","name":"","method":"GET","ret":"txt","paytoqs":"ignore","url":"https://dati.arpa.puglia.it/api/v1/measurements?language=ITA&format=CSV&network=RRQA&id_station=93&debugMode=false","tls":"","persist":false,"proxy":"","insecureHTTPParser":false,"authType":"","senderr":false,"headers":[],"x":250,"y":500,"wires":[["7b24b8a365cbd0b7"]]},{"id":"7b24b8a365cbd0b7","type":"csv","z":"7e71bf58d0d8df1b","name":"","spec":"rfc","sep":",","hdrin":true,"hdrout":"none","multi":"mult","ret":"\\r\\n","temp":"","skip":"0","strings":true,"include_empty_strings":"","include_---_values":"","x":390,"y":500,"wires":[["f7125ef0498ddb37"]]},{"id":"f7125ef0498ddb37","type":"function","z":"7e71bf58d0d8df1b","name":"Estrae i dati delle misurazioni","func":"// Ottieni l`array dal payload\nlet misurazioni = msg.payload;\n\n// Crea un array per memorizzare i risultati\nlet risultati = [];\n\n// Itera su ogni oggetto nell`array\nmisurazioni.forEach((misurazione, index) => {\n    // Estrai i campi che ti interessano\n    let risultato = {\n        data: misurazione.data_di_misurazione,\n        inquinante: misurazione.inquinante_misurato,\n        valore: misurazione.valore_inquinante_misurato,\n        limite: misurazione.limite,\n        unita: misurazione.unita_misura,\n        indice_qualita: misurazione.indice_qualita,\n        classe_qualita: misurazione.classe_qualita,\n        superamenti:misurazione.superamenti\n    };\n\n    // Aggiungi il risultato all`array\n    risultati.push(risultato);\n});\n\n// Imposta il nuovo payload con i risultati\nmsg.payload = risultati;\n\n// Restituisci il messaggio\nreturn msg;","outputs":1,"timeout":0,"noerr":0,"initialize":"","finalize":"","libs":[],"x":580,"y":500,"wires":[["c7de10a4328dec6d"]]},{"id":"c7de10a4328dec6d","type":"function","z":"7e71bf58d0d8df1b","name":"divide i messaggi per ogni inquinante","func":"// Ottieni l`array dal payload\nlet misurazioni = msg.payload;\n\n// Verifica che ci siano almeno due elementi nell`array\nif (misurazioni.length >= 4) {\n    // Crea due messaggi separati\n    let msg1 = { payload: misurazioni[0] }; // Primo oggetto\n    let msg2 = { payload: misurazioni[1] }; // Secondo oggetto\n    let msg3 = { payload: misurazioni[2] }; // Terzo oggetto\n    let msg4 = { payload: misurazioni[3] }; // Quarto oggetto\n\n    // Restituisci entrambi i messaggi\n    return [msg1, msg2, msg3, msg4];\n} else {\n    // Se non ci sono abbastanza elementi, restituisci un messaggio di errore\n    msg.payload = \"Errore: Il payload non contiene abbastanza elementi.\";\n    return msg;\n}","outputs":4,"timeout":0,"noerr":0,"initialize":"","finalize":"","libs":[],"x":870,"y":500,"wires":[[],["58c90af411350d55"],[],["14571d8042e7b752"]],"info":"### ## # "},{"id":"a70c8588afb667ec","type":"mqtt out","z":"7e71bf58d0d8df1b","name":"SO2","topic":"sensors/so2","qos":"","retain":"","respTopic":"","contentType":"","userProps":"","correl":"","expiry":"","broker":"374295b309ce444f","x":1450,"y":540,"wires":[]},{"id":"08c20a666bf9b9ef","type":"mqtt out","z":"7e71bf58d0d8df1b","name":"PM25","topic":"sensors/pm25","qos":"","retain":"","respTopic":"","contentType":"","userProps":"","correl":"","expiry":"","broker":"374295b309ce444f","x":1450,"y":460,"wires":[]},{"id":"48b112b1b5f0cc47","type":"http request","z":"7e71bf58d0d8df1b","name":"","method":"GET","ret":"txt","paytoqs":"ignore","url":"https://dati.arpa.puglia.it/api/v1/measurements?language=ITA&format=CSV&network=RRQA&id_station=27&debugMode=false","tls":"","persist":false,"proxy":"","insecureHTTPParser":false,"authType":"","senderr":false,"headers":[],"x":250,"y":640,"wires":[["5d7c315282a8de56"]]},{"id":"5d7c315282a8de56","type":"csv","z":"7e71bf58d0d8df1b","name":"","spec":"rfc","sep":",","hdrin":true,"hdrout":"none","multi":"mult","ret":"\\r\\n","temp":"","skip":"0","strings":true,"include_empty_strings":"","include_---_values":"","x":390,"y":640,"wires":[["8c601449f5f7080a"]]},{"id":"8c601449f5f7080a","type":"function","z":"7e71bf58d0d8df1b","name":"Estrae i dati delle misurazioni","func":"// Ottieni l`array dal payload\nlet misurazioni = msg.payload;\n\n// Crea un array per memorizzare i risultati\nlet risultati = [];\n\n// Itera su ogni oggetto nell`array\nmisurazioni.forEach((misurazione, index) => {\n    // Estrai i campi che ti interessano\n    let risultato = {\n        data: misurazione.data_di_misurazione,\n        inquinante: misurazione.inquinante_misurato,\n        valore: misurazione.valore_inquinante_misurato,\n        limite: misurazione.limite,\n        unita: misurazione.unita_misura,\n        indice_qualita: misurazione.indice_qualita,\n        classe_qualita: misurazione.classe_qualita,\n        superamenti:misurazione.superamenti\n    };\n\n    // Aggiungi il risultato all`array\n    risultati.push(risultato);\n});\n\n// Imposta il nuovo payload con i risultati\nmsg.payload = risultati;\n\n// Restituisci il messaggio\nreturn msg;","outputs":1,"timeout":0,"noerr":0,"initialize":"","finalize":"","libs":[],"x":580,"y":640,"wires":[["ab1d71e891de1336"]]},{"id":"ab1d71e891de1336","type":"function","z":"7e71bf58d0d8df1b","name":"divide i messaggi per ogni inquinante","func":"// Ottieni l`array dal payload\nlet misurazioni = msg.payload;\n\n// Verifica che ci siano almeno due elementi nell`array\nif (misurazioni.length >= 7) {\n    // Crea due messaggi separati\n    let msg1 = { payload: misurazioni[0] }; // Primo oggetto\n    let msg2 = { payload: misurazioni[1] }; // Secondo oggetto\n    let msg3 = { payload: misurazioni[2] }; // Terzo oggetto\n    let msg4 = { payload: misurazioni[3] }; // Quarto oggetto\n    let msg5 = { payload: misurazioni[4] }; // Quinto oggetto\n    let msg6 = { payload: misurazioni[5] }; // Sesto oggetto\n    let msg7 = { payload: misurazioni[6] }; // settimo oggetto\n\n    // Restituisci entrambi i messaggi\n    return [msg1, msg2, msg3, msg4, msg5, msg6, msg7];\n} else {\n    // Se non ci sono abbastanza elementi, restituisci un messaggio di errore\n    msg.payload = \"Errore: Il payload non contiene abbastanza elementi.\";\n    return msg;\n}","outputs":7,"timeout":0,"noerr":0,"initialize":"","finalize":"","libs":[],"x":870,"y":640,"wires":[[],[],[],["e8030c314ae0b123"],["71fa75be75d2a4fa"],[],["526e230a4fe3aa4d"]],"info":"### ## # "},{"id":"899b55a471331944","type":"mqtt out","z":"7e71bf58d0d8df1b","name":"CO","topic":"sensors/co","qos":"","retain":"","respTopic":"","contentType":"","userProps":"","correl":"","expiry":"","broker":"374295b309ce444f","x":1450,"y":660,"wires":[]},{"id":"de42a07e56cd4752","type":"mqtt out","z":"7e71bf58d0d8df1b","name":"C6H6","topic":"sensors/c6h6","qos":"","retain":"","respTopic":"","contentType":"","userProps":"","correl":"","expiry":"","broker":"374295b309ce444f","x":1450,"y":600,"wires":[]},{"id":"4429c59fa49d1159","type":"mqtt out","z":"7e71bf58d0d8df1b","name":"IPA","topic":"sensors/ipa","qos":"","retain":"","respTopic":"","contentType":"","userProps":"","correl":"","expiry":"","broker":"374295b309ce444f","x":1450,"y":720,"wires":[]},{"id":"34ab8ce6de39ed9f","type":"delay","z":"7e71bf58d0d8df1b","name":"","pauseType":"delay","timeout":"5","timeoutUnits":"seconds","rate":"1","nbRateUnits":"1","rateUnits":"second","randomFirst":"1","randomLast":"5","randomUnits":"seconds","drop":false,"allowrate":false,"outputs":1,"x":240,"y":440,"wires":[["640e1cd659bc8bcc"]]},{"id":"17b49fe2099cae18","type":"delay","z":"7e71bf58d0d8df1b","name":"","pauseType":"delay","timeout":"10","timeoutUnits":"seconds","rate":"1","nbRateUnits":"1","rateUnits":"second","randomFirst":"1","randomLast":"5","randomUnits":"seconds","drop":false,"allowrate":false,"outputs":1,"x":240,"y":580,"wires":[["48b112b1b5f0cc47"]]},{"id":"d61ca08685d2e68f","type":"function","z":"7e71bf58d0d8df1b","name":"formatta in valore \"valore\" in caso di errore","func":"\n    if (msg.payload.valore === \"---\") \n{\n    msg.payload.valore = \"0\";\n}\n\nif (msg.payload.indice_qualita === \"---\") \n{\n    msg.payload.indice_qualita = \"0\";\n}\n\nif (msg.payload.classe_qualita === \"---\") \n{\n    msg.payload.classe_qualita = \"0\";\n}\n\nif (msg.payload.superamenti === \"---\") \n{\n    msg.payload.superamenti = \"0\";\n}\n\nif (msg.payload.limite === \"---\") \n{\n    msg.payload.limite = \"0\";\n}\nreturn msg;","outputs":1,"timeout":0,"noerr":0,"initialize":"","finalize":"","libs":[],"x":1210,"y":300,"wires":[["61e79e4d18ac53ff"]]},{"id":"58c90af411350d55","type":"function","z":"7e71bf58d0d8df1b","name":"formatta in valore \"valore\" in caso di errore","func":"\n    if (msg.payload.valore === \"---\") \n{\n    msg.payload.valore = \"0\";\n}\n\nif (msg.payload.indice_qualita === \"---\") \n{\n    msg.payload.indice_qualita = \"0\";\n}\n\nif (msg.payload.classe_qualita === \"---\") \n{\n    msg.payload.classe_qualita = \"0\";\n}\n\nif (msg.payload.superamenti === \"---\") \n{\n    msg.payload.superamenti = \"0\";\n}\n\nif (msg.payload.limite === \"---\") \n{\n    msg.payload.limite = \"0\";\n}\nreturn msg;","outputs":1,"timeout":0,"noerr":0,"initialize":"","finalize":"","libs":[],"x":1210,"y":460,"wires":[["08c20a666bf9b9ef"]]},{"id":"14571d8042e7b752","type":"function","z":"7e71bf58d0d8df1b","name":"formatta in valore \"valore\" in caso di errore","func":"\n    if (msg.payload.valore === \"---\") \n{\n    msg.payload.valore = \"0\";\n}\n\nif (msg.payload.indice_qualita === \"---\") \n{\n    msg.payload.indice_qualita = \"0\";\n}\n\nif (msg.payload.classe_qualita === \"---\") \n{\n    msg.payload.classe_qualita = \"0\";\n}\n\nif (msg.payload.superamenti === \"---\") \n{\n    msg.payload.superamenti = \"0\";\n}\n\nif (msg.payload.limite === \"---\") \n{\n    msg.payload.limite = \"0\";\n}\nreturn msg;","outputs":1,"timeout":0,"noerr":0,"initialize":"","finalize":"","libs":[],"x":1210,"y":540,"wires":[["a70c8588afb667ec"]]},{"id":"e8030c314ae0b123","type":"function","z":"7e71bf58d0d8df1b","name":"formatta in valore \"valore\" in caso di errore","func":"\n    if (msg.payload.valore === \"---\") \n{\n    msg.payload.valore = \"0\";\n}\n\nif (msg.payload.indice_qualita === \"---\") \n{\n    msg.payload.indice_qualita = \"0\";\n}\n\nif (msg.payload.classe_qualita === \"---\") \n{\n    msg.payload.classe_qualita = \"0\";\n}\n\nif (msg.payload.superamenti === \"---\") \n{\n    msg.payload.superamenti = \"0\";\n}\n\nif (msg.payload.limite === \"---\") \n{\n    msg.payload.limite = \"0\";\n}\nreturn msg;","outputs":1,"timeout":0,"noerr":0,"initialize":"","finalize":"","libs":[],"x":1210,"y":600,"wires":[["de42a07e56cd4752"]]},{"id":"71fa75be75d2a4fa","type":"function","z":"7e71bf58d0d8df1b","name":"formatta in valore \"valore\" in caso di errore","func":"\n    if (msg.payload.valore === \"---\") \n{\n    msg.payload.valore = \"0\";\n}\n\nif (msg.payload.indice_qualita === \"---\") \n{\n    msg.payload.indice_qualita = \"0\";\n}\n\nif (msg.payload.classe_qualita === \"---\") \n{\n    msg.payload.classe_qualita = \"0\";\n}\n\nif (msg.payload.superamenti === \"---\") \n{\n    msg.payload.superamenti = \"0\";\n}\n\nif (msg.payload.limite === \"---\") \n{\n    msg.payload.limite = \"0\";\n}\nreturn msg;","outputs":1,"timeout":0,"noerr":0,"initialize":"","finalize":"","libs":[],"x":1210,"y":660,"wires":[["899b55a471331944"]]},{"id":"526e230a4fe3aa4d","type":"function","z":"7e71bf58d0d8df1b","name":"formatta in valore \"valore\" in caso di errore","func":"\n    if (msg.payload.valore === \"---\") \n{\n    msg.payload.valore = \"0\";\n}\n\nif (msg.payload.indice_qualita === \"---\") \n{\n    msg.payload.indice_qualita = \"0\";\n}\n\nif (msg.payload.classe_qualita === \"---\") \n{\n    msg.payload.classe_qualita = \"0\";\n}\n\nif (msg.payload.superamenti === \"---\") \n{\n    msg.payload.superamenti = \"0\";\n}\n\nif (msg.payload.limite === \"---\") \n{\n    msg.payload.limite = \"0\";\n}\nreturn msg;","outputs":1,"timeout":0,"noerr":0,"initialize":"","finalize":"","libs":[],"x":1210,"y":720,"wires":[["4429c59fa49d1159"]]},{"id":"b6920f1155d953e0","type":"comment","z":"7e71bf58d0d8df1b","name":"Dati centralina San Pietro Vernotico","info":"","x":800,"y":140,"wires":[]},{"id":"165037e5d42fa2c9","type":"comment","z":"7e71bf58d0d8df1b","name":"Dati centraline Torchiarolo","info":"","x":810,"y":400,"wires":[]},{"id":"374295b309ce444f","type":"mqtt-broker","name":"HA MQTT","broker":"192.168.31.160","port":"1883","clientid":"","autoConnect":true,"usetls":false,"protocolVersion":"4","keepalive":"60","cleansession":true,"autoUnsubscribe":true,"birthTopic":"","birthQos":"0","birthRetain":"false","birthPayload":"","birthMsg":{},"closeTopic":"","closeQos":"0","closeRetain":"false","closePayload":"","closeMsg":{},"willTopic":"","willQos":"0","willRetain":"false","willPayload":"","willMsg":{},"userProps":"","sessionExpiry":""}]
```
1. Aprite il nodo denominato `http request` e nel campo `URL` copiate ed incollate la stringa ottenuta prima;
1. Riavviate il tutto! Il gioco è fatto!

---

## Personalizzazione ed analisi dei flussi NodeRED

I flussi da me illustrati sono ovviamente meritevoli di sviluppo. Personalmente mi sono occupato di raccogliere i dati esposti dalle centraline vicine alle zone in cui abito ma ciò non toglie che si possano utilizzare tutti i valori a disposizione, ovvero quelli esposti nella tabella "Caratteristiche principali" sopra riportata. Il flusso NodeRED in questo caso sarà il seguente:

![nodered3](https://github.com/kapkirk/Indice-di-qualita-dell-aria-via-Home-Assistant/blob/main/images/Flusso%20Node-RED%20centralina%20completa.jpg)

codice:
```json
[{"id":"83ae842a038866d3","type":"tab","label":"DatiARPA1","disabled":false,"info":"","env":[]},{"id":"bccfd7c9f2db270f","type":"csv","z":"83ae842a038866d3","name":"","spec":"rfc","sep":",","hdrin":true,"hdrout":"none","multi":"mult","ret":"\\r\\n","temp":"","skip":"0","strings":true,"include_empty_strings":"","include_---_values":"","x":370,"y":380,"wires":[["2324c1401af40bd2"]]},{"id":"2324c1401af40bd2","type":"function","z":"83ae842a038866d3","name":"Estrae i dati delle misurazioni","func":"// Ottieni l'array dal payload\nlet misurazioni = msg.payload;\n\n// Crea un array per memorizzare i risultati\nlet risultati = [];\n\n// Itera su ogni oggetto nell'array\nmisurazioni.forEach((misurazione, index) => {\n    // Estrai i campi che ti interessano\n    let risultato = {\n        data: misurazione.data_di_misurazione,\n        inquinante: misurazione.inquinante_misurato,\n        valore: misurazione.valore_inquinante_misurato,\n        limite: misurazione.limite,\n        unita: misurazione.unita_misura,\n        indice_qualita: misurazione.indice_qualita,\n        classe_qualita: misurazione.classe_qualita,\n        superamenti:misurazione.superamenti\n    };\n\n    // Aggiungi il risultato all'array\n    risultati.push(risultato);\n});\n\n// Imposta il nuovo payload con i risultati\nmsg.payload = risultati;\n\n// Restituisci il messaggio\nreturn msg;","outputs":1,"timeout":0,"noerr":0,"initialize":"","finalize":"","libs":[],"x":580,"y":380,"wires":[["10c547891c3baf9e"]]},{"id":"10c547891c3baf9e","type":"function","z":"83ae842a038866d3","name":"divide i messaggi per ogni inquinante","func":"// Ottieni l'array dal payload\nlet misurazioni = msg.payload;\n\n// Verifica che ci siano almeno due elementi nell'array\nif (misurazioni.length >= 9) {\n    // Crea due messaggi separati\n    let msg1 = { payload: misurazioni[0] }; // Primo oggetto\n    let msg2 = { payload: misurazioni[1] }; // Secondo oggetto\n    let msg3 = { payload: misurazioni[2] }; // Terzo oggetto\n    let msg4 = { payload: misurazioni[3] }; // Quarto oggetto\n    let msg5 = { payload: misurazioni[4] }; // Quinto oggetto\n    let msg6 = { payload: misurazioni[5] }; // Sesto oggetto\n    let msg7 = { payload: misurazioni[6] }; // settimo oggetto\n    let msg8 = { payload: misurazioni[7] }; // ottavo oggetto\n    let msg9 = { payload: misurazioni[8] }; // nono oggetto\n\n    // Restituisci entrambi i messaggi\n    return [msg1, msg2, msg3, msg4, msg5, msg6, msg7, msg8, msg9];\n} else {\n    // Se non ci sono abbastanza elementi, restituisci un messaggio di errore\n    msg.payload = \"Errore: Il payload non contiene abbastanza elementi.\";\n    return msg;\n}","outputs":9,"timeout":0,"noerr":0,"initialize":"","finalize":"","libs":[],"x":870,"y":380,"wires":[["c78bf7f00a9df94f"],["a92129cd90dbb91c"],["baacb7b203c98073"],["2019bc966017df5c"],["9f95695360a832b5"],["bd3b68228abce048"],["6a89ae6b2939c5f3"],["919b7562c0f30678"],["82a6fa3f55689262"]],"info":"### ## # "},{"id":"2019bc966017df5c","type":"function","z":"83ae842a038866d3","name":"formatta in valore \"valore\" in caso di errore","func":"\n    if (msg.payload.valore === \"---\") \n{\n    msg.payload.valore = \"0\";\n}\n\nif (msg.payload.indice_qualita === \"---\") \n{\n    msg.payload.indice_qualita = \"0\";\n}\n\nif (msg.payload.classe_qualita === \"---\") \n{\n    msg.payload.classe_qualita = \"0\";\n}\n\nif (msg.payload.superamenti === \"---\") \n{\n    msg.payload.superamenti = \"0\";\n}\n\nif (msg.payload.limite === \"---\") \n{\n    msg.payload.limite = \"0\";\n}\nreturn msg;","outputs":1,"timeout":0,"noerr":0,"initialize":"","finalize":"","libs":[],"x":1430,"y":320,"wires":[["2144cb4c68a97c98"]]},{"id":"9f95695360a832b5","type":"function","z":"83ae842a038866d3","name":"formatta in valore \"valore\" in caso di errore","func":"\n    if (msg.payload.valore === \"---\") \n{\n    msg.payload.valore = \"0\";\n}\n\nif (msg.payload.indice_qualita === \"---\") \n{\n    msg.payload.indice_qualita = \"0\";\n}\n\nif (msg.payload.classe_qualita === \"---\") \n{\n    msg.payload.classe_qualita = \"0\";\n}\n\nif (msg.payload.superamenti === \"---\") \n{\n    msg.payload.superamenti = \"0\";\n}\n\nif (msg.payload.limite === \"---\") \n{\n    msg.payload.limite = \"0\";\n}\nreturn msg;","outputs":1,"timeout":0,"noerr":0,"initialize":"","finalize":"","libs":[],"x":1430,"y":380,"wires":[["9eafd411f52e9071"]]},{"id":"82a6fa3f55689262","type":"function","z":"83ae842a038866d3","name":"formatta in valore \"valore\" in caso di errore","func":"\n    if (msg.payload.valore === \"---\") \n{\n    msg.payload.valore = \"0\";\n}\n\nif (msg.payload.indice_qualita === \"---\") \n{\n    msg.payload.indice_qualita = \"0\";\n}\n\nif (msg.payload.classe_qualita === \"---\") \n{\n    msg.payload.classe_qualita = \"0\";\n}\n\nif (msg.payload.superamenti === \"---\") \n{\n    msg.payload.superamenti = \"0\";\n}\n\nif (msg.payload.limite === \"---\") \n{\n    msg.payload.limite = \"0\";\n}\nreturn msg;","outputs":1,"timeout":0,"noerr":0,"initialize":"","finalize":"","libs":[],"x":1430,"y":620,"wires":[["f671d733e673a541"]]},{"id":"a92129cd90dbb91c","type":"function","z":"83ae842a038866d3","name":"formatta in valore \"valore\" in caso di errore","func":"\n    if (msg.payload.valore === \"---\") \n{\n    msg.payload.valore = \"0\";\n}\n\nif (msg.payload.indice_qualita === \"---\") \n{\n    msg.payload.indice_qualita = \"0\";\n}\n\nif (msg.payload.classe_qualita === \"---\") \n{\n    msg.payload.classe_qualita = \"0\";\n}\n\nif (msg.payload.superamenti === \"---\") \n{\n    msg.payload.superamenti = \"0\";\n}\n\nif (msg.payload.limite === \"---\") \n{\n    msg.payload.limite = \"0\";\n}\nreturn msg;","outputs":1,"timeout":0,"noerr":0,"initialize":"","finalize":"","libs":[],"x":1430,"y":200,"wires":[["ac820c6ebe3d0e94"]]},{"id":"c78bf7f00a9df94f","type":"function","z":"83ae842a038866d3","name":"formatta in valore \"valore\" in caso di errore","func":"\n    if (msg.payload.valore === \"---\") \n{\n    msg.payload.valore = \"0\";\n}\n\nif (msg.payload.indice_qualita === \"---\") \n{\n    msg.payload.indice_qualita = \"0\";\n}\n\nif (msg.payload.classe_qualita === \"---\") \n{\n    msg.payload.classe_qualita = \"0\";\n}\n\nif (msg.payload.superamenti === \"---\") \n{\n    msg.payload.superamenti = \"0\";\n}\n\nif (msg.payload.limite === \"---\") \n{\n    msg.payload.limite = \"0\";\n}\nreturn msg;","outputs":1,"timeout":0,"noerr":0,"initialize":"","finalize":"","libs":[],"x":1430,"y":140,"wires":[["5f4b97d3437bf760"]]},{"id":"baacb7b203c98073","type":"function","z":"83ae842a038866d3","name":"formatta in valore \"valore\" in caso di errore","func":"\n    if (msg.payload.valore === \"---\") \n{\n    msg.payload.valore = \"0\";\n}\n\nif (msg.payload.indice_qualita === \"---\") \n{\n    msg.payload.indice_qualita = \"0\";\n}\n\nif (msg.payload.classe_qualita === \"---\") \n{\n    msg.payload.classe_qualita = \"0\";\n}\n\nif (msg.payload.superamenti === \"---\") \n{\n    msg.payload.superamenti = \"0\";\n}\n\nif (msg.payload.limite === \"---\") \n{\n    msg.payload.limite = \"0\";\n}\nreturn msg;","outputs":1,"timeout":0,"noerr":0,"initialize":"","finalize":"","libs":[],"x":1430,"y":260,"wires":[["a44e6a7982d71cf0"]]},{"id":"bd3b68228abce048","type":"function","z":"83ae842a038866d3","name":"formatta in valore \"valore\" in caso di errore","func":"\n    if (msg.payload.valore === \"---\") \n{\n    msg.payload.valore = \"0\";\n}\n\nif (msg.payload.indice_qualita === \"---\") \n{\n    msg.payload.indice_qualita = \"0\";\n}\n\nif (msg.payload.classe_qualita === \"---\") \n{\n    msg.payload.classe_qualita = \"0\";\n}\n\nif (msg.payload.superamenti === \"---\") \n{\n    msg.payload.superamenti = \"0\";\n}\n\nif (msg.payload.limite === \"---\") \n{\n    msg.payload.limite = \"0\";\n}\nreturn msg;","outputs":1,"timeout":0,"noerr":0,"initialize":"","finalize":"","libs":[],"x":1430,"y":440,"wires":[["f599221c6e0a7324"]]},{"id":"6a89ae6b2939c5f3","type":"function","z":"83ae842a038866d3","name":"formatta in valore \"valore\" in caso di errore","func":"\n    if (msg.payload.valore === \"---\") \n{\n    msg.payload.valore = \"0\";\n}\n\nif (msg.payload.indice_qualita === \"---\") \n{\n    msg.payload.indice_qualita = \"0\";\n}\n\nif (msg.payload.classe_qualita === \"---\") \n{\n    msg.payload.classe_qualita = \"0\";\n}\n\nif (msg.payload.superamenti === \"---\") \n{\n    msg.payload.superamenti = \"0\";\n}\n\nif (msg.payload.limite === \"---\") \n{\n    msg.payload.limite = \"0\";\n}\nreturn msg;","outputs":1,"timeout":0,"noerr":0,"initialize":"","finalize":"","libs":[],"x":1430,"y":500,"wires":[["4961370bae9c1cf9"]]},{"id":"919b7562c0f30678","type":"function","z":"83ae842a038866d3","name":"formatta in valore \"valore\" in caso di errore","func":"\n    if (msg.payload.valore === \"---\") \n{\n    msg.payload.valore = \"0\";\n}\n\nif (msg.payload.indice_qualita === \"---\") \n{\n    msg.payload.indice_qualita = \"0\";\n}\n\nif (msg.payload.classe_qualita === \"---\") \n{\n    msg.payload.classe_qualita = \"0\";\n}\n\nif (msg.payload.superamenti === \"---\") \n{\n    msg.payload.superamenti = \"0\";\n}\n\nif (msg.payload.limite === \"---\") \n{\n    msg.payload.limite = \"0\";\n}\nreturn msg;","outputs":1,"timeout":0,"noerr":0,"initialize":"","finalize":"","libs":[],"x":1430,"y":560,"wires":[["f767e3bfd173b9fb"]]},{"id":"8e1d2d5c56127fd9","type":"http request","z":"83ae842a038866d3","name":"","method":"GET","ret":"txt","paytoqs":"ignore","url":"https://dati.arpa.puglia.it/api/v1/measurements?language=ITA&format=CSV&network=RRQA&id_station=26&debugMode=false","tls":"","persist":false,"proxy":"","insecureHTTPParser":false,"authType":"","senderr":false,"headers":[],"x":230,"y":380,"wires":[["bccfd7c9f2db270f"]]},{"id":"ce883c9ded520944","type":"inject","z":"83ae842a038866d3","name":"12.00","props":[{"p":"payload"},{"p":"topic","vt":"str"}],"repeat":"","crontab":"00 12 * * *","once":false,"onceDelay":0.1,"topic":"","payload":"","payloadType":"date","x":90,"y":380,"wires":[["8e1d2d5c56127fd9"]]},{"id":"f671d733e673a541","type":"mqtt out","z":"83ae842a038866d3","name":"IPA","topic":"sensors/ipa","qos":"","retain":"","respTopic":"","contentType":"","userProps":"","correl":"","expiry":"","broker":"374295b309ce444f","x":1670,"y":620,"wires":[]},{"id":"f767e3bfd173b9fb","type":"mqtt out","z":"83ae842a038866d3","name":"BLACK CARB","topic":"sensors/black_carb","qos":"","retain":"","respTopic":"","contentType":"","userProps":"","correl":"","expiry":"","broker":"374295b309ce444f","x":1700,"y":560,"wires":[]},{"id":"4961370bae9c1cf9","type":"mqtt out","z":"83ae842a038866d3","name":"H2S","topic":"sensors/hs2","qos":"","retain":"","respTopic":"","contentType":"","userProps":"","correl":"","expiry":"","broker":"374295b309ce444f","x":1670,"y":500,"wires":[]},{"id":"f599221c6e0a7324","type":"mqtt out","z":"83ae842a038866d3","name":"SO2","topic":"sensors/so2","qos":"","retain":"","respTopic":"","contentType":"","userProps":"","correl":"","expiry":"","broker":"374295b309ce444f","x":1670,"y":440,"wires":[]},{"id":"9eafd411f52e9071","type":"mqtt out","z":"83ae842a038866d3","name":"CO","topic":"sensors/co","qos":"","retain":"","respTopic":"","contentType":"","userProps":"","correl":"","expiry":"","broker":"374295b309ce444f","x":1670,"y":380,"wires":[]},{"id":"2144cb4c68a97c98","type":"mqtt out","z":"83ae842a038866d3","name":"C6H6","topic":"sensors/c6h6","qos":"","retain":"","respTopic":"","contentType":"","userProps":"","correl":"","expiry":"","broker":"374295b309ce444f","x":1670,"y":320,"wires":[]},{"id":"a44e6a7982d71cf0","type":"mqtt out","z":"83ae842a038866d3","name":"NO2","topic":"sensors/no2","qos":"","retain":"","respTopic":"","contentType":"","userProps":"","correl":"","expiry":"","broker":"374295b309ce444f","x":1670,"y":260,"wires":[]},{"id":"ac820c6ebe3d0e94","type":"mqtt out","z":"83ae842a038866d3","name":"PM25","topic":"sensors/pm25","qos":"","retain":"","respTopic":"","contentType":"","userProps":"","correl":"","expiry":"","broker":"374295b309ce444f","x":1670,"y":200,"wires":[]},{"id":"5f4b97d3437bf760","type":"mqtt out","z":"83ae842a038866d3","name":"PM10","topic":"sensors/pm10","qos":"","retain":"","respTopic":"","contentType":"","userProps":"","correl":"","expiry":"","broker":"374295b309ce444f","x":1670,"y":140,"wires":[]},{"id":"374295b309ce444f","type":"mqtt-broker","name":"HA MQTT","broker":"192.168.31.160","port":"1883","clientid":"","autoConnect":true,"usetls":false,"protocolVersion":"4","keepalive":"60","cleansession":true,"autoUnsubscribe":true,"birthTopic":"","birthQos":"0","birthRetain":"false","birthPayload":"","birthMsg":{},"closeTopic":"","closeQos":"0","closeRetain":"false","closePayload":"","closeMsg":{},"willTopic":"","willQos":"0","willRetain":"false","willPayload":"","willMsg":{},"userProps":"","sessionExpiry":""}]
```

---

**Commentiamolo:**
--

1. Tramite una chiamata giornaliera alle ore 12.00 lancio l`aggiornamento dei sensori (le rilevazioni sono aggiornate al giorno precedente, quindi non ha senso ripeterla più volte al giorno) tramite il nodo `inject`;
2. Il successivo nodo `http request` è il nodo che invia la stringa per la chiamata dei dati, personalizzabile come detto prima;
3. Il nodo `csv` riceve i dati e li interpreta suddividendoli;
4. Il nodo `function` che segue, denominato `Estrae i dati delle misurazioni`, suddivide l`_array_ ricevuto in stringhe separate producendo più _payload_ per quante sono le righe trasmesse dalla centralina.
     Qui interviene una ulteriore personalizzazione, come faccio a sapere quali inquinanti espone una centralina? La risposta non è complessa:
     1. andare sul sito dei [dati ARPA](https://dati.arpa.puglia.it/openapi/index.html)
     2. scorrere fino alla Sezione `Misurazioni`
     3. cliccare sul successivo tasto `GET`
     4. poi cliccare sulla destra sul tasto `TRY IT OUT`
     5. inserite nel campo `format` il formato dei dati, vi consiglio `csv` per una maggiore intellegibilità
     6. inserite nel campo `id-station` il numero identificativo della centralina che vi interessa, ad esempio `104`
     7. cliccare su `debug-mode` ed impostare a `true` così da avere la risposta a video (non cambia ---a, se lasciate l`impostazione su  `false` vi scaricherà un file di testo con i dati)
     8. quindi cliccare su `Execute`
     9. dopo pochi secondi otterrete la seguente risposta:
        il link per ottenere i dati, nel caso che ci occupa, sarà:


                                 `https://dati.arpa.puglia.it/api/v1/measurements?language=ITA&format=CSV&id_station=104&debugMode=true`

        Nella successiva sezione `Response body` potremo leggere i seguenti dati:
```yaml
         <pre>=== measurements/executeQuery ===
formatParam: CSV
=== measurements/executeQuery ===
<pre>data_di_misurazione,id_station,denominazione,comune,provincia,Longitude,Latitude,tipologia_di_area,tipologia_di_stazione,rete,interesse_rete,id_pollutant,inquinante_misurato,valore_inquinante_misurato,limite,unita_misura,superamenti,indice_qualita,classe_qualita
2025-01-28,104,"Meteo Parchi","Taranto","Taranto",17.222180,40.496730,null,null,"ADI","PRIVATO","13","PM10",null,null,"µg/m³",null,null,null
2025-01-28,104,"Meteo Parchi","Taranto","Taranto",17.222180,40.496730,null,null,"ADI","PRIVATO","12","PM2.5",null,null,"µg/m³",null,null,null
2025-01-28,104,"Meteo Parchi","Taranto","Taranto",17.222180,40.496730,null,null,"ADI","PRIVATO","4","NO2",null,null,"µg/m³",null,null,null
2025-01-28,104,"Meteo Parchi","Taranto","Taranto",17.222180,40.496730,null,null,"ADI","PRIVATO","2","C6H6",null,null,"µg/m³",null,null,null
2025-01-28,104,"Meteo Parchi","Taranto","Taranto",17.222180,40.496730,null,null,"ADI","PRIVATO","1","CO",null,null,"mg/m³",null,null,null
2025-01-28,104,"Meteo Parchi","Taranto","Taranto",17.222180,40.496730,null,null,"ADI","PRIVATO","6","SO2",null,null,"µg/m³",null,null,null
2025-01-28,104,"Meteo Parchi","Taranto","Taranto",17.222180,40.496730,null,null,"ADI","PRIVATO","8","H2S",null,null,"µg/m³",null,null,null
2025-01-28,104,"Meteo Parchi","Taranto","Taranto",17.222180,40.496730,null,null,"ADI","PRIVATO","10","BLACK CARB",null,null,"ng/m³",null,null,null
2025-01-28,104,"Meteo Parchi","Taranto","Taranto",17.222180,40.496730,null,null,"ADI","PRIVATO","11","IPA",null,null,"ng/m³",null,null,null
```

   
5. Il nodo `function` che segue, denominato `divide i messaggi per ogni inquinante`, è dotate di tante uscite quanti sono le righe dell`_array_ ricevuto. Quindi se una centralina espone 6 inquinanti, bisognerà modificarlo come segue:
   Nella Scheda `setup` va modificato il numero delle uscite che sarà uguale al numero degli inquinanti esposti;
   Nella Scheda `on message` va inserita una striga `let msg1 = { payload: misurazioni[0] };` per ogni inquinante esposto, così ad esempio:
```yaml
              let msg1 = { payload: misurazioni[0] }; // Primo oggetto
              let msg2 = { payload: misurazioni[1] }; // Secondo oggetto
              let msg3 = { payload: misurazioni[2] }; // Terzo oggetto
              let msg4 = { payload: misurazioni[3] }; // Quarto oggetto
              let msg5 = { payload: misurazioni[4] }; // Quinto oggetto
              let msg6 = { payload: misurazioni[5] }; // Sesto oggetto
              let msg7 = { payload: misurazioni[6] }; // settimo oggetto
              let msg8 = { payload: misurazioni[7] }; // ottavo oggetto
              let msg9 = { payload: misurazioni[8] }; // nono oggetto
```

ovviamente poi modificheremo anche il successivo messaggio di  `return` del _payload_ ottenendo quindi:

```yaml 
          return [msg1, msg2, msg3, msg4, msg5, msg6, msg7, msg8, msg9];` 
```

in questo modo avremo una uscita per ogni inquinante a cui collegheremo, nello stesso ordine mostrato dall'`API`, il canale MQTT tramite il nodo `mqtt out`. I nodi, per maggiore chiarezza e celerità, li ho denominati così come previsto dalla sigla breve utilizzata nella stessa API regionale.
6. Prima di arrivare alla pubblicazione del dato in `MQTT` ho dovuto inserire un nuovo nodo `function` denominato `formatta in valore "valore" in caso di errore` che ha lo scopo di sostituire i dati non pervenuti, esposti dalle API con la dicitura `null`, con il numero `0`. Questo si è reso necessario perchè altrimenti Home Assistant non è in grado di interpetrare il dato restituendo così un errore generale del sensore che non esporrà nulla.
7. L'ultima cosa è quindi la configurazione dei relativi sensori in Home Assistant, la struttura è identica per tutti, va cambiato solo il nome del sensore nel campo `name` ed il canale mqtt nel campo `json_attributes_topic:`, null`altro:

 ```yaml

#_configuration.yaml_

mqtt:
  sensor:
    - name: "NO2"
      state_topic: "sensors/no2"
      unit_of_measurement: "µg/m³"
      value_template: "{{ value_json.valore }}"
      json_attributes_topic: "sensors/no2"
      json_attributes_template: >
        {
          "data": "{{ value_json.data }}",
          "inquinante": "{{ value_json.inquinante }}",
          "limite": {{ value_json.limite }},
          "unita": "{{ value_json.unita }}",
          "indice_qualita": "{{ value_json.indice_qualita }}",
          "classe_qualita": "{{ value_json.classe_qualita }}",
          "superamenti": {{ value_json.superamenti }}
        }
```

8. Lavoro finito e buon divertimento a tutti!


