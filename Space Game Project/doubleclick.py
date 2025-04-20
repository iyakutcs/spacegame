#pgzero'da çift tıklama olayını ele almak, on_mouse_down fonksiyonunu kullanarak gerçekleştirilebilir; bu fonksiyonla, ardışık fare tıklamaları arasındaki süreyi izleyebilir ve bunların çift tıklama olup olmadığını belirleyebiliriz.
import time
import random
# Ekran boyutu
WIDTH = 400
HEIGHT = 600

# Başlangıç renk ve zaman değişkenleri
color = (255, 0, 0)  # Kırmızı
last_click_time = 0  # Son tıklama zamanı
double_click_time_limit = 0.3  # 0.3 saniye içinde iki tıklama kabul edilir

# Rect (dikdörtgen) şekli
rect = Rect(150, 250, 100, 100)

def draw():
    screen.clear()
    screen.draw.filled_rect(rect, color)  # Dikdörtgeni çiz
    screen.draw.text("Double Click to Change Color", (10, 10), fontsize=20, color="white")

def on_mouse_down(pos):
    global last_click_time, color

    current_time = time.time()

    # Eğer son tıklama ile şu anki tıklama arasındaki fark 0.3 saniye ise, bu bir çift tıklama
    if current_time - last_click_time <= double_click_time_limit:
        # Çift tıklama olduğunda renk değiştir
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    last_click_time = current_time  # Son tıklama zamanını güncell# Write your code here :-)
