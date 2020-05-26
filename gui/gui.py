import sys
from multiprocessing import Queue

import pygame

from . import const


def visualize_search(size: int, event_queue: Queue = None):
    def get_optimal_tile_size(grid_size, initial_tile_size):
        info = pygame.display.Info()
        tile_size = initial_tile_size
        # make tiles smaller until all of them will fit into the screen
        while tile_size * grid_size > info.current_h or tile_size * grid_size > info.current_w:
            tile_size = int(tile_size * 0.75)

        return tile_size

    def window_init(tile_size, tiles_count):
        surface = pygame.display.set_mode(
            (tile_size * tiles_count, tile_size * tiles_count),
            flags=pygame.SCALED | pygame.RESIZABLE
        )
        pygame.display.set_caption('Eight Queens Puzzle Visualization')
        return surface

    def draw_grid(surface, tiles_count):
        def get_color_for_tile(row: int, col: int):
            return const.COLOR_TILE_2 if (row + col) % 2 == 0 else const.COLOR_TILE_1

        for row in range(tiles_count):
            for col in range(tiles_count):
                tile = pygame.Rect(row * const.TILE_SIZE, col * const.TILE_SIZE, const.TILE_SIZE, const.TILE_SIZE)
                pygame.draw.rect(surface, get_color_for_tile(row, col), tile)

    def draw_set(surface, tiles_count, tile_size, board):
        draw_grid(surface, tile_size)
        [mark_field(surface, row, col, tile_size) for col in range(tiles_count) for row in range(tiles_count) if
         board[row][col]]

    def mark_field(surface, row, col, tile_size):
        x_pos = col * tile_size + tile_size / 2
        y_pos = row * tile_size + tile_size / 2
        pygame.draw.circle(surface, const.COLOR_MARKER, (x_pos, y_pos), const.MARKER_RADIUS)
        pygame.display.update()

    def game_loop(surface, tiles_count, tile_size):
        poll_events = True
        first_drawn = False
        sets = []
        i = 0

        draw_grid(surface, tile_size)

        while True:
            event = pygame.event.poll() if poll_events else pygame.event.wait()
            if event.type == pygame.NOEVENT:
                if event_queue is not None and event_queue.qsize() > 0:
                    new_event = event_queue.get()
                    if 'board' in new_event:
                        if first_drawn:
                            new_set = new_event.get('board')
                            if new_set not in sets:  # discard improperly removed items
                                sets.append(new_event.get('board'))
                        else:
                            draw_set(surface, tiles_count, tile_size, new_event.get('board'))
                            first_drawn = True
                    elif 'state' in new_event:
                        if new_event['state'] == 'finished':
                            poll_events = False
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_LEFT:
                    if i > 0 and len(sets) > 0:
                        i -= 1
                        draw_set(surface, tiles_count, tile_size, sets[i])
                elif event.key == pygame.K_RIGHT:
                    if i < len(sets) - 1:
                        i += 1
                        draw_set(surface, tiles_count, tile_size, sets[i])

    pygame.display.init()
    tile_size = get_optimal_tile_size(size, const.TILE_SIZE)
    surface = window_init(tile_size, size)
    game_loop(surface, size, tile_size)
