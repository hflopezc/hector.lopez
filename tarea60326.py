import os

def clean_environment():
    os.system("sudo apt-get autoremove")
    os.system("sudo apt-get autoclean")

if __name__ == "__main__":
    clean_environment()
