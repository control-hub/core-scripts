computers = [{"mac": "68:54:5A:D3:F0:30"}, {"mac": "8C:C6:81:42:00:0F"}, {"mac": "E8:48:B8:C8:20:00"}]

import socket
import re

def send_wol(mac_address):
    if not re.match(r"^[0-9A-Fa-f]{2}(:[0-9A-Fa-f]{2}){5}$", mac_address):
        raise ValueError(
            "Неверный формат MAC-адреса. Используйте формат AA:BB:CC:DD:EE:FF."
        )

    mac_bytes = bytes.fromhex(mac_address.replace(":", ""))
    magic_packet = b"\xff" * 6 + mac_bytes * 16

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(magic_packet, ("255.255.255.255", 9))

for computer in computers:
    try:
        send_wol(computer["mac"])
        print(f"Wake-on-LAN пакет отправлен на ({computer['mac']}).")
    except ValueError as e:
        print(f"Ошибка: {e}")