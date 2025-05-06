import os
from controlhub import download

url = r"{{URL}}"
install_path = rf"{{INSTALL_PATH or Default download path}}"

if install_path == "Default download path":
    install_path = os.getenv("USERPROFILE") + r"\Downloads"

print(f"Downloading from {url} to {install_path}...")
file_path = download(url, install_path)
print(f"Downloaded file: {file_path}")
