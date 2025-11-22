# Documentazione SottoMonte Framework

Il **SottoMonte Framework** è una piattaforma modulare e flessibile progettata per la creazione rapida di applicazioni web moderne e scalabili. Sfrutta Python, Jinja2 e Supabase, adottando un'architettura esagonale (Ports and Adapters) e il pattern MVA (Model-View-Action).

## 🏗️ Architettura

Il framework si basa su due concetti architettonici fondamentali:

### 1. Architettura Esagonale (Ports and Adapters)
Il codice è organizzato per separare la logica di business dai dettagli implementativi (database, interfacce utente, servizi esterni).
- **Framework (Core)**: Contiene la logica di business pura e le interfacce (Porte). Non dipende da librerie esterne o dettagli infrastrutturali.
- **Infrastructure (Adapters)**: Contiene le implementazioni concrete delle porte. Ad esempio, un adattatore per Supabase, uno per Redis, uno per il rendering HTML, ecc.

### 2. Pattern MVA (Model-View-Action)
Un'evoluzione del classico MVC:
- **Model**: Definisce le entità del dominio e la logica dei dati.
- **View**: Gestisce la presentazione (HTML, JSON, ecc.).
- **Action**: Unità indipendenti di logica che rispondono agli input. A differenza dei controller monolitici, le azioni sono granulari e modulari.

---

## 📂 Struttura del Progetto

La struttura delle directory riflette l'architettura:

### `/src/framework/` (Il Core)
Qui risiede la logica di orchestrazione e le definizioni delle interfacce.
- **`manager/`**: Componenti che coordinano le operazioni.
    - **`executor.py`**: Gestisce l'esecuzione delle azioni e dei task (sequenziali, paralleli).
    - **`storekeeper.py`**: Gestisce la persistenza dei dati (CRUD) astraendo il repository sottostante.
    - **`messenger.py`**: Gestisce la comunicazione, il logging e gli eventi.
    - **`presenter.py`**: Gestisce la presentazione dei dati verso l'esterno (UI o API).
- **`port/`**: Definisce le interfacce (contratti) che gli adattatori devono implementare (es. `persistence.contract.json`).
- **`service/`**: Servizi di business logic puri.

### `/src/infrastructure/` (Gli Adattatori)
Contiene le implementazioni concrete delle porte definite nel framework.
- **`persistence/`**: Adattatori per database (es. Supabase, Redis, FileSystem).
- **`presentation/`**: Adattatori per interfacce web (es. Starlette, Flask) o API.
- **`authentication/`**: Adattatori per l'autenticazione (es. Supabase Auth, OAuth).
- **`message/`**: Adattatori per logging e messaggistica.

### `/src/application/` (L'Applicazione)
Contiene il codice specifico dell'applicazione che si sta costruendo.
- **`action/`**: Le azioni specifiche dell'app.
- **`model/`**: I modelli di dati dell'app.
- **`view/`**: Template e layout.

---

## ⚙️ Configurazione

La configurazione è centralizzata nel file `pyproject.toml`. Questo approccio dichiarativo permette di definire quali adattatori usare senza modificare il codice.

Esempio di configurazione:

```toml
[project]
name = "my-app"
version = "0.1.0"

# Configurazione della persistenza (scegliere l'adapter)
[persistence.supabase]
adapter = "supabase"
url = "..."
key = "..."

# Configurazione della presentazione (web server)
[presentation.web]
adapter = "starlette"
host = "0.0.0.0"
port = "5000"
```

---

## 🔑 Componenti Chiave

### Executor
L'`Executor` è il motore che esegue le azioni. Supporta diverse modalità di esecuzione:
- **Sequenziale (`chain_completed`)**: Esegue i task uno dopo l'altro.
- **Parallela (`all_completed`)**: Esegue i task contemporaneamente e attende che tutti finiscano.
- **Race (`first_completed`)**: Restituisce il risultato del primo task completato.

### Storekeeper
Lo `Storekeeper` astrae l'accesso ai dati. Offre metodi standard CRUD:
- `gather` (Read)
- `store` (Create)
- `change` (Update)
- `remove` (Delete)
Utilizza i `repository` definiti nell'applicazione per mappare le richieste sui provider di persistenza configurati.

### Messenger
Il `Messenger` gestisce il flusso di informazioni non di business, come log di debug, errori e notifiche. Può inviare messaggi a diversi canali (console, websocket, file) a seconda della configurazione.

---

## 🚀 Guida Rapida

> **Nota**: Per una guida passo-passo dettagliata su come creare la tua prima applicazione, consulta la [Guida per lo Sviluppatore](developer_guide.md).

### Installazione

1.  **Clona il repository**:
    ```bash
    git clone https://github.com/SottoMonte/framework.git
    cd framework
    ```

2.  **Crea un ambiente virtuale**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Su Windows: venv\Scripts\activate
    ```

3.  **Installa le dipendenze**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Avvia l'applicazione**:
    ```bash
    python3 public/app.py
    ```

L'applicazione si avvierà in base alla configurazione definita in `pyproject.toml` (default: localhost:5000).
