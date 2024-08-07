from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

# 示例数据
data_list = [
    {
        'user_id': '123456',
        'user_nickname': 'User1',
        'message': 'Hello, this is a test message.',
        'image': [],
        'reply': None
    },
    {
        'user_id': '789012',
        'user_nickname': 'User2',
        'message': None,
        'image': ['./avatar.jpg'],
        'reply': {
            'user_nickname': 'User3',
            'message': 'This is a reply.',
            'image': None
        }
    }
]

# 字体和尺寸
font_path = "msyh.ttc" 
font_size = 30
font = ImageFont.truetype(font_path, font_size)
avatar_size = 100

def fetch_avatar(user_id):
    response = requests.get(f'https://q1.qlogo.cn/g?b=qq&nk={user_id}&s=640')
    return Image.open(BytesIO(response.content))

def fetch_image(path):
    return Image.open(path)

# 创建空白画布
canvas_width = 800
canvas_height = 600 * len(data_list)
canvas = Image.new('RGB', (canvas_width, canvas_height), (241, 241, 241))
draw = ImageDraw.Draw(canvas)

y_offset = 10

for index, data in enumerate(data_list):
    avatar = fetch_avatar(data['user_id'])
    avatar = avatar.resize((avatar_size, avatar_size))

    canvas.paste(avatar, (20, y_offset))
    draw.text((140, y_offset + 40), data['user_nickname'], font=font, fill=(148, 151, 163))

    if data['reply']:
        reply_box_top = y_offset + 120
        reply_box_height = 100
        reply_box_width = canvas_width - 160
        draw.rectangle([(140, reply_box_top), (canvas_width - 20, reply_box_top + reply_box_height)], fill=(245, 245, 245))
        draw.text((160, reply_box_top + 10), data['reply']['user_nickname'], font=font, fill=(0, 0, 0))
        if data['reply']['message']:
            draw.text((160, reply_box_top + 50), data['reply']['message'], font=font, fill=(0, 0, 0))
        if data['reply']['image']:
            reply_image = fetch_image(data['reply']['image'])
            reply_image.thumbnail((200, 200))
            canvas.paste(reply_image, (canvas_width - 240, reply_box_top + 10))
        y_offset += reply_box_height + 20

    message_box_top = y_offset + 120
    message_box_height = 100
    message_box_width = canvas_width - 160
    draw.rectangle([(140, message_box_top), (canvas_width - 20, message_box_top + message_box_height)], fill=(255, 255, 255))

    if data['message']:
        draw.text((160, message_box_top + 10), data['message'], font=font, fill=(0, 0, 0))
    if data['image']:
        for image_url in data['image']:
            message_image = fetch_image(image_url)
            message_image.thumbnail((200, 200))
            canvas.paste(message_image, (canvas_width - 240, message_box_top + 10))
            y_offset += 200 + 20

    y_offset += message_box_height + 40
canvas.save('output.png')
canvas.show()
