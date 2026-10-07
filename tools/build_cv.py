"""Build the bilingual, two-page CV PDFs for the portfolio site.

The content in this file is intentionally kept close to the supported portfolio
facts and the current service brief. The generated PDFs are static, selectable
text documents with clickable contact and project links.
"""

from __future__ import annotations

import argparse
from html import escape
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab import rl_config
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "assets" / "documents"

NAVY = HexColor("#14263D")
BLUE = HexColor("#1C5D85")
INK = HexColor("#1F2933")
MUTED = HexColor("#52606D")
PALE_BLUE = HexColor("#EEF5F8")
RULE = HexColor("#C9D6DE")
WHITE = colors.white

# Keep repeated builds byte-stable apart from any future intentional content
# change. This also avoids embedding the current build timestamp in metadata.
rl_config.invariant = True

PAGE_W, PAGE_H = A4
LEFT = 17 * mm
RIGHT = 17 * mm
TOP = 15 * mm
BOTTOM = 16 * mm
CONTENT_W = PAGE_W - LEFT - RIGHT


def e(value: str) -> str:
    """Escape plain text for ReportLab's small XML-like markup."""

    return escape(value, quote=True)


def link(label: str, url: str, color: str = "#1C5D85") -> str:
    return (
        f'<link href="{e(url)}" color="{color}" underline="1">{e(label)}</link>'
    )


def styles(locale: str) -> dict[str, ParagraphStyle]:
    indonesian = locale == "id"
    body_font = "Helvetica"
    bold_font = "Helvetica-Bold"
    return {
        "name": ParagraphStyle(
            "cv-name",
            fontName=bold_font,
            fontSize=25,
            leading=28,
            textColor=NAVY,
            spaceAfter=1.5 * mm,
        ),
        "role": ParagraphStyle(
            "cv-role",
            fontName=body_font,
            fontSize=10.5,
            leading=13,
            textColor=BLUE,
            spaceAfter=2.5 * mm,
        ),
        "contact": ParagraphStyle(
            "cv-contact",
            fontName=body_font,
            fontSize=7.9,
            leading=11.5,
            textColor=MUTED,
            spaceAfter=0,
        ),
        "section": ParagraphStyle(
            "cv-section",
            fontName=bold_font,
            fontSize=10.2,
            leading=12,
            textColor=NAVY,
            spaceBefore=3.5 * mm,
            spaceAfter=1.2 * mm,
            uppercase=True,
        ),
        "body": ParagraphStyle(
            "cv-body",
            fontName=body_font,
            fontSize=9.5,
            leading=12.2,
            textColor=INK,
            spaceAfter=1.5 * mm,
            splitLongWords=False,
        ),
        "body_tight": ParagraphStyle(
            "cv-body-tight",
            fontName=body_font,
            fontSize=9.2,
            leading=11.8,
            textColor=INK,
            spaceAfter=1.1 * mm,
            splitLongWords=False,
        ),
        "entry_title": ParagraphStyle(
            "cv-entry-title",
            fontName=bold_font,
            fontSize=8.75,
            leading=10.7,
            textColor=INK,
            spaceAfter=0.45 * mm,
        ),
        "entry_meta": ParagraphStyle(
            "cv-entry-meta",
            fontName=body_font,
            fontSize=7.75,
            leading=9.5,
            textColor=MUTED,
            spaceAfter=0.7 * mm,
        ),
        "small": ParagraphStyle(
            "cv-small",
            fontName=body_font,
            fontSize=7.55,
            leading=9.5,
            textColor=MUTED,
            spaceAfter=0.9 * mm,
        ),
        "callout": ParagraphStyle(
            "cv-callout",
            fontName=body_font,
            fontSize=8.5,
            leading=11.2,
            textColor=NAVY,
            leftIndent=1.5 * mm,
            rightIndent=1.5 * mm,
            spaceAfter=0,
        ),
        "page_note": ParagraphStyle(
            "cv-page-note",
            fontName=body_font,
            fontSize=7.5,
            leading=9.5,
            textColor=MUTED,
            alignment=TA_RIGHT,
        ),
    }


