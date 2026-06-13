"""Generate SDS扫地僧 icons - bald monk with broom (小和尚扫帚)"""
from PIL import Image
import os

# 24x24 pixel design
design = [
    '........................',
    '........................',
    '........................',
    '.......IIIIIIII.........',
    '......ISSSSSSSSI........',
    '.....ISSSSSSSSSI........',
    '.....ISSISSISSSI........',
    '.....ISSSSSSSSSI........',
    '.....ISSSRRRSSSI........',
    '......ISSSSSSI..........',
    '.......IIIIII...........',
    '......IIIRIIII..........',
    '.....IRRRRRRRRII........',
    '....IRRRRGRRRRRI........',
    '....IRRRRGRRRRRI........',
    '....IRRRRRRRRRRIHH......',
    '....IRRRRRRRRRRIHBB.....',
    '....IRRRRRRRRRRIHBBH....',
    '....IRRRRRRRRRRIHHBB....',
    '....IDDDDDDDDDDIIBBBB...',
    '.....IIIIIIIIIIIIHBBB...',
    '..................IHH...',
    '........................',
    '........................',
]

COLORS = {
    'I': (44, 24, 16, 255),     # #2C1810 ink
    'S': (245, 213, 168, 255),  # #F5D5A8 skin
    'R': (139, 105, 20, 255),   # #8B6914 robe
    'G': (212, 160, 23, 255),   # #D4A017 gold
    'D': (92, 72, 48, 255),     # #5C4830 dark hem
    'H': (192, 132, 87, 255),   # #C08457 handle
    'B': (232, 217, 184, 255),  # #E8D9B8 bristles
}

# Create 24x24 source
src = Image.new('RGBA', (24, 24), (0, 0, 0, 0))
for y, row in enumerate(design):
    for x, ch in enumerate(row):
        if ch in COLORS:
            src.putpixel((x, y), COLORS[ch])

icon_dir = os.path.join(os.path.dirname(__file__), 'apps', 'desktop', 'src-tauri', 'icons')

# Generate PNGs at various sizes
for size, filename in [(32, '32x32.png'), (128, '128x128.png'), (256, '128x128@2x.png'), (512, 'icon.png')]:
    img = src.resize((size, size), Image.NEAREST)
    img.save(os.path.join(icon_dir, filename))
    print(f'  wrote {filename}')

# Generate ICO
src.save(os.path.join(icon_dir, 'icon.ico'), format='ICO', sizes=[(16,16),(24,24),(32,32),(48,48),(64,64),(128,128),(256,256)])
print('  wrote icon.ico')

# Also save a 64x64 preview
img64 = src.resize((64, 64), Image.NEAREST)
img64.save(os.path.join(icon_dir, '64x64.png'))
print('  wrote 64x64.png')

print('Done!')
