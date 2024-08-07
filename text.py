from PIL import Image, ImageDraw, ImageFont
def insert_newline(text):
    return '\n'.join([text[i:i+30] for i in range(0, len(text), 30)])

def draw_text_bubble(draw, text, position, font, text_color='black', bubble_color='white'):
    # 计算文本的边界框
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # 气泡框的填充和边框宽度
    padding = 10
    border_radius = 15 # 圆角弧度
    bubble_margin = 5

    # 计算气泡框的大小和位置
    bubble_width = text_width + 2 * padding
    bubble_height = text_height + 2 * padding
    bubble_x, bubble_y = position

    # 绘制气泡框的圆角矩形 
    draw.rounded_rectangle(
        [(bubble_x - bubble_margin, bubble_y - bubble_margin), 
         (bubble_x + bubble_width + bubble_margin, bubble_y + bubble_height + bubble_margin+10)],
        radius=border_radius,
        fill=bubble_color,
        outline=None
    )

    # 绘制文本
    text_position = (bubble_x + padding, bubble_y + padding)
    draw.text(text_position, text, font=font, fill=text_color)

# 创建空白图像
image_width, image_height = 800, 600
image = Image.new('RGB', (image_width, image_height), '#f1f1f1')
draw = ImageDraw.Draw(image)

# 设置字体
font_path = "msyh.ttc" 
font_size = 30
font = ImageFont.truetype(font_path, font_size)

# 绘制文字气泡框
text = "123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"
text = insert_newline(text)

position = (50, 100)
draw_text_bubble(draw, text, position, font, bubble_color='#ffffff')

# 显示图像
image.show()

# 保存图像
image.save('text_bubble_example.png')
