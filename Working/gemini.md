# IMPLEMENTATION ORDER

You should build this project in this order only
You have access to terminal and arduino-cli, curl and websocat

1. Project structure
2. Configuration
3. WebSocket server
4. Audio streaming
5. Wake word detection
6. STT
7. Gemini integration
8. TTS
9. JSON protocol
10. ESP32 communication
11. OLED integration
12. Motors
13. Sensors
14. Error handling
15. Final testing

Testing Requirements

Each module should be independently testable.

Provide:

- Unit tests where appropriate.
- Mock websocket client.
- Mock Gemini responses.
- Mock microphone input.
- Mock ESP32 client.

Ensure every module can be tested without physical hardware where possible.

NOTE: 1st create a working server.py, test the application from cli or GUI and then start with the ESP32 client implementation part
