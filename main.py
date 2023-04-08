# from rembg import remove

# input_path = 'input.jpg'
# output_path = 'output.png'

# with open(input_path, 'rb') as i:
#     with open(output_path, 'wb') as o:
#         input = i.read()
#         output = remove(input)
#         o.write(output)


from rembg import remove
from PIL import Image

input_path = '41d3e93963ab0ed82565.jpeg'
output_path = f'{input_path}.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)