# 👩‍💻 Guida per lo Sviluppatore SottoMonte

Questa guida ti accompagnerà nella creazione della tua prima applicazione con il SottoMonte Framework.

## 1. Prerequisiti

*   Python 3.9 o superiore
*   pip (Python Package Installer)
*   Git

## 2. Installazione e Setup

1.  **Clona il repository**:
    ```bash
    git clone https://github.com/SottoMonte/framework.git
    cd framework
    ```

2.  **Crea l'ambiente virtuale**:
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Linux/Mac
    source venv/bin/activate
    ```

3.  **Installa le dipendenze**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Crea la struttura dell'applicazione**:
    Il framework si aspetta che il codice specifico della tua app risieda in `src/application`. Poiché questa directory potrebbe non esistere inizialmente, creala con la seguente struttura:

    ```bash
    mkdir -p src/application/action
    mkdir -p src/application/model
    mkdir -p src/application/view/page
    mkdir -p src/application/view/layout
    mkdir -p src/application/view/component
    mkdir -p src/application/policy/presentation
    ```

## 3. Configurazione

Il file `pyproject.toml` è il punto centrale di configurazione. Assicurati che le impostazioni di base siano corrette per il tuo ambiente locale.

```toml
[project]
name = "my-first-app"
version = "0.1.0"

[presentation.web]
adapter = "starlette"
host = "0.0.0.0"
port = "5000"
route = "web.xml"  # File di routing
```

## 4. Creare la Prima Azione (Hello World)

Le **Azioni** contengono la logica di business. Creiamo una semplice azione che restituisce un messaggio.

Crea il file `src/application/action/hello.py`:

```python
# src/application/action/hello.py

async def world(**constants):
    """
    Una semplice azione che restituisce un saluto.
    I parametri passati dalla richiesta sono in **constants.
    """
    name = constants.get('name', 'Mondo')
    return {'message': f"Ciao, {name}!"}
```

## 5. Definire le Rotte

Le rotte mappano gli URL alle viste o alle azioni. Il framework usa file XML per definire le rotte.

Crea il file `src/application/policy/presentation/web.xml`:

```xml
<!-- src/application/policy/presentation/web.xml -->
<routes>
    <!-- Rotta Home -->
    <route path="/" method="GET" view="home.xml" type="html" layout="main" />
    
    <!-- Esempio di rotta con parametro -->
    <route path="/hello/{name}" method="GET" view="hello.xml" type="html" />
</routes>
```

## 6. Creare le Viste

Le viste definiscono l'interfaccia utente. Il framework usa un sistema di templating basato su XML/HTML e Jinja2.

Crea il layout base `src/application/view/layout/main.xml`:

```xml
<!-- src/application/view/layout/main.xml -->
<html>
    <head>
        <title>La Mia App</title>
    </head>
    <body>
        <Container>
            <!-- Il contenuto della pagina verrà iniettato qui -->
            {{ inner | safe }}
        </Container>
    </body>
</html>
```

Crea la pagina home `src/application/view/page/home.xml`:

```xml
<!-- src/application/view/page/home.xml -->
<Row>
    <Column>
        <Text>Benvenuto nel SottoMonte Framework!</Text>
    </Column>
</Row>
```

## 7. Avviare l'Applicazione

Per avviare il server di sviluppo:

```bash
python src/framework/service/run.py
```

Il server dovrebbe avviarsi (default: `http://localhost:5000`).

## ⚠️ Risoluzione Problemi

*   **Errore `ModuleNotFoundError: No module named 'framework.service.flow'`**:
    Se incontri questo errore, verifica che tutti i file del framework siano presenti. In alcune versioni, potrebbe essere necessario verificare l'integrità della directory `src/framework`.

*   **Directory `src/application` mancante**:
    Ricorda che questa directory è destinata al *tuo* codice e potrebbe non essere presente nel repository base. Devi crearla manualmente come descritto al punto 2.
