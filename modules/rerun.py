import os

def rerun():
    import subprocess

    if os.name == "nt":
        subprocess.run(["python", "skytrack.py"])
    else:
        subprocess.run(["python3", "skytrack.py"])