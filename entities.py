import pygame

# COLORS
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

"""
WE ASUME THAT O OPENS THE GAME
"""


class Board:
    pygame.font.init()

    def __init__(self, screen, x, y, width, height):
        # SET BOARD VARIABLES
        self.values = ["" for a in range(9)]
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.value_counter = 0
        # Paddings are used to know where to draw the lines X´s and O´s and the font size to be used
        self.x_padding = width/3
        self.y_padding = height/3
        self.SCREEN_LINE_RATIO = 50
        # Text related
        self.font = pygame.font.Font("freesansbold.ttf", int(min(self.x_padding, self.y_padding)))

        # Start a new board
        self.draw_table()

    def draw_table(self):
        """ FILLS THE BACKGROUND AND DRAWS THE 2 VERTICAL AND 2 HORIZONTAL LINES OF THE TIC TAC TOE BOARD"""
        self.screen.fill(BLACK)

        vertical_line_1 = pygame.Rect(self.x + 1 * self.x_padding - self.width/(2 * self.SCREEN_LINE_RATIO), self.y,
                                      self.width/self.SCREEN_LINE_RATIO, self.height)

        vertical_line_2 = pygame.Rect(self.x + 2 * self.x_padding - self.width/(2 * self.SCREEN_LINE_RATIO), self.y,
                                      self.width/self.SCREEN_LINE_RATIO, self.height)

        horizontal_line_1 = pygame.Rect(self.x, self.y + 1 * self.y_padding - self.height/(2 * self.SCREEN_LINE_RATIO),
                                        self.width, self.height/self.SCREEN_LINE_RATIO)

        horizontal_line_2 = pygame.Rect(self.x, self.y + 2 * self.y_padding - self.height/(2 * self.SCREEN_LINE_RATIO),
                                        self.width, self.height/self.SCREEN_LINE_RATIO)

        for line in [horizontal_line_1, horizontal_line_2, vertical_line_1, vertical_line_2]:
            pygame.draw.rect(self.screen, RED, line)

    def update_square(self, index):
        """
        UPDATES ONE SPECIFIC SQUARE AND DRAWS IT. RETURNS A BOOL REPRESENTING WHETHER THE CHANGE WAS CORRECTLY MADE
        """
        if not self.values[index]:
            self.value_counter += 1
            self.value_counter %= 2
            self.values[index] = ["X", "O"][self.value_counter]

            rendered_text = self.font.render(self.values[index], True, WHITE)

            x = (index % 3) * self.x_padding + (self.x_padding - rendered_text.get_width())/2
            y = (index // 3) * self.y_padding + (self.y_padding - rendered_text.get_height())/2

            self.screen.blit(rendered_text, (x, y))
            pygame.display.update()
            # If the change was correctly made, returns True
            return True
        else:
            # If the square could not de updated returns False
            return False

    def draw_symbols(self):
        """ RUNS draw_table() AND DRAWS ALL OF THE SYMBOLS INSIDE THE TABLE """
        self.draw_table()
        for index, item in enumerate(self.values):
            rendered_text = self.font.render(self.values[index], True, WHITE)

            x = (index % 3) * self.x_padding + (self.x_padding - rendered_text.get_width()) / 2
            y = (index // 3) * self.y_padding + (self.y_padding - rendered_text.get_height()) / 2

            self.screen.blit(rendered_text, (x, y))
            pygame.display.update()

    def reset(self):
        """
        VACATES BOARD CONTENTS AND DRAWS IT AGAIN
        """
        self.values = ["" for a in range(9)]
        self.value_counter = 0
        self.draw_symbols()

    def check_win(self):
        """CHECKS IF A PLAYER HAS WON THE GAME"""
        # INDEXES OF THE VALUES THAT HAVE TO BE EQUAL TO WIN
        # 0, 1, 2
        # 3, 4, 5
        # 6, 7, 8
        # 0, 3, 6
        # 1, 4, 7
        # 2, 5, 8
        # 0, 4, 8
        # 2, 4, 6
        for line in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
            if self.values[line[0]] == self.values[line[1]] == self.values[line[2]] and self.values[line[0]] in ["X", "O"]:
                return True
        return False

    def check_full(self):
        """ CHECKS IF THE BOARD IS FULL"""
        for item in self.values:
            if not item:
                return False
        return True
