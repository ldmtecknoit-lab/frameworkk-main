# Source Code (`/src`)

Questa directory contiene il codice sorgente principale del framework SottoMonte.

## Struttura

*   **`framework/`**: Il "Core" del sistema. Contiene la logica di business, i manager di orchestrazione e le definizioni delle interfacce (Porte). È indipendente dai dettagli implementativi.
*   **`infrastructure/`**: Gli "Adattatori". Contiene le implementazioni concrete delle interfacce definite nel framework. Qui si trovano i collegamenti a database, API esterne, framework web, ecc.

## Logica

Il codice è organizzato seguendo l'**Architettura Esagonale** (Ports and Adapters).
- **Framework** definisce *cosa* deve essere fatto (es. "salva questo dato").
- **Infrastructure** definisce *come* farlo (es. "salvalo su Supabase" o "salvalo su Redis").

Questa separazione permette di cambiare le tecnologie sottostanti (es. cambiare database) senza modificare la logica di business nel framework.
