"""Build the bilingual one-page CV PDFs used by the portfolio website.

The layout follows the supplied CV reference: a full-height maroon sidebar with
the portrait and contact/skills information, then a compact white main column.
The builder uses ReportLab directly so both language versions share the same
measured geometry and stay on one A4 page.
"""

from __future__ import annotations

import argparse
import html
from pathlib import Path

from reportlab import rl_config
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "assets" / "documents"
PORTRAIT = OUTPUT_DIR / "cv-portrait.jpg"

# Reference colors sampled from the supplied original CV.
MAROON = HexColor("#7A1420")
INK = HexColor("#2B2B2B")
SIDEBAR_TEXT = HexColor("#F4EAEA")
WHITE = colors.white

PAGE_W, PAGE_H = A4
SIDEBAR_W = 203.0
MAIN_X = SIDEBAR_W + 19.0
MAIN_RIGHT = 19.0
MAIN_W = PAGE_W - MAIN_X - MAIN_RIGHT
SIDEBAR_PAD = 15.0
PHOTO_H = SIDEBAR_W * 4.0 / 3.0

# Keep repeat builds deterministic and avoid embedding a current timestamp.
rl_config.invariant = True


def register_fonts() -> None:
    """Register the Arial family used by the original-style layout."""

    font_dir = Path("C:/Windows/Fonts")
    fonts = {
        "Arial": font_dir / "arial.ttf",
        "Arial-Bold": font_dir / "arialbd.ttf",
        "Arial-Italic": font_dir / "ariali.ttf",
        "Arial-BoldItalic": font_dir / "arialbi.ttf",
    }
    for name, path in fonts.items():
        if not path.exists():
            raise FileNotFoundError(f"Required font is missing: {path}")
        if name not in pdfmetrics.getRegisteredFontNames():
            pdfmetrics.registerFont(TTFont(name, str(path)))


register_fonts()


CONTACTS = {
    "email": "aliyus.hedri@gmail.com",
    "gmail_url": "https://mail.google.com/mail/?view=cm&fs=1&to=aliyus.hedri@gmail.com",
    "linkedin": "linkedin.com/in/aliyushedri/",
    "linkedin_url": "https://www.linkedin.com/in/aliyushedri/",
    "github": "github.com/aliyushedri",
    "github_url": "https://github.com/aliyushedri",
    "portfolio": "aliyushedri-portfolio.tech",
    "portfolio_url": "https://aliyushedri-portfolio.tech/",
    "play_url": "https://play.google.com/store/apps/details?id=id.acslab.telubot",
}


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def link(label: str, url: str, color: str = "#7A1420", underline: bool = False) -> str:
    decoration = "1" if underline else "0"
    return (
        f'<link href="{esc(url)}" color="{color}" underline="{decoration}">'
        f"{esc(label)}</link>"
    )


def make_styles() -> dict[str, ParagraphStyle]:
    return {
        "name": ParagraphStyle(
            "cv-name", fontName="Arial-Bold", fontSize=24.0, leading=26.0, textColor=MAROON
        ),
        "role": ParagraphStyle(
            "cv-role", fontName="Arial", fontSize=10.0, leading=12.0, textColor=HexColor("#555555")
        ),
        "main-section": ParagraphStyle(
            "cv-main-section", fontName="Arial-Bold", fontSize=10.9, leading=12.6, textColor=MAROON
        ),
        "main-body": ParagraphStyle(
            "cv-main-body", fontName="Arial", fontSize=8.9, leading=11.2, textColor=INK,
            splitLongWords=False, wordWrap="LTR"
        ),
        "main-body-small": ParagraphStyle(
            "cv-main-body-small", fontName="Arial", fontSize=8.8, leading=10.8, textColor=INK,
            splitLongWords=False, wordWrap="LTR"
        ),
        "main-title": ParagraphStyle(
            "cv-main-title", fontName="Arial-Bold", fontSize=9.7, leading=11.6, textColor=INK,
            splitLongWords=False, wordWrap="LTR"
        ),
        "main-date": ParagraphStyle(
            "cv-main-date", fontName="Arial-Bold", fontSize=8.35, leading=10.0, textColor=MAROON,
            alignment=TA_RIGHT, splitLongWords=False
        ),
        "sidebar-section": ParagraphStyle(
            "cv-sidebar-section", fontName="Arial-Bold", fontSize=12.8, leading=14.6, textColor=WHITE
        ),
        "sidebar-label": ParagraphStyle(
            "cv-sidebar-label", fontName="Arial-Bold", fontSize=8.45, leading=9.7, textColor=SIDEBAR_TEXT
        ),
        "sidebar-body": ParagraphStyle(
            "cv-sidebar-body", fontName="Arial", fontSize=8.8, leading=10.9, textColor=SIDEBAR_TEXT,
            splitLongWords=False, wordWrap="LTR"
        ),
        "sidebar-skill-label": ParagraphStyle(
            "cv-sidebar-skill-label", fontName="Arial-Bold", fontSize=8.45, leading=9.7, textColor=WHITE
        ),
        "sidebar-skill-body": ParagraphStyle(
            "cv-sidebar-skill-body", fontName="Arial", fontSize=8.8, leading=10.5, textColor=SIDEBAR_TEXT,
            splitLongWords=False, wordWrap="LTR"
        ),
    }


