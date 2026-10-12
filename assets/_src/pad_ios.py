# Pads short (16:9) iPhone screenshots to the 9:19.5 device-frame ratio using the screenshot's own
# top-bar and bottom colours, so the frame does not crop RTL content. No UI content is changed.
import sys
from PIL import Image
for src in sys.argv[1:]:
    im = Image.open(src).convert('RGB'); w, h = im.size
    H = round(w * 19.5 / 9); extra = H - h
    if extra <= 0: continue
    top = round(extra * 0.45); bot = extra - top
    out = Image.new('RGB', (w, H), im.getpixel((w // 2, 1)))
    out.paste(Image.new('RGB', (w, bot), im.getpixel((w // 2, h - 2))), (0, H - bot))
    out.paste(im, (0, top))
    out.save(src.replace('ios_shot_', 'ios_pad_'))
    print('padded', src)
