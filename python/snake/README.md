# Неделя 6, проектная работа
## **Тема**: Объектно-ориентированное программирование на Python 
### Студентки группы ПИЖ-б-о-23-1(1) Алдабаевой Виктории Владимировны
#### Репозиторий Git: https://github.com/Pharrower/pizh2311_Aldabaeva <br><br>

*Задание:*  
Необходимо написать на Python классическую игру
"Змейка".
Код состоит из нескольких основных частей:
1. Инициализация Pygame и настройка игрового окна. В начале программы настраиваются основные параметры игргры, такие как размер и цвет фона.
2. Классы игровых объектов:
    - GameObject - это базовый класс, от которого наследуются другие игровые объекты.
    - Snake - класс, унаследованный от GameObject, описывающий змейку и её поведение. Этот класс управляет её движением, отрисовкой, а также обрабатывает действия пользователя.
    - Apple - класс, унаследованный от GameObject, описывающий яблоко и действия с ним.
3. Логика игры:
    - сначала создаются необходимые объекты;
    - в основном цикле происходит обновление состояний объектов;
    - если змейка съедает яблоко, её размер увеличивается на один сегмент, а яблоко перемещается на новую позицию;
    - при столкновении змейки с самой собой игра начинается заново.
4. Отрисовка объектов. В каждой итерации цикла змейка меняет своё положение на игровом поле на одну ячейку. Координаты для нового элемента определяются в зависимости от направления движения.
5. Обновление экрана. На каждой итерации цикла while программа вычисляет новое состояние игрового поля: определяет координаты каждого семента змейки и, при необходимости, координаты яблока, а также проверяет, не столкнулась ли змкейка сама с собой.

    Задание:
    - Напишите классы GameObject, Apple и Snake, а также их атрибуты и методы.
    - Допишите основной цикл иры и функции main().
    - Всё, к чему можно написать докстринги, должно содержать докстринги.
    - Код должен соответствовать PEP 8.

*Ответ:* 

