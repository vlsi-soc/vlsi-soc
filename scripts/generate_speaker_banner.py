#!/usr/bin/env python3
"""Generate a keynote speakers image similar to img/carousel/1.png.

Usage:
  python scripts/generate_speaker_banner.py --config scripts/speaker_banner_config.example.json
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Optional, Tuple

from PIL import Image, ImageDraw, ImageFont


@dataclass
class Speaker:
    name: str
    affiliation: str
    email: str
    image: str
    website: Optional[str] = None


def parse_color(value: str, fallback: Tuple[int, int, int]) -> Tuple[int, int, int]:
    if not value:
        return fallback
    v = value.strip()
    if v.startswith("#") and len(v) == 7:
        return tuple(int(v[i : i + 2], 16) for i in (1, 3, 5))
    return fallback


def try_load_font(candidates: Iterable[str], size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, size=size)
        except OSError:
            continue
    return ImageFont.load_default()


def load_fonts(title_size: int, body_size: int):
    title_font = try_load_font(
        [
            "arialbi.ttf",
            "Arial Bold Italic.ttf",
            "/usr/share/fonts/truetype/msttcorefonts/Arial_Bold_Italic.ttf",
            "/usr/share/fonts/truetype/msttcorefonts/arialbi.ttf",
            "/usr/share/fonts/truetype/liberation2/LiberationSans-BoldItalic.ttf",
            "DejaVuSans-BoldOblique.ttf",
            "DejaVuSans-Bold.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-BoldOblique.ttf",
        ],
        title_size,
    )
    label_font = try_load_font(
        [
            "arialbi.ttf",
            "Arial Bold Italic.ttf",
            "/usr/share/fonts/truetype/msttcorefonts/Arial_Bold_Italic.ttf",
            "/usr/share/fonts/truetype/msttcorefonts/arialbi.ttf",
            "/usr/share/fonts/truetype/liberation2/LiberationSans-BoldItalic.ttf",
            "DejaVuSans-BoldOblique.ttf",
            "DejaVuSans-Bold.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-BoldOblique.ttf",
        ],
        body_size,
    )
    value_font = try_load_font(
        [
            "arial.ttf",
            "Arial.ttf",
            "Arial Regular.ttf",
            "/usr/share/fonts/truetype/msttcorefonts/Arial.ttf",
            "/usr/share/fonts/truetype/msttcorefonts/arial.ttf",
            "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
            "DejaVuSans.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        ],
        body_size,
    )
    return title_font, label_font, value_font


def text_size(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont) -> Tuple[int, int]:
    left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
    return right - left, bottom - top


def wrap_text(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont, max_width: int) -> List[str]:
    def split_long_token(token: str) -> List[str]:
        if draw.textlength(token, font=font) <= max_width:
            return [token]
        parts: List[str] = []
        current = ""
        for ch in token:
            trial = current + ch
            if current and draw.textlength(trial, font=font) > max_width:
                parts.append(current)
                current = ch
            else:
                current = trial
        if current:
            parts.append(current)
        return parts

    words = text.split()
    if not words:
        return [""]

    expanded_words: List[str] = []
    for word in words:
        expanded_words.extend(split_long_token(word))

    lines: List[str] = []
    current = expanded_words[0]
    for word in expanded_words[1:]:
        trial = f"{current} {word}"
        if draw.textlength(trial, font=font) <= max_width:
            current = trial
        else:
            lines.append(current)
            current = word
    lines.append(current)
    return lines


def draw_underlined_text(
    draw: ImageDraw.ImageDraw,
    position: Tuple[int, int],
    text: str,
    font: ImageFont.ImageFont,
    fill: Tuple[int, int, int],
    underline_offset: int = 1,
    underline_thickness: int = 1,
) -> Tuple[int, int]:
    x, y = position
    draw.text((x, y), text, font=font, fill=fill)
    width, height = text_size(draw, text, font)

    if hasattr(font, "getmetrics"):
        ascent, _ = font.getmetrics()
        underline_y = y + ascent + underline_offset
    else:
        underline_y = y + height + underline_offset

    draw.line([(x, underline_y), (x + width, underline_y)], fill=fill, width=underline_thickness)
    return width, height


def draw_labeled_line(
    draw: ImageDraw.ImageDraw,
    x: int,
    y: int,
    label: str,
    value: str,
    max_width: int,
    label_font: ImageFont.ImageFont,
    value_font: ImageFont.ImageFont,
    label_color: Tuple[int, int, int],
    value_color: Tuple[int, int, int],
) -> int:
    label_with_colon = f"{label}:"
    label_width, label_height = draw_underlined_text(draw, (x, y), label_with_colon, label_font, label_color)

    value_x = x + label_width + 6
    remaining_width = max(10, max_width - (label_width + 6))
    value_lines = wrap_text(draw, value, value_font, remaining_width)

    line_height = max(text_size(draw, "Ag", value_font)[1], label_height)
    for i, line in enumerate(value_lines):
        draw.text((value_x, y + i * (line_height + 2)), line, font=value_font, fill=value_color)

    return len(value_lines) * (line_height + 2)


def measure_labeled_line(
    draw: ImageDraw.ImageDraw,
    label: str,
    value: str,
    max_width: int,
    label_font: ImageFont.ImageFont,
    value_font: ImageFont.ImageFont,
) -> int:
    label_with_colon = f"{label}:"
    label_width, label_height = text_size(draw, label_with_colon, label_font)
    remaining_width = max(10, max_width - (label_width + 6))
    value_lines = wrap_text(draw, value, value_font, remaining_width)
    line_height = max(text_size(draw, "Ag", value_font)[1], label_height)
    return len(value_lines) * (line_height + 2)


def generate_banner(config_path: Path) -> Path:
    with config_path.open("r", encoding="utf-8") as f:
        cfg = json.load(f)

    title = cfg.get("title", "Confirmed Keynote Speakers")
    width = int(cfg.get("width", 640))
    height = int(cfg.get("height", 313))
    output = Path(cfg.get("output", "img/carousel/generated.png"))

    bg_color = parse_color(cfg.get("background", "#d9d9d9"), (217, 217, 217))
    text_color = parse_color(cfg.get("text_color", "#111111"), (17, 17, 17))
    link_color = parse_color(cfg.get("link_color", "#1a0dab"), (26, 13, 171))

    speakers_raw = cfg.get("speakers", [])
    speakers = [Speaker(**s) for s in speakers_raw]
    if not speakers:
        raise ValueError("Config must contain at least one speaker in 'speakers'.")

    title_size = int(cfg.get("title_font_size", 56 // 2))
    body_size = int(cfg.get("body_font_size", 38 // 2))
    title_font, label_font, value_font = load_fonts(title_size=title_size, body_size=body_size)

    top_margin = int(cfg.get("top_margin", 8))
    side_padding = int(cfg.get("side_padding", 36))
    gap = int(cfg.get("speaker_gap", 16))
    image_height = int(cfg.get("speaker_image_height", 138))
    auto_expand_height = bool(cfg.get("auto_expand_height", True))
    bottom_padding = int(cfg.get("bottom_padding", 8))

    measure_image = Image.new("RGB", (width, max(1, height)), bg_color)
    measure_draw = ImageDraw.Draw(measure_image)

    title_w, title_h = text_size(measure_draw, title, title_font)
    content_top = top_margin + title_h + 16

    available_width = width - side_padding * 2
    column_width = (available_width - gap * (len(speakers) - 1)) // len(speakers)
    base_line_h = text_size(measure_draw, "Ag", value_font)[1] + 6

    max_text_block_height = 0
    for speaker in speakers:
        name_h = text_size(measure_draw, speaker.name, label_font)[1]
        block_height = name_h + base_line_h
        block_height += measure_labeled_line(
            measure_draw,
            label="Affiliation",
            value=speaker.affiliation,
            max_width=column_width,
            label_font=label_font,
            value_font=value_font,
        )
        block_height += measure_labeled_line(
            measure_draw,
            label="Email",
            value=speaker.email,
            max_width=column_width,
            label_font=label_font,
            value_font=value_font,
        )
        if speaker.website and speaker.website.strip():
            block_height += measure_labeled_line(
                measure_draw,
                label="Website",
                value=speaker.website,
                max_width=column_width,
                label_font=label_font,
                value_font=value_font,
            )
        if block_height > max_text_block_height:
            max_text_block_height = block_height

    required_height = content_top + image_height + 12 + max_text_block_height + bottom_padding
    if auto_expand_height and required_height > height:
        height = required_height

    image = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(image)

    title_w, title_h = text_size(draw, title, title_font)
    title_x = (width - title_w) // 2
    title_y = top_margin
    draw_underlined_text(
        draw,
        position=(title_x, title_y),
        text=title,
        font=title_font,
        fill=text_color,
        underline_offset=1,
        underline_thickness=1,
    )

    content_top = title_y + title_h + 16
    available_width = width - side_padding * 2
    column_width = (available_width - gap * (len(speakers) - 1)) // len(speakers)

    for idx, speaker in enumerate(speakers):
        col_x = side_padding + idx * (column_width + gap)

        src = Image.open(speaker.image).convert("RGB")
        src_w, src_h = src.size
        target_w = column_width
        scale = max(target_w / src_w, image_height / src_h)
        resized = src.resize((int(src_w * scale), int(src_h * scale)), Image.LANCZOS)

        crop_x = max(0, (resized.width - target_w) // 2)
        crop_y = max(0, (resized.height - image_height) // 2)
        cropped = resized.crop((crop_x, crop_y, crop_x + target_w, crop_y + image_height))
        image.paste(cropped, (col_x, content_top))

        text_y = content_top + image_height + 12
        draw.text((col_x, text_y), speaker.name, font=label_font, fill=text_color)

        base_line_h = text_size(draw, "Ag", value_font)[1] + 6
        text_y += base_line_h

        text_y += draw_labeled_line(
            draw,
            x=col_x,
            y=text_y,
            label="Affiliation",
            value=speaker.affiliation,
            max_width=column_width,
            label_font=label_font,
            value_font=value_font,
            label_color=text_color,
            value_color=text_color,
        )

        text_y += draw_labeled_line(
            draw,
            x=col_x,
            y=text_y,
            label="Email",
            value=speaker.email,
            max_width=column_width,
            label_font=label_font,
            value_font=value_font,
            label_color=text_color,
            value_color=link_color,
        )

        if speaker.website and speaker.website.strip():
            draw_labeled_line(
                draw,
                x=col_x,
                y=text_y,
                label="Website",
                value=speaker.website,
                max_width=column_width,
                label_font=label_font,
                value_font=value_font,
                label_color=text_color,
                value_color=link_color,
            )

    output.parent.mkdir(parents=True, exist_ok=True)
    image.save(output)
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate keynote speaker banner image")
    parser.add_argument("--config", required=True, help="Path to JSON config")
    args = parser.parse_args()

    out = generate_banner(Path(args.config))
    print(f"Generated: {out}")


if __name__ == "__main__":
    main()
