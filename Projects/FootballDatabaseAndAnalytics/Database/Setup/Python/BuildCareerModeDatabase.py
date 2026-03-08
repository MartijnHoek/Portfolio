import os
import subprocess

scripts = os.listdir("Scripts")

print(scripts)

for script in scripts:
    file_path = os.path.join("Scripts", script)
    print(f"Running {script}...")
    subprocess.run(["python", file_path])