*the_snake.py*
```python
"""Модуль игры 'Змейка' с использованием библиотеки Pygame."""

from random import choice, randint
import pygame
import sys
from typing import Dict, Tuple, Set, Optional

# Константы для размеров поля и сетки:
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
CENTER_POSITION = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Направления движения:
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Цвета:
BOARD_BACKGROUND_COLOR = (0, 0, 0)
BORDER_COLOR = (93, 216, 228)
APPLE_COLOR = (255, 0, 0)
SNAKE_COLOR = (0, 255, 0)

# Скорости:
SPEEDS = {'normal': 10, 'fast': 20, 'slow': 5}
DEFAULT_SPEED = 'normal'

# Настройка окна:
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Змейка')
clock = pygame.time.Clock()

# Все возможные ячейки поля
ALL_CELLS = {(x * GRID_SIZE, y * GRID_SIZE)
             for x in range(GRID_WIDTH)
             for y in range(GRID_HEIGHT)}

# Словарь для управления направлениями
DIRECTION_MAP = {
    (pygame.K_UP, RIGHT): UP, (pygame.K_UP, LEFT): UP,
    (pygame.K_DOWN, RIGHT): DOWN, (pygame.K_DOWN, LEFT): DOWN,
    (pygame.K_LEFT, UP): LEFT, (pygame.K_LEFT, DOWN): LEFT,
    (pygame.K_RIGHT, UP): RIGHT, (pygame.K_RIGHT, DOWN): RIGHT
}


class GameObject:
    """Базовый класс для игровых объектов."""

    def __init__(self, position: Tuple[int, int] = CENTER_POSITION,
                 body_color: Tuple[int, int, int] = None):
        """
        Инициализация игрового объекта.

        Args:
            position: Начальная позиция объекта.
            body_color: Цвет объекта.
        """
        self.position = position
        self.body_color = body_color
        self.last = None

    def draw_cell(self, position: Tuple[int, int], color: Tuple[int, int, int]):
        """
        Отрисовывает одну ячейку объекта.

        Args:
            position: Позиция ячейки.
            color: Цвет ячейки.
        """
        rect = pygame.Rect(position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

    def draw(self):
        """Абстрактный метод для отрисовки объекта."""
        raise NotImplementedError("Метод draw должен быть реализован в подклассе")


class Apple(GameObject):
    """Класс, описывающий яблоко."""

    def __init__(self):
        """Инициализация яблока со случайной позицией."""
        super().__init__(body_color=APPLE_COLOR)
        self.randomize_position()

    def randomize_position(self, occupied_positions: Set[Tuple[int, int]] = None):
        """
        Устанавливает случайное положение яблока на свободной ячейке.

        Args:
            occupied_positions: Множество занятых позиций.
        """
        occupied = occupied_positions if occupied_positions else set()
        available_cells = ALL_CELLS - occupied
        if available_cells:
            self.position = choice(tuple(available_cells))

    def draw(self):
        """Отрисовывает яблоко."""
        self.draw_cell(self.position, self.body_color)


class Snake(GameObject):
    """Класс, описывающий змейку."""

    def __init__(self):
        """Инициализация змейки в начальном состоянии."""
        super().__init__(body_color=SNAKE_COLOR)
        self.reset()
        self.high_score = 0

    def reset(self):
        """Сбрасывает змейку в начальное состояние."""
        self.positions = [CENTER_POSITION]
        self.direction = RIGHT
        self.next_direction = None
        self.length = 1
        self.last = None

    def update_direction(self):
        """Обновляет направление движения змейки."""
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def get_head_position(self) -> Tuple[int, int]:
        """
        Возвращает позицию головы змейки.

        Returns:
            Координаты головы змейки.
        """
        return self.positions[0]

    def move(self):
        """Обновляет позицию змейки."""
        head = self.get_head_position()
        x, y = self.direction
        new_head = (
            (head[0] + x * GRID_SIZE) % SCREEN_WIDTH,
            (head[1] + y * GRID_SIZE) % SCREEN_HEIGHT
        )

        self.positions.insert(0, new_head)
        if len(self.positions) > self.length:
            self.last = self.positions.pop()
        else:
            self.last = None

    def check_self_collision(self) -> bool:
        """
        Проверяет столкновение змейки с собой.

        Returns:
            True если произошло столкновение, иначе False.
        """
        return len(self.positions) > 4 and self.get_head_position() in self.positions[1:]

    def draw(self):
        """Отрисовывает змейку."""
        # Отрисовка головы
        self.draw_cell(self.positions[0], self.body_color)

        # Отрисовка тела (кроме головы)
        for position in self.positions[1:]:
            self.draw_cell(position, self.body_color)

        # Затирание последнего сегмента
        if self.last:
            pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR,
                           pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE)))


def handle_keys(snake: Snake, speed_mode: str) -> str:
    """
    Обрабатывает нажатия клавиш.

    Args:
        snake: Объект змейки.
        speed_mode: Текущий режим скорости.

    Returns:
        Новый режим скорости.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_q:
                speed_mode = 'slow'
            elif event.key == pygame.K_w:
                speed_mode = 'normal'
            elif event.key == pygame.K_e:
                speed_mode = 'fast'
            else:
                # Обработка направлений через словарь
                new_direction = DIRECTION_MAP.get((event.key, snake.direction))
                if new_direction:
                    snake.next_direction = new_direction
    return speed_mode


def main():
    """Основной игровой цикл."""
    snake = Snake()
    apple = Apple()
    speed_mode = DEFAULT_SPEED

    while True:
        clock.tick(SPEEDS[speed_mode])

        # Обновление заголовка окна
        pygame.display.set_caption(
            f'Змейка | Рекорд: {snake.high_score} | Текущий: {snake.length} | '
            f'Скорость (Q, W, E): {speed_mode} ({SPEEDS[speed_mode]})'
        )

        speed_mode = handle_keys(snake, speed_mode)
        snake.update_direction()
        snake.move()

        # Проверка на съедение яблока
        if snake.get_head_position() == apple.position:
            snake.length += 1
            snake.high_score = max(snake.high_score, snake.length)
            apple.randomize_position(set(snake.positions))

        # Проверка на столкновение с собой
        if snake.check_self_collision():
            snake.reset()

        # Отрисовка
        screen.fill(BOARD_BACKGROUND_COLOR)
        snake.draw()
        apple.draw()
        pygame.display.update()


if __name__ == '__main__':
    main()

```
