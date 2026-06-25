import urllib.request
import os

# Updated working URLs for the MobileNet-SSD architecture
files = {
    "MobileNetSSD_deploy.prototxt": "https://raw.githubusercontent.com/chuanqi305/MobileNet-SSD/master/voc/MobileNetSSD_deploy.prototxt",
    "MobileNetSSD_deploy.caffemodel": "https://raw.githubusercontent.com/nikmart/pi-object-detection/master/MobileNetSSD_deploy.caffemodel"
}

print("--- Initializing DecodeLabs Dependency Downloader ---")

for filename, url in files.items():
    if not os.path.exists(filename):
        print(f"[INFO] Downloading {filename}...")
        try:
            # Set a User-Agent header so GitHub doesn't block the automated request
            opener = urllib.request.build_opener()
            opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
            urllib.request.install_opener(opener)
            
            urllib.request.urlretrieve(url, filename)
            print(f"[SUCCESS] {filename} saved successfully.")
        except Exception as e:
            print(f"[ERROR] Failed to download {filename}: {e}")
    else:
        print(f"[INFO] {filename} already exists in this directory. Skipping.")

print("\nAll model architecture dependencies are ready for Project 4!")