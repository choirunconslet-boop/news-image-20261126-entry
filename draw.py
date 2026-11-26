#!/usr/bin/env python3
"""Draw the 1024x1024 front page for Thursday 26 November 2026.

Every story below happened, or was first reported, on Thursday
26 November 2026 (checked against Reuters, CNN, BBC and Al Jazeera
on the morning of 26 Nov WIB). Figures are the ones reported
that day. Pure PIL vector drawing, no photos, no network.

Stories deliberately left OUT although they lead 26 Nov front pages:
the US tariff plan, the Netanyahu judges' recommendation, the
Savasleyka airbase strike, the Cairo tanker fire, the Ras Tanura
claim, the Sudan drone strikes, the Bangladesh wage rise, the
Ramaphosa court win, the Macy's parade postponement, the nine
children reunited and the Miss Universe crowning were all first
reported on Wednesday 25 Nov (or earlier); the Norway oil-licence
ruling was 13 Nov; the Gaza storm warning was 24 Nov.
"""
import math
import textwrap
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (248, 244, 234)
INK = (26, 26, 26)
RED = (164, 30, 34)
GREY = (90, 86, 76)
PANEL = (255, 253, 245)
RULE = (200, 192, 172)
YELLOW = (255, 200, 60)
BLUE = (30, 80, 140)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF_R = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap returning lines that fit `width` px."""
    lines = []
    for para in text.split("\n"):
        words, line = para.split(), ""
        for w in words:
            trial = (line + " " + w).strip()
            if draw.textlength(trial, font=fnt) <= width:
                line = trial
            else:
                if line:
                    lines.append(line)
                line = w
        if line:
            lines.append(line)
    return lines


def text_block(draw, x, y, text, fnt, width, fill=INK, leading=1.25):
    for ln in wrap(draw, text, fnt, width):
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += int(fnt.size * leading)
    return y


# ---- simple vector icons, each drawn in a s x s box at (x, y) ----

def icon_atom(d, x, y, s, c):
    # nucleus + three elliptical orbits = nuclear weapons
    cx, cy = x + 0.5 * s, y + 0.5 * s
    for ang in (0, 60, 120):
        pts = []
        for i in range(49):
            t = 2 * math.pi * i / 48
            rx, ry = 0.44 * s, 0.18 * s
            px = rx * math.cos(t)
            py = ry * math.sin(t)
            ca, sa = math.cos(math.radians(ang)), math.sin(math.radians(ang))
            pts.append((cx + px * ca - py * sa, cy + px * sa + py * ca))
        d.line(pts, fill=c, width=3)
    d.ellipse([cx - 0.10 * s, cy - 0.10 * s, cx + 0.10 * s, cy + 0.10 * s],
              fill=RED)


def icon_missile(d, x, y, s, c):
    # missile streaking up-right with a blast starburst behind it
    cx, cy = x + 0.5 * s, y + 0.5 * s
    outer, inner = 0.48 * s, 0.20 * s
    pts = []
    for i in range(16):
        r = outer if i % 2 == 0 else inner
        a = math.pi * i / 8 - math.pi / 2
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    d.polygon(pts, fill=YELLOW, outline=RED)
    d.polygon([(x + 0.62 * s, y + 0.30 * s), (x + 0.86 * s, y + 0.06 * s),
               (x + 0.78 * s, y + 0.38 * s), (x + 0.54 * s, y + 0.46 * s)],
              fill=c)
    d.polygon([(x + 0.30 * s, y + 0.62 * s), (x + 0.54 * s, y + 0.46 * s),
               (x + 0.46 * s, y + 0.70 * s)], fill=RED)


def icon_treaty(d, x, y, s, c):
    # document with a seal = treaty text published
    d.rectangle([x + 0.14 * s, y + 0.08 * s, x + 0.78 * s, y + 0.92 * s],
                fill=PANEL, outline=c, width=4)
    for i in range(4):
        yy = y + (0.24 + i * 0.13) * s
        d.line([x + 0.24 * s, yy, x + 0.68 * s, yy], fill=c, width=3)
    d.ellipse([x + 0.58 * s, y + 0.68 * s, x + 0.90 * s, y + 0.98 * s],
              fill=RED, outline=INK, width=2)
    d.text((x + 0.74 * s, y + 0.78 * s), "*", font=font(SANS_B, int(0.22 * s)),
           fill=PANEL, anchor="mm")


def icon_bank(d, x, y, s, c):
    # classical bank: pediment, columns, steps = central bank
    d.polygon([(x + 0.05 * s, y + 0.28 * s), (x + 0.50 * s, y + 0.05 * s),
               (x + 0.95 * s, y + 0.28 * s)], fill=RED)
    d.rectangle([x + 0.08 * s, y + 0.32 * s, x + 0.92 * s, y + 0.38 * s], fill=c)
    for i in range(3):
        xx = x + (0.18 + i * 0.26) * s
        d.rectangle([xx, y + 0.42 * s, xx + 0.10 * s, y + 0.78 * s], fill=c)
    d.rectangle([x + 0.08 * s, y + 0.82 * s, x + 0.92 * s, y + 0.88 * s], fill=c)
    d.rectangle([x + 0.04 * s, y + 0.90 * s, x + 0.96 * s, y + 0.96 * s], fill=c)


def icon_storm(d, x, y, s, c):
    # storm cloud, rain and waves = nor'easter and king tides
    d.ellipse([x + 0.10 * s, y + 0.14 * s, x + 0.48 * s, y + 0.48 * s], fill=c)
    d.ellipse([x + 0.38 * s, y + 0.06 * s, x + 0.78 * s, y + 0.44 * s], fill=c)
    d.ellipse([x + 0.62 * s, y + 0.18 * s, x + 0.92 * s, y + 0.48 * s], fill=c)
    d.rectangle([x + 0.10 * s, y + 0.36 * s, x + 0.92 * s, y + 0.50 * s], fill=c)
    for i in range(3):
        xx = x + (0.24 + i * 0.26) * s
        d.line([xx, y + 0.56 * s, xx - 0.06 * s, y + 0.70 * s],
               fill=BLUE, width=4)
    for i in range(2):
        yy = y + (0.80 + i * 0.10) * s
        d.arc([x + 0.08 * s, yy - 0.06 * s, x + 0.92 * s, yy + 0.06 * s],
              180, 360, fill=BLUE, width=4)


def icon_barrel(d, x, y, s, c):
    # oil barrel with a rising price arrow = oil climbs
    d.rectangle([x + 0.18 * s, y + 0.22 * s, x + 0.62 * s, y + 0.92 * s],
                fill=INK, outline=c, width=3)
    d.ellipse([x + 0.18 * s, y + 0.14 * s, x + 0.62 * s, y + 0.30 * s],
              fill=YELLOW, outline=c, width=3)
    for yy in (0.42, 0.72):
        d.line([x + 0.18 * s, y + yy * s, x + 0.62 * s, y + yy * s],
               fill=YELLOW, width=3)
    d.line([x + 0.76 * s, y + 0.86 * s, x + 0.76 * s, y + 0.18 * s],
           fill=RED, width=5)
    d.polygon([(x + 0.76 * s, y + 0.06 * s), (x + 0.62 * s, y + 0.26 * s),
               (x + 0.90 * s, y + 0.26 * s)], fill=RED)


def icon_shield(d, x, y, s, c):
    # shield with a star = NATO defence readiness
    d.polygon([(x + 0.10 * s, y + 0.08 * s), (x + 0.90 * s, y + 0.08 * s),
               (x + 0.90 * s, y + 0.48 * s), (x + 0.50 * s, y + 0.94 * s),
               (x + 0.10 * s, y + 0.48 * s)], fill=BLUE, outline=INK, width=3)
    cx, cy, r = x + 0.50 * s, y + 0.42 * s, 0.16 * s
    d.polygon([(cx, cy - r), (cx + 0.32 * r, cy - 0.32 * r),
               (cx + r, cy), (cx + 0.32 * r, cy + 0.32 * r),
               (cx, cy + r), (cx - 0.32 * r, cy + 0.32 * r),
               (cx - r, cy), (cx - 0.32 * r, cy - 0.32 * r)], fill=YELLOW)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    # outer frame
    d.rectangle([8, 8, W - 9, H - 9], outline=INK, width=4)
    d.rectangle([18, 18, W - 19, H - 19], outline=RULE, width=1)

    # ---- masthead ----
    d.text((W // 2, 34), "THE WORLD", font=font(SERIF, 96), fill=INK, anchor="ma")
    d.line([40, 138, W - 40, 138], fill=INK, width=3)
    d.text((W // 2, 148), "Thursday, 26 November 2026",
           font=font(SERIF, 30), fill=RED, anchor="ma")
    d.text((W // 2, 190),
           "THE DAY'S NEWS IN ONE PAGE  —  ALL STORIES FIRST REPORTED TODAY",
           font=font(SANS, 19), fill=GREY, anchor="ma")
    d.line([40, 224, W - 40, 224], fill=INK, width=2)

    # ---- lead story: Kim Jong Un / tactical nukes ----
    lx, ly, lw = 40, 240, W - 80
    d.rectangle([lx, ly, lx + lw, ly + 176], fill=PANEL, outline=RULE, width=1)
    d.text((lx + 20, ly + 12), "NORTH KOREA  •  LEAD STORY",
           font=font(SANS_B, 17), fill=RED)
    d.text((lx + 20, ly + 38), "Kim orders wider tactical nukes",
           font=font(SERIF, 44), fill=INK)
    d.text((lx + 20, ly + 92),
           "Kim Jong Un inspects nuclear sites and calls for tactical",
           font=font(SANS, 21), fill=INK)
    text_block(d, lx + 20, ly + 124,
               "nuclear weapons across more domains; Pyongyang's status as a nuclear state is 'absolutely inviolable'.",
               font(SANS, 19), lw - 40, fill=GREY)
    icon_atom(d, lx + lw - 96, ly + 36, 64, INK)

    # ---- six panels, 2 cols x 3 rows ----
    panels = [
        ("MIDDLE EAST", "Blast in Sanaa; Riyadh missiles stopped",
         "Two Houthi missiles aimed at Riyadh intercepted; Jizan port also hit.",
         icon_missile),
        ("EUROPE", "UK publishes EU treaty texts today",
         "Food and emissions treaties out today, with a 10-year exit clause.",
         icon_treaty),
        ("EUROPE", "EU leaders meet to pick Lagarde's successor",
         "Euro chiefs meet today; Lagarde steps down early in February.",
         icon_bank),
        ("USA", "Thanksgiving storms batter both coasts",
         "Nor'easter floods the East Coast; king tides swamp California today.",
         icon_storm),
        ("ENERGY", "Oil climbs on Gulf shipping fears",
         "Crude rises as Iran says tankers hit mines in Hormuz.",
         icon_barrel),
        ("DEFENCE", "NATO chief: Europe must ready for major war",
         "Alliance chief urges Europe to prepare for large-scale conflict.",
         icon_shield),
    ]
    pw, ph, gap = 462, 148, 20
    x0, y0 = 40, 432
    for i, (kick, head, body, icon) in enumerate(panels):
        x = x0 + (i % 2) * (pw + gap)
        y = y0 + (i // 2) * (ph + 14)
        d.rectangle([x, y, x + pw, y + ph], fill=PANEL, outline=RULE, width=1)
        d.text((x + 14, y + 10), kick, font=font(SANS_B, 15), fill=RED)
        ty = text_block(d, x + 14, y + 34, head, font(SANS_B, 24),
                        pw - 110, leading=1.12)
        # body uses the same narrow width as the headline so its lines can
        # never run into the icon at the panel's right edge
        text_block(d, x + 14, ty + 4, body, font(SANS, 18), pw - 110,
                   fill=GREY, leading=1.18)
        icon(d, x + pw - 78, y + 30, 58, INK)

    # ---- in brief strip ----
    by = y0 + 3 * ph + 2 * 14 + 12
    d.line([40, by, W - 40, by], fill=INK, width=2)
    d.text((40, by + 10), "IN BRIEF", font=font(SANS_B, 17), fill=RED)
    text_block(d, 40, by + 36,
               "• Trump says the US could sustain an Iran conflict until late January.  "
               "• Ukraine's parliament votes to legalise cryptocurrency.  "
               "• France's population is projected to fall by 3.9 million by 2070.",
               font(SANS, 17), W - 80, leading=1.25)

    img.save("entry.png", optimize=True)
    print("saved entry.png")


if __name__ == "__main__":
    main()
