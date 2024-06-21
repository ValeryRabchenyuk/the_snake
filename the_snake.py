from random import randint

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
SPEED = 10

# Настройка игрового окна:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Заголовок окна игрового поля:
pygame.display.set_caption('Змейка')

# Настройка времени:
clock = pygame.time.Clock()


# Тут опишите все классы игры.
class GameObject:
    """ Родительский класс """
    def __init__(self):
        """ 1 метод — инициализация """
        self.position = ((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))
        self.body_color = None

    def draw(self):
        """ Абстрактный метод для переопределения  """
        pass


class Apple(GameObject):
    """ Дочерний класс """
    def __init__(self, body_color=APPLE_COLOR):
        """ 1 метод — инициализация """
        super().__init__()
        self.body_color = body_color
        self.randomize_position()

    def randomize_position(self):
        """ 2 метод — случайное положение яблока """
        self.position = (
            randint(0, GRID_WIDTH) * GRID_SIZE,
            randint(0, GRID_HEIGHT) * GRID_SIZE,
        )

    def draw(self):
        """ 3 метод — отрисовка яблока (прекод) """
        rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)


class Snake(GameObject):
    """ Дочерний класс """
    def __init__(self, body_color=SNAKE_COLOR):
        """ 1 метод — инициализация """
        super().__init__()
        self.length = 1  # 1 атрибут — длинна
        self.positions = [self.position]  # 2 атрибут — начало — центр экрана
        self.direction = RIGHT  # 3 атрибут — направление движения
        self.next_direction = None  # 4 атрибут — след. направление
        self.body_color = body_color  # 5 атрибут — цвет
        self.last = None  # 6 атрибут — цвет позиция последнего сегмента

    def update_direction(self):
        """ 2 метод — обновление направления (прекод) """
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def get_head_position(self):
        """ 3 метод — возвращает позицию головы """
        return self.positions[0]

    def move(self):
        """ 4 метод — обновление позиции """
        self.update_direction()
        head_position = self.get_head_position()
        x, y = self.direction
        new_head = (
            (head_position[0] + x * GRID_SIZE) % SCREEN_WIDTH,
            (head_position[1] + y * GRID_SIZE) % SCREEN_HEIGHT
        )

        if new_head in self.positions[2:]:
            self.reset()
        else:
            self.positions = [new_head] + self.positions
            if len(self.positions) > self.length:
                self.last = self.positions.pop()

    def draw(self):
        """ 5 метод — отрисовка змеи (прекод) """
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
        """ 6 метод — сброс змеи """
        self.leght = 1
        self.positions = [self.position]
        self.direction = RIGHT
        self.next_direction = None
        self.last = None
        screen.fill(BOARD_BACKGROUND_COLOR)


def handle_keys(game_object):
    """ Обработка нажатия клавиш (прекод) """
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


def main():
    """ Главный цикл игры """
    # Инициализация PyGame:
    pygame.init()
    # Экземпляры классов
    snake = Snake()
    apple = Apple()
  
    while True:
        clock.tick(SPEED)
        handle_keys(snake)

        apple.draw()
        snake.draw()
        snake.move()

        # Поедание яблока
        if snake.get_head_position() == apple.position:
            snake.length += 1
            apple.randomize_position()

        # Обновление экрана
        pygame.display.update()

        # Завершение игры
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break


if __name__ == '__main__':
    main()
