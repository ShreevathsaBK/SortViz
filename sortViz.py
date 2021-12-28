import pygame
from random import randint

pygame.init()
clock = pygame.time.Clock()

WIDTH, HEIGHT = 1200, 700
FPS = 60
BAR_COUNT = 100
PADDING = 50
TOP_MARGIN = 0

WHITE = 255, 255, 255
BLACK = 0, 0, 0
COLOR_SCHEME = [(207, 227, 207), (84, 145, 85), (110, 171, 111), (174, 208, 175), (66, 113, 66)]

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SortViz")


def generate():
	BARS = []
	bar_width = (WIDTH - PADDING*2) / (BAR_COUNT)
	
	for count in range(BAR_COUNT):
		bar_height = randint(5, HEIGHT - TOP_MARGIN)
		bar = pygame.Rect(PADDING + count * bar_width , HEIGHT - bar_height, bar_width ,bar_height)
		BARS.append(bar)

	return BARS


def draw_rect(BARS):
	WIN.fill(WHITE)
	
	for count, bar in enumerate(BARS):
		bar.x = PADDING + count * bar.width
		pygame.draw.rect(WIN, COLOR_SCHEME[count % (len(COLOR_SCHEME)-1)], bar)
	
	pygame.display.update()
	
	
def bubble_sort(BARS):
	n = len(BARS)
	for i in range(n):
		for j in range(0, n-i-1):
			if BARS[j].height > BARS[j+1].height:
				BARS[j], BARS[j+1] = BARS[j+1], BARS[j]
				draw_rect(BARS)

			clock.tick(FPS)
			pygame.event.pump()


def merge(arr, low, mid, high):
	p1 = low
	p2 = mid + 1
	m = mid

	while p1 <= m and p2 <= high:
		if arr[p1].height < arr[p2].height:
			p1 += 1
		else:
			temp = arr[p2]
			for i in range(p2, p1, -1):
				arr[i] = arr[i-1]
			
			arr[p1] = temp
			p1 += 1
			p2 += 1
			m += 1

		clock.tick(FPS)
		pygame.event.pump()
		draw_rect(arr)


def merge_sort(arr, l, r):
    if (l < r):
        m = l + (r - l) // 2
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)


def eventloop():
	running = True

	BARS = generate()
	draw_rect(BARS)

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_g:
					BARS = generate()
					draw_rect(BARS)
				elif event.key == pygame.K_b:
					bubble_sort(BARS)
				elif event.key == pygame.K_m:
					merge_sort(BARS, 0, len(BARS)-1)
					

		clock.tick(FPS)
					
	pygame.quit()


eventloop()

