import ujson

class MQTTTopicContract:
    def __init__(self, student_id, device_id):
        self.student_id = student_id
        self.device_id = device_id
        self.base_topic = f"internship/{student_id}/{device_id}"
        
        # Topic Tanımlamaları
        self.TOPIC_AVAILABILITY = f"{self.base_topic}/availability"
        self.TOPIC_STATE = f"{self.base_topic}/state"
        self.TOPIC_COMMAND = f"{self.base_topic}/command"
        self.TOPIC_COMMAND_ACK = f"{self.base_topic}/command-ack"
        self.TOPIC_COMMAND_RESULT = f"{self.base_topic}/command-result"

    def get_topics(self):
        """Cihazın dinleyeceği ve yayınlayacağı tüm topic listesini döner."""
        return {
            "availability": self.TOPIC_AVAILABILITY,
            "state": self.TOPIC_STATE,
            "command": self.TOPIC_COMMAND,
            "command_ack": self.TOPIC_COMMAND_ACK,
            "command_result": self.TOPIC_COMMAND_RESULT
        }

    def create_availability_payload(self, is_online=True):
        """Availability (Last Will / Online Status) payload'ı üretir."""
        return "online" if is_online else "offline"

    def create_state_payload(self, is_online, is_time_valid, pump_state, started_at=None, auto_stop_at=None, last_error=None):
        """Cihaz canlı durum payload'ını hazırlar."""
        payload = {
            "deviceId": self.device_id,
            "online": is_online,
            "timeValid": is_time_valid,
            "pump": {
                "state": pump_state,
                "startedAt": started_at,
                "autoStopAt": auto_stop_at
            },
            "lastError": last_error
        }
        return ujson.dumps(payload)

    def create_command_ack_payload(self, client_request_id, status, reason=""):
        """Komut alındı (ACK) yanıt payload'ı üretir."""
        payload = {
            "clientRequestId": client_request_id,
            "status": status, # "accepted" veya "rejected"
            "reason": reason
        }
        return ujson.dumps(payload)