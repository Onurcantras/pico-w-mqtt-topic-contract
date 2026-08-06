from mqtt_contract import MQTTTopicContract

# Öğrenci ve Cihaz Kimliği Tanımlamaları
STUDENT_ID = "onurcan"
DEVICE_ID = "pico-w-pump-01"

print("=== PICO W MQTT TOPIC & CONTRACT ARCHITECTURE ===")

# Topic Yapılandırıcıyı Başlat
contract = MQTTTopicContract(student_id=STUDENT_ID, device_id=DEVICE_ID)

topics = contract.get_topics()
print("\n--> Tasarlanan MQTT Topic Ağacı:")
for name, topic_path in topics.items():
    print(f"  [{name.upper()}] -> {topic_path}")

print("\n--> Örnek Mesaj Testleri:")

# 1. Availability Payload
print("Availability (Online):", contract.create_availability_payload(True))

# 2. Cihaz Durum (State) Payload
sample_state = contract.create_state_payload(
    is_online=True,
    is_time_valid=True,
    pump_state="running",
    started_at=1774218000,
    auto_stop_at=1774218060,
    last_error=None
)
print("State Payload:", sample_state)

# 3. Komut ACK (Kabul) Payload
sample_ack = contract.create_command_ack_payload(
    client_request_id="req-mob-999",
    status="accepted",
    reason="Pompa başlatma talebi kabul edildi."
)
print("Command ACK Payload:", sample_ack)