CONTACTS = {
    "location_en": "Bandung, West Java, Indonesia",
    "location_id": "Bandung, Jawa Barat, Indonesia",
    "whatsapp": "WhatsApp @aliyushedri",
    "email": "aliyus.hedri@gmail.com",
    "linkedin": "linkedin.com/in/aliyushedri/",
    "github": "github.com/aliyushedri",
    "portfolio": "aliyushedri-portfolio.tech",
    "linkedin_url": "https://www.linkedin.com/in/aliyushedri/",
    "github_url": "https://github.com/aliyushedri",
    "portfolio_url": "https://aliyushedri-portfolio.tech/",
    "play_url": "https://play.google.com/store/apps/details?id=id.acslab.telubot",
}


CONTENT = {
    "en": {
        "role": "Freelance Robotics, Embedded Systems & IoT",
        "engagement": (
            "Remote freelance and project-based work. Onsite collaboration and scope are "
            "discussed per project."
        ),
        "engagement_label": "Engagement",
        "summary": (
            "Electrical Engineering Master by Research student at Telkom University, "
            "supporting research at ACS Laboratory. I work across robotics, SLAM, "
            "embedded systems, IoT, automation, and AI, with a practical focus on "
            "integrating sensors, firmware, software, and operator tools."
        ),
        "services": [
            (
                "Robotics & SLAM",
                "Mobile and legged robot integration, LiDAR-inertial odometry / SLAM, sensor fusion, and ROS2 workflows.",
            ),
            (
                "Embedded & IoT",
                "Arduino, ESP32, Raspberry Pi, sensor interfacing, MQTT / HTTP, telemetry, and connected prototypes.",
            ),
            (
                "Programming",
                "C/C++, Python, and MATLAB for embedded control, computer vision, data work, and system integration.",
            ),
            (
                "Automation & AI",
                "Automation workflows, LLM integrations, Telegram bots with or without AI, and ML / DL training for image detection and processing in embedded or standalone setups.",
            ),
            (
                "Android & web",
                "Android Studio development for robot control and research support, plus HTML / CSS / JavaScript portfolio work on GitHub Pages.",
            ),
            (
                "Electronics & writing",
                "PCB design with EasyEDA / EasyEDA Pro, and technical paper or journal editing with LaTeX support.",
            ),
        ],
        "selected_projects": "SELECTED PROJECTS",
        "projects": [
            {
                "title": "TEL-U BOT Android application",
                "period": "2026",
                "body": (
                    "Android Studio application developed to support TEL-U BOT robot research. "
                    "The published app supports local Wi-Fi UDP control with ESP32, robot speed and direction, "
                    "actuator control, line / LiDAR / odometry telemetry, calibration and settings, planner "
                    "configuration, EEPROM planner read / write / test, and JSON import / export. "
                    "<i>Published listing:</i> "
                    + link("Google Play - TEL-U BOT", CONTACTS["play_url"])
                    + "."
                ),
            },
            {
                "title": "3D SLAM for AGV using FAST-LIO",
                "period": "2026",
                "body": (
                    "Final-year project focused on adapting FAST-LIO for four low-cost Kinect V1 RGB-D cameras "
                    "and a distributed STM32 + Mini PC architecture on ROS2 Jazzy."
                ),
            },
            {
                "title": "Bilingual portfolio website",
                "period": "2026",
                "body": (
                    "Designed and built a personal HTML / CSS / JavaScript portfolio for GitHub Pages, with "
                    "bilingual project pages, certificate views, and downloadable CVs. "
                    + link("View portfolio", CONTACTS["portfolio_url"])
                    + "."
                ),
            },
            {
                "title": "ARJUNA hexapod robot",
                "period": "2023 - 2024",
                "body": (
                    "Led the team developing a six-legged robot with IMU-based automatic balance and real-time "
                    "YOLOv8 object detection. Team ARJUNA became a finalist in the 2024 Kontes Robot Indonesia "
                    "SAR division."
                ),
            },
        ],
        "experience": "EXPERIENCE & LEADERSHIP",
        "experience_entries": [
            (
                "Mechatronics Engineering Intern - PT Arthatronic Studio Teknologi",
                "30 Jun - 9 Aug 2025",
                "Mechatronics engineering internship.",
            ),
            (
                "Lab Coordinator - EIRRG",
                "2024 - 2025",
                "Electronics & Intelligence Robotics Research Group.",
            ),
            (
                "Basic Computer Laboratory Assistant",
                "2023 - 2025",
                "Telkom University laboratory role.",
            ),
            (
                "Committee Member - Telkom University Student Orientation (PKKMB)",
                "2023",
                "Student orientation committee.",
            ),
        ],
        "education": "EDUCATION",
        "education_entries": [
            (
                "Master by Research in Electrical Engineering - Telkom University",
                "Ongoing - Bandung",
                "Current S2 program; research context at ACS Laboratory.",
            ),
            (
                "Bachelor of Engineering in Electrical Engineering - Telkom University",
                "2022 - 2026",
                "GPA 3.8 / 4.0 - APERTI BUMN Scholarship Awardee 2022.",
            ),
            (
                "SMA Negeri Plus Provinsi Riau, Pekanbaru",
                "2019 - 2022",
                "Science major - graduated with good standing.",
            ),
        ],
        "additional_projects": "ADDITIONAL PROJECTS",
        "additional_project_entries": [
            (
                "TIRNARA - IoT water-quality monitoring for fish farming",
                "2025",
                "Portable biofloc water-quality monitoring product using IoT and renewable energy. Participant in PIMNAS 2025, PKM-KI class.",
            ),
            (
                "Household water-quality monitoring system",
                "Feb - Jun 2025",
                "ESP32 prototype with pH, temperature, and turbidity sensors; real-time data transmission through MQTT / HTTP to a cloud dashboard.",
            ),
            (
                "TOMOT - plant monitoring stick (PKM-KI)",
                "Mar - Nov 2024",
                "Portable soil monitoring device with pH, moisture, NPK, and temperature sensors. Bronze Medal, PIMNAS 37 presentation category.",
            ),
        ],
        "toolkit": "TOOLKIT",
        "toolkit_text": (
            "C/C++, Python, Arduino, ESP32, Raspberry Pi, STM32, ROS / ROS2, FAST-LIO, SLAM, IMU, "
            "LiDAR, RGB-D cameras, OpenCV, YOLOv8, TensorFlow / PyTorch, NumPy / Pandas, MQTT, HTTP / REST, "
            "Android Studio, EasyEDA, EasyEDA Pro, MATLAB / Simulink, Git / GitHub, Linux, and LaTeX."
        ),
        "awards": "SELECTED AWARDS",
        "awards_entries": [
            "Top 20 Outstanding Students in Student Affairs - Telkom University, 2024.",
            "Finalist, Kontes Robot Indonesia 2024, SAR division - Team Leader, ARJUNA.",
            "Bronze Medal, PIMNAS 37 (2024), presentation category - PKM-KI, TOMOT.",
            "Participant, PIMNAS 2025 - PKM-KI class, TIRNARA.",
            "2nd Place, Laboratory Competency Contest - Pekan Raya Biologi 2020, Universitas Riau.",
            "Participant, Madrasah Science Competition (KSM) 2021, Biology, Riau Province.",
        ],
        "languages": "LANGUAGES",
        "languages_text": "Indonesian - native. English - intermediate / working proficiency.",
        "page2_note": "Project details and supporting certificates: aliyushedri-portfolio.tech",
    },
    "id": {
        "role": "Freelance Robotika, Embedded Systems & IoT",
        "engagement": (
            "Pekerjaan freelance dan berbasis proyek secara remote. Kolaborasi onsite dan ruang lingkup "
            "dibahas sesuai kebutuhan proyek."
        ),
        "engagement_label": "Skema kerja",
        "summary": (
            "Mahasiswa Master by Research Teknik Elektro di Telkom University yang mendukung riset di ACS "
            "Laboratory. Bekerja pada robotika, SLAM, embedded systems, IoT, otomasi, dan AI, dengan fokus "
            "praktis pada integrasi sensor, firmware, perangkat lunak, dan alat bantu operator."
        ),
        "services": [
            (
                "Robotika & SLAM",
                "Integrasi robot mobile dan berkaki, LiDAR-inertial odometry / SLAM, sensor fusion, dan workflow ROS2.",
            ),
            (
                "Embedded & IoT",
                "Arduino, ESP32, Raspberry Pi, antarmuka sensor, MQTT / HTTP, telemetri, dan prototipe terhubung.",
            ),
            (
                "Pemrograman",
                "C/C++, Python, dan MATLAB untuk kendali embedded, computer vision, pengolahan data, dan integrasi sistem.",
            ),
            (
                "Otomasi & AI",
                "Workflow otomasi, integrasi LLM, bot Telegram dengan atau tanpa AI, serta pelatihan ML / DL untuk deteksi dan pemrosesan citra pada sistem embedded atau standalone.",
            ),
            (
                "Android & web",
                "Pengembangan Android Studio untuk kendali robot dan dukungan riset, serta pekerjaan HTML / CSS / JavaScript untuk portofolio di GitHub Pages.",
            ),
            (
                "Elektronika & penulisan",
                "Desain PCB dengan EasyEDA / EasyEDA Pro, serta penyuntingan paper atau jurnal teknis dengan dukungan LaTeX.",
            ),
        ],
        "selected_projects": "PROYEK PILIHAN",
        "projects": [
            {
                "title": "Aplikasi Android TEL-U BOT",
                "period": "2026",
                "body": (
                    "Aplikasi Android Studio yang dikembangkan untuk mendukung riset robot TEL-U BOT. "
                    "Aplikasi yang dipublikasikan mendukung kendali UDP melalui Wi-Fi lokal dengan ESP32, kecepatan "
                    "dan arah robot, aktuator, telemetri line / LiDAR / odometri, kalibrasi dan pengaturan, konfigurasi "
                    "planner, baca / tulis / uji planner EEPROM, serta impor / ekspor JSON. "
                    "<i>Listing:</i> "
                    + link("Google Play - TEL-U BOT", CONTACTS["play_url"])
                    + "."
                ),
            },
            {
                "title": "3D SLAM untuk AGV dengan FAST-LIO",
                "period": "2026",
                "body": (
                    "Tugas akhir yang berfokus pada adaptasi FAST-LIO untuk empat kamera RGB-D Kinect V1 murah dan "
                    "arsitektur komputasi terdistribusi STM32 + Mini PC pada ROS2 Jazzy."
                ),
            },
            {
                "title": "Website portofolio bilingual",
                "period": "2026",
                "body": (
                    "Merancang dan membangun portofolio pribadi HTML / CSS / JavaScript untuk GitHub Pages, dengan "
                    "halaman proyek bilingual, tampilan sertifikat, dan CV yang dapat diunduh. "
                    + link("Lihat portofolio", CONTACTS["portfolio_url"])
                    + "."
                ),
            },
            {
                "title": "Robot hexapod ARJUNA",
                "period": "2023 - 2024",
                "body": (
                    "Memimpin tim yang mengembangkan robot berkaki enam dengan keseimbangan otomatis berbasis IMU dan "
                    "deteksi objek YOLOv8 secara real-time. Tim ARJUNA menjadi finalis Kontes Robot Indonesia 2024 "
                    "divisi SAR."
                ),
            },
        ],
        "experience": "PENGALAMAN & KEPEMIMPINAN",
        "experience_entries": [
            (
                "Magang Mechatronics Engineer - PT Arthatronic Studio Teknologi",
                "30 Jun - 9 Agu 2025",
                "Magang pada bidang mechatronics engineering.",
            ),
            (
                "Koordinator Lab - EIRRG",
                "2024 - 2025",
                "Electronics & Intelligence Robotics Research Group.",
            ),
            (
                "Asisten Laboratorium Dasar Komputer",
                "2023 - 2025",
                "Peran laboratorium di Telkom University.",
            ),
            (
                "Panitia PKKMB Telkom University",
                "2023",
                "Panitia orientasi mahasiswa.",
            ),
        ],
        "education": "PENDIDIKAN",
        "education_entries": [
            (
                "Master by Research Teknik Elektro - Telkom University",
                "Sedang berjalan - Bandung",
                "Program S2 saat ini; konteks riset di ACS Laboratory.",
            ),
            (
                "Sarjana Teknik Elektro - Telkom University",
                "2022 - 2026",
                "IPK 3,8 / 4,0 - Penerima Beasiswa APERTI BUMN 2022.",
            ),
            (
                "SMA Negeri Plus Provinsi Riau, Pekanbaru",
                "2019 - 2022",
                "Jurusan IPA - lulus dengan predikat baik.",
            ),
        ],
        "additional_projects": "PROYEK LAINNYA",
        "additional_project_entries": [
            (
                "TIRNARA - monitoring kualitas air budidaya ikan berbasis IoT",
                "2025",
                "Produk portable monitoring kualitas air bioflok berbasis IoT dan renewable energy. Peserta PIMNAS 2025, kelas PKM-KI.",
            ),
            (
                "Sistem monitoring kualitas air rumah tangga",
                "Feb - Jun 2025",
                "Prototipe ESP32 dengan sensor pH, suhu, dan kekeruhan; pengiriman data real-time melalui MQTT / HTTP ke dashboard cloud.",
            ),
            (
                "TOMOT - tongkat monitoring tanaman (PKM-KI)",
                "Mar - Nov 2024",
                "Perangkat monitoring tanah portabel dengan sensor pH, kelembaban, NPK, dan suhu. Medali Perunggu, kategori Presentasi PIMNAS 37.",
            ),
        ],
        "toolkit": "TOOLKIT",
        "toolkit_text": (
            "C/C++, Python, Arduino, ESP32, Raspberry Pi, STM32, ROS / ROS2, FAST-LIO, SLAM, IMU, LiDAR, "
            "kamera RGB-D, OpenCV, YOLOv8, TensorFlow / PyTorch, NumPy / Pandas, MQTT, HTTP / REST, Android Studio, "
            "EasyEDA, EasyEDA Pro, MATLAB / Simulink, Git / GitHub, Linux, dan LaTeX."
        ),
        "awards": "PRESTASI PILIHAN",
        "awards_entries": [
            "Top 20 Mahasiswa Berprestasi Bidang Kemahasiswaan - Telkom University, 2024.",
            "Finalis Kontes Robot Indonesia 2024, divisi SAR - Ketua Tim, ARJUNA.",
            "Medali Perunggu PIMNAS 37 (2024), kategori Presentasi - PKM-KI, TOMOT.",
            "Peserta PIMNAS 2025 - kelas PKM-KI, TIRNARA.",
            "Juara II Lomba Uji Kompetensi Laboratorium - Pekan Raya Biologi 2020, Universitas Riau.",
            "Peserta Kompetisi Sains Madrasah (KSM) 2021 - Biologi, Provinsi Riau.",
        ],
        "languages": "BAHASA",
        "languages_text": "Bahasa Indonesia - bahasa ibu. Bahasa Inggris - menengah.",
        "page2_note": "Detail proyek dan sertifikat pendukung: aliyushedri-portfolio.tech",
    },
}


