# Sensor Adapters (`/src/infrastructure/sensor`)

Questa directory contiene gli adattatori per i "Sensori", ovvero componenti che raccolgono dati dall'ambiente esterno.

## File Principali

*   **`webcam.py`**: Acquisizione video da webcam.
*   **`microphone.py`**: Acquisizione audio da microfono.
*   **`accelerometer.py`, `gyroscope.py`, `magnetometer.py`**: Sensori di movimento e orientamento (utili su mobile o IoT).
*   **`ambientlight.py`**: Sensore di luce ambientale.
*   **`api.py`**: Sensore virtuale che riceve dati da API esterne.
