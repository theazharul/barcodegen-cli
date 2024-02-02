import click
import barcode
from barcode.writer import ImageWriter
from PIL import Image, ImageDraw, ImageFont
import textwrap

@click.command()

@click.option('--business', '-b', default='Ethnic Blaze', help='Business name', required=True, type=str)
@click.option('--code', '-c', default='A002851', help='Product code for barcode.', required=True, type=str)
@click.option('--name', '-n', default='Panjabi', help='Product name.', required=True, type=str)
@click.option('--price', '-p', default='500 taka', help='Product price.', required=True, type=str)

def run(business, code, name, price):
    # Generate a barcode object (CODE128 type)
    code128 = barcode.get_barcode_class('code128')

    # Render the barcode to a PIL image
    options = {'module_width': 0.3, 'module_height': 6, 'font_size': 5, 'text_distance': 2.2}
    barcode_img = code128(code, writer=ImageWriter()).render(options)
    # barcode_img = barcode_img.resize((barcode_img.width, 120))

    # Add margin to the barcode image
    barcode_img_with_margin = add_margin(barcode_img, 80, 0, 20, 0, (255, 255, 255))

    # Add text to the image
    image_with_text = add_text(barcode_img_with_margin, (0, 190), f"{business}", font_size=22)
    image_with_text = add_text(image_with_text, (0, 110), f"{name}", font_size=16)
    image_with_text = add_text(image_with_text, (0, -170), f"Price: {price}", font_size=20)

    # Save the barcode image
    image_with_text.save(f'{code}.png')

def add_margin(pil_img, top, right, bottom, left, color):
    width, height = pil_img.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(pil_img.mode, (new_width, new_height), color)
    result.paste(pil_img, (left, top))
    return result

def add_text(pil_img, position, text, font_path='arial.ttf', font_size=24, text_color=(0, 0, 0)):
    draw = ImageDraw.Draw(pil_img)
    font = ImageFont.truetype(font_path, font_size)


    wrapped_text = wrap_text_with_padding(text, font, 60, 10)
    wrapped_text = "\n".join(wrapped_text)

     # Calculate text size and position
    _, _, text_width, text_height =  draw.textbbox(position, text=wrapped_text, font=font)
    img_width, img_height = pil_img.size
    x = (img_width - text_width) // 2
    y = (img_height - text_height) // 2

    draw.text((x, y), wrapped_text, fill=text_color, font=font)
    return pil_img

# Function to wrap text with padding
def wrap_text_with_padding(text, font, max_width, padding):
    wrapper = textwrap.TextWrapper(width=max_width - 2 * padding)
    wrapped_text = wrapper.wrap(text)
    return wrapped_text

if __name__ == '__main__':
    run()
