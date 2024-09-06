import pygame, random, math, sys
from pygame import mixer


def main():
    main_menu()


def main_menu():
    # Initialise Pygame
    pygame.init()

    # Create Space Invaders Window
    screen = display_window()

    # Opens the Space Invaders Lobby
    running = True
    while running:
        # Background and check for events
        background = pygame.image.load("space-invaders-background.png")
        screen.blit(background, (0, 0))

        # Displays Main menu and options text
        menu_font = pygame.font.Font("freesansbold.ttf", 45)
        menu_text = menu_font.render("Main Menu", True, (255, 255, 255))
        play_text = menu_font.render("1. Play", True, (255, 255, 255))
        lb_text = menu_font.render("2. Leaderboard", True, (255, 255, 255))
        exit_text = menu_font.render("3. Exit", True, (255, 255, 255))
        screen.blit(menu_text, (260, 120))
        screen.blit(play_text, (220, 200))
        screen.blit(lb_text, (220, 280))
        screen.blit(exit_text, (220, 360))

        # Update Pygame Display
        pygame.display.update()

        # Checks for events like key presses and press exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game(screen)
                    running = False
                if event.key == pygame.K_2:
                    lb = leaderboard(screen)
                    running = False
                if event.key == pygame.K_3:
                    running = False
    sys.exit()


def game(screen):

    # Player Location
    player_x = 370
    player_y = 480
    player_x_change = 0

    # Enemies
    number_of_enemies = 6
    enemy_x = []
    enemy_y = []
    enemy_x_change = []
    enemy_y_change = []
    for _ in range(number_of_enemies):
        enemy_x.append(random.randint(0, 735))
        enemy_y.append(random.randint(50, 150))
        enemy_x_change.append(4)
        enemy_y_change.append(40)

    # Bullet Location (bullet_status: ready = can't see bullet on screen, fire = bullet moving on screen)
    bullet_x = 370
    bullet_y = 440
    bullet_x_change = 0
    bullet_y_change = 10
    bullet_status = "ready"

    # Score
    score = 0
    score_x = 10
    score_y = 10
    show_text = True

    running = True
    while running:
        # Update Background Continuously
        background = pygame.image.load("space-invaders-background.png")
        screen.blit(background, (0, 0))
        # Check for Key Presses For player movement or Window exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player_x_change = -5
                if event.key == pygame.K_d:
                    player_x_change = 5
                if event.key == pygame.K_SPACE and bullet_status == "ready":
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.set_volume(0.2)
                    bullet_sound.play()
                    bullet_x = player_x
                    bullet_status = fire_bullet(screen, bullet_x, bullet_y)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    player_x_change = 0

        # check for player boundaries so doesn't go out of bounds
        if player_x <= 0:
            player_x = 0
        if player_x >= 736:
            player_x = 735

        for i in range(number_of_enemies):
            # Game Over
            if enemy_y[i] > 440:
                for j in range(number_of_enemies):
                    enemy_y[j] = 2000
                    screen.blit(background, (0, 0))
                    game_over(screen, score)

            # check for enemy boundaries and moves down if hits a boundary and updates movement of enemy
            if enemy_x[i] <= 0:
                enemy_x_change[i] = 4
                enemy_y[i] += enemy_y_change[i]
            if enemy_x[i] >= 736:
                enemy_x_change[i] = -4
                enemy_y[i] += enemy_y_change[i]
            enemy_x[i] += enemy_x_change[i]
            enemy(screen, enemy_x[i], enemy_y[i])

            # Collision between player and enemy
            collision = detect_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
            if collision and bullet_status == "fire":
                bullet_y = 440
                bullet_status = "ready"
                kill_sound = mixer.Sound("explosion.wav")
                kill_sound.set_volume(0.1)
                kill_sound.play()
                enemy_x[i] = random.randint(0, 735)
                enemy_y[i] = random.randint(50, 150)
                score += 1

        # Updates Movement for player
        player_x += player_x_change
        player(screen, player_x, player_y)

        # Bullet Movement
        if bullet_status == "fire":
            fire_bullet(screen, bullet_x, bullet_y)
            bullet_y -= bullet_y_change
        if bullet_y <= 0:
            bullet_y = 440
            bullet_status = "ready"

        # Call Score Whilst running
        if show_text:
            show_score(screen, score_x, score_y, score)

        # Updates Pygame Display
        pygame.display.update()


