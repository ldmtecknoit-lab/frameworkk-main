# Framework Core (`/src/framework`)

Questa directory rappresenta il cuore dell'applicazione. Contiene la logica di business pura, le regole di orchestrazione e le definizioni delle interfacce.

## Logica

Il codice qui contenuto è **agnostico** rispetto all'infrastruttura. Non sa se i dati vengono salvati su un database SQL o NoSQL, né se l'interfaccia è web o mobile. Comunica con il mondo esterno solo attraverso le **Porte** (interfacce) e i **Manager**.

## Struttura

*   **`manager/`**: I "Direttori d'Orchestra". Coordinano i flussi di lavoro.
    *   `executor.py`: Esegue le azioni.
    *   `storekeeper.py`: Gestisce i dati.
    *   `messenger.py`: Gestisce le comunicazioni.
*   **`port/`**: I "Contratti". Definiscono le interfacce che l'infrastruttura deve rispettare.
*   **`service/`**: La "Business Logic". Contiene la logica specifica del dominio.
*   **`scheme/`**: Schemi e definizioni di dati (probabilmente Pydantic models o simili).
