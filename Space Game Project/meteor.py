import random

# Ekran boyutu
WIDTH = 400
HEIGHT = 500

# Oyuncu (uzay gemisi)
spaceship = Actor("spaceship")
spaceship.midbottom = (WIDTH // 2, HEIGHT - 10)

# Meteorlar listesi
meteors = []

# Puan ve oyun durumu
score = 0
game_over = False

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

def update():
    global game_over, score

    if game_over:
        return

    # Oyuncuyu sola-sağa hareket ettir
    if keyboard.left and spaceship.left > 0:
        spaceship.x -= 5
    if keyboard.right and spaceship.right < WIDTH:
        spaceship.x += 5

    # Meteorları güncelle
    for m in meteors:
        m.y += 4
        if m.colliderect(spaceship):
            game_over = True
        if m.top > HEIGHT:
            meteors.remove(m)
            score += 1

def spawn_meteor():
    x = random.randint(20, WIDTH - 20)
    m = Actor("meteor")
    m.pos = (x, 0)
    meteors.append(m)




# Her 1 saniyede bir meteor üret
clock.schedule_interval(spawn_meteor, 1.0)# Write your code here :-)
