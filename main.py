from entities import *
import pickle
import random
"""
WE ASUME THAT O OPENS THE GAME
"""


def load_bot(file_path):
    with open(file_path, "rb") as f:
        return pickle.load(f)


def start_new_game(bot):
    
    # SCREEN
    pygame.init()
    WIDTH = 653
    HEIGHT = 653
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("TIC TAC TOE BOT")
    FPS = 30
    CLOCK = pygame.time.Clock()

    # BOARD
    tablero = Board(screen, 0, 0, WIDTH, HEIGHT)

    pygame.display.update()
    # O opens the game
    player_symbol = random.choice(("X", "O"))
    player_turn = True
    if player_symbol != "O":
        player_turn = False
    
    # MAIN LOOP
    running = True
    while running:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    running = False
            if player_turn:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x, y = pygame.mouse.get_pos()
                        x = x // (WIDTH / 3)
                        y = y // (HEIGHT / 3)
                        index = x + 3*y
                        if tablero.update_square(int(index)):
                            # IF THE SQUARE WAS CORRECTLY CHANGED, IT IS THE BOT´S TURN
                            player_turn = False
        if not player_turn and not tablero.check_full():
            pygame.time.wait(random.randint(200, 400))
            response = bot[tuple(tablero.values)]
            tablero.update_square(response)
            player_turn = True

        if tablero.check_win():
            if not player_turn:
                print("YOU WIN!")
            else:
                print("YOU LOSE!")
            pygame.time.wait(1000)
            tablero.reset()

        elif tablero.check_full():
            print("TIE!")
            pygame.time.wait(1000)
            tablero.reset()

            

start_new_game(load_bot(input("Under which filepath was the dict pickled? : ")))