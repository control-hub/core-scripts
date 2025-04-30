from controlhub import download, open_file

url = "{{URL}}"
install_path = "{{INSTALL_PATH}}"

print(f"Downloading from {url} to {install_path}...")
file_path = download(url, install_path)
print(f"Downloaded file: {file_path}")

open_file(file_path)
print(f"Opened file: {file_path}")