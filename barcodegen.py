import click
import barcode
from barcode.writer import ImageWriter

@click.command()

@click.option('--code', '-c', default='Hello', help='The greeting to use.', required=True, type=str)
@click.option('--name', '-n', default='Hello', help='The greeting to use.', required=True, type=str)
@click.option('--price', '-p', default='Hello', help='The greeting to use.', required=True, type=str)

def run(code, name, price):

  # Initialize the ImageWriter
  writer = ImageWriter()

  # Generate a barcode object (CODE128 type)
  code128 = barcode.get_barcode_class('code128')

  # Check if the barcode class is found
  if code128 is None:
      print("Error: Unable to find the 'code128' barcode class.")
      exit()

  # Create the barcode instance with the ImageWriter
  barcode_instance = code128(code, writer)

  # Save the barcode image
  barcode_instance.save(code)

if __name__ == '__main__':
  run()