CONTENT = {
    "en": {
        "role": "Freelance Robotics, Embedded Systems & IoT",
        "contact_heading": "CONTACT", "location_label": "LOCATION", "location": "Bandung, West Java",
        "whatsapp_label": "WHATSAPP", "whatsapp": "@aliyushedri", "email_label": "GMAIL",
        "linkedin_label": "LINKEDIN", "github_label": "GITHUB", "portfolio_label": "PORTFOLIO",
        "scope_label": "SCOPE", "scope": "Remote work; onsite by discussion.",
        "languages_heading": "LANGUAGES",
        "language_rows": [("Indonesian", "Native"), ("English", "Intermediate / Working proficiency")],
        "skills_heading": "SKILLS",
        "skills": [
            ("Programming", "C/C++, Python, MATLAB, JavaScript"),
            ("Robotics & SLAM", "ROS/ROS2, FAST-LIO, SLAM, sensor fusion, mobile & legged robots"),
            ("Embedded & IoT", "Arduino, ESP32, STM32, Raspberry Pi, MQTT, HTTP/REST"),
            ("AI & automation", "OpenCV, YOLOv8, ML/DL, TensorFlow/PyTorch, LLM and Telegram bots"),
            ("Android & web", "Android Studio, HTML/CSS/JS, GitHub Pages"),
            ("Electronics & research", "EasyEDA, EasyEDA Pro / PCB, Git/Linux, LaTeX, technical writing"),
        ],
        "summary_heading": "SUMMARY",
        "summary": (
            "Electrical Engineering Master by Research student at Telkom University, conducting research with "
            "ACS Laboratory. Focused on robotics, LiDAR-inertial odometry / SLAM, embedded systems, IoT, "
            "automation, and AI. Available for freelance and project-based work. Remote work; onsite by discussion."
        ),
        "education_heading": "EDUCATION",
        "education": [
            ("Master by Research in Electrical Engineering - Telkom University", "Ongoing", "ACS Laboratory, Bandung."),
            ("Bachelor of Engineering in Electrical Engineering - Telkom University", "2022 - 2026", "GPA 3.8 / 4.0 - APERTI BUMN Scholarship Awardee 2022."),
            ("SMA Negeri Plus Provinsi Riau, Pekanbaru", "2019 - 2022", "Science major."),
        ],
        "internship_heading": "INTERNSHIP",
        "internship": ("Mechatronics Engineer - PT Arthatronic Studio Teknologi", "30 Jun - 9 Aug 2025"),
        "projects_heading": "SELECTED PROJECTS",
        "projects": [
            ("TEL-U BOT Android application", "2026", "Published Android app built with Android Studio, supporting lecturer research through local Wi-Fi UDP control of an ESP32 robot, actuator commands, line/LiDAR/odometry telemetry, calibration, planner and JSON tools. " + link("Google Play - TEL-U BOT", CONTACTS["play_url"])),
            ("Final-year project - 3D SLAM for AGV using FAST-LIO", "2026", "Adapted FAST-LIO for four Kinect V1 RGB-D cameras on ROS2 Jazzy with an STM32 + Mini PC distributed architecture."),
            ("TIRNARA - IoT fish-farming water-quality monitor", "2025", "Portable biofloc water-quality monitor using IoT and renewable energy; PIMNAS 2025 participant, PKM-KI."),
            ("Household water-quality monitoring system", "Feb - Jun 2025", "ESP32 with pH, temperature, and turbidity sensors; real-time MQTT / HTTP cloud dashboard."),
            ("ARJUNA hexapod robot", "2023 - 2024", "Led development of a six-legged robot with IMU balance and real-time YOLOv8 detection; KRI 2024 SAR finalist."),
            ("TOMOT plant-monitoring stick (PKM-KI)", "Mar - Nov 2024", "Portable pH, moisture, NPK, and temperature monitor; Bronze Medal, PIMNAS 37 presentation."),
            ("Bilingual portfolio website", "2026", "Built an HTML / CSS / JavaScript GitHub Pages portfolio with bilingual project pages, certificates, and downloadable CV. " + link("aliyushedri-portfolio.tech", CONTACTS["portfolio_url"])),
        ],
        "organization_heading": "ORGANIZATION",
        "organization": [
            ("Lab Coordinator - EIRRG (Electronics & Intelligence Robotics Research Group)", "2024 - 2025"),
            ("Basic Computer Laboratory Assistant", "2023 - 2025"),
            ("Committee Member - Telkom University Student Orientation (PKKMB)", "2023"),
        ],
        "awards_heading": "AWARDS & ACHIEVEMENTS",
        "awards": [
            "Top 20 Outstanding Students in Student Affairs - Telkom University, 2024.",
            "Finalist, Kontes Robot Indonesia 2024 SAR division - Team Leader, ARJUNA.",
            "Bronze Medal, PIMNAS 37 (2024) presentation - PKM-KI, TOMOT.",
            "Participant, PIMNAS 2025 - PKM-KI, TIRNARA.",
            "2nd Place, Laboratory Competency Contest - Pekan Raya Biologi 2020, Universitas Riau.",
            "Participant, Madrasah Science Competition (KSM) 2021, Biology, Riau.",
        ],
    },
    "id": {
        "role": "Freelance Robotika, Embedded Systems & IoT",
        "contact_heading": "KONTAK", "location_label": "LOKASI", "location": "Bandung, Jawa Barat",
        "whatsapp_label": "WHATSAPP", "whatsapp": "@aliyushedri", "email_label": "GMAIL",
        "linkedin_label": "LINKEDIN", "github_label": "GITHUB", "portfolio_label": "PORTOFOLIO",
        "scope_label": "SKEMA KERJA", "scope": "Remote; onsite dibahas sesuai proyek.",
        "languages_heading": "BAHASA",
        "language_rows": [("Indonesia", "Bahasa ibu"), ("Inggris", "Menengah")],
        "skills_heading": "KEAHLIAN",
        "skills": [
            ("Pemrograman", "C/C++, Python, MATLAB, JavaScript"),
            ("Robotika & SLAM", "ROS/ROS2, FAST-LIO, SLAM, sensor fusion, robot mobile & berkaki"),
            ("Embedded & IoT", "Arduino, ESP32, STM32, Raspberry Pi, MQTT, HTTP/REST"),
            ("AI & otomasi", "OpenCV, YOLOv8, ML/DL, TensorFlow/PyTorch, LLM dan bot Telegram"),
            ("Android & web", "Android Studio, HTML/CSS/JS, GitHub Pages"),
            ("Elektronika & riset", "EasyEDA, EasyEDA Pro / PCB, Git/Linux, LaTeX, penulisan teknis"),
        ],
        "summary_heading": "RINGKASAN",
        "summary": (
            "Mahasiswa Master by Research Teknik Elektro di Telkom University yang melakukan riset bersama ACS "
            "Laboratory. Berfokus pada robotika, LiDAR-inertial odometry / SLAM, embedded systems, IoT, otomasi, "
            "dan AI. Terbuka untuk pekerjaan freelance dan berbasis proyek. Pekerjaan remote; onsite dibahas sesuai proyek."
        ),
        "education_heading": "PENDIDIKAN",
        "education": [
            ("Master by Research Teknik Elektro - Telkom University", "Sedang berjalan", "ACS Laboratory, Bandung."),
            ("Sarjana Teknik Elektro - Telkom University", "2022 - 2026", "IPK 3,8 / 4,0 - Penerima Beasiswa APERTI BUMN 2022."),
            ("SMA Negeri Plus Provinsi Riau, Pekanbaru", "2019 - 2022", "Jurusan IPA."),
        ],
        "internship_heading": "PENGALAMAN MAGANG",
        "internship": ("Mechatronics Engineer - PT Arthatronic Studio Teknologi", "30 Jun - 9 Agu 2025"),
        "projects_heading": "PENGALAMAN PROYEK",
        "projects": [
            ("Aplikasi Android TEL-U BOT", "2026", "Aplikasi Android yang dibuat dengan Android Studio dan dipublikasikan untuk mendukung riset dosen melalui kendali UDP Wi-Fi lokal robot ESP32, aktuator, telemetri line/LiDAR/odometri, kalibrasi, planner, dan JSON. " + link("Google Play - TEL-U BOT", CONTACTS["play_url"])),
            ("Tugas akhir - 3D SLAM untuk AGV dengan FAST-LIO", "2026", "Adaptasi FAST-LIO untuk empat kamera RGB-D Kinect V1 pada ROS2 Jazzy dengan arsitektur STM32 + Mini PC terdistribusi."),
            ("TIRNARA - monitoring kualitas air budidaya ikan berbasis IoT", "2025", "Monitor kualitas air bioflok portabel berbasis IoT dan renewable energy; peserta PIMNAS 2025, kelas PKM-KI."),
            ("Sistem monitoring kualitas air rumah tangga", "Feb - Jun 2025", "ESP32 dengan sensor pH, suhu, dan kekeruhan; dashboard cloud melalui MQTT / HTTP secara real-time."),
            ("Robot hexapod ARJUNA", "2023 - 2024", "Memimpin pengembangan robot berkaki enam dengan keseimbangan IMU dan deteksi YOLOv8 real-time; finalis KRI 2024 divisi SAR."),
            ("TOMOT - tongkat monitoring tanaman (PKM-KI)", "Mar - Nov 2024", "Monitor portabel pH, kelembaban, NPK, dan suhu; Medali Perunggu, presentasi PIMNAS 37."),
            ("Website portofolio bilingual", "2026", "Membangun portofolio HTML / CSS / JavaScript di GitHub Pages dengan halaman proyek, sertifikat, dan CV bilingual. " + link("aliyushedri-portfolio.tech", CONTACTS["portfolio_url"])),
        ],
        "organization_heading": "ORGANISASI",
        "organization": [
            ("Koordinator Lab - EIRRG (Electronics & Intelligence Robotics Research Group)", "2024 - 2025"),
            ("Asisten Laboratorium Dasar Komputer", "2023 - 2025"),
            ("Panitia Orientasi Mahasiswa Telkom University (PKKMB)", "2023"),
        ],
        "awards_heading": "PRESTASI & PENGHARGAAN",
        "awards": [
            "Top 20 Mahasiswa Berprestasi Bidang Kemahasiswaan - Telkom University, 2024.",
            "Finalis Kontes Robot Indonesia 2024 divisi SAR - Ketua Tim, ARJUNA.",
            "Medali Perunggu PIMNAS 37 (2024) kategori Presentasi - PKM-KI, TOMOT.",
            "Peserta PIMNAS 2025 - kelas PKM-KI, TIRNARA.",
            "Juara II Uji Kompetensi Laboratorium - Pekan Raya Biologi 2020, Universitas Riau.",
            "Peserta Kompetisi Sains Madrasah (KSM) 2021 - Biologi, Riau.",
        ],
    },
}


