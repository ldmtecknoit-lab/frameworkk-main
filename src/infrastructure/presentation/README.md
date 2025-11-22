# Presentation Adapters (`/src/infrastructure/presentation`)

Questa directory contiene gli adattatori per l'interfaccia utente e l'esposizione dei servizi.

## File Principali

*   **`starlette.py`**: Adattatore basato su Starlette (framework ASGI). Gestisce le richieste HTTP, le rotte e i websocket per l'applicazione web backend.
*   **`wasm.py`**: Adattatore per WebAssembly. Permette di eseguire parti del framework direttamente nel browser (es. con PyScript).
*   **`flutter.py`**: Adattatore per integrazione con Flutter (probabilmente per app mobile/desktop).