def section_heading(title: str, st: dict[str, ParagraphStyle]) -> list:
    return [
        Paragraph(e(title), st["section"]),
        HRFlowable(width="100%", thickness=0.6, color=RULE, spaceBefore=0, spaceAfter=2.1 * mm),
    ]


def entry(title: str, period: str, body: str, st: dict[str, ParagraphStyle]) -> list:
    return [
        Paragraph(
            f"{e(title)} <font color=\"#52606D\">| {e(period)}</font>",
            st["entry_title"],
        ),
        Paragraph(body, st["body_tight"]),
    ]


def service_rows(items: list[tuple[str, str]], st: dict[str, ParagraphStyle]) -> list:
    rows = []
    for label, description in items:
        rows.append(
            Paragraph(
                f"- <b>{e(label)}.</b> {e(description)}",
                st["body_tight"],
            )
        )
    return rows


def header_flowables(locale: str, st: dict[str, ParagraphStyle]) -> list:
    data = CONTENT[locale]
    location = CONTACTS["location_en" if locale == "en" else "location_id"]
    row1 = (
        f"{e(location)}  |  {e(CONTACTS['whatsapp'])}  |  "
        f"{link(CONTACTS['email'], 'mailto:' + CONTACTS['email'])}"
    )
    row2 = (
        f"{link(CONTACTS['linkedin'], CONTACTS['linkedin_url'])}  |  "
        f"{link(CONTACTS['github'], CONTACTS['github_url'])}  |  "
        f"{link(CONTACTS['portfolio'], CONTACTS['portfolio_url'])}"
    )
    return [
        Paragraph("ALIYUS HEDRI", st["name"]),
        Paragraph(e(data["role"]), st["role"]),
        Paragraph(row1, st["contact"]),
        Paragraph(row2, st["contact"]),
        HRFlowable(width="100%", thickness=1.1, color=BLUE, spaceBefore=2.5 * mm, spaceAfter=3.0 * mm),
    ]