def draw_paragraph(canvas: Canvas, markup: str, style: ParagraphStyle, x: float, top: float, width: float) -> float:
    paragraph = Paragraph(markup, style)
    _, height = paragraph.wrap(width, PAGE_H)
    paragraph.drawOn(canvas, x, top - height)
    return height


def draw_rule(canvas: Canvas, x: float, y: float, width: float, color: colors.Color = MAROON, thickness: float = 1.2) -> None:
    canvas.saveState()
    canvas.setStrokeColor(color)
    canvas.setLineWidth(thickness)
    canvas.line(x, y, x + width, y)
    canvas.restoreState()


def draw_main_heading(canvas: Canvas, title: str, x: float, top: float, width: float, styles: dict[str, ParagraphStyle]) -> float:
    height = draw_paragraph(canvas, esc(title), styles["main-section"], x, top, width)
    draw_rule(canvas, x, top - height - 3.2, width, MAROON, 1.25)
    return height + 9.0


def draw_sidebar_heading(canvas: Canvas, title: str, x: float, top: float, width: float, styles: dict[str, ParagraphStyle]) -> float:
    height = draw_paragraph(canvas, esc(title), styles["sidebar-section"], x, top, width)
    draw_rule(canvas, x, top - height - 3.0, width, SIDEBAR_TEXT, 0.9)
    return height + 10.0


