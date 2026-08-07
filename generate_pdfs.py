#!/usr/bin/env python3
"""
Generate styled PDFs from Danish markdown documents.
Design: clean academic, muted navy/blue palette, DejaVu fonts for Danish character support.
"""

import re
import os
import math
from fpdf import FPDF

FONT_DIR = next(
    d for d in [
        "/Users/pmackinnon/Library/Fonts",          # macOS
        "/usr/share/fonts/truetype/dejavu",          # Linux
    ] if os.path.isdir(d)
)
OUTPUT_DIR = "/Users/pmackinnon/fun-projects/aerospace-study-usa/da/pdf"

# Color palette
NAVY      = (30,  60,  100)   # H1
BLUE_MID  = (45,  90,  140)   # H2
BLUE_LT   = (60, 110, 160)    # H3
BODY      = (30,  30,   30)   # body text
RULE      = (90, 130, 180)    # H1 underline, table header bg
WHITE     = (255, 255, 255)
ROW_ALT   = (240, 245, 252)   # alternating table row
BLOCKQUOTE= (100, 120, 150)   # blockquote text color
BQ_BAR    = (120, 160, 200)   # blockquote left bar color
FOOTER    = (150, 160, 170)

MARGIN_L  = 20
MARGIN_R  = 20
MARGIN_T  = 22
MARGIN_B  = 22


