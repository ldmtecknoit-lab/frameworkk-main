# Authorization Adapters (`/src/infrastructure/authorization`)

Questa directory contiene gli adattatori per la gestione dei permessi e delle politiche di accesso.

## File Principali

*   **`opa.py`**: Integrazione con OPA (Open Policy Agent), un motore di policy general-purpose.
*   **`verdict.py`**: Motore di autorizzazione interno che emette un "verdetto" (Permetti/Nega) basato su regole definite.
