import os
import shutil

# مسارات ملفات السجلات والبيانات المؤقتة لعام 2026
BASE_PATH = "/sdcard/Android/data/com.dts.freefireth/"
LOG_FILES = [
    "files/report_info.txt",
    "files/logs",
    "files/UnityAdsCache",
    "cache"
]

def purge_evidence():
    print("[!] Initiating System Purge...")
    
    for folder in LOG_FILES:
        full_path = os.path.join(BASE_PATH, folder)
        try:
            if os.path.isfile(full_path):
                os.remove(full_path)
                print(f"[+] File Shredded: {folder}")
            elif os.path.isdir(full_path):
                shutil.rmtree(full_path)
                print(f"[+] Directory Purged: {folder}")
        except Exception:
            continue

    print("[*] Logs Cleared. System Stealth Active.")

if __name__ == "__main__":
    purge_evidence()

