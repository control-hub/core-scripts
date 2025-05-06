import os

keys = r"{{KEYS}}".lower()  # Ctrl + a, Backspace
os.environ["CH_DELAY"] = "{{DELAY or 0.8}}"

from controlhub import press

key_groups = keys.split(",")
key_groups = [key_group.strip() for key_group in key_groups]
key_groups = [key_group.split("+") for key_group in key_groups]
key_groups = [
    [key.replace(" ", "") for key in key_group]
    if len(key_group) > 1
    else key_group[0].replace(" ", "")
    for key_group in key_groups
]

print(key_groups)
press(*key_groups)
print(f"Pressed keys: {keys}")