from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme

img_dir = Path(__file__).parent / "images"


def snap(images: list[BuildImage], texts, args):
    locs = [(20, 95, 54, 54), (178,79,50,50)]
    frame = BuildImage.open(img_dir / "0.png")
    for i in range(len(locs)):
        x, y, w, h = locs[i]
        img = images[i].convert("RGBA").resize((w, h), keep_ratio=True).circle()
        frame.paste(img, (x, y), alpha=True)
    return frame.save_jpg()


add_meme(
    "snap",
    snap,
    min_images=2,
    max_images=2,
    keywords=["啪"],
    date_created=datetime(2025, 4, 27),
    date_modified=datetime(2025, 4, 27),
)
