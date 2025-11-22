# Persistence Adapters (`/src/infrastructure/persistence`)

Questa directory contiene gli adattatori per la persistenza dei dati.

## File Principali

*   **`supabase.py`**: Adattatore per Supabase (PostgreSQL + API). Gestisce le operazioni CRUD tramite la libreria client di Supabase.
*   **`redis.py`**: Adattatore per Redis. Utilizzato per caching, sessioni o dati volatili.
*   **`fs.py`**: Adattatore per il File System locale. Permette di leggere/scrivere file su disco.
*   **`sql.py`**: Adattatore generico per database SQL (probabilmente via SQLAlchemy o simili).
*   **`api.py`**: Adattatore per persistere dati su API remote.
*   **`jwt.py`**: Gestione della persistenza tramite token JWT (es. salvataggio stato nel token).
*   **`web.py`**: Adattatore per storage web (es. LocalStorage se in ambiente WASM/JS).
