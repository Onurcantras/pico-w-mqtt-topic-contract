# 📡 Pico W - MQTT Topic Tree & Data Contract Architecture

A structured specification and MicroPython utility class defining the **MQTT Topic Tree** and **JSON Payload Contracts** for the IoT Irrigation Controller system.

## 🚀 Features

- **Unique Namespace Separation:** Enforces `internship/{studentId}/{deviceId}/...` structure to eliminate message collisions across multi-tenant brokers.
- **Strict Decoupling:** Separates command ingestion channels (`command`) from state telemetries (`state`) and request acknowledgments (`command-ack`).
- **Standardized Payload Formatters:** Provides helper methods to encode state snapshots, last-will availability messages, and transaction execution results.

## 📋 Topic Specifications

- `.../availability`: Retained LWT string (`online` / `offline`).
- `.../state`: Retained JSON snapshot reflecting device clock integrity, relay states, and current runtime metrics.
- `.../command`: Non-retained incoming command channel (`StartPump`, `StopPump`).
- `.../command-ack`: Non-retained command confirmation response paired with `clientRequestId`.

## 🛠️ Requirements

- **Hardware:** Raspberry Pi Pico W
- **Firmware:** MicroPython (v1.20.0+)
- **IDE:** Thonny IDE