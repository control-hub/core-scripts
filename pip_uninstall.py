import os
from controlhub import run_program

package = r"{{PACKAGE}}"

run_program(
    os.getenv("PROGRAMPATH") + r"\python\python.exe -m pip uninstall " + package
)
print(f"Package{'s' if ' ' in package else ''} {package} uninstalled successfully.")