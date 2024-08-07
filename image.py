from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

def draw_text_bubble(draw, text, image_path, position, font, text_color='black', bubble_color='white'):
    # 气泡框的填充和边框宽度
    padding = 10
    border_radius = 15
    bubble_margin = 5
    
    # 计算文本的边界框
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # 图片大小
    if image_path:
        image = Image.open(image_path)
        image.thumbnail((200, 200))
        image_width, image_height = image.size
        image_height += 1 * padding
    else:
        image_width, image_height = 0, 0

    # 计算气泡框的大小和位置
    bubble_width = max(text_width, image_width) + 2 * padding
    bubble_height = text_height + image_height + 3 * padding
    bubble_x, bubble_y = position

    # 绘制气泡框的圆角矩形（无描边）
    draw.rounded_rectangle(
        [(bubble_x - bubble_margin, bubble_y - bubble_margin), 
         (bubble_x + bubble_width + bubble_margin, bubble_y + bubble_height + bubble_margin)],
        radius=border_radius,
        fill=bubble_color,
        outline=None  # 无描边
    )

    # 绘制文本
    text_position = (bubble_x + padding, bubble_y + padding)
    draw.text(text_position, text, font=font, fill=text_color)

    # 绘制图片
    if image_path:
        image_position = (bubble_x + padding, bubble_y + padding + text_height + padding*2)
        img.paste(image, image_position)

# 设置图像尺寸和背景颜色
image_width, image_height = 800, 600
background_color = '#FFDDC1'  # 使用十六进制颜色代码

# 创建带有指定背景颜色的图像
img = Image.new('RGB', (image_width, image_height), background_color)
draw = ImageDraw.Draw(img)

# 设置字体
font_path = "msyh.ttc"   # 你可以使用系统中可用的字体路径
font_size = 30
font = ImageFont.truetype(font_path, font_size)

# 绘制文字气泡框
text = "你好，世界！这是一个气泡框示例。"
image_path = "./avatar.jpg"
position = (50, 100)
draw_text_bubble(draw, text, image_path, position, font, text_color='black', bubble_color='#D3EAFD')

# 显示图像
img.show()

# 保存图像
img.save('text_bubble_with_image_example.png')
