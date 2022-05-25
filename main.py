import sys, pygame, random

pygame.init()


class Application:
    # color palette
    C1 = 240, 249, 232
    C2 = 186, 228, 188
    C3 = 123, 204, 196
    C4 = 67, 162, 202
    C5 = 8, 104, 172
    COLORS = [C1, C2, C3, C4, C5]

    def __init__(self, window, res, BG):
        self.window = window
        self.BG = BG
        self.width = res[0]
        self.height = res[1]

    def generate_data(self, n, min, max):
        data = []
        for _ in range(n):
            data.append(random.randint(min, max))
        return data

    def init_data(self, data):
        side_padding = 5 * (self.width / len(data))
        top_padding = self.height / 5
        begin = side_padding

        self.min = min(data)
        self.max = max(data)
        bar_width = (self.width - side_padding * 2) // len(data)
        max_bar_height = self.height - top_padding

        self.window.fill(self.BG)

        # iterate through data and determine coordinates
        for i, val in enumerate(data):
            bar_height = round((self.height - top_padding) / (self.max - self.min))
            x = begin + i * bar_width
            y = self.height - (val * bar_height)
            bar_color = self.COLORS[i % 5]

            # draw data
            pygame.draw.rect(self.window, bar_color, (x, y, bar_width, self.height))
            # bar borders (WIP)
            # pygame.draw.line(window, BLACK)

        pygame.display.update()

    def bubble_sort(self, data):
        for i in range(len(data) - 1):
            for j in range(0, len(data) - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    # redraw
                    self.init_data(data)

    def selection_sort(self, data):
        for i in range(len(data)):
            min = i
            for j in range(i + 1, len(data)):
                if data[min] > data[j]:
                    min = j
            data[i], data[min] = data[min], data[i]
            # redraw chart
            self.init_data(data)

    def insertion_sort(self, data):
        for i in range(1, len(data)):
            key = data[i]
            temp = i - 1
            while temp >= 0 and key < data[temp]:
                data[temp + 1] = data[temp]
                temp -= 1
                # redraw chart
                self.init_data(data)
            data[temp + 1] = key

    def cocktail_sort(self, data):
        swapped = True
        start = 0
        end = len(data) - 1
        while swapped == True:
            swapped = False
            for i in range(end):
                if data[i] > data[i + 1]:
                    data[i], data[i + 1] = data[i + 1], data[i]
                    swapped = True
            if swapped == False:
                break
            swapped = False
            end -= 1
            for i in range(end - 1, start - 1, -1):
                if data[i] > data[i + 1]:
                    data[i], data[i + 1] = data[i + 1], data[i]
                    self.init_data(data)
                    swapped = True
            start += 1


def main():
    run = True
    res = 1600, 900
    BG = 211, 211, 211

    window = pygame.display.set_mode(res, pygame.RESIZABLE)
    pygame.display.set_caption("Sorting Visualizer")
    window.fill(BG)

    n = 200
    min = 1
    max = 500

    app = Application(window, res, BG)
    data = app.generate_data(n, min, max)
    app.init_data(data)

    # main loop
    while run:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    data = app.generate_data(n, min, max)
                    app.init_data(data)
                elif event.key == pygame.K_1:
                    app.bubble_sort(data)
                elif event.key == pygame.K_2:
                    app.selection_sort(data)
                elif event.key == pygame.K_3:
                    app.insertion_sort(data)
                elif event.key == pygame.K_4:
                    app.cocktail_sort(data)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