def draw_entry(canvas: Canvas, title: str, period: str, body: str | None, x: float, top: float, width: float, styles: dict[str, ParagraphStyle], body_style: str = "main-body") -> float:
    date_width = min(92.0, max(55.0, pdfmetrics.stringWidth(period, styles["main-date"].fontName, styles["main-date"].fontSize) + 4.0))
    title_width = width - date_width - 6.0
    title_height = draw_paragraph(canvas, esc(title), styles["main-title"], x, top, title_width)
    date_height = draw_paragraph(canvas, esc(period), styles["main-date"], x + width - date_width, top, date_width)
    used = max(title_height, date_height)
    if body:
        body_height = draw_paragraph(canvas, body, styles[body_style], x + 8.0, top - used - 1.0, width - 8.0)
        used += 1.0 + body_height
    return used + 4.0


def draw_bullet(canvas: Canvas, text: str, x: float, top: float, width: float, styles: dict[str, ParagraphStyle]) -> float:
    # A small square matches the original CV's maroon bullets without relying
    # on a font-specific bullet glyph.
    canvas.saveState()
    canvas.setFillColor(MAROON)
    canvas.rect(x, top - 7.0, 2.7, 2.7, stroke=0, fill=1)
    canvas.restoreState()
    height = draw_paragraph(canvas, esc(text), styles["main-body-small"], x + 9.0, top, width - 9.0)
    return height + 2.0


