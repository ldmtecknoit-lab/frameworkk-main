# 🧠 SottoMonte: Strategia per la "AI-Dominance"

Per rendere il framework **perfetto** per LLM, Vibe Coding e Agenti Autonomi, dobbiamo trasformarlo da "strumento per umani" a "interfaccia per intelligenze".

Ecco i 4 pilastri per l'evoluzione AI-Native.

## 1. Ottimizzazione del Contesto (Token Efficiency) 📉

Gli LLM hanno una finestra di contesto limitata e "costosa". Il framework deve essere **denso**.

*   **Tipizzazione Forte (Pydantic ovunque)**:
    *   *Adesso*: `def action(**constants)` -> L'IA deve indovinare cosa c'è in `constants`.
    *   *Futuro*: `def action(input: UserLoginSchema)`.
    *   **Perché**: L'IA legge la firma della funzione e sa *esattamente* cosa passare. Zero allucinazioni sui parametri.
*   **Docstring "LLM-Optimized"**:
    *   Invece di descrizioni discorsive, usare formati strutturati che spiegano *intento* e *effetti collaterali*.
    *   Esempio: `"""Effect: Creates user in DB. Triggers: WelcomeEmail."""`

## 2. Interfaccia Agentica (The Framework as a Tool) 🤖

Gli Agenti (come me) lavorano meglio se possono "interrogare" il sistema invece di leggere file di testo grezzi.

*   **Introspection API (`sottomonte inspect`)**:
    *   Un comando che restituisce un JSON con:
        *   Tutte le Action disponibili e i loro schemi di input.
        *   Tutte le Rotte e le Viste associate.
        *   Lo schema del Database corrente.
    *   **Uso**: L'Agente esegue `inspect`, ottiene la mappa completa del sistema in un solo JSON pulito, e pianifica le modifiche senza dover leggere 50 file.
*   **CLI Deterministica**:
    *   L'Agente non dovrebbe scrivere file manualmente se può evitarlo.
    *   Comando: `sottomonte add-field --model User --name age --type int`.
    *   Questo garantisce che l'Agente non rompa la sintassi del file.

## 3. "Vibe Coding" & Astrazione dello Stile 🎨

Il "Vibe Coding" è programmare per intenti ("Fammi una login page stile Cyberpunk").

*   **Design Tokens in XML**:
    *   Espandere l'XML per supportare "Vibes" (temi semantici).
    *   `<Button vibe="danger">` invece di `<Button color="red">`.
    *   L'IA capisce il "vibe" (pericolo) meglio del dettaglio implementativo (codice esadecimale).
*   **Generazione UI da Prompt**:
    *   Integrare un "LLM Compiler" nel framework che trasforma un commento XML in UI.
    *   Input: `<!-- A list of users with avatars -->`
    *   Runtime: Il framework (in dev mode) chiama un LLM e sostituisce il commento con i tag `<List>...`.

## 4. Auto-Correzione (Self-Healing) ❤️‍🩹

L'IA sbaglia. Il framework deve aiutarla a correggersi.

*   **Errori Strutturati (JSON Logs)**:
    *   Quando un'app crasha, il framework non deve solo stampare uno stacktrace. Deve stampare un JSON:
        ```json
        {
          "error": "KeyError",
          "message": "'email' not found in constants",
          "context": "Action: user.login",
          "suggestion": "Check if the form input name matches the action parameter."
        }
        ```
    *   Un Agente può leggere questo JSON e applicare la fix automaticamente ("Ah, ho chiamato il campo 'mail' invece di 'email', correggo").

---

## 🏗️ Piano d'Azione Immediato

1.  **Refactoring Pydantic**: Iniziare a tipizzare le Action core.
2.  **Schema Generator**: Creare uno script che genera `schema.json` di tutto il progetto.
3.  **Error Middleware**: Intercettare le eccezioni e formattarle per gli Agenti.

Trasformando SottoMonte in questo modo, non sarà solo un framework Python, ma un **sistema operativo per lo sviluppo software autonomo**.
