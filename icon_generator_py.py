"""
Generador de iconos para ¡Súper Sumas!
Ejecutar: python generar_iconos.py
Requiere: pip install Pillow
"""

from PIL import Image, ImageDraw, ImageFont
import os, math

def draw_icon(size):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    s = size

    # ── Fondo circular con degradado (667eea → f5576c) ──
    for y in range(s):
        t = y / s
        r_c = int(0x66 + (0xf5 - 0x66) * t)
        g_c = int(0x7e + (0x57 - 0x7e) * t)
        b_c = int(0xea + (0x6c - 0xea) * t)
        # Solo dentro del círculo
        cx = s // 2
        half_chord = int(math.sqrt(max(0, (s/2)**2 - (y - s/2)**2)))
        x0, x1 = cx - half_chord, cx + half_chord
        draw.line([(x0, y), (x1, y)], fill=(r_c, g_c, b_c, 255))

    # ── Tarjeta blanca redondeada ──
    pad = int(s * 0.10)
    card_x0 = pad
    card_y0 = int(s * 0.22)
    card_x1 = s - pad
    card_y1 = int(s * 0.78)
    draw.rounded_rectangle(
        [card_x0, card_y0, card_x1, card_y1],
        radius=int(s * 0.07),
        fill=(255, 255, 255, 245)
    )

    # ── Fuentes ──
    font_size_title = max(10, int(s * 0.085))
    font_size_op    = max(10, int(s * 0.17))
    font_size_res   = max(10, int(s * 0.17))

    try:
        font_title = ImageFont.truetype("arialbd.ttf", font_size_title)
        font_op    = ImageFont.truetype("arialbd.ttf", font_size_op)
        font_res   = ImageFont.truetype("arialbd.ttf", font_size_res)
    except:
        try:
            font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size_title)
            font_op    = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size_op)
            font_res   = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size_res)
        except:
            font_title = ImageFont.load_default()
            font_op    = font_title
            font_res   = font_title

    cx = s // 2

    # ── Título ──
    title = "Super Sumas!"
    bb = draw.textbbox((0, 0), title, font=font_title)
    tw = bb[2] - bb[0]
    draw.text((cx - tw // 2, int(s * 0.08)), title, font=font_title, fill=(255, 255, 255))

    # ── Operación "3 + 4" ──
    op_text = "3  +  4"
    bb = draw.textbbox((0, 0), op_text, font=font_op)
    tw = bb[2] - bb[0]
    op_y = int(s * 0.31)
    draw.text((cx - tw // 2, op_y), op_text, font=font_op, fill=(51, 51, 51))

    # ── Línea divisoria ──
    line_y = int(s * 0.535)
    lw = int(s * 0.012)
    draw.line([(card_x0 + int(s*0.04), line_y), (card_x1 - int(s*0.04), line_y)],
              fill=(51, 51, 51), width=lw)

    # ── Resultado "= 7" ──
    res_text = "=  7"
    bb = draw.textbbox((0, 0), res_text, font=font_res)
    tw = bb[2] - bb[0]
    res_y = int(s * 0.565)
    draw.text((cx - tw // 2, res_y), res_text, font=font_res, fill=(86, 171, 47))

    # ── Estrellas en esquinas (texto ASCII) ──
    star_font_size = max(8, int(s * 0.07))
    try:
        star_font = ImageFont.truetype("arialbd.ttf", star_font_size)
    except:
        star_font = ImageFont.load_default()

    draw.text((int(s*0.08), int(s*0.12)), "*", font=star_font, fill=(255, 220, 60))
    draw.text((int(s*0.82), int(s*0.12)), "*", font=star_font, fill=(255, 220, 60))
    draw.text((int(s*0.08), int(s*0.80)), "*", font=star_font, fill=(255, 180, 60))
    draw.text((int(s*0.82), int(s*0.80)), "*", font=star_font, fill=(255, 180, 60))

    # ── Círculo de máscara para bordes redondeados del icono ──
    mask = Image.new("L", (s, s), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.ellipse([0, 0, s, s], fill=255)
    img.putalpha(mask)

    return img


def main():
    os.makedirs("icons", exist_ok=True)

    for size in [192, 512]:
        icon = draw_icon(size)
        path = f"icons/icon-{size}.png"
        icon.save(path, "PNG")
        print(f"OK: {path}")

    print("Listo! Copia la carpeta icons/ en tu repositorio Super_sumas.")


if __name__ == "__main__":
    main()
