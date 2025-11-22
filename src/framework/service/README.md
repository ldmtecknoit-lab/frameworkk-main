# Framework Services (`/src/framework/service`)

Questa directory contiene i servizi core che forniscono funzionalità di base al framework.

## File Principali

*   **`language.py`**: Il cuore del sistema dinamico. Probabilmente gestisce il DSL (Domain Specific Language) interno, l'iniezione delle dipendenze e le funzionalità di metaprogrammazione.
*   **`loader.py`**: Responsabile del caricamento dinamico dei moduli e delle risorse. Permette al framework di essere estensibile senza riavvii.
*   **`factory.py`**: Implementa il pattern Factory per la creazione di oggetti complessi.
*   **`run.py`**: Gestisce il ciclo di vita dell'applicazione e l'esecuzione runtime.
*   **`contract.py`**: Gestisce la validazione dei contratti (interfacce) per assicurare che gli adattatori rispettino le specifiche.
