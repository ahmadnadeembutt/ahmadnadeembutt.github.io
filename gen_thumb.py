from PIL import Image, ImageDraw, ImageFont
import math, os

W, H = 1320, 742
img = Image.new('RGB', (W, H), color=(5, 10, 21))
draw = ImageDraw.Draw(img)

# ── subtle radial-ish glow on left side ──────────────────────────────
for r in range(350, 0, -1):
    alpha = int(40 * (1 - r / 350))
    draw.ellipse([290 - r, H//2 - r, 290 + r, H//2 + r],
                 fill=None, outline=(0, 50+alpha, 120+alpha))

# ── Hexagon ───────────────────────────────────────────────────────────
hx, hy, hr = 290, int(H * 0.44), 195

def hex_points(cx, cy, r):
    pts = []
    for i in range(6):
        angle = math.pi / 3 * i - math.pi / 6
        pts.append((cx + r * math.cos(angle), cy + r * math.sin(angle)))
    return pts

# glow rings
for g in range(8, 0, -1):
    pts = hex_points(hx, hy, hr + g * 3)
    draw.polygon(pts, outline=(0, int(191 * g/8), int(255 * g/8)))

pts = hex_points(hx, hy, hr)
draw.polygon(pts, fill=(0, 18, 55), outline=(0, 191, 255))
draw.polygon(hex_points(hx, hy, hr - 3), outline=(0, 160, 220))

# ── Package/Scan icon ──────────────────────────────────────────────────
iw, ih = 100, 100
bx, by = hx - iw//2, hy - ih//2 - 10
lw = 5
cyan  = (0, 191, 255)
blue  = (59, 130, 246)

# Box Outline
draw.polygon([(hx, by), (bx + iw, by + 30), (bx + iw, by + 30 + ih), (hx, by + ih + 60), (bx, by + 30 + ih), (bx, by + 30)], outline=blue, width=lw)
# Inner Box Lines
draw.line([(hx, by), (hx, by + ih + 60)], fill=blue, width=lw)
draw.line([(bx, by + 30), (hx, by + 60)], fill=blue, width=lw)
draw.line([(bx + iw, by + 30), (hx, by + 60)], fill=blue, width=lw)

# Scanning Line
scan_y = by + 70
draw.line([(bx - 20, scan_y), (bx + iw + 20, scan_y)], fill=cyan, width=lw+2)
# Glow dots on scanning line
dots = [(bx - 20, scan_y), (bx + iw + 20, scan_y)]
for dx, dy in dots:
    draw.ellipse([dx-7, dy-7, dx+7, dy+7], fill=cyan)

# ── Bottom label ─────────────────────────────────────────────────────
try:
    fnt_label = ImageFont.truetype("arialbd.ttf", 26)
except:
    fnt_label = ImageFont.load_default()

draw.text((hx, hy + hr + 30), "AUTONOMOUS INVENTORY", fill=cyan, font=fnt_label, anchor="mm")
draw.text((hx, hy + hr + 62), "INTELLIGENCE", fill=cyan, font=fnt_label, anchor="mm")

# ── Right side text ───────────────────────────────────────────────────
rx = 660

try:
    fnt_big   = ImageFont.truetype("arialbd.ttf", 88)
    fnt_mid   = ImageFont.truetype("arialbd.ttf", 82)
    fnt_bullet= ImageFont.truetype("arial.ttf",   32)
except:
    fnt_big = fnt_mid = fnt_bullet = ImageFont.load_default()

draw.text((rx, 110), "INVENTRAY",     fill=(0, 191, 255), font=fnt_big)
draw.text((rx, 200), "AUTONOMOUS",       fill=(255, 255, 255), font=fnt_mid)
draw.text((rx, 286), "INVENTORY",     fill=(255, 255, 255), font=fnt_mid)

# Divider
draw.line([(rx, 395), (W - 40, 395)], fill=(0, 100, 180), width=2)

# Bullet points
bullets = [
    "•  Smartphone-Based AI Inventory",
    "•  YOLOv8 & MiDaS 3D Depth",
    "•  ERP Integration & JSON Output",
]
for i, b in enumerate(bullets):
    draw.text((rx, 420 + i * 52), b, fill=(209, 213, 219), font=fnt_bullet)

# ── Save ──────────────────────────────────────────────────────────────
out = r"assets\images\projects\inventray.png"
img.save(out)
print(f"Saved: {out}  ({W}x{H})")