def draw_sidebar(canvas: Canvas, locale: str, styles: dict[str, ParagraphStyle]) -> None:
    data = CONTENT[locale]
    canvas.saveState()
    canvas.setFillColor(MAROON)
    canvas.rect(0, 0, SIDEBAR_W, PAGE_H, stroke=0, fill=1)
    canvas.restoreState()

    if not PORTRAIT.exists():
        raise FileNotFoundError(f"Portrait asset is missing: {PORTRAIT}")
    canvas.drawImage(str(PORTRAIT), 0, PAGE_H - PHOTO_H, width=SIDEBAR_W, height=PHOTO_H, preserveAspectRatio=False, mask="auto")

    x = SIDEBAR_PAD
    width = SIDEBAR_W - 2 * SIDEBAR_PAD
    top = PAGE_H - PHOTO_H - 14.0

    top -= draw_sidebar_heading(canvas, data["contact_heading"], x, top, width, styles)
    contact_items = [
        (data["location_label"], data["location"], None),
        (data["whatsapp_label"], data["whatsapp"], None),
        (data["email_label"], CONTACTS["email"], CONTACTS["gmail_url"]),
        (data["linkedin_label"], CONTACTS["linkedin"], CONTACTS["linkedin_url"]),
        (data["github_label"], CONTACTS["github"], CONTACTS["github_url"]),
        (data["portfolio_label"], CONTACTS["portfolio"], CONTACTS["portfolio_url"]),
    ]
    for label, value, url in contact_items:
        top -= draw_paragraph(canvas, esc(label), styles["sidebar-label"], x, top, width)
        rendered = link(value, url, "#F4EAEA") if url else esc(value)
        top -= draw_paragraph(canvas, rendered, styles["sidebar-body"], x, top, width) + 4.3

    top -= draw_paragraph(canvas, esc(data["scope_label"]), styles["sidebar-label"], x, top, width)
    top -= draw_paragraph(canvas, esc(data["scope"]), styles["sidebar-body"], x, top, width) + 3.0

    top -= 4.0
    top -= draw_sidebar_heading(canvas, data["languages_heading"], x, top, width, styles)
    for label, value in data["language_rows"]:
        markup = f"<b>{esc(label)}</b> - {esc(value)}"
        top -= draw_paragraph(canvas, markup, styles["sidebar-body"], x, top, width) + 3.0

    top -= 5.0
    top -= draw_sidebar_heading(canvas, data["skills_heading"], x, top, width, styles)
    for label, value in data["skills"]:
        top -= draw_paragraph(canvas, esc(label), styles["sidebar-skill-label"], x, top, width)
        top -= draw_paragraph(canvas, esc(value), styles["sidebar-skill-body"], x, top, width) + 3.5

    if top < 12.0:
        raise RuntimeError(f"Sidebar overflow for {locale}: {top:.1f} points remaining")