def engagement_callout(label: str, text: str, st: dict[str, ParagraphStyle]) -> Table:
    table = Table([[Paragraph(f"<b>{e(label)}:</b> {e(text)}", st["callout"])]], colWidths=[CONTENT_W])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), PALE_BLUE),
                ("BOX", (0, 0), (-1, -1), 0.6, HexColor("#C8DDE8")),
                ("LEFTPADDING", (0, 0), (-1, -1), 3.3 * mm),
                ("RIGHTPADDING", (0, 0), (-1, -1), 3.3 * mm),
                ("TOPPADDING", (0, 0), (-1, -1), 2.2 * mm),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 2.2 * mm),
            ]
        )
    )
    return table


def page_one(locale: str, st: dict[str, ParagraphStyle]) -> list:
    data = CONTENT[locale]
    story: list = []
    story.extend(header_flowables(locale, st))
    story.append(engagement_callout(data["engagement_label"], data["engagement"], st))
    story.append(Spacer(1, 2.0 * mm))

    story.extend(section_heading("PROFILE" if locale == "en" else "PROFIL", st))
    story.append(Paragraph(e(data["summary"]), st["body"]))

    story.extend(section_heading("SERVICES", st) if locale == "en" else section_heading("LAYANAN", st))
    story.extend(service_rows(data["services"], st))

    story.extend(section_heading(data["selected_projects"], st))
    for project in data["projects"]:
        story.extend(entry(project["title"], project["period"], project["body"], st))
    story.append(PageBreak())
    return story


