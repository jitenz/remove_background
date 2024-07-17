# !pip install rembg

from rembg import remove
from PIL import Image

input_path = "/content/obama.jpg"
output_path = "/content/obama.png"

inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)

Image.open(output_path)