import os

url = r"{{URL}}"
install_path = r"{{INSTALL_PATH or os.getenv('USERPROFILE') + r'\Downloads'}}"

from controlhub import download, open_file

print(f"Downloading from {url} to {install_path}...")
file_path = download(url, install_path)
print(f"Downloaded file: {file_path}")

open_file(file_path)
print(f"Opened file: {file_path}")