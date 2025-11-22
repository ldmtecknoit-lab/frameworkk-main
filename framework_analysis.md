# Analisi Comparativa: SottoMonte Framework vs Ecosistema Python (Django, FastAPI, Flask)

Questa analisi evidenzia i punti di forza distintivi del **SottoMonte Framework** rispetto ai framework Python tradizionali come Django, FastAPI e Flask.

## 🏆 Punti di Forza Unici (Unique Selling Points)

### 1. Architettura "Write Once, Run Everywhere" (Web & Native)
*   **SottoMonte**: Grazie agli adapter di presentazione (`starlette` per il web, `flutter` per il nativo), puoi scrivere la logica di business e le viste (in XML) **una sola volta** e distribuirle sia come Web App che come applicazione Desktop/Mobile nativa.
*   **Django/FastAPI/Flask**: Sono framework puramente Web. Per creare un'app mobile o desktop devi riscrivere il frontend usando tecnologie completamente diverse (React Native, Flutter, Electron) e collegarle via API.
*   **Vantaggio**: Risparmio enorme di tempo e codice per progetti multi-piattaforma.

### 2. Architettura Esagonale (Ports and Adapters) Nativa
*   **SottoMonte**: È costruito dalle fondamenta sull'architettura esagonale. La logica di business (`src/framework/service`) non sa nulla del database o del web server. Cambiare da Redis a SQL o da Starlette a Flask è una questione di configurazione (`pyproject.toml`), non di riscrittura del codice.
*   **Django**: Segue il pattern MVT (Model-View-Template) ed è fortemente accoppiato al suo ORM. Sostituire l'ORM di Django o il sistema di template è difficile.
*   **FastAPI/Flask**: Sono più flessibili, ma l'architettura pulita deve essere imposta manualmente dallo sviluppatore. SottoMonte la impone strutturalmente.

### 3. Configurazione Dichiarativa Estrema
*   **SottoMonte**: Tutto, dalla scelta del database all'adapter di autenticazione (Supabase, OAuth, Fake), è definito in `pyproject.toml`.
*   **Altri**: Richiedono codice "glue" (colla) per inizializzare e configurare le librerie (es. `settings.py` in Django, istanziazione manuale in Flask).
*   **Vantaggio**: Deployment e switch di ambienti (Dev/Prod) molto più puliti e meno proni a errori di codice.

### 4. Pattern MVA (Model-View-Action) Granulare
*   **SottoMonte**: Le "Action" sono unità di logica piccole, atomiche e riutilizzabili. Non esistono "Controller" giganti con migliaia di righe.
*   **Django**: I file `views.py` tendono a diventare enormi (Fat Views) se non gestiti con disciplina.
*   **Vantaggio**: Manutenibilità e testabilità superiori. Ogni Action fa una cosa sola.

### 5. Astrazione dell'UI (XML Views)
*   **SottoMonte**: Le viste sono definite in XML astratto (`<Row>`, `<Column>`, `<Input>`). Questo permette al framework di decidere come renderizzarle: `<div>` HTML per il web, Widget `ft.Row` per Flutter.
*   **Django/Flask**: Usano template HTML (Jinja2, DTL). Sono legati indissolubilmente al Web/Browser.
*   **Vantaggio**: Disaccoppiamento totale tra definizione dell'interfaccia e tecnologia di rendering.

## ⚖️ Tabella di Confronto

| Caratteristica | SottoMonte | Django | FastAPI |
| :--- | :--- | :--- | :--- |
| **Architettura** | Esagonale (Ports & Adapters) | MVT (Monolitico) | MVC/Micro (Flessibile) |
| **Target** | Web, Desktop, Mobile | Web | Web (API) |
| **UI** | XML Astratto (Renderizza HTML/Flutter) | HTML Templates | JSON (API) / HTML opzionale |
| **Database** | Agnostico (Adapter per SQL, Redis, FS, Supabase) | ORM proprietario (SQL) | Agnostico (SQLAlchemy, Tortoise, ecc.) |
| **Configurazione** | Dichiarativa (`pyproject.toml`) | Imperativa (`settings.py`) | Imperativa (Codice) |
| **Async** | Nativo | Aggiunto successivamente | Nativo |
| **Curva di Apprendimento** | Media (Nuovi concetti: XML Views, Hexagonal) | Media (Tante "batterie" da imparare) | Bassa (Molto intuitivo) |

## 🎯 Quando scegliere SottoMonte?

SottoMonte è la scelta vincente se:
1.  Devi sviluppare un sistema che deve essere accessibile via **Web, Desktop e Mobile** senza duplicare il team di sviluppo.
2.  Vuoi un'architettura che ti permetta di **cambiare stack tecnologico** (es. database) in futuro senza riscrivere la business logic.
3.  Apprezzi la **configurazione rispetto alla convenzione** e vuoi un controllo granulare tramite file di config.

Django rimane superiore per siti web content-heavy standard (CMS, E-commerce classici) grazie al suo ecosistema immenso. FastAPI è imbattibile per microservizi API puri ad alte prestazioni. **SottoMonte brilla nelle applicazioni complesse multi-interfaccia.**
