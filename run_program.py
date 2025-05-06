import os

program_name = r"{{PROGRAM_NAME}}"
os.environ["CH_DELAY"] = "{{DELAY or 0.8}}"

from controlhub import run_program

run_program(program_name)
print(f"Program {program_name} lunched successfully.")