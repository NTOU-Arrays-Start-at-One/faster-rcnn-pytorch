import cv2
import numpy as np

merged_image = None  # 定義全域變數，防止函數內的變數被回收

def imageCompare(img1, img2):
    global merged_image  # 定義全域變數，防止函數內的變數被回收

    # 檢查圖片大小是否一致，若不同可使用cv2.resize()函數進行調整
    img1 = cv2.resize(img1, (500, 500))
    img2 = cv2.resize(img2, (500, 500))

    # 生成一條紅色的線
    height, width, channels = img1.shape
    line_thickness = 2
    line_length = int(width / 2)
    line_color = (0, 0, 255) # BGR格式，此處為紅色
    line_x = int(width / 2)
    line_start = (line_x, 0)
    line_end = (line_x, height)

    # 生成一張空白的黑色圖片，大小與img1相同
    merged_image = np.zeros((height, width, channels), dtype=np.uint8)

    # 將img1與img2分別放在空白圖片的左半邊與右半邊
    merged_image[:, :line_end[0], :] = img1[:, :line_end[0], :]
    merged_image[:, line_end[0]:, :] = img2[:, line_end[0]:, :]

    # 顯示疊加後的圖片
    cv2.imshow("Merged Image", merged_image)

    # 滑鼠事件的回調函數
    def on_mouse(event, x, y, flags, param):
        global line_x, merged_image
        if event == cv2.EVENT_MOUSEMOVE:
            line_x = x
            # 更新線的位置
            line_start = (line_x, 0)
            line_end = (line_x, height)
            # 將img1與img2分別放在空白圖片的左半邊與右半邊
            merged_image[:, :line_end[0], :] = img1[:, :line_end[0], :]
            merged_image[:, line_end[0]:, :] = img2[:, line_end[0]:, :]
            # 重新畫線
            cv2.line(merged_image, line_start, line_end, line_color, thickness=line_thickness)
            # 顯示更新後的圖片
            cv2.imshow("Merged Image", merged_image)

    # 設置滑鼠事件的回調函數
    cv2.setMouseCallback("Merged Image", on_mouse)

    cv2.waitKey(0)
    cv2.destroyAllWindows()