import random

# Ekran boyutu
WIDTH = 400
HEIGHT = 600

# Oyuncu (uzay gemisi)
spaceship = Actor("spaceship")
spaceship.midbottom = (WIDTH // 2, HEIGHT - 10)


# Meteorlar listesi
meteors = []

# Puan ve oyun durumu
score = 0
game_over = False
meteor_speed = 4  # Başlangıç meteor hızı

# Oyun sıfırlama fonksiyonu
def restart_game():
    global spaceship, meteors, score, game_over, meteor_speed
    spaceship = Actor("spaceship")
    spaceship.midbottom = (WIDTH // 2, HEIGHT - 10)
    meteors = []
    score = 0
    game_over = False
    meteor_speed = 4

def draw():
    screen.clear()
    if not game_over:
        spaceship.draw()
        for m in meteors:
            m.draw()
        screen.draw.text(f"Score: {score}", (10, 10), fontsize=30, color="white")
    else:
        screen.draw.text("GAME OVER", center=(WIDTH//2, HEIGHT//2), fontsize=60, color="red")
        screen.draw.text(f"Final Score: {score}", center=(WIDTH//2, HEIGHT//2 + 50), fontsize=40, color="white")
        screen.draw.text("Click to Restart", center=(WIDTH//2, HEIGHT//2 + 100), fontsize=30, color="green")

def update():
    global game_over, score, meteor_speed

    if game_over:
        return

    # Oyuncuyu sola-sağa hareket ettir
    if keyboard.left and spaceship.left > 0:
        spaceship.x -= 5
    if keyboard.right and spaceship.right < WIDTH:
        spaceship.x += 5

    # Meteorları güncelle
    for m in meteors:
        m.y += meteor_speed
        if m.colliderect(spaceship):
            game_over = True
        if m.top > HEIGHT:
            meteors.remove(m)
            score += 1

    # Meteor hızını zamanla artır
    if score % 10 == 0 and meteor_speed < 10:  # Her 10 puanda hız artar
        meteor_speed += 0.5

def spawn_meteor():
    x = random.randint(20, WIDTH - 20)
    m = Actor("meteor")
    m.pos = (x, 0)
    meteors.append(m)

# Her 1 saniyede bir meteor üret
clock.schedule_interval(spawn_meteor, 1.0)

# Fare tıklama olayında oyun sıfırlama
def on_mouse_down(pos):
    global game_over
    if game_over:
        # Eğer oyun bitmişse ve "Yeniden Oyna" yazısına tıklanmışsa, oyunu yeniden başlat
        if (WIDTH//2 - 150 < pos[0] < WIDTH//2 + 150) and (HEIGHT//2 + 80 < pos[1] < HEIGHT//2 + 120):
            restart_game()# Write your code here :-)
