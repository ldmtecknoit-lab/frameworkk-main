# 🚀 Roadmap e Miglioramenti Proposti

Basandomi sulla filosofia del **SottoMonte Framework** (Architettura Esagonale, MVA, Configurazione Dichiarativa, Multi-piattaforma), ecco le aree chiave dove il framework può evolvere per diventare ancora più potente e developer-friendly.

## 1. Developer Experience (DX) 🛠️

### CLI di Scaffolding (`sottomonte-cli`)
Attualmente, la creazione di nuovi progetti o componenti richiede la creazione manuale di file e directory.
*   **Proposta**: Creare uno strumento CLI.
*   **Comandi**:
    *   `sottomonte new app my-app`: Crea la struttura directory e il `pyproject.toml`.
    *   `sottomonte generate action user.login`: Crea lo scheletro dell'azione Python.
    *   `sottomonte generate view login`: Crea il file XML della vista.
*   **Filosofia**: Riduce la barriera all'ingresso e standardizza la struttura dei progetti.

## 2. Espansione Infrastruttura (Nuovi Adapter) 🔌

### Adapter TUI (Text User Interface)
Hai già Web (Starlette) e Native (Flutter). Il prossimo passo logico per dimostrare la potenza del "Write Once, Run Everywhere" è il terminale.
*   **Proposta**: Implementare un adapter `presentation` basato su **Textual** o **Curses**.
*   **Risultato**: Le stesse viste XML (`<Row>`, `<Input>`, `<Button>`) verrebbero renderizzate come interfaccia testuale interattiva nel terminale.
*   **Filosofia**: Dimostrazione definitiva del disaccoppiamento UI.

### Adapter GraphQL
Attualmente le azioni sembrano esposte via REST/RPC implicito.
*   **Proposta**: Un adapter `presentation` che espone automaticamente le Action come mutation/query GraphQL.
*   **Filosofia**: Flessibilità nell'esposizione dei servizi senza toccare la logica.

## 3. Core & Robustezza 🧠

### Validazione Tipizzata (Pydantic Integration)
Le Action ricevono `**constants` generici. Questo è flessibile ma prono a errori.
*   **Proposta**: Integrare **Pydantic** per definire gli input/output delle Action.
*   **Esempio**:
    ```python
    class LoginInput(BaseModel):
        email: EmailStr
        password: str

    async def login(input: LoginInput): ...
    ```
*   **Filosofia**: Mantenere la semplicità ma aggiungere robustezza enterprise.

### Sistema di Middleware / Pipeline
Manca un modo standard per intercettare l'esecuzione delle azioni globalmente (es. per logging centralizzato, metriche, rate limiting).
*   **Proposta**: Estendere `executor.py` per supportare una catena di middleware configurabili in `pyproject.toml`.
*   **Filosofia**: Composizione e configurabilità.

## 4. Testing & Quality Assurance 🧪

### Test Runner Integrato
*   **Proposta**: Un runner che sa leggere i file `web.xml` e generare test di integrazione automatici che verificano se le rotte puntano ad azioni esistenti e se le viste sono ben formate.
*   **Filosofia**: Sicurezza e stabilità.

---

## 📋 Priorità Consigliata

1.  **CLI**: Fondamentale per l'adozione.
2.  **Pydantic**: Fondamentale per la stabilità del codice.
3.  **TUI Adapter**: "Killer feature" per mostrare l'unicità del framework.
4.  **Middleware**: Necessario man mano che le app crescono.
