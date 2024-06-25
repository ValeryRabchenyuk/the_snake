from random import randint

import pygame


SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

BOARD_BACKGROUND_COLOR = (0, 0, 0)

BORDER_COLOR = (93, 216, 228)

APPLE_COLOR = (255, 0, 0)

SNAKE_COLOR = (0, 255, 0)

SPEED = 20

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

pygame.display.set_caption('Змейка')

clock = pygame.time.Clock()


class GameObject:
    """Родительский класс"""

    def __init__(self):
        """Инициализация"""
        self.position = ((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))
        self.body_color = None

    def draw(self):
        """Абстрактный метод для переопределения"""
        raise NotImplementedError

    @staticmethod
    def draw_rect(position, color):
        """Отрисовка прямоугольника"""
        rect = (pygame.Rect(position, (GRID_SIZE, GRID_SIZE)))
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)


class Apple(GameObject):
    """Дочерний класс"""

    def __init__(self, body_color=APPLE_COLOR):
        """Инициализация"""
        super().__init__()
        self.body_color = body_color
        self.randomize_position([])

    def randomize_position(self, snake_positions):
        """Случайное положение яблока"""
        check_position = True
        position = None
        while check_position:
            position = (
                randint(0, GRID_WIDTH) * GRID_SIZE,
                randint(0, GRID_HEIGHT) * GRID_SIZE,
            )
            if position not in snake_positions:
                check_position = False
        self.position = position

    def draw(self):
        """Отрисовка яблока (прекод)"""
        Apple.draw_rect(self.position, APPLE_COLOR)


class Snake(GameObject):
    """Дочерний класс"""

    def __init__(self, body_color=SNAKE_COLOR):
        """Инициализация"""
        super().__init__()
        self.length = 1
        self.positions = [self.position]
        self.direction = RIGHT
        self.next_direction = None
        self.body_color = body_color
        self.last = None

    def update_direction(self):
        """Обновление направления (прекод)"""
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def get_head_position(self):
        """Возвращает позицию головы"""
        return self.positions[0]

    def get_positions(self):
        """Возвращает координаты змеи"""
        return self.positions

    def move(self):
        """Обновление позиции"""
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
        """Отрисовка змеи (прекод)"""
        for position in self.positions[:-1]:
            Snake.draw_rect(position, SNAKE_COLOR)

        # Отрисовка головы змейки
        Snake.draw_rect(self.positions[0], SNAKE_COLOR)

        # Затирание последнего сегмента
        if self.last:
            last_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)

    def reset(self):
        """Сброс змеи"""
        self.leght = 1
        self.positions = [self.position]
        self.direction = RIGHT
        self.next_direction = None
        self.last = None
        screen.fill(BOARD_BACKGROUND_COLOR)


def handle_keys(game_object):
    """Обработка нажатия клавиш (прекод)"""
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
    """Главный цикл игры"""
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
            apple.randomize_position(snake.get_positions())

        # Обновление экрана
        pygame.display.update()

        # Завершение игры
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break


if __name__ == '__main__':
    main()
