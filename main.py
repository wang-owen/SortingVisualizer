import sys, pygame, random

pygame.init()


class SortingVisualizer:
    GRAY = 128, 128, 128
    C1 = 255, 225, 148
    C2 = 163, 207, 167
    C3 = 247, 220, 236

    BG = GRAY
    GRADIENT = [C1, C2, C3]

    def __init__(self, width, height, data):
        self.width = width
        self.height = height
        self.set_data(data)

    def set_data(self, data):
        self.side_padding = 75
        self.top_padding = 100

        self.data = data
        self.max = max(data)
        self.min = min(data)
        self.bar_width = round((self.width - self.side_padding * 2) / len(data))
        self.bar_height = round(
            (self.height - self.top_padding) / (self.max - self.min)
        )
        self.first_bar = round(self.side_padding)


def generate_data(n, max, min):
    data = []
    for _ in range(n):
        data.append(random.randint(min, max))

    return data


def blit(app):
    app.window.fill(app.BG)
    blit_data(app)
    pygame.display.flip()


def blit_data(app):
    data = app.data
    BLACK = 0, 0, 0
    # iterate through data list
    for i, val in enumerate(data):
        # determine which x and y coordinates to draw bar
        x = app.first_bar + i * app.bar_width
        y = app.height - (val * app.bar_height)
        # determine bar color
        color = app.GRADIENT[i % 3]

        pygame.draw.rect(app.window, color, (x, y, app.bar_width, app.height))

        # bar borders WIP
        # pygame.draw.line(app.window, BLACK, (x, y), (x, app.height), 1)
        # pygame.draw.line(app.window, BLACK, (x, y), (x, app.bar_width), 1)


def main():
    run = True
    clock = pygame.time.Clock()
    res = width, height = 1000, 1000

    pygame.display.set_mode(res, pygame.RESIZABLE)
    pygame.display.set_caption("Sorting Visualizer")

    n = 100
    max = 100
    min = 0

    data = generate_data(n, max, min)
    app = SortingVisualizer(width, height, data)

    while run:
        clock.tick(60)
        blit(app)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    data = generate_data(n, max, min)
                    app.set_data(data)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
