import pygame as pg
from random import randint
import sys
from pygame.locals import *

FPS = 15  # 画面帧数，代表蛇的移动速率
window_width = 600
window_height = 500
cellsize = 20
cell_width = int(window_width / cellsize)
cell_height = int(window_height / cellsize)
BGcolor = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
apple_color = (255, 0, 0)
snake_color = (0, 150, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
DARKGRAY = (40, 40, 40)

UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"
HEAD = 0

def main():  # 有函数
    global FPSclock, window, BASICFONT
    pg.init()
    FPSclock = pg.time.Clock()
    window = pg.display.set_mode((window_width, window_height))
    BASICFONT = pg.font.Font("freesansbold.ttf", 18)
    pg.display.set_caption("贪吃蛇")
    showStartScreen()
    while True:
        runGame()
        showGameOverScreen()

def runGame():  # 运行游戏函数
    startx = randint(5, cell_width - 6)
    starty = randint(5, cell_height - 6)
    snakeCoords = [{"x": startx, "y": starty}, {"x": startx - 1, "y": starty}, {"x": startx - 2, "y": starty}]
    direction = RIGHT
    apple = getRandomLocation()
    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT and direction != RIGHT:
                    direction = LEFT
                elif event.key == K_RIGHT and direction != LEFT:
                    direction = RIGHT
                elif event.key == K_UP and direction != DOWN:
                    direction = UP
                elif event.key == K_DOWN and direction != UP:
                    direction = DOWN
                elif event.key == K_ESCAPE:
                    terminate()
        if snakeCoords[HEAD]["x"] == -1 or snakeCoords[HEAD]["x"] == cell_width or snakeCoords[HEAD]["y"] == -1 or \
                snakeCoords[HEAD]["y"] == cell_height:
            return
        for snakeBody in snakeCoords[1:]:
            if snakeBody["x"] == snakeCoords[HEAD]["x"] and snakeBody["y"] == snakeCoords[HEAD]["y"]:
                return
            if snakeCoords[HEAD]["x"] == apple["x"] and snakeCoords[HEAD]["y"] == apple["y"]:
                apple = getRandomLocation()
            else:
                del snakeCoords[-1]
            if direction == UP:
                newHead = {"x": snakeCoords[HEAD]["x"], "y": snakeCoords[HEAD]["y"] - 1}
            elif direction == DOWN:
                newHead = {"x": snakeCoords[HEAD]["x"], "y": snakeCoords[HEAD]["y"] + 1}
            elif direction == LEFT:
                newHead = {"x": snakeCoords[HEAD]["x"] - 1, "y": snakeCoords[HEAD]["y"]}
            elif direction == RIGHT:
                newHead = {"x": snakeCoords[HEAD]["x"] + 1, "y": snakeCoords[HEAD]["y"]}


            snakeCoords.insert(0, newHead)
            window.fill(BGcolor)
            drawGrid()
            drawSnake(snakeCoords)
            drawApple(apple)

            drawScore(len(snakeCoords) - 3)
            pg.display.update()
            FPSclock.tick(FPS)

def drawPressKeyMsg():  # 游戏开始提示信息
    pressKeySurf = BASICFONT.render("press a key to play", True, BLUE)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (window_width - 200, window_height - 30)
    window.blit(pressKeySurf, pressKeyRect)

def checkForKeyPress():  # 检查是否触发按键
    if len(pg.event.get(QUIT)) > 0:
        terminate()
    keyUpEvents = pg.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key

def showStartScreen():  # 开始画面
    window.fill(BGcolor)
    titleFont = pg.font.Font("freesansbold.ttf", 100)
    titleSurf = titleFont.render("snake!", True, RED)
    titleRect = titleSurf.get_rect()
    titleRect.center = (window_width / 2, window_height / 2)
    window.blit(titleSurf, titleRect)
    drawPressKeyMsg()
    pg.display.update()
    while True:
        if checkForKeyPress():
            pg.event.get()
            return
def terminate():  # 退出
    pg.quit()
    sys.exit()
def getRandomLocation():  # 出现位置
    return {"x": randint(0, cell_width - 1), "y": randint(0, cell_height - 1)}

def showGameOverScreen():  # 游戏结束
    gameOverFont = pg.font.Font("freesansbold.tff", 150)
    gameSurf = gameOverFont.render("Game", True, WHITE)
    overSurf = gameOverFont.render("over", True, WHITE)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (window_width / 2, 10)
    overRect.midtop = (window_width / 2, gameRect.height10 + 25)
    window.blit(gameSurf, gameRect)
    window.blit(overSurf, overRect)


    drawPressKeyMsg()
    pg.display.update()
    pg.time.wait(500)
    checkForKeyPress()
    while True:
        if checkForKeyPress():
            pg.event.get()
            return

def drawScore(score):  # 显示分数
    scoreSurf = BASICFONT.render("Score:%s" % (score), True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (window_width - 120, 10)
    window.blit(scoreSurf, scoreRect)

def drawSnake(snakeCoords):  # 画蛇
    for coord in snakeCoords:
        x = coord["x"] * cellsize
        y = coord["y"] * cellsize
        snakeSegmentRect = pg.Rect(x, y, cellsize, cellsize)
        pg.draw.rect(window, snake_color, snakeSegmentRect)
        snakeInnerSegmentRect = pg.Rect(x + 4, y + 4, cellsize - 8, cellsize - 8)
        pg.draw.rect(window, GREEN, snakeInnerSegmentRect)

def drawApple(coord):
    x = coord["x"] * cellsize
    y = coord["y"] * cellsize
    appleRect = pg.Rect(x, y, cellsize, cellsize)
    pg.draw.rect(window, apple_color, appleRect)

def drawGrid():  # 画方格
    for x in range(0, window_width, cellsize):
        pg.draw.line(window, DARKGRAY, (x, 0), (x, window_height))
    for y in range(0, window_height, cellsize):
        pg.draw.line(window, DARKGRAY, (0, y), (window_width, y))

if __name__ == "__main__":
    main()