def display_window():
    # Creates Pygame Space Invaders Window (setting window caption, window icon, music and sound effects)
    mixer.music.load("background.wav")
    mixer.music.set_volume(0.1)
    mixer.music.play(-1)
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Space Invaders")
    icon = pygame.image.load("space-invaders.png")
    pygame.display.set_icon(icon)
    return screen


def player(screen, x, y):
    # Displays Player and Updated Movement of player
    player_image = pygame.image.load("player.png")
    screen.blit(player_image, (x, y))


def enemy(screen, x, y):
    # Displays enemies and Updated Movement of enemies
    enemy_image = pygame.image.load("enemy.png")
    screen.blit(enemy_image, (x, y))


def fire_bullet(screen, x, y):
    # Displays Bullet When Fired
    bullet_status = "fire"
    bullet_image = pygame.image.load("bullet.png")
    screen.blit(bullet_image, (x + 12, y))
    return bullet_status


def detect_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    # Checks whether a bullet has collided with an enemy
    #'distance' variable is the distance between coordinates of enemy and bullet, using the formula
    distance = math.sqrt(
        (math.pow(enemy_x - bullet_x, 2)) + (math.pow(enemy_y - bullet_y, 2))
    )
    if distance < 27:
        return True
    else:
        return False


def show_score(screen, x, y, score):
    # Displays the score on screen
    score_font = pygame.font.Font("freesansbold.ttf", 30)
    show_score = score_font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(show_score, (x, y))


def game_over(screen, score):
    # Displays game over texts and shows final score as well as an input box for username
    show_score(screen, 340, 310, score)
    game_over_font = pygame.font.Font("freesansbold.ttf", 40)
    to_menu_font = pygame.font.Font("freesansbold.ttf", 25)
    to_menu_text = to_menu_font.render(
        "Press 1 to Return to Menu:", True, (255, 255, 255)
    )
    text = game_over_font.render("Game Over!", True, (255, 255, 255))
    screen.blit(text, (295, 270))
    screen.blit(to_menu_text, (240, 100))
    user_input = ""
    input_box = pygame.Rect(290, 400, 220, 50)
    box_color = pygame.Color("black")
    active = True
    while active:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    main_menu()
                    active = False
                if event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                if event.key == pygame.K_RETURN and user_input:
                    submitted = submit_score(score, user_input)
                    main_menu()
                    active = False
                elif event.key != pygame.K_BACKSPACE and event.key != pygame.K_RETURN:
                    user_input += event.unicode.upper()
        pygame.draw.rect(screen, box_color, input_box)
        display_box = game_over_font.render(user_input, True, (255, 255, 255))
        screen.blit(display_box, (305, 405))
        input_box.w = max(100, display_box.get_width() + 20)
    pygame.quit()


def leaderboard(screen):
    # Used to Display Leaderboard from leaderboard file
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    main_menu()

        # Resets Background
        background = pygame.image.load("space-invaders-background.png")
        screen.blit(background, (0, 0))
        lb_font = pygame.font.Font("freesansbold.ttf", 60)
        leaderboard_text = lb_font.render("LEADERBOARD", True, (255, 255, 255))
        screen.blit(leaderboard_text, (160, 20))

        # Displays top 10 scores from "leaderboard.csv" file
        text_x = 300
        text_y = 120
        i = 1
        lb_font = pygame.font.Font("freesansbold.ttf", 25)
        return_text = lb_font.render("Press 1 to return to menu", True, (255, 255, 255))
        screen.blit(return_text, (230, 75))
        with open("leaderboard.csv") as file:
            for line in file:
                name, score = line.rstrip().split(",")
                text = lb_font.render(
                    f"{i}.  {score}  -  {name}", True, (255, 255, 255)
                )
                screen.blit(text, (text_x, text_y))
                i += 1
                text_y += 45

        # Updates Display
        pygame.display.update()


def submit_score(score, user_input):
    # Used to submit score to leaderboard
    with open("leaderboard.csv", "a") as file:
        file.write(f"{user_input},{score}\n")

    leaders = []
    with open("leaderboard.csv") as file:
        for line in file:
            name, scored = line.rstrip().split(",")
            leader = {"name": name, "score": scored}
            leaders.append(leader)

    lines = 0
    with open("leaderboard.csv", "w") as file:
        file.close()

    for leader in sorted(
        leaders, key=lambda leader: int(leader["score"]), reverse=True
    ):
        lines += 1
        with open("leaderboard.csv", "a") as file:
            if lines <= 10:
                file.write(f"{leader['name']},{leader['score']}\n")
    return f"{name},{score}"


if __name__ == "__main__":
    main()