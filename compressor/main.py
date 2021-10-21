from enum import Enum
from PIL import Image
from tkinter.filedialog import askopenfilename, asksaveasfilename


class Quality(Enum):
    LOW = 15
    MEDIUM = 50
    HIGH = 80


file_path = askopenfilename()
image = Image.open(file_path)
if image.mode in ['RGBA', 'P']:
    image = image.convert('RGB')

save_path = asksaveasfilename()
image.save(f'{save_path}_compressed_low.jpg', optimize=True, quality=Quality.LOW.value)
image.save(f'{save_path}_compressed_medium.jpg', optimize=True, quality=Quality.MEDIUM.value)
image.save(f'{save_path}_compressed_high.jpg', optimize=True, quality=Quality.HIGH.value)
