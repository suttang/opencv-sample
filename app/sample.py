# -*- coding: utf-8 -*-

import cv2
import numpy as np


if __name__ == '__main__':
    main = cv2.imread('image.jpg', 1)
    bg = cv2.imread('bg.png', 1)

    # 背景画像との差分を算出
    diff = cv2.absdiff(bg, main)

    # 差分を二値化
    threshold = cv2.threshold(diff, 20, 255, cv2.THRESH_BINARY)[1]

    # 膨張処理、収縮処理を施してマスク画像を生成
    operator = np.ones((3, 3), np.uint8)
    dilate = cv2.dilate(threshold, operator, iterations=4)
    mask = cv2.erode(dilate, operator, iterations=4)
    cv2.imwrite('output-mask.jpg', mask)

    # # マスク画像を使って対象を切り出す
    img_dst = cv2.bitwise_and(main, mask)
    cv2.imwrite('output.jpg', img_dst)
