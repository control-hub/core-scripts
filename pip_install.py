import os
from controlhub import run_program

package = "{{PACKAGE}}"

run_program(os.getenv("PROGRAMPATH") + r"\python\python.exe -m pip install " + package)
print(f"Package{'s' if ' ' in package else ''} {package} installed successfully.")