def draw_main(canvas: Canvas, locale: str, styles: dict[str, ParagraphStyle]) -> None:
    data = CONTENT[locale]
    x = MAIN_X
    width = MAIN_W
    top = PAGE_H - 17.0

    top -= draw_paragraph(canvas, "ALIYUS HEDRI", styles["name"], x, top, width)
    top -= 1.0
    top -= draw_paragraph(canvas, esc(data["role"]), styles["role"], x, top, width)
    top -= 4.0

    top -= draw_main_heading(canvas, data["summary_heading"], x, top, width, styles)
    top -= draw_paragraph(canvas, data["summary"], styles["main-body"], x, top, width) + 4.0

    top -= draw_main_heading(canvas, data["education_heading"], x, top, width, styles)
    for title, period, body in data["education"]:
        top -= draw_entry(canvas, title, period, esc(body), x, top, width, styles, "main-body-small")

    top -= draw_main_heading(canvas, data["internship_heading"], x, top, width, styles)
    title, period = data["internship"]
    top -= draw_entry(canvas, title, period, None, x, top, width, styles)

    top -= draw_main_heading(canvas, data["projects_heading"], x, top, width, styles)
    for title, period, body in data["projects"]:
        top -= draw_entry(canvas, title, period, body, x, top, width, styles, "main-body-small")

    top -= draw_main_heading(canvas, data["organization_heading"], x, top, width, styles)
    for title, period in data["organization"]:
        top -= draw_entry(canvas, title, period, None, x, top, width, styles)

    top -= draw_main_heading(canvas, data["awards_heading"], x, top, width, styles)
    for award in data["awards"]:
        top -= draw_bullet(canvas, award, x, top, width, styles)

    if top < 13.0:
        raise RuntimeError(f"Main column overflow for {locale}: {top:.1f} points remaining")


def build(locale: str, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    canvas = Canvas(str(output), pagesize=A4, pageCompression=1)
    canvas.setTitle("Aliyus Hedri CV" if locale == "en" else "CV Aliyus Hedri")
    canvas.setAuthor("Aliyus Hedri")
    canvas.setSubject("Curriculum vitae")
    styles = make_styles()
    draw_sidebar(canvas, locale, styles)
    draw_main(canvas, locale, styles)
    canvas.showPage()
    canvas.save()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--language", choices=("en", "id", "both"), default="both")
    parser.add_argument("--output-dir", type=Path, default=OUTPUT_DIR)
    args = parser.parse_args()
    targets = {
        "en": args.output_dir / "CV-Aliyus-Hedri-EN.pdf",
        "id": args.output_dir / "CV-Aliyus-Hedri.pdf",
    }
    locales = ("en", "id") if args.language == "both" else (args.language,)
    for locale in locales:
        build(locale, targets[locale])
        print(f"Built {targets[locale]}")


if __name__ == "__main__":
    main()
