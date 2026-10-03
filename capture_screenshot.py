import os
from time import sleep, strftime
from pyautogui import screenshot

# Bu kodun çalıştığı dosyanın tam klasör yolunu alır
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "Images")

def take_screenshot(screenshot_dir):
    os.makedirs(screenshot_dir, exist_ok=True)
    
    timestamp = strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(screenshot_dir, f"screenshot_{timestamp}.png")
    
    img = screenshot()
    img.save(filename)
    print(f"Kaydedildi -> {filename}")

# Her 5 saniyede bir ekran görüntüsü al
while True:
    take_screenshot(file_path)
    sleep(5)