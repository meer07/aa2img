#coding:utf-8
__author__ = 'naoya-kaige'
import sys
from PIL import Image, ImageFont, ImageDraw

class aa2img():
    # textsはリスト
    def outputimg(self, texts):
        # フォント情報
        font = ImageFont.truetype("ipaexg.ttf", 17)

        # 文字列の最大値を取得
        size = max(font.getsize(line) for line in texts)

        # 文字列の大きさから空白の画像を生成
        imag = Image.new("RGB",(size[0], size[1] * len(texts)), "#ffffff")

        # 画像に文字列を１行づつ書き込む
        drawimag = ImageDraw.Draw(imag)
        for i,line in enumerate(texts):
            drawimag.text(xy=(0, i*size[1]), text=line, font=font, fill="#000000")

        return imag

"""
if __name__ == "__main__":
    texts = sys.stdin.read().splitlines()
    a2i = aa2img()
    a2i.outputimg(texts)
"""