# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys

SCREEN = Rect(0, 0, 800, 800)

class piece(pygame.sprite.Sprite):
    # スプライトを作成(画像ファイル名, 位置(x, y), 速さ(vx, vy), 回転angle)
    def __init__(self, filename, x, y, vx, vy):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load(filename).convert_alpha()
        w = self.img.get_width()
        h = self.img.get_height()
        self.rect = Rect(x, y, w, h)
        # self.vx = vx
        # self.vy = vy

    # def update(self):
    #     self.rect.move_ip(self.vx, self.vy)
    #     # 壁と衝突時の処理(跳ね返り)
    #     if self.rect.left < 0 or self.rect.right > SCREEN.width:
    #         self.vx = -self.vx
    #     if self.rect.top < 0 or self.rect.bottom > SCREEN.height:
    #         self.vy = -self.vy
    #     # 壁と衝突時の処理(壁を超えないように)
    #     self.rect = self.rect.clamp(SCREEN)

    def draw(self, screen):
        screen.blit(self.img, self.rect)

    def move(self, x, y):
        self.rect.move_ip(x, y)

def main():
    (w,h) = (800,800)   # 画面サイズ
    (x,y) = (w//2, h//2)
    pygame.init()       # pygame初期化
    screen = pygame.display.set_mode(SCREEN.size)
    screen = pygame.display.get_surface()
    bg = pygame.image.load("Board.png").convert_alpha()
    rect_bg = bg.get_rect()

    A = []
    B = []

    ay_pos = 100
    by_pos = 500
    for i in range(2):
        x_pos = 100
        for i in range(4):
            x_pos += 100
            A.append(piece("black.png", x_pos, ay_pos, 0, 0))
            B.append(piece("white.png", x_pos, by_pos, 0, 0))
        ay_pos += 100
        by_pos += 100
    
    clock = pygame.time.Clock()

    while (1):
        clock.tick(30)  # フレームレート(30fps)
        screen.fill((0, 20, 0, 0)) # 画面の背景色
        screen.blit(bg, (100, 100))

        num = 0
        for i in range(8):
            A[num].draw(screen)
            B[num].draw(screen)
            num += 1

        # player1.draw(screen)
        # player2.draw(screen)

        pygame.display.update()     # 画面更新
        pygame.time.wait(30)        # 更新時間間隔
        screen.fill((0, 20, 0, 0))  # 画面の背景色

        # イベント処理
        for event in pygame.event.get():
            # 画面の閉じるボタンを押したとき
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # キーを押したとき
            if event.type == KEYDOWN:
                # ESCキーなら終了
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                # 矢印キーなら円の中心座標を矢印の方向に移動
                if event.key == K_LEFT:
                    A[0].move(-100, 0)
                if event.key == K_RIGHT:
                    A[0].move(100, 0)
                if event.key == K_UP:
                    A[0].move(0, -100)
                if event.key == K_DOWN:
                    A[0].move(0, 100)


if __name__ == "__main__":
    main()