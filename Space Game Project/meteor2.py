import random
import math

# Ekran boyutu
WIDTH = 400
HEIGHT = 600

# Oyuncu (uzay gemisi)
spaceship = Actor("spaceship")
spaceship.midbottom = (WIDTH // 2, HEIGHT - 10)

# Asteroidler listesi
asteroids = []

# Puan ve oyun durumu
score = 0
game_over = False
asteroid_speed = 2  # Asteroidlerin hızının başlangıcı

# Oyun sıfırlama fonksiyonu
def restart_game():
    global spaceship, asteroids, score, game_over, asteroid_speed
    spaceship = Actor("spaceship")
    spaceship.midbottom = (WIDTH // 2, HEIGHT - 10)
    asteroids = []
    score = 0
    game_over = False
    asteroid_speed = 2

def draw():
    screen.clear()
    if not game_over:
        spaceship.draw()
        for a in asteroids:
            a.draw()
        screen.draw.text(f"Score: {score}", (10, 10), fontsize=30, color="white")
    else:
        screen.draw.text("GAME OVER", center=(WIDTH//2, HEIGHT//2), fontsize=60, color="red")
        screen.draw.text(f"Final Score: {score}", center=(WIDTH//2, HEIGHT//2 + 50), fontsize=40, color="white")
        screen.draw.text("Click to Restart", center=(WIDTH//2, HEIGHT//2 + 100), fontsize=30, color="green")

def update():
    global game_over, score, asteroid_speed

    if game_over:
        return

    # Oyuncuyu sola-sağa hareket ettir
    if keyboard.left and spaceship.left > 0:
        spaceship.x -= 5
    if keyboard.right and spaceship.right < WIDTH:
        spaceship.x += 5

    # Asteroidleri güncelle ve uzay gemisine olan mesafeyi ve açıyı hesapla
    for a in asteroids:
        a.y += asteroid_speed
        if a.colliderect(spaceship):
            game_over = True
        if a.top > HEIGHT:
            asteroids.remove(a)
            score += 1

        # Asteroidler uzay gemisine doğru hareket etsin
        angle = a.angle_to(spaceship)  # Asteroidin gemiye olan açısını hesapla
        distance = a.distance_to(spaceship)  # Asteroid ile gemi arasındaki mesafeyi hesapla

        if distance > 100:  # Asteroid çok uzakta değilse
            # Asteroid, gemiye doğru hareket etsin
            a.x += 1.5 * math.cos(math.radians(angle))
            a.y += 1.5 * math.sin(math.radians(angle))

    # Asteroid hızını zamanla artır
    if score % 10 == 0 and asteroid_speed < 5:  # Her 10 puanda hız artar
        asteroid_speed += 0.5

def spawn_asteroid():
    x = random.randint(20, WIDTH - 20)
    a = Actor("meteor")
    a.pos = (x, 0)
    asteroids.append(a)

# Her 1 saniyede bir asteroid üret
clock.schedule_interval(spawn_asteroid, 1.0)

# Fare tıklama olayında asteroidleri yok etme
def on_mouse_down(pos):
    global score
    if not game_over:
        # Asteroidlere tıklayarak yok et
        for a in asteroids[:]:
            if a.collidepoint(pos):
                asteroids.remove(a)
                score += 5  # Her asteroid yok edildikçe puan ekle
    else:
         # Eğer oyun bitmişse ve "Yeniden Oyna" yazısına tıklanmışsa, oyunu yeniden başlat
        if (WIDTH//2 - 150 < pos[0] < WIDTH//2 + 150) and (HEIGHT//2 + 80 < pos[1] < HEIGHT//2 + 120):
            restart_game()# Write your code here :-)
# Write your code here :-)