class PDF(FPDF):
    def __init__(self, title=""):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.doc_title = title
        self.set_margins(MARGIN_L, MARGIN_T, MARGIN_R)
        self.set_auto_page_break(auto=True, margin=MARGIN_B)

        # Register fonts
        self.add_font("DejaVu",     "",  os.path.join(FONT_DIR, "DejaVuSans.ttf"))
        self.add_font("DejaVu",     "B", os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf"))
        # No oblique variant available — reuse regular for "italic" and bold for "bold-italic"
        self.add_font("DejaVu",     "I", os.path.join(FONT_DIR, "DejaVuSans.ttf"))
        self.add_font("DejaVu",     "BI",os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf"))
        self.add_font("DejaVuMono", "",  os.path.join(FONT_DIR, "DejaVuSansMono.ttf"))

    def header(self):
        pass  # no running header

    def footer(self):
        self.set_y(-14)
        self.set_font("DejaVu", "", 8)
        self.set_text_color(*FOOTER)
        self.cell(0, 6, str(self.page_no()), align="C")

    def effective_width(self):
        return self.w - MARGIN_L - MARGIN_R


def strip_inline(text):
    """Remove markdown bold/italic/code markers and return plain text + style info."""
    return text


def render_inline(pdf, text, base_size, base_color):
    """Render a line of text with inline bold/italic/code formatting."""
    # Split on **bold**, *italic*, `code` markers
    pattern = re.compile(r'(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`)')
    parts = pattern.split(text)
    for part in parts:
        if part.startswith("**") and part.endswith("**"):
            pdf.set_font("DejaVu", "B", base_size)
            pdf.set_text_color(*base_color)
            pdf.write(5, part[2:-2])
        elif part.startswith("*") and part.endswith("*"):
            pdf.set_font("DejaVu", "I", base_size)
            pdf.set_text_color(*base_color)
            pdf.write(5, part[1:-1])
        elif part.startswith("`") and part.endswith("`"):
            pdf.set_font("DejaVuMono", "", base_size - 0.5)
            pdf.set_text_color(80, 80, 80)
            pdf.write(5, part[1:-1])
        else:
            pdf.set_font("DejaVu", "", base_size)
            pdf.set_text_color(*base_color)
            pdf.write(5, part)


def count_wrapped_lines(pdf, text, width, font_size):
    """Count lines multi_cell will produce by simulating word-wrap."""
    if not text:
        return 1
    pdf.set_font("DejaVu", "", font_size)
    effective_w = width - 2 * pdf.c_margin
    words = text.split()
    if not words:
        return 1
    lines = 1
    line_w = 0.0
    space_w = pdf.get_string_width(" ")
    for word in words:
        word_w = pdf.get_string_width(word)
        if line_w == 0.0:
            line_w = word_w
        elif line_w + space_w + word_w <= effective_w:
            line_w += space_w + word_w
        else:
            lines += 1
            line_w = word_w
    return lines


def parse_table(lines):
    """Parse markdown table lines into header + rows."""
    rows = []
    for line in lines:
        if re.match(r'^\|[-| :]+\|$', line.strip()):
            continue  # separator row
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        rows.append(cells)
    return rows[0] if rows else [], rows[1:] if len(rows) > 1 else []


def render_table(pdf, header, rows, base_size=9.5):
    w = pdf.effective_width()
    if not header:
        return

    ncols = len(header)
    # Column widths by shape
    if ncols == 2:
        col_widths = [w * 0.32, w * 0.68]
    elif ncols == 3:
        # Contact table: School / Name / Email — give email plenty of room, no clipping
        col_widths = [w * 0.28, w * 0.28, w * 0.44]
    elif ncols == 4:
        col_widths = [w * 0.07, w * 0.20, w * 0.28, w * 0.45]
    elif ncols == 5:
        col_widths = [w * 0.07, w * 0.15, w * 0.20, w * 0.21, w * 0.37]
    else:
        col_widths = [w / ncols] * ncols

    line_h = 5.0

    # Header row (single line, no wrapping needed)
    pdf.set_fill_color(*NAVY)
    pdf.set_text_color(*WHITE)
    pdf.set_font("DejaVu", "B", base_size)
    for i, cell in enumerate(header):
        pdf.cell(col_widths[i], 7, cell, border=0, fill=True)
    pdf.ln()

    # Data rows — all columns use multi_cell for proper wrapping
    for ri, row in enumerate(rows):
        row_padded = (row + [""] * ncols)[:ncols]
        cleaned = []
        for cell in row_padded:
            plain = re.sub(r'\*\*([^*]+)\*\*', r'\1', cell)
            plain = re.sub(r'\*([^*]+)\*', r'\1', plain)
            plain = re.sub(r'`([^`]+)`', r'\1', plain)
            cleaned.append(plain)

        # Row height = max lines needed across all columns
        max_lines = max(
            count_wrapped_lines(pdf, text, cw, base_size)
            for text, cw in zip(cleaned, col_widths)
        )
        row_h = max_lines * line_h + 1

        # Force a clean page break before the row if it won't fit
        if pdf.get_y() + row_h > (pdf.h - MARGIN_B - 5):
            pdf.add_page()

        fill_color = ROW_ALT if (ri % 2 == 0) else WHITE
        y_row = pdf.get_y()

        # Disable auto page break for the whole row — no mid-row cascade
        pdf.set_auto_page_break(False)

        # Fill entire row background first, then draw text without fill
        pdf.set_fill_color(*fill_color)
        pdf.set_xy(MARGIN_L, y_row)
        pdf.cell(w, row_h, "", border=0, fill=True)

        pdf.set_text_color(*BODY)
        pdf.set_font("DejaVu", "", base_size)
        for i in range(ncols):
            pdf.set_xy(MARGIN_L + sum(col_widths[:i]), y_row)
            pdf.multi_cell(col_widths[i], line_h, cleaned[i], align="L", fill=False)

        pdf.set_auto_page_break(True, margin=MARGIN_B)
        pdf.set_y(y_row + row_h)

    pdf.ln(2)


def render_markdown(pdf, md_text):
    lines = md_text.split('\n')
    i = 0
    w = pdf.effective_width()

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Blank line
        if stripped == "":
            pdf.ln(3)
            i += 1
            continue

        # H1
        if stripped.startswith("# ") and not stripped.startswith("## "):
            text = stripped[2:].strip()
            pdf.ln(4)
            pdf.set_font("DejaVu", "B", 20)
            pdf.set_text_color(*NAVY)
            pdf.multi_cell(w, 9, text, align="L")
            # Thin rule
            pdf.set_draw_color(*RULE)
            pdf.set_line_width(0.5)
            x = pdf.get_x()
            y = pdf.get_y() + 1
            pdf.line(MARGIN_L, y, pdf.w - MARGIN_R, y)
            pdf.ln(4)
            i += 1
            continue

        # H2
        if stripped.startswith("## ") and not stripped.startswith("### "):
            text = stripped[3:].strip()
            pdf.ln(5)
            pdf.set_font("DejaVu", "B", 14)
            pdf.set_text_color(*BLUE_MID)
            pdf.multi_cell(w, 7, text, align="L")
            pdf.ln(1)
            i += 1
            continue

        # H3
        if stripped.startswith("### "):
            text = stripped[4:].strip()
            pdf.ln(3)
            pdf.set_font("DejaVu", "B", 11.5)
            pdf.set_text_color(*BLUE_LT)
            pdf.multi_cell(w, 6, text, align="L")
            pdf.ln(0.5)
            i += 1
            continue

        # H4 (#### )
        if stripped.startswith("#### "):
            text = stripped[5:].strip()
            pdf.ln(2)
            pdf.set_font("DejaVu", "B", 10.5)
            pdf.set_text_color(*BODY)
            pdf.multi_cell(w, 6, text, align="L")
            i += 1
            continue

        # HR (---) — thin rule
        if re.match(r'^-{3,}$', stripped):
            pdf.ln(2)
            pdf.set_draw_color(*RULE)
            pdf.set_line_width(0.3)
            y = pdf.get_y()
            pdf.line(MARGIN_L, y, pdf.w - MARGIN_R, y)
            pdf.ln(3)
            i += 1
            continue

        # Table — collect all table lines
        if stripped.startswith('|'):
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                table_lines.append(lines[i].strip())
                i += 1
            if table_lines:
                header, rows = parse_table(table_lines)
                render_table(pdf, header, rows)
            continue

        # Blockquote
        if stripped.startswith('> '):
            bq_text = stripped[2:]
            x_orig = pdf.get_x()
            y_start = pdf.get_y()
            # Left bar
            pdf.set_draw_color(*BQ_BAR)
            pdf.set_line_width(1.5)
            indent = 6
            pdf.set_x(MARGIN_L + indent)
            pdf.set_font("DejaVu", "I", 9.5)
            pdf.set_text_color(*BLOCKQUOTE)
            pdf.multi_cell(w - indent - 2, 5.5, bq_text, align="L")
            y_end = pdf.get_y()
            pdf.line(MARGIN_L + 1.5, y_start, MARGIN_L + 1.5, y_end)
            pdf.ln(1)
            i += 1
            continue

        # Unordered list item
        if stripped.startswith('- '):
            text = stripped[2:]
            bullet = "\u2022  "
            pdf.set_x(MARGIN_L + 4)
            pdf.set_font("DejaVu", "B", 10)
            pdf.set_text_color(*BLUE_MID)
            bullet_w = pdf.get_string_width(bullet)
            pdf.write(5.5, bullet)
            pdf.set_font("DejaVu", "", 10)
            pdf.set_text_color(*BODY)
            # Inline formatting in list items
            text_x = MARGIN_L + 4 + bullet_w
            pdf.set_x(text_x)
            # Use multi_cell for wrapping
            # Render inline bold
            inner_w = w - 4 - bullet_w
            # Simple approach: strip bold markers for multi_cell, handle inline below
            display = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
            display = re.sub(r'\*([^*]+)\*', r'\1', display)
            display = re.sub(r'`([^`]+)`', r'\1', display)
            pdf.multi_cell(inner_w, 5.5, display, align="L")
            i += 1
            continue

        # Numbered list item
        m = re.match(r'^(\d+)\.\s+(.*)', stripped)
        if m:
            num = m.group(1)
            text = m.group(2)
            label = f"{num}.  "
            pdf.set_x(MARGIN_L + 4)
            pdf.set_font("DejaVu", "B", 10)
            pdf.set_text_color(*BLUE_MID)
            label_w = pdf.get_string_width(label)
            pdf.write(5.5, label)
            pdf.set_font("DejaVu", "", 10)
            pdf.set_text_color(*BODY)
            text_x = MARGIN_L + 4 + label_w
            pdf.set_x(text_x)
            display = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
            display = re.sub(r'\*([^*]+)\*', r'\1', display)
            display = re.sub(r'`([^`]+)`', r'\1', display)
            pdf.multi_cell(w - 4 - label_w, 5.5, display, align="L")
            i += 1
            continue

        # Italic note line (starts with *text*)
        if re.match(r'^\*[^*].*\*$', stripped):
            text = stripped[1:-1]
            pdf.set_font("DejaVu", "I", 9)
            pdf.set_text_color(120, 130, 150)
            pdf.set_x(MARGIN_L)
            pdf.multi_cell(w, 5, text, align="L")
            i += 1
            continue

        # Regular paragraph
        pdf.set_x(MARGIN_L)
        pdf.set_font("DejaVu", "", 10)
        pdf.set_text_color(*BODY)
        # Strip markdown bold/italic for multi_cell (fpdf2 multi_cell doesn't support inline styles)
        display = re.sub(r'\*\*([^*]+)\*\*', r'\1', stripped)
        display = re.sub(r'\*([^*]+)\*', r'\1', display)
        display = re.sub(r'`([^`]+)`', r'\1', display)
        pdf.multi_cell(w, 5.5, display, align="L")
        i += 1


def md_to_pdf(md_path, pdf_path):
    with open(md_path, encoding="utf-8") as f:
        md_text = f.read()

    title = os.path.splitext(os.path.basename(md_path))[0]
    pdf = PDF(title=title)
    pdf.add_page()
    render_markdown(pdf, md_text)
    pdf.output(pdf_path)
    print(f"  Written: {pdf_path}")


def main():
    base = "/Users/pmackinnon/fun-projects/aerospace-study-usa"

    danish_docs = [
        ("da/README.md",            "da/pdf/01-oversigt.pdf"),
        ("da/landscape.md",         "da/pdf/02-landskabet.pdf"),
        ("da/programs.md",          "da/pdf/03-programmer.pdf"),
        ("da/application-guide.md", "da/pdf/04-ansøgningsguide.pdf"),
    ]

    english_docs = [
        ("README.md",            "en/pdf/01-overview.pdf"),
        ("landscape.md",         "en/pdf/02-landscape.pdf"),
        ("programs.md",          "en/pdf/03-programs.pdf"),
        ("application-guide.md", "en/pdf/04-application-guide.pdf"),
    ]

    for md_rel, pdf_rel in danish_docs + english_docs:
        pdf_path = os.path.join(base, pdf_rel)
        os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
        md_path  = os.path.join(base, md_rel)
        print(f"Processing {md_rel}...")
        md_to_pdf(md_path, pdf_path)

    print("\nAll PDFs written.")


if __name__ == "__main__":
    main()
