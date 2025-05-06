# test data
computers = [
    {"mac": "68:54:5A:D3:F0:30"},  # ...
    {"mac": "8C:C6:81:42:00:0F"},  # ...
    {"mac": "E8:48:B8:C8:20:00"},  # ...
]

# comment computers adds variable computers,
# that includes all computers,
# witch were selected on execution moment

# COMPUTERS

from wakeonlan import send_magic_packet

for pc in computers:
    if pc["status"] == "0":
        try:
            send_magic_packet(pc["mac"])
            print(f"Sent magic packet to {pc['name']}")
        except Exception as e:
            print(e, pc["name"])