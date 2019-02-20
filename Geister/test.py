# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys

SCREEN = Rect(0, 0, 1960, 1280)
# スプライトのクラス
class Sprite(pygame.sprite.Sprite):
    # スプライトを作成(画像ファイル名, 位置(x, y), 速さ(vx, vy), 回転angle)
    def __init__(self, filename, x, y, vx, vy, angle=0):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load(filename).convert_alpha()
        if angle != 0: self.img = pygame.transform.rotate(self.img, angle)
        w = self.img.get_width()
        h = self.img.get_height()
        self.rect = Rect(x, y, w, h)
        self.vx = vx
        self.vy = vy
        self.angle = angle

    def update(self):
        self.rect.move_ip(self.vx, self.vy)
        # 壁と衝突時の処理(跳ね返り)
        if self.rect.left < 0 or self.rect.right > SCREEN.width:
            self.vx = -self.vx
        if self.rect.top < 0 or self.rect.bottom > SCREEN.height:
            self.vy = -self.vy
        # 壁と衝突時の処理(壁を超えないように)
        self.rect = self.rect.clamp(SCREEN)

    def draw(self, screen):
        screen.blit(self.img, self.rect)

    def move(self, x, y):
        self.rect.move_ip(x, y)

# メイン
def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN.size)
    (x, y) = (0, 0)
    # スプライトを作成(画像ファイル名, 位置(x, y), 速さ(vx, vy), 回転angle)
    player = Sprite("player.png", 200, 200, 0, 0, 0)
    enemy1 = Sprite("enemy1.png", 200, 20, 2, 20, 50)
    enemy2 = Sprite("enemy2.png", 200, 20, 2, 2, 10)
    clock = pygame.time.Clock()

    while (1):
        clock.tick(30)  # フレームレート(30fps)
        screen.fill((0, 20, 0, 0)) # 画面の背景色
        # スプライトを更新
        player.update()
        enemy1.update()
        enemy2.update()
        # スプライトを描画
        player.draw(screen)
        enemy1.draw(screen)
        enemy2.draw(screen)
        # 画面更新
        pygame.display.update()
        # イベント処理
        for event in pygame.event.get():
            # 終了用のイベント処理
            if event.type == QUIT:          # 閉じるボタンが押されたとき
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:       # キーを押したとき
                if event.key == K_ESCAPE:   # Escキーが押されたとき
                    pygame.quit()
                    sys.exit()

                 # 矢印キーなら円の中心座標を矢印の方向に移動
                if event.key == K_LEFT:
                    player.move(-10, 0)
                if event.key == K_RIGHT:
                    player.move(10, 0)
                if event.key == K_UP:
                    player.move(0, -10)
                if event.key == K_DOWN:
                    player.move(0, 10)

if __name__ == "__main__":
    main()