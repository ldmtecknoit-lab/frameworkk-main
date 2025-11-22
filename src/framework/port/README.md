# Framework Ports (`/src/framework/port`)

Questa directory definisce le **Porte** (interfacce) dell'architettura esagonale.

## Logica

Le porte sono contratti che specificano *cosa* un adattatore deve fare, ma non *come*. Il framework dipende solo da queste interfacce, mai dalle implementazioni concrete.

## File Principali

*   **`persistence.py` / `.contract.json`**: Interfaccia per la persistenza dei dati (Database).
*   **`presentation.py` / `.contract.json`**: Interfaccia per la presentazione (Web, API).
*   **`authentication.py`**: Interfaccia per l'autenticazione utenti.
*   **`authorization.py`**: Interfaccia per la gestione dei permessi.
*   **`message.py`**: Interfaccia per i sistemi di messaggistica.
*   **`actuator.py`**: Interfaccia per azioni esterne (es. chiamate API, script).
*   **`sensor.py`**: Interfaccia per input esterni (es. webhook, sensori IoT).
