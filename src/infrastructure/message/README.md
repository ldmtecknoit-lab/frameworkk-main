# Message Adapters (`/src/infrastructure/message`)

Questa directory contiene gli adattatori per la messaggistica e il logging.

## File Principali

*   **`console.py`**: Adattatore per stampare log e messaggi sulla console standard.
*   **`log.py`**: Adattatore per scrivere log su file.
*   **`redis.py`**: Adattatore per utilizzare Redis Pub/Sub per la messaggistica asincrona tra componenti.
*   **`websocket.py`**: Adattatore per inviare messaggi ai client via WebSocket.
*   **`api.py`**: Adattatore per inviare messaggi a servizi esterni via API (es. notifiche push, webhooks).
*   **`mqtt.py`**: Adattatore per protocollo MQTT, utile per IoT.
