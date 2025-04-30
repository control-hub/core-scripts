from controlhub import download

url = "{{URL}}"
install_path = "{{INSTALL_PATH}}"

print(f"Downloading from {url} to {install_path}...")
file_path = download(url, install_path)
print(f"Downloaded file: {file_path}")
