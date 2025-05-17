import cv2
import numpy as np

# 必要に応じてIDを変更（例：0 → 1）
# もしiPhoneが起動してしまうなら、1 や 2 を試す
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("カメラを開けませんでした。別のIDを試してください。")
    exit()

# ドット絵のサイズ（小さくすると荒くなる）
DOT_WIDTH = 64
DOT_HEIGHT = 48

while True:
    ret, frame = cap.read()
    if not ret:
        print("フレームを取得できませんでした。")
        break

    # フレームを小さくしてドット化
    small = cv2.resize(frame, (DOT_WIDTH, DOT_HEIGHT), interpolation=cv2.INTER_NEAREST)

    # 色を減らす（各チャンネルを0, 64, 128, 192で丸める）
    quantized = (small // 64) * 64

    # ドット絵風に引き伸ばして戻す
    dot_image = cv2.resize(quantized, (frame.shape[1], frame.shape[0]), interpolation=cv2.INTER_NEAREST)

    # 表示
    cv2.imshow('DotCam', dot_image)

    # 'q' キーで終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 終了処理
cap.release()
cv2.destroyAllWindows()