def page_two(locale: str, st: dict[str, ParagraphStyle]) -> list:
    data = CONTENT[locale]
    story: list = []
    story.append(Paragraph("ALIYUS HEDRI  /  CURRICULUM VITAE", st["entry_title"]))
    story.append(Spacer(1, 1.2 * mm))

    story.extend(section_heading(data["experience"], st))
    for title, period, body in data["experience_entries"]:
        story.extend(entry(title, period, e(body), st))

    story.extend(section_heading(data["education"], st))
    for title, period, body in data["education_entries"]:
        story.extend(entry(title, period, e(body), st))

    story.extend(section_heading(data["additional_projects"], st))
    for title, period, body in data["additional_project_entries"]:
        story.extend(entry(title, period, e(body), st))

    story.extend(section_heading(data["toolkit"], st))
    story.append(Paragraph(e(data["toolkit_text"]), st["body_tight"]))

    story.extend(section_heading(data["awards"], st))
    for award in data["awards_entries"]:
        story.append(Paragraph(f"- {e(award)}", st["body_tight"]))

    story.extend(section_heading(data["languages"], st))
    story.append(Paragraph(e(data["languages_text"]), st["body_tight"]))
    story.append(Spacer(1, 1.0 * mm))
    story.append(Paragraph(link(data["page2_note"], CONTACTS["portfolio_url"]), st["page_note"]))
    return story


