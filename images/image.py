from PIL import Image, ImageDraw

# 创建透明画布
img = Image.new("RGBA", (60, 40), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# 飞碟底部椭圆（灰色）
draw.ellipse((5, 20, 55, 35), fill=(128, 128, 128, 255))

# 飞碟顶部圆顶（浅灰色）
draw.ellipse((15, 5, 45, 25), fill=(192, 192, 192, 255))

# 飞碟装饰点（白色，可选）
draw.ellipse((25, 12, 30, 17), fill=(255, 255, 255, 255))
draw.ellipse((35, 12, 40, 17), fill=(255, 255, 255, 255))

# 保存图片
img.save("alien_ship_gray.png")
print("透明背景灰色外星飞船已生成：alien_ship_gray.png")