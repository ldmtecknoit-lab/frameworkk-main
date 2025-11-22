# Framework Managers (`/src/framework/manager`)

Questa directory contiene i componenti che orchestrano le operazioni del sistema. Sono responsabili del coordinamento tra i servizi e gli adattatori.

## File Principali

*   **`executor.py`**: Il motore di esecuzione. Gestisce l'esecuzione delle azioni in diverse modalità:
    *   Sequenziale (`chain_completed`)
    *   Parallela (`all_completed`)
    *   Race (`first_completed`)
*   **`storekeeper.py`**: Il gestore della persistenza. Astrae le operazioni CRUD (Create, Read, Update, Delete) e le delega ai repository e agli adattatori appropriati.
*   **`messenger.py`**: Gestisce la comunicazione interna ed esterna, inclusi log, notifiche e messaggi di sistema.
*   **`presenter.py`**: Gestisce la logica di presentazione, preparando i dati per essere visualizzati dall'interfaccia utente o restituiti via API.
*   **`defender.py`**: (Dedotto) Gestisce la sicurezza e la validazione delle richieste.
*   **`tester.py`**: Utilità per il testing dei componenti.
