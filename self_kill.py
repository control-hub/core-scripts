import os

process_name = "ControlHub.exe"
os.system(f"taskkill /F /IM {process_name}")
