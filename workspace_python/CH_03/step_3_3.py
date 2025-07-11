from pathlib import Path

from PIL import Image

# 이미지 폴더와 출력 폴더
IMG_DIR = Path(__file__).parent / "img"
OUT_DIR = Path(__file__).parent / "output"
OUT_DIR.mkdir(exist_ok=True)

# 이미지 리스트 jpg/jpeg/png 모두 불러오기
images = sorted(
    list(IMG_DIR.glob("*.jpg"))
    + list(IMG_DIR.glob("*.jpeg"))
    + list(IMG_DIR.glob("*.png"))
)

if not images:
    raise FileNotFoundError(f"이미지를 찾을 수 없습니다: {IMG_DIR}")

# 콜라주 크기 설정 (가로 3장, 세로 자동 계산)
cols = 3
thumb_width = 300
thumb_height = 300

rows = (len(images) + cols - 1) // cols

# 콜라주 이미지 크기 계산
collage_width = cols * thumb_width
collage_height = rows * thumb_height

collage_img = Image.new("RGB", (collage_width, collage_height), (255, 255, 255))

for idx, img_path in enumerate(images):
    img = Image.open(img_path)
    img.thumbnail((thumb_width, thumb_height))

    x = (idx % cols) * thumb_width
    y = (idx // cols) * thumb_height

    collage_img.paste(img, (x, y))

# 저장 및 출력
out_path = OUT_DIR / "collage.jpg"
collage_img.save(out_path)
collage_img.show()
print(f"콜라주 이미지 저장 완료: {out_path}")
