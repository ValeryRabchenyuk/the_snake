from random import choice, randint

import pygame

# Константы для размеров поля и сетки:
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Направления движения:
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Цвет фона - черный:
BOARD_BACKGROUND_COLOR = (0, 0, 0)

# Цвет границы ячейки
BORDER_COLOR = (93, 216, 228)

# Цвет яблока
APPLE_COLOR = (255, 0, 0)

# Цвет змейки
SNAKE_COLOR = (0, 255, 0)

# Скорость движения змейки:
SPEED = 20

# Настройка игрового окна:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Заголовок окна игрового поля:
pygame.display.set_caption('Змейка')

# Настройка времени:
clock = pygame.time.Clock()


# Тут опишите все классы игры.
class GameObject:
    def __init__(self):                            
        self.position = ((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))
        self.body_color = None

    def draw(self):
        pass


class Apple(GameObject):

    def __init__(self, body_color=APPLE_COLOR):
        """ 1 метод — инициализация """                        #проверить body_color=APPLE_COLOR  MOZNO UBRAT'
        super().__init__()               #super.__init__(body_color=APPLE_COLOR)
        self.body_color = body_color                      #=APPLE_COLOR    BILO bez position arg 
        self.randomize_position()       

    def randomize_position(self):
        return (
            randint(0, GRID_WIDTH) * GRID_SIZE,
            randint(0, GRID_HEIGHT) * GRID_SIZE,
        )

    def draw(self):
        rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)


class Snake(GameObject):

    def __init__(self, body_color=SNAKE_COLOR):
        """ 1 метод — инициализация """
        super().__init__()
        self.leght = 1  # 1 атрибут — длинна
        self.positions = self.position  # 2 атрибут — начало — центр экрана.
        self.direction = RIGHT  # 3 атрибут — направление движения
        self.next_direction = None  # 4 атрибут — след. направление
        self.body_color = body_color  # 5 атрибут — цвет

    def update_direction(self):
        """ 2 метод — обновление направления (из прекода) """
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def get_head_position(self):
        """ 3 метод — возвращает позицию головы """
        return self.posirtion[0]

    def move(self):
        """ 4 метод — обновление позиции """
        self.update_direction()
        head_position = self.get_head_position():
        x, y = self.direction
        new_head = (

        )


    # Метод draw класса Snake
    def draw(self):
        for position in self.positions[:-1]:
            rect = (pygame.Rect(position, (GRID_SIZE, GRID_SIZE)))
            pygame.draw.rect(screen, self.body_color, rect)
            pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

        # Отрисовка головы змейки
        head_rect = pygame.Rect(self.positions[0], (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, head_rect)
        pygame.draw.rect(screen, BORDER_COLOR, head_rect, 1)

        # Затирание последнего сегмента
        if self.last:
            last_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)


        
    def reset(self): 
        pass#сбрасывает змейку в начальное состояние после столкновения с собой.   

def main():
    """Главный цикл игры"""
    # Инициализация PyGame:
    pygame.init()
    # Тут нужно создать экземпляры классов.
    apple = Apple()
    apple.draw()                         #PROVERIT'   PRO KAKOI-TO CICLE I NE DVIGAUSH APPLE


def handle_keys(game_object):                 # BILO (game_object)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game_object.direction != DOWN:
                game_object.next_direction = UP
            elif event.key == pygame.K_DOWN and game_object.direction != UP:
                game_object.next_direction = DOWN
            elif event.key == pygame.K_LEFT and game_object.direction != RIGHT:
                game_object.next_direction = LEFT
            elif event.key == pygame.K_RIGHT and game_object.direction != LEFT:
                game_object.next_direction = RIGHT

    while True:
        clock.tick(SPEED)
        handle_keys(Snake) #bilo apple
        Apple.draw()
        Snake.draw()
        pygame.display.updates()

        # Тут опишите основную логику игры.
        # ...
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break

        #pygame.display.updates()   To li zdec' To li vishe
        

if __name__ == '__main__':
    main()





# Функция обработки действий пользователя
# def handle_keys(game_object):
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             raise SystemExit
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP and game_object.direction != DOWN:
#                 game_object.next_direction = UP
#             elif event.key == pygame.K_DOWN and game_object.direction != UP:
#                 game_object.next_direction = DOWN
#             elif event.key == pygame.K_LEFT and game_object.direction != RIGHT:
#                 game_object.next_direction = LEFT
#             elif event.key == pygame.K_RIGHT and game_object.direction != LEFT:
#                 game_object.next_direction = RIGHT


