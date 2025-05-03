from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme

img_dir = Path(__file__).parent / "images"


def work(images: list[BuildImage], texts, args):
    x,y,h,w = (0, 242, 130, 130)
    img = images[0].convert("RGBA").resize((w, h), keep_ratio=True).circle()
    frame = BuildImage.open(img_dir / "0.png")
    frame.paste(img, (x, y), alpha=True)
    return frame.save_jpg()


add_meme(
    "work",
    work,
    min_images=1,
    max_images=1,
    keywords=["干活"],
    date_created=datetime(2025, 5, 3),
    date_modified=datetime(2025, 5, 3),
)
