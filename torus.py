import os
from time import sleep
from controlhub import press, write, download

download(
    "https://github.com/control-hub/core-scripts/raw/refs/heads/main/torus.exe"
)

file_path = os.path.join(os.getcwd(), "download", "torus.exe")

press("win")
sleep(1)
write("cmd\n")
sleep(2)
press("f11")
write(f'color 0a\n"{file_path}"\n')
sleep(2)
