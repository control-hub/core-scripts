import os

process_name = "{{PROCESS_NAME}}"
os.system(f"taskkill /F /IM {process_name}")