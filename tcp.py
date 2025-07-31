import socket
import json
from random import randint, uniform
from time import sleep

# Adres IP i port serwera
SERVER_IP = '20.215.133.78'  # Zmień na adres serwera, jeśli to nie localhost
SERVER_PORT = 65432

# Funkcja generująca przykładowe dane maszyny
def generate_sample_data():
    return {
        "machine_id": randint(1, 10),
        "is_running": bool(randint(0, 1)),
        "has_error": bool(randint(0, 1)),
        "cycle_completed": randint(0, 100),
        "tag1": round(uniform(0.0, 100.0), 2),
        "tag2": round(uniform(0.0, 100.0), 2),
        "tag3": round(uniform(0.0, 100.0), 2),
        "tag4": round(uniform(0.0, 100.0), 2)
    }

# Funkcja wysyłająca dane do serwera
def send_data_to_server(data: dict):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((SERVER_IP, SERVER_PORT))
            json_data = json.dumps(data)
            sock.sendall(json_data.encode('utf-8'))

            response = sock.recv(1024)
            print(f"📬 Odpowiedź serwera: {response.decode().strip()}")
    except Exception as e:
        print(f"❌ Błąd połączenia z serwerem: {e}")

if __name__ == "__main__":
    while True:
        sample_data = generate_sample_data()
        print(f"📤 Wysyłanie danych: {sample_data}")
        send_data_to_server(sample_data)
        sleep(5)  # Wysyłaj dane co 5 sekund