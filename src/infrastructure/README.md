# Infrastructure Adapters (`/src/infrastructure`)

Questa directory contiene gli **Adattatori** dell'architettura esagonale. Qui risiedono le implementazioni concrete delle tecnologie utilizzate dall'applicazione.

## Logica

Ogni sottocartella corrisponde a una "Porta" definita nel framework. Gli adattatori qui contenuti implementano quelle interfacce, permettendo al framework di interagire con il mondo esterno (database, API, utenti) senza conoscere i dettagli specifici della tecnologia usata.

## Struttura

*   **`persistence/`**: Adattatori per il salvataggio dati (Supabase, Redis, FileSystem).
*   **`presentation/`**: Adattatori per l'interfaccia utente e API (Starlette, Flask, CLI).
*   **`authentication/`**: Adattatori per l'identità (Supabase Auth, OAuth, JWT).
*   **`message/`**: Adattatori per logging e code di messaggi.
*   **`actuator/`**: Adattatori per eseguire azioni esterne.
*   **`sensor/`**: Adattatori per ricevere input esterni.
*   **`encryption/`**: Implementazioni di algoritmi crittografici.
*   **`authorization/`**: Implementazioni di logiche di permesso.
*   **`perception/`**: Moduli per l'analisi dati o AI.