def draw_page_chrome(canvas, doc) -> None:
    canvas.saveState()
    canvas.setStrokeColor(RULE)
    canvas.setLineWidth(0.45)
    canvas.line(LEFT, 10.5 * mm, PAGE_W - RIGHT, 10.5 * mm)
    canvas.setFillColor(MUTED)
    canvas.setFont("Helvetica", 7.1)
    canvas.drawString(LEFT, 6.8 * mm, "Aliyus Hedri - Robotics, Embedded Systems & IoT")
    canvas.drawRightString(PAGE_W - RIGHT, 6.8 * mm, f"{doc.page} / 2")
    canvas.restoreState()


def build(locale: str, output: Path) -> None:
    st = styles(locale)
    output.parent.mkdir(parents=True, exist_ok=True)
    doc = BaseDocTemplate(
        str(output),
        pagesize=A4,
        leftMargin=LEFT,
        rightMargin=RIGHT,
        topMargin=TOP,
        bottomMargin=BOTTOM,
        title="Aliyus Hedri CV" if locale == "en" else "CV Aliyus Hedri",
        author="Aliyus Hedri",
        subject="Curriculum vitae",
    )
    frame = Frame(
        doc.leftMargin,
        doc.bottomMargin,
        doc.width,
        doc.height,
        id="cv-frame",
        leftPadding=0,
        rightPadding=0,
        topPadding=0,
        bottomPadding=0,
    )
    doc.addPageTemplates([PageTemplate(id="cv", frames=[frame], onPage=draw_page_chrome)])
    doc.build(page_one(locale, st) + page_two(locale, st))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--language",
        choices=("en", "id", "both"),
        default="both",
        help="Language to build (default: both).",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=OUTPUT_DIR,
        help="Directory for generated PDFs.",
    )
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
