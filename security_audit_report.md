# Rapporto di Sicurezza SottoMonte Framework

In seguito a un'analisi approfondita del codice sorgente, sono state individuate diverse vulnerabilità critiche che potrebbero essere sfruttate da malintenzionati per compromettere il sistema.

## 🚨 Vulnerabilità Critiche (High Severity)

### 1. Remote Code Execution (RCE) via `eval()` in `loader.py` (RISOLTO)
**Stato**: ✅ Risolto (sostituito con `json.loads`).

### 2. Command Injection in `ansible.py` e `flow.py` (RISOLTO)
**Stato**: ✅ Risolto (rimosso `shell=True` e codice vulnerabile).

### 3. Hardcoded Secrets (Credenziali Esposte) (RISOLTO)
**Stato**: ✅ Risolto (rimossi segreti da `pyproject.toml` e `ansible.py`).

### 4. Path Traversal in `fs.py` (NUOVO)
**File**: `src/infrastructure/persistence/fs.py` (Righe 25, 51)
**Descrizione**: L'adapter `fs` utilizza direttamente i percorsi forniti in input (`constants['file']`, `constants['path']`) senza alcuna validazione o sanitizzazione.
**Impatto**: Un attaccante può leggere file arbitrari sul server (es. `/etc/passwd`, file di configurazione) utilizzando sequenze come `../../`.
**Rimedio**: Implementare una validazione del percorso per assicurarsi che sia contenuto all'interno di una directory sicura (whitelist) usando `os.path.abspath` e `os.path.commonpath`.

## ⚠️ Vulnerabilità Medie (Medium Severity)

### 5. Insecure Deserialization (RISOLTO)
**Stato**: ✅ Risolto (sostituito `literal_eval` con `json.loads` in `redis.py`).

### 6. SQL Connection String Injection in `sql.py` (NUOVO)
**File**: `src/infrastructure/persistence/sql.py` (Riga 21)
**Descrizione**: La stringa di connessione al database è costruita concatenando direttamente username e password.
**Impatto**: Se la password contiene caratteri speciali (es. `@`, `/`, `:`), può rompere la stringa di connessione o permettere l'iniezione di parametri non previsti.
**Rimedio**: Utilizzare `urllib.parse.quote_plus` per codificare username e password prima dell'inserimento nella stringa di connessione.

### 7. Configurazione CORS e Sicurezza Web
**File**: `src/infrastructure/presentation/starlette.py`
**Descrizione**: Verificare che le configurazioni CORS e i cookie (Secure, HttpOnly) siano impostati correttamente. Attualmente `allow_origins=['*']` è molto permissivo.

### 8. Dipendenze Mancanti
**File**: `requirements.txt`
**Descrizione**: `sqlalchemy` e `asyncmy` sono usati in `sql.py` ma non sono elencati in `requirements.txt`. Questo può causare fallimenti nel deployment.

### 6. Configurazione CORS e Sicurezza Web
**File**: `src/infrastructure/presentation/starlette.py` (non analizzato in dettaglio ma da verificare)
**Descrizione**: Verificare che le configurazioni CORS e i cookie (Secure, HttpOnly) siano impostati correttamente per prevenire XSS e CSRF.

## 🛡️ Piano di Remediation

1.  **Immediato**: Ruotare tutte le chiavi e i segreti esposti in `pyproject.toml`.
2.  **Immediato**: Patchare `loader.py` sostituendo `eval` con `json.loads`.
3.  **Breve Termine**: Rifattorizzare `ansible.py` e `flow.py` per rimuovere `shell=True`.
4.  **Medio Termine**: Implementare un sistema di gestione dei segreti basato su variabili d'ambiente.
5.  **Lungo Termine**: Rivedere l'architettura di caricamento dinamico per minimizzare l'uso di `exec` e introdurre sandboxing.
