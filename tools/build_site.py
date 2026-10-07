"""Generate the bilingual static portfolio using only Python's standard library."""

from html import escape
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
SITE_ORIGIN = "https://aliyushedri-portfolio.tech"
PERSON_SAME_AS = [
    "https://www.linkedin.com/in/aliyushedri/",
    "https://github.com/aliyushedri",
    "https://www.instagram.com/aliyushedri",
]

ARROW = (
    '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
    'stroke-width="1.6" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
)
EXTERNAL = (
    '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
    'stroke-width="1.6" aria-hidden="true"><path d="M6 18 18 6M6 6h12v12"/></svg>'
)
DOWNLOAD = (
    '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
    'stroke-width="1.6" aria-hidden="true"><path d="M12 3v12m-5-5 5 5 5-5M5 16v5h14v-5"/></svg>'
)
CROSS = (
    '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
    'stroke-width="1.8" aria-hidden="true"><path d="m6 6 12 12M18 6 6 18"/></svg>'
)


def text(value: str) -> str:
    """Escape text used in HTML text nodes and attribute values."""

    return escape(value, quote=True)


def home_file(locale: str) -> str:
    return "index.html" if locale == "en" else "index-id.html"


def home_url(locale: str) -> str:
    return "./" if locale == "en" else "id/"


def detail_file(slug: str, locale: str) -> str:
    suffix = "" if locale == "en" else "-id"
    return f"proyek-{slug}{suffix}.html"


def home_href(locale: str, anchor: str) -> str:
    return f"{home_url(locale)}#{anchor}"


PROJECTS = [
    {
        "slug": "hexapod",
        "image": "hexapod",
        "category": "robotics ai",
        "year": "2023–2024",
        "alt": {
            "en": "ARJUNA hexapod robot during a robotics competition",
            "id": "Robot hexapod ARJUNA saat kompetisi robot",
        },
        "title": {"en": "ARJUNA hexapod robot", "id": "Robot hexapod ARJUNA"},
        "label": {
            "en": "Robotics & computer vision",
            "id": "Robotika & computer vision",
        },
        "summary": {
            "en": "Automatic IMU-based balance and real-time YOLOv8 object detection for a six-legged robot.",
            "id": "Keseimbangan otomatis berbasis IMU dan deteksi objek real-time YOLOv8 untuk robot berkaki enam.",
        },
        "role": {"en": "Team leader, ARJUNA", "id": "Ketua tim, ARJUNA"},
        "tools": {
            "en": "C/C++, IMU, YOLOv8, actuator control",
            "id": "C/C++, IMU, YOLOv8, kontrol aktuator",
        },
        "result": {
            "en": "Finalist, KRI 2024 SAR division",
            "id": "Finalis KRI 2024 divisi SAR",
        },
        "lead": {
            "en": "A six-legged robot project combining automatic balance and real-time object detection for the Kontes Robot Indonesia.",
            "id": "Proyek robot berkaki enam yang menggabungkan keseimbangan otomatis dan deteksi objek real-time untuk Kontes Robot Indonesia.",
        },
        "sections": {
            "en": [
                (
                    "Project scope",
                    "The project covered a six-legged robot with automatic IMU-based balance and real-time YOLOv8 object detection for autonomous navigation.",
                ),
                (
                    "My role",
                    "I led Team ARJUNA. The project combined a six-legged platform, automatic balance, perception, and the integration needed for the competition.",
                ),
                (
                    "Outcome",
                    "Team ARJUNA became a finalist in the 2024 Kontes Robot Indonesia, Kontes Robot SAR Indonesia division.",
                ),
            ],
            "id": [
                (
                    "Ruang lingkup proyek",
                    "Proyek ini mencakup robot berkaki enam dengan keseimbangan otomatis berbasis IMU dan deteksi objek real-time menggunakan YOLOv8 untuk navigasi otonom.",
                ),
                (
                    "Peran saya",
                    "Saya memimpin Tim ARJUNA. Proyek ini menggabungkan platform robot berkaki enam, keseimbangan otomatis, persepsi, dan integrasi untuk kompetisi.",
                ),
                (
                    "Hasil",
                    "Tim ARJUNA menjadi finalis Kontes Robot Indonesia 2024 pada divisi Kontes Robot SAR Indonesia.",
                ),
            ],
        },
        "gallery": [],
        "certificate": {"image": "kri-2024"},
        "certificate_title": {
            "en": "Finalist, Kontes Robot Indonesia National Competition 2024",
            "id": "Finalis Kontes Robot Indonesia Tingkat Nasional 2024",
        },
    },
    {
        "slug": "tomot",
        "image": "tomot",
        "category": "embedded iot",
        "year": "2024",
        "alt": {
            "en": "TOMOT portable soil monitoring device",
            "id": "Perangkat monitoring tanah portabel TOMOT",
        },
        "title": {"en": "TOMOT", "id": "TOMOT"},
        "label": {
            "en": "Embedded systems & agriculture",
            "id": "Embedded systems & pertanian",
        },
        "summary": {
            "en": "A portable soil monitoring stick for checking parameters used in fertilization decisions.",
            "id": "Tongkat monitoring tanah portabel untuk memeriksa parameter yang digunakan dalam keputusan pemupukan.",
        },
        "role": {
            "en": "PKM-KI project development",
            "id": "Pengembangan proyek PKM-KI",
        },
        "tools": {
            "en": "pH, moisture, NPK, and temperature sensors",
            "id": "Sensor pH, kelembaban, NPK, dan suhu",
        },
        "result": {
            "en": "Bronze Medal, PIMNAS 37 presentation category",
            "id": "Medali Perunggu, kategori Presentasi PIMNAS 37",
        },
        "lead": {
            "en": "A portable soil monitoring device that brings pH, moisture, NPK, and temperature readings to the field.",
            "id": "Perangkat monitoring tanah portabel yang membawa pembacaan pH, kelembaban, NPK, dan suhu ke lahan.",
        },
        "sections": {
            "en": [
                (
                    "Project purpose",
                    "TOMOT was developed as a portable soil monitoring stick to help farmers check parameters relevant to fertilization decisions.",
                ),
                (
                    "Implementation",
                    "The device combines pH, moisture, NPK, and temperature sensors in a stick-shaped form for measurements at the plant site.",
                ),
                (
                    "Outcome",
                    "The project was developed from March to November 2024 through PKM-Karya Inovatif. It received a Bronze Medal in the presentation category at PIMNAS 37 in 2024.",
                ),
            ],
            "id": [
                (
                    "Tujuan proyek",
                    "TOMOT dikembangkan sebagai tongkat monitoring tanah portabel untuk membantu petani memeriksa parameter yang relevan dengan keputusan pemupukan.",
                ),
                (
                    "Implementasi",
                    "Perangkat ini menggabungkan sensor pH, kelembaban, NPK, dan suhu dalam bentuk tongkat untuk pengukuran di lokasi tanaman.",
                ),
                (
                    "Hasil",
                    "Proyek dikembangkan pada Maret–November 2024 melalui PKM-Karya Inovatif. TOMOT meraih Medali Perunggu kategori Presentasi pada PIMNAS ke-37 tahun 2024.",
                ),
            ],
        },
        "gallery": [("tomot-field", "TOMOT being used in an agricultural field")],
        "gallery_id": [("tomot-field", "Penggunaan TOMOT di lahan pertanian")],
        "certificate": {"image": "pimnas-2024"},
        "certificate_title": {
            "en": "Bronze Medal, PIMNAS 37 presentation category",
            "id": "Medali Perunggu kategori Presentasi PIMNAS ke-37",
        },
    },
    {
        "slug": "instalasi",
        "image": "nawa",
        "category": "embedded",
        "year": "2025",
        "alt": {
            "en": "Nawa Majika interactive installation during an internship",
            "id": "Instalasi interaktif Nawa Majika saat magang",
        },
        "title": {
            "en": "Nawa Majika & Skyward installations",
            "id": "Instalasi Nawa Majika & Skyward",
        },
        "label": {
            "en": "Mechatronics & interactive installations",
            "id": "Mekatronika & instalasi interaktif",
        },
        "summary": {
            "en": "Interactive installation work encountered during an internship at PT Arthatronic Studio Teknologi.",
            "id": "Pekerjaan instalasi interaktif yang ditemui selama magang di PT Arthatronic Studio Teknologi.",
        },
        "role": {
            "en": "Mechatronics Engineering Intern",
            "id": "Magang Mechatronics Engineer",
        },
        "tools": {
            "en": "Mechatronics and device integration",
            "id": "Mekatronika dan integrasi perangkat",
        },
        "result": {
            "en": "Internship context",
            "id": "Konteks magang",
        },
        "lead": {
            "en": "Interactive installations and physical devices were part of the work encountered during this internship.",
            "id": "Instalasi interaktif dan perangkat fisik menjadi bagian dari pekerjaan yang ditemui selama magang ini.",
        },
        "sections": {
            "en": [
                (
                    "Internship context",
                    "I worked as a Mechatronics Engineer at PT Arthatronic Studio Teknologi from 30 June to 9 August 2025.",
                ),
                (
                    "Installation work",
                    "The portfolio includes photographs of the Nawa Majika installation, interactive lantern devices, and the Skyward project during the internship.",
                ),
                (
                    "Role",
                    "I worked as a Mechatronics Engineer at PT Arthatronic Studio Teknologi during this internship.",
                ),
            ],
            "id": [
                (
                    "Konteks magang",
                    "Saya menjalani magang sebagai Mechatronics Engineer di PT Arthatronic Studio Teknologi pada 30 Juni–9 Agustus 2025.",
                ),
                (
                    "Pekerjaan instalasi",
                    "Portofolio ini memuat foto instalasi Nawa Majika, perangkat lentera interaktif, dan proyek Skyward selama magang.",
                ),
                (
                    "Peran",
                    "Saya bekerja sebagai Mechatronics Engineer di PT Arthatronic Studio Teknologi selama magang ini.",
                ),
            ],
        },
        "gallery": [
            ("lantern", "Interactive lantern device from the Nawa Majika project"),
            ("lantern-detail", "Detail of the Nawa Majika lantern device"),
            ("skyward", "Skyward project device"),
        ],
        "gallery_id": [
            ("lantern", "Perangkat lentera interaktif dari proyek Nawa Majika"),
            ("lantern-detail", "Detail perangkat lentera Nawa Majika"),
            ("skyward", "Perangkat proyek Skyward"),
        ],
        "certificate": None,
        "certificate_title": None,
    },
    {
        "slug": "kualitas-air",
        "image": "water",
        "category": "embedded iot",
        "year": "2025",
        "alt": {
            "en": "ESP32 household water quality monitoring prototype",
            "id": "Prototipe monitoring kualitas air rumah tangga berbasis ESP32",
        },
        "title": {
            "en": "Household water quality monitoring",
            "id": "Sistem monitoring kualitas air rumah tangga",
        },
        "label": {
            "en": "Internet of Things",
            "id": "Internet of Things",
        },
        "summary": {
            "en": "An ESP32 prototype that sends pH, temperature, and turbidity readings to a cloud dashboard.",
            "id": "Prototipe ESP32 yang mengirim data pH, suhu, dan kekeruhan ke dashboard cloud.",
        },
        "role": {
            "en": "Capstone design project",
            "id": "Proyek capstone design",
        },
        "tools": {
            "en": "ESP32, pH, temperature, turbidity, MQTT/HTTP",
            "id": "ESP32, pH, suhu, kekeruhan, MQTT/HTTP",
        },
        "result": {
            "en": "IoT monitoring prototype",
            "id": "Prototipe monitoring IoT",
        },
        "lead": {
            "en": "A household water quality prototype integrating sensors, an embedded device, and a cloud dashboard.",
            "id": "Prototipe kualitas air rumah tangga yang mengintegrasikan sensor, perangkat embedded, dan dashboard cloud.",
        },
        "sections": {
            "en": [
                (
                    "Project purpose",
                    "The prototype monitors household water quality parameters and makes the readings available through a dashboard.",
                ),
                (
                    "Implementation",
                    "An ESP32 is used with pH, temperature, and turbidity sensors. The readings are sent in real time through MQTT/HTTP to a cloud dashboard.",
                ),
                (
                    "Prototype context",
                    "The project ran from February to June 2025 and used a physical prototype with a water container and sensor installation.",
                ),
            ],
            "id": [
                (
                    "Tujuan proyek",
                    "Prototipe ini memantau parameter kualitas air rumah tangga dan menyediakan pembacaannya melalui dashboard.",
                ),
                (
                    "Implementasi",
                    "ESP32 digunakan bersama sensor pH, suhu, dan kekeruhan. Data dikirim secara real-time melalui MQTT/HTTP ke dashboard cloud.",
                ),
                (
                    "Konteks prototipe",
                    "Proyek berlangsung pada Februari–Juni 2025 dan menggunakan prototipe fisik dengan wadah air serta pemasangan sensor.",
                ),
            ],
        },
        "gallery": [],
        "certificate": None,
        "certificate_title": None,
    },
    {
        "slug": "telubot-android",
        "image": "telubot",
        "image_label": {
            "en": "Android app · TEL-U BOT",
            "id": "Aplikasi Android · TEL-U BOT",
        },
        "category": "software android robotics",
        "year": "2026",
        "alt": {
            "en": "TEL-U BOT Android app project",
            "id": "Proyek aplikasi Android TEL-U BOT",
        },
        "title": {
            "en": "TEL-U BOT Android app",
            "id": "Aplikasi Android TEL-U BOT",
        },
        "label": {
            "en": "Android · robotics support",
            "id": "Android · dukungan robotika",
        },
        "summary": {
            "en": "A published Android app for controlling, monitoring, and configuring TEL-U BOT over local Wi-Fi.",
            "id": "Aplikasi Android terbit untuk mengendalikan, memantau, dan mengonfigurasi TEL-U BOT melalui Wi-Fi lokal.",
        },
        "role": {
            "en": "Android app developer · research support",
            "id": "Pengembang aplikasi Android · dukungan riset",
        },
        "tools": {
            "en": "Android Studio, local Wi-Fi UDP, robot telemetry, planner configuration",
            "id": "Android Studio, UDP Wi-Fi lokal, telemetri robot, konfigurasi planner",
        },
        "result": {
            "en": "Published on Google Play",
            "id": "Terbit di Google Play",
        },
        "lead": {
            "en": "An Android control and monitoring app for TEL-U BOT, developed to support lecturer research at ACS Laboratory.",
            "id": "Aplikasi Android untuk mengendalikan dan memantau TEL-U BOT, dikembangkan untuk mendukung riset dosen di ACS Laboratory.",
        },
        "sections": {
            "en": [
                (
                    "Purpose",
                    "TEL-U BOT is an Android app for controlling and monitoring the robot over local Wi-Fi. I developed it to support research activities at ACS Laboratory.",
                ),
                (
                    "Selected scope",
                    "The app includes speed, direction, and actuator controls; line, LiDAR, and odometry telemetry; calibration; and planner configuration workflows. It also supports reading, writing, and testing planner EEPROM data plus JSON draft import and export.",
                ),
                (
                    "Availability",
                    "The app is published on Google Play under ACS Laboratory. Use the listing below for the current release and app details.",
                ),
            ],
            "id": [
                (
                    "Tujuan",
                    "TEL-U BOT adalah aplikasi Android untuk mengendalikan dan memantau robot melalui Wi-Fi lokal. Saya mengembangkannya untuk mendukung kegiatan riset di ACS Laboratory.",
                ),
                (
                    "Ruang lingkup pilihan",
                    "Aplikasi mencakup kontrol kecepatan, arah, dan aktuator; telemetri line, LiDAR, dan odometri; kalibrasi; serta alur konfigurasi planner. Aplikasi juga mendukung pembacaan, penulisan, dan pengujian data EEPROM planner serta impor dan ekspor draft JSON.",
                ),
                (
                    "Ketersediaan",
                    "Aplikasi ini terbit di Google Play di bawah ACS Laboratory. Gunakan tautan di bawah untuk melihat rilis dan detail aplikasi saat ini.",
                ),
            ],
        },
        "external_link": "https://play.google.com/store/apps/details?id=id.acslab.telubot",
        "external_label": {
            "en": "View on Google Play",
            "id": "Lihat di Google Play",
        },
        "gallery": [],
        "certificate": None,
        "certificate_title": None,
    },
    {
        "slug": "portfolio-site",
        "image": "portfolio",
        "image_label": {
            "en": "HTML · CSS · JavaScript · GitHub Pages",
            "id": "HTML · CSS · JavaScript · GitHub Pages",
        },
        "category": "software web",
        "year": {
            "en": "Current",
            "id": "Saat ini",
        },
        "alt": {
            "en": "Aliyus Hedri portfolio website",
            "id": "Situs portofolio Aliyus Hedri",
        },
        "title": {
            "en": "Aliyus Hedri portfolio site",
            "id": "Situs portofolio Aliyus Hedri",
        },
        "label": {
            "en": "Static web · portfolio",
            "id": "Web statis · portofolio",
        },
        "summary": {
            "en": "A bilingual static portfolio built with HTML, CSS, and JavaScript and published on GitHub Pages.",
            "id": "Portofolio statis bilingual berbasis HTML, CSS, dan JavaScript yang dipublikasikan melalui GitHub Pages.",
        },
        "role": {
            "en": "Designer and developer",
            "id": "Perancang dan pengembang",
        },
        "tools": {
            "en": "HTML, CSS, JavaScript, GitHub Pages",
            "id": "HTML, CSS, JavaScript, GitHub Pages",
        },
        "result": {
            "en": "Bilingual portfolio site",
            "id": "Situs portofolio bilingual",
        },
        "lead": {
            "en": "The current portfolio site presents freelance engineering services, selected projects, research context, and contact routes in English and Bahasa Indonesia.",
            "id": "Situs portofolio saat ini menyajikan layanan engineering freelance, proyek pilihan, konteks riset, dan jalur kontak dalam bahasa Inggris dan Bahasa Indonesia.",
        },
        "sections": {
            "en": [
                (
                    "Purpose",
                    "The site gives individuals, UMKM, startups, companies, and research teams a clear way to review my services, project examples, and research context.",
                ),
                (
                    "Implementation",
                    "The site is generated as static HTML with HTML, CSS, and JavaScript and published through GitHub Pages. The bilingual home route keeps /id/ for Bahasa Indonesia.",
                ),
                (
                    "Scope",
                    "This site is an example of a portfolio deliverable. New website work and revisions are discussed against the agreed scope.",
                ),
            ],
            "id": [
                (
                    "Tujuan",
                    "Situs ini memberi individu, UMKM, startup, perusahaan, dan tim riset cara yang jelas untuk melihat layanan, contoh proyek, dan konteks riset saya.",
                ),
                (
                    "Implementasi",
                    "Situs ini digenerasikan sebagai HTML statis dengan HTML, CSS, dan JavaScript lalu dipublikasikan melalui GitHub Pages. Rute beranda bilingual mempertahankan /id/ untuk Bahasa Indonesia.",
                ),
                (
                    "Ruang lingkup",
                    "Situs ini merupakan contoh keluaran portofolio. Pekerjaan website baru dan revisi dibahas berdasarkan ruang lingkup yang disepakati.",
                ),
            ],
        },
        "external_link": "https://aliyushedri-portfolio.tech/",
        "external_label": {
            "en": "Open live site",
            "id": "Buka situs live",
        },
        "gallery": [],
        "certificate": None,
        "certificate_title": None,
    },
]


AWARDS = [
    {
        "image": "pimnas-2024",
        "year": "2024",
        "title": {
            "en": "Bronze Medal, PIMNAS 37",
            "id": "Medali Perunggu PIMNAS 37",
        },
        "description": {
            "en": "Presentation category, PKM-Karya Inovatif, for the TOMOT project.",
            "id": "Kategori Presentasi, PKM-Karya Inovatif, untuk proyek TOMOT.",
        },
    },
    {
        "image": "kri-2024",
        "year": "2024",
        "title": {
            "en": "Finalist, Kontes Robot Indonesia 2024",
            "id": "Finalis Kontes Robot Indonesia 2024",
        },
        "description": {
            "en": "Team ARJUNA, Kontes Robot SAR Indonesia division.",
            "id": "Tim ARJUNA, divisi Kontes Robot SAR Indonesia.",
        },
    },
    {
        "image": "mawapres-2024",
        "year": "2024",
        "title": {
            "en": "Top 20 Student Achievement Award",
            "id": "Top 20 Mahasiswa Berprestasi",
        },
        "description": {
            "en": "Student affairs category, Telkom University.",
            "id": "Bidang Kemahasiswaan, Telkom University.",
        },
    },
]


SERVICES = [
    {
        "number": "01",
        "title": {
            "en": "Robotics, SLAM & embedded IoT",
            "id": "Robotika, SLAM & embedded IoT",
        },
        "summary": {
            "en": "Build or improve robot and device systems around ROS2, LiDAR, sensors, embedded boards, and connected data flows.",
            "id": "Membangun atau memperbaiki sistem robot dan perangkat dengan ROS2, LiDAR, sensor, board embedded, dan alur data terhubung.",
        },
        "tools": {
            "en": "ROS2 · C/C++ · Python · Arduino · ESP32 · Raspberry Pi",
            "id": "ROS2 · C/C++ · Python · Arduino · ESP32 · Raspberry Pi",
        },
    },
    {
        "number": "02",
        "title": {
            "en": "PCB design & automation",
            "id": "Desain PCB & otomasi",
        },
        "summary": {
            "en": "Turn a circuit idea into a practical board or automation flow, from schematic and layout work to embedded integration.",
            "id": "Mengubah ide rangkaian menjadi board atau alur otomasi yang praktis, dari skematik dan layout hingga integrasi embedded.",
        },
        "tools": {
            "en": "EasyEDA · EasyEDA Pro · Arduino · ESP32 · automation",
            "id": "EasyEDA · EasyEDA Pro · Arduino · ESP32 · otomasi",
        },
    },
    {
        "number": "03",
        "title": {
            "en": "Android & web development",
            "id": "Pengembangan Android & web",
        },
        "summary": {
            "en": "Build Android apps for device control or internal workflows, and static websites for portfolios, businesses, and projects.",
            "id": "Membuat aplikasi Android untuk kendali perangkat atau alur kerja internal, serta website statis untuk portofolio, usaha, dan proyek.",
        },
        "tools": {
            "en": "Android Studio · HTML · CSS · JavaScript · GitHub Pages",
            "id": "Android Studio · HTML · CSS · JavaScript · GitHub Pages",
        },
    },
    {
        "number": "04",
        "title": {
            "en": "AI, bots & machine learning",
            "id": "AI, bot & machine learning",
        },
        "summary": {
            "en": "Integrate LLMs into automation, build Telegram bots with or without AI, and train ML/DL models for image detection and processing on embedded or standalone systems.",
            "id": "Mengintegrasikan LLM ke otomasi, membuat bot Telegram dengan atau tanpa AI, serta melatih model ML/DL untuk deteksi dan pemrosesan citra pada sistem embedded atau standalone.",
        },
        "tools": {
            "en": "LLM integration · Telegram bots · ML/DL · computer vision",
            "id": "Integrasi LLM · bot Telegram · ML/DL · computer vision",
        },
    },
    {
        "number": "05",
        "title": {
            "en": "Research assistance, papers & LaTeX",
            "id": "Bantuan riset, paper & LaTeX",
        },
        "summary": {
            "en": "Help structure technical work, edit research papers or journal manuscripts, and prepare LaTeX documents around an agreed research scope.",
            "id": "Membantu menstrukturkan pekerjaan teknis, menyunting paper atau manuskrip jurnal, dan menyiapkan dokumen LaTeX sesuai ruang lingkup riset yang disepakati.",
        },
        "tools": {
            "en": "Technical writing · paper editing · LaTeX · research workflow",
            "id": "Penulisan teknis · penyuntingan paper · LaTeX · alur kerja riset",
        },
    },
]


TRANSLATIONS = {
    "en": {
        "skip": "Skip to main content",
        "home": "Aliyus Hedri, home",
        "open_menu": "Open navigation menu",
        "close_menu": "Close navigation menu",
        "nav_label": "Main navigation",
        "services": "Services",
        "projects": "Projects",
        "how_work": "How I work",
        "about": "About",
        "experience": "Experience",
        "education": "Education",
        "research": "Research",
        "awards": "Awards & certificates",
        "cv_short": "CV",
        "contact": "Contact",
        "language_label": "Language selection",
        "switch_language": "Switch to Bahasa Indonesia",
        "role": "Freelance Robotics & Embedded Engineer",
        "hero_description": "I build and improve robotics, SLAM, embedded, IoT, Android, web, and AI systems while completing a Master by Research in Electrical Engineering at Telkom University.",
        "location": "Bandung, West Java, Indonesia",
        "discuss_project": "Discuss a project",
        "explore_projects": "View projects",
        "download_cv": "Download CV",
        "focus_robotics": "Robotics",
        "focus_slam": "SLAM",
        "focus_embedded": "Embedded systems",
        "focus_iot": "Internet of Things",
        "portrait_alt": "Aliyus Hedri wearing a Telkom University jacket",
        "portrait_caption": "Master by Research · Electrical Engineering",
        "selected_projects": "Selected projects",
        "projects_intro": "Robotics, embedded, and software projects from research, competitions, and development work.",
        "filter_label": "Filter projects by field",
        "all_projects": "All projects",
        "filter_robotics": "Robotics",
        "filter_embedded": "Embedded",
        "filter_iot": "IoT",
        "filter_software": "Software",
        "filter_ai": "AI",
        "projects_shown": "6 projects shown",
        "view_project": "View project",
        "services_heading": "Services",
        "services_intro": "Engineering support for individuals, small businesses, startups, companies, and research teams. I work remotely; onsite work, full projects, and debugging can be discussed.",
        "service_tools_label": "Typical tools",
        "how_work_heading": "How I work",
        "how_work_intro": "Share a brief, agree the scope, then start the technical work.",
        "step_brief_title": "Start with the brief",
        "step_brief_text": "We discuss the problem, current system, constraints, audience, and desired outcome.",
        "step_scope_title": "Agree the scope",
        "step_scope_text": "Before implementation, we confirm the work area, interfaces, proposed deliverables, and handoff format.",
        "step_build_title": "Build and hand over",
        "step_build_text": "Depending on the agreed scope, deliverables can include source code, design files, setup notes, documentation, a working demo, or a handoff session.",
        "about_heading": "About",
        "about_p1": "I am Aliyus Hedri, a freelance engineer and an Electrical Engineering Master by Research student at ACS Laboratory, Telkom University.",
        "about_p2": "My work sits between robotics and practical software: LiDAR-inertial odometry and SLAM, embedded and IoT devices, Android tools, automation, AI, and technical research support.",
        "about_p3": "I have led Team ARJUNA, developed monitoring prototypes, coordinated EIRRG, assisted in a computer laboratory, and completed a mechatronics engineering internship at PT Arthatronic Studio Teknologi.",
        "see_cv": "See curriculum vitae",
        "expertise_robotics": "Robotics and perception",
        "expertise_robotics_text": "ROS2, SLAM, sensor fusion, mobile and legged robots, YOLOv8, and OpenCV.",
        "expertise_embedded": "Embedded systems and sensors",
        "expertise_embedded_text": "C/C++, ESP32, STM32, Raspberry Pi, IMU, camera, distance, and environmental sensors.",
        "expertise_iot": "IoT and software",
        "expertise_iot_text": "Python, MQTT, HTTP/REST API, Wi-Fi, Git, Linux, and MATLAB/Simulink.",
        "experience_heading": "Experience",
        "experience_intro": "Experience across industry, laboratory, research, and university activities.",
        "industry": "Industry",
        "leadership": "Leadership",
        "laboratory": "Laboratory",
        "organization": "Organization",
        "internship_detail": "Internship in mechatronics and interactive installations.",
        "eirrg_detail": "Coordinator for the Electronics & Intelligence Robotics Research Group.",
        "lab_detail": "Computer Basics Laboratory Assistant at Telkom University.",
        "pkkmb_detail": "Committee member for Telkom University's PKKMB in 2023.",
        "education_heading": "Education",
        "education_intro": "Electrical Engineering at Telkom University.",
        "in_progress": "In progress",
        "master_context": "Master by Research · ACS Laboratory, Telkom University",
        "bachelor_context": "Telkom University · GPA 3.8",
        "bachelor_detail": "APERTI BUMN 2022 scholarship recipient.",
        "school_context": "Science track",
        "school_detail": "Graduated with good standing.",
        "education_type": "Education",
        "research_heading": "Research",
        "research_p1": "My current master's research focuses on LiDAR-inertial odometry and SLAM for mobile robots.",
        "research_p2": "A 2026 AGV project adapts FAST-LIO to four low-cost RGB-D Kinect V1 cameras and distributes computation between an STM32 and a Mini PC on ROS2 Jazzy.",
        "target_label": "Research tools",
        "research_note": "ROS2, C++, and Python for robot software and LiDAR-inertial odometry.",
        "awards_heading": "Awards & certificates",
        "awards_intro": "Selected competition and academic recognition.",
        "view_certificate": "View certificate",
        "award_button_label": "View certificate: ",
        "additional_award": "PIMNAS 2025 participant, PKM-KI1, with TIRNARA.",
        "cv_heading": "Curriculum vitae",
        "cv_intro": "Download the current curriculum vitae in English or Bahasa Indonesia.",
        "download_english_cv": "Download English CV",
        "download_indonesian_cv": "Download Bahasa Indonesia CV",
        "contact_heading": "Contact",
        "contact_intro": "Tell me what you are building, repairing, or researching. We can discuss the right scope and next step.",
        "whatsapp": "WhatsApp",
        "gmail": "Gmail",
        "open_gmail": "Open Gmail",
        "instagram": "Instagram",
        "linkedin": "LinkedIn",
        "github": "GitHub",
        "contact_whatsapp": "WhatsApp: @aliyushedri",
        "contact_gmail": "Gmail: aliyus.hedri@gmail.com",
        "contact_instagram": "Instagram: aliyushedri",
        "contact_linkedin": "LinkedIn: aliyushedri",
        "contact_github": "GitHub: aliyushedri",
        "copy_username": "Copy WhatsApp username",
        "copy_email": "Copy email address",
        "copy_action": "Copy",
        "copy_username_status": "WhatsApp username copied",
        "copy_email_status": "Email address copied",
        "copy_failed_status": "Copy failed; select the text manually",
        "find_username": "Find me by username in WhatsApp",
        "footer_links": "Footer links",
        "back_to_top": "Back to top",
        "footer_location": "Based in Bandung, Indonesia.",
        "back_projects": "Back to projects",
        "other_projects": "View other projects",
        "project_link_label": "Project link",
        "detail_scope": "Role / context",
        "detail_period": "Period",
        "detail_tools": "Technology / field",
        "detail_result": "Outcome / output",
        "project_documentation": "Project details",
        "close_certificate": "Close certificate dialog",
        "certificate_alt": "Certificate preview",
        "certificate_proof": "View certificate",
        "page_title": "Aliyus Hedri | Freelance Robotics & Embedded Engineer",
        "page_description": "Aliyus Hedri is a freelance robotics and embedded engineer and Electrical Engineering Master by Research student working across SLAM, IoT, Android, web, AI, and research support.",
    },
    "id": {
        "skip": "Lewati ke konten utama",
        "home": "Aliyus Hedri, beranda",
        "open_menu": "Buka menu navigasi",
        "close_menu": "Tutup menu navigasi",
        "nav_label": "Navigasi utama",
        "services": "Layanan",
        "projects": "Proyek",
        "how_work": "Cara kerja",
        "about": "Tentang",
        "experience": "Pengalaman",
        "education": "Pendidikan",
        "research": "Riset",
        "awards": "Penghargaan & sertifikat",
        "cv_short": "CV",
        "contact": "Kontak",
        "language_label": "Pilihan bahasa",
        "switch_language": "Beralih ke bahasa Inggris",
        "role": "Freelance Engineer Robotika & Embedded",
        "hero_description": "Saya membangun dan memperbaiki sistem robotika, SLAM, embedded, IoT, Android, web, dan AI sambil menempuh S2 Master by Research Teknik Elektro di Telkom University.",
        "location": "Bandung, Jawa Barat, Indonesia",
        "discuss_project": "Diskusikan proyek",
        "explore_projects": "Lihat proyek",
        "download_cv": "Unduh CV",
        "focus_robotics": "Robotika",
        "focus_slam": "SLAM",
        "focus_embedded": "Embedded systems",
        "focus_iot": "Internet of Things",
        "portrait_alt": "Aliyus Hedri mengenakan jaket Telkom University",
        "portrait_caption": "Master by Research · Teknik Elektro",
        "selected_projects": "Proyek pilihan",
        "projects_intro": "Proyek robotika, embedded, dan perangkat lunak dari kegiatan riset, kompetisi, serta pengembangan.",
        "filter_label": "Filter proyek berdasarkan bidang",
        "all_projects": "Semua proyek",
        "filter_robotics": "Robotika",
        "filter_embedded": "Embedded",
        "filter_iot": "IoT",
        "filter_software": "Perangkat lunak",
        "filter_ai": "AI",
        "projects_shown": "6 proyek ditampilkan",
        "view_project": "Lihat proyek",
        "services_heading": "Layanan",
        "services_intro": "Dukungan engineering untuk individu, UMKM, startup, perusahaan, dan tim riset. Pekerjaan remote menjadi pilihan utama; pekerjaan onsite, proyek penuh, dan debugging dibahas sesuai kebutuhan.",
        "service_tools_label": "Contoh teknologi",
        "how_work_heading": "Cara kerja",
        "how_work_intro": "Ceritakan kebutuhan, sepakati ruang lingkup, lalu mulai pekerjaan teknis.",
        "step_brief_title": "Mulai dari brief",
        "step_brief_text": "Kita membahas masalah, sistem saat ini, batasan, pengguna, dan hasil yang diinginkan.",
        "step_scope_title": "Sepakati ruang lingkup",
        "step_scope_text": "Sebelum implementasi, kita menyepakati area kerja, antarmuka, keluaran yang diusulkan, dan format serah terima.",
        "step_build_title": "Bangun dan serahkan",
        "step_build_text": "Sesuai ruang lingkup yang disepakati, keluaran dapat berupa source code, file desain, catatan setup, dokumentasi, demo kerja, atau sesi serah terima.",
        "about_heading": "Tentang",
        "about_p1": "Saya Aliyus Hedri, freelance engineer dan mahasiswa S2 Master by Research Teknik Elektro di ACS Laboratory, Telkom University.",
        "about_p2": "Pekerjaan saya berada di antara robotika dan perangkat lunak praktis: LiDAR-inertial odometry dan SLAM, perangkat embedded dan IoT, alat Android, otomasi, AI, serta dukungan teknis untuk riset.",
        "about_p3": "Saya pernah memimpin Tim ARJUNA, mengembangkan prototipe monitoring, menjadi koordinator EIRRG, menjadi asisten laboratorium komputer, dan menjalani magang mekatronika di PT Arthatronic Studio Teknologi.",
        "see_cv": "Lihat curriculum vitae",
        "expertise_robotics": "Robotika dan persepsi",
        "expertise_robotics_text": "ROS2, SLAM, sensor fusion, robot bergerak dan robot berkaki, YOLOv8, serta OpenCV.",
        "expertise_embedded": "Embedded systems dan sensor",
        "expertise_embedded_text": "C/C++, ESP32, STM32, Raspberry Pi, IMU, kamera, sensor jarak, dan sensor lingkungan.",
        "expertise_iot": "IoT dan perangkat lunak",
        "expertise_iot_text": "Python, MQTT, HTTP/REST API, Wi-Fi, Git, Linux, dan MATLAB/Simulink.",
        "experience_heading": "Pengalaman",
        "experience_intro": "Pengalaman di industri, laboratorium, riset, dan kegiatan universitas.",
        "industry": "Industri",
        "leadership": "Kepemimpinan",
        "laboratory": "Laboratorium",
        "organization": "Organisasi",
        "internship_detail": "Magang di bidang mekatronika dan instalasi interaktif.",
        "eirrg_detail": "Koordinator Electronics & Intelligence Robotics Research Group.",
        "lab_detail": "Asisten Laboratorium Dasar Komputer di Telkom University.",
        "pkkmb_detail": "Panitia PKKMB Telkom University pada 2023.",
        "education_heading": "Pendidikan",
        "education_intro": "Pendidikan Teknik Elektro di Telkom University.",
        "in_progress": "Sedang berjalan",
        "master_context": "Master by Research · ACS Laboratory, Telkom University",
        "bachelor_context": "Telkom University · IPK 3,8",
        "bachelor_detail": "Penerima Beasiswa APERTI BUMN 2022.",
        "school_context": "Jurusan IPA",
        "school_detail": "Lulus dengan predikat baik.",
        "education_type": "Pendidikan",
        "research_heading": "Riset",
        "research_p1": "Riset magister saya saat ini berfokus pada LiDAR-inertial odometry dan SLAM untuk robot bergerak.",
        "research_p2": "Proyek AGV 2026 mengadaptasi FAST-LIO untuk empat kamera RGB-D Kinect V1 berbiaya rendah dan membagi komputasi antara STM32 dan Mini PC pada ROS2 Jazzy.",
        "target_label": "Perangkat riset",
        "research_note": "ROS2, C++, dan Python untuk perangkat lunak robot dan LiDAR-inertial odometry.",
        "awards_heading": "Penghargaan & sertifikat",
        "awards_intro": "Pilihan penghargaan kompetisi dan akademik.",
        "view_certificate": "Lihat sertifikat",
        "award_button_label": "Lihat sertifikat: ",
        "additional_award": "Peserta PIMNAS 2025, PKM-KI1, melalui TIRNARA.",
        "cv_heading": "Curriculum vitae",
        "cv_intro": "Unduh curriculum vitae terbaru dalam bahasa Inggris atau Bahasa Indonesia.",
        "download_english_cv": "Unduh CV bahasa Inggris",
        "download_indonesian_cv": "Unduh CV Bahasa Indonesia",
        "contact_heading": "Kontak",
        "contact_intro": "Ceritakan apa yang sedang Anda bangun, perbaiki, atau teliti. Kita dapat membahas ruang lingkup dan langkah berikutnya.",
        "whatsapp": "WhatsApp",
        "gmail": "Gmail",
        "open_gmail": "Buka Gmail",
        "instagram": "Instagram",
        "linkedin": "LinkedIn",
        "github": "GitHub",
        "contact_whatsapp": "WhatsApp: @aliyushedri",
        "contact_gmail": "Gmail: aliyus.hedri@gmail.com",
        "contact_instagram": "Instagram: aliyushedri",
        "contact_linkedin": "LinkedIn: aliyushedri",
        "contact_github": "GitHub: aliyushedri",
        "copy_username": "Salin username WhatsApp",
        "copy_email": "Salin alamat email",
        "copy_action": "Salin",
        "copy_username_status": "Username WhatsApp disalin",
        "copy_email_status": "Alamat email disalin",
        "copy_failed_status": "Penyalinan gagal; pilih teks secara manual",
        "find_username": "Cari saya dengan username ini di WhatsApp",
        "footer_links": "Tautan footer",
        "back_to_top": "Kembali ke atas",
        "footer_location": "Berbasis di Bandung, Indonesia.",
        "back_projects": "Kembali ke proyek",
        "other_projects": "Lihat proyek lainnya",
        "project_link_label": "Tautan proyek",
        "detail_scope": "Peran / konteks",
        "detail_period": "Periode",
        "detail_tools": "Teknologi / bidang",
        "detail_result": "Hasil / keluaran",
        "project_documentation": "Detail proyek",
        "close_certificate": "Tutup dialog sertifikat",
        "certificate_alt": "Pratinjau sertifikat",
        "certificate_proof": "Lihat sertifikat",
        "page_title": "Aliyus Hedri | Freelance Engineer Robotika & Embedded",
        "page_description": "Aliyus Hedri adalah freelance engineer robotika dan embedded serta mahasiswa S2 Master by Research Teknik Elektro dengan fokus SLAM, IoT, Android, web, AI, dan dukungan riset.",
    },
}


def t(locale: str, key: str) -> str:
    return TRANSLATIONS[locale][key]


def header(locale: str, slug: str | None = None) -> str:
    other_locale = "id" if locale == "en" else "en"
    current_home = home_url(locale)
    language_target = home_url(other_locale)
    checked = "false" if locale == "en" else "true"
    logo_alt = "Aliyus Hedri logo" if locale == "en" else "Logo Aliyus Hedri"
    return f'''<a class="skip-link" href="#main">{text(t(locale, "skip"))}</a>
<header class="site-header"><div class="container header-inner">
<a class="brand" href="{current_home}" aria-label="{text(t(locale, "home"))}"><img class="logo" src="assets/images/logo.png" alt="{text(logo_alt)}" width="140" height="100"></a>
<div class="language-control" aria-label="{text(t(locale, "language_label"))}"><span>EN</span><button class="language-switch" type="button" role="switch" aria-checked="{checked}" aria-label="{text(t(locale, "switch_language"))}" data-language-target="{language_target}"><span class="switch-thumb"></span></button><span>ID</span></div>
<button class="nav-toggle" type="button" aria-expanded="false" aria-controls="navigation" aria-label="{text(t(locale, "open_menu"))}"><svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
<nav class="desktop-nav" id="navigation" aria-label="{text(t(locale, "nav_label"))}"><a href="{home_href(locale, "services")}">{text(t(locale, "services"))}</a><a href="{home_href(locale, "projects")}">{text(t(locale, "projects"))}</a><a href="{home_href(locale, "about")}">{text(t(locale, "about"))}</a><a class="nav-contact" href="{home_href(locale, "contact")}">{text(t(locale, "contact"))} {EXTERNAL}</a></nav>
</div></header>'''


def footer(locale: str) -> str:
    return f'''<footer class="site-footer"><div class="container footer-inner"><span>© 2026 Aliyus Hedri</span><span>{text(t(locale, "footer_location"))}</span><nav class="footer-nav" aria-label="{text(t(locale, "footer_links"))}"><a href="{home_href(locale, "awards")}">{text(t(locale, "awards"))}</a><a href="{home_href(locale, "cv")}">{text(t(locale, "cv_short"))}</a><a href="#main">{text(t(locale, "back_to_top"))} ↑</a></nav></div></footer>'''


def certificate_dialog(locale: str) -> str:
    return f'''<dialog id="certificate-dialog" class="certificate-dialog" aria-labelledby="certificate-title"><button class="dialog-close" type="button" aria-label="{text(t(locale, "close_certificate"))}">{CROSS}</button><h2 id="certificate-title"></h2><img id="certificate-image" alt=""></dialog>'''


def absolute_url(path: str) -> str:
    return f'{SITE_ORIGIN}{path if path.startswith("/") else "/" + path}'


def person_json_ld() -> str:
    person = {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": "Aliyus Hedri",
        "url": absolute_url("/"),
        "jobTitle": "Freelance Robotics & Embedded Engineer",
        "sameAs": PERSON_SAME_AS,
    }
    return json.dumps(person, ensure_ascii=False, separators=(",", ":"))


def document(
    locale: str,
    title: str,
    description: str,
    body: str,
    canonical_path: str,
    alternate_paths: dict[str, str],
    og_image_path: str = "/assets/images/aliyus.webp",
) -> str:
    locale_code = "en_US" if locale == "en" else "id_ID"
    alternate_locale_code = "id_ID" if locale == "en" else "en_US"
    canonical_url = absolute_url(canonical_path)
    alternate_en = absolute_url(alternate_paths["en"])
    alternate_id = absolute_url(alternate_paths["id"])
    x_default = absolute_url(alternate_paths.get("x-default", alternate_paths["en"]))
    og_image = absolute_url(og_image_path)
    return f'''<!doctype html>
<html lang="{locale}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="theme-color" content="#14263d"><meta name="description" content="{text(description)}"><meta name="robots" content="index,follow"><link rel="canonical" href="{text(canonical_url)}"><link rel="alternate" hreflang="en" href="{text(alternate_en)}"><link rel="alternate" hreflang="id" href="{text(alternate_id)}"><link rel="alternate" hreflang="x-default" href="{text(x_default)}"><meta property="og:type" content="website"><meta property="og:site_name" content="Aliyus Hedri"><meta property="og:locale" content="{locale_code}"><meta property="og:locale:alternate" content="{alternate_locale_code}"><meta property="og:url" content="{text(canonical_url)}"><meta property="og:title" content="{text(title)}"><meta property="og:description" content="{text(description)}"><meta property="og:image" content="{text(og_image)}"><meta property="og:image:alt" content="{text(title)}"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{text(title)}"><meta name="twitter:description" content="{text(description)}"><meta name="twitter:image" content="{text(og_image)}"><title>{text(title)}</title><link rel="icon" type="image/png" href="assets/images/logo.png"><link rel="preload" href="assets/fonts/manrope-latin.woff2" as="font" type="font/woff2" crossorigin><link rel="stylesheet" href="styles.css"><script type="application/ld+json">{person_json_ld()}</script><script src="app.js" defer></script></head><body data-locale="{locale}">{body}</body></html>'''


def project_year(project: dict, locale: str) -> str:
    value = project["year"]
    return value[locale] if isinstance(value, dict) else value


def project_visual(project: dict, locale: str, detail: bool = False) -> str:
    image = project.get("image")
    image_class = f'image-{image}' if image else "project-image-empty"
    label = project.get("image_label", {}).get(locale, project["title"][locale])
    if image:
        size = "1500" if detail else "1200"
        height = "1000" if detail else "900"
        loading = "" if detail else ' loading="lazy"'
        fetchpriority = ' fetchpriority="high"' if detail else ""
        tag = "figure" if detail else "div"
        return f'<{tag} class="{"detail-cover" if detail else "project-image"} {image_class}"><img src="assets/images/{text(image)}.webp" alt="{text(project["alt"][locale])}" width="{size}" height="{height}"{loading}{fetchpriority}></{tag}>'
    if detail:
        return f'<div class="detail-cover project-cover-text {image_class}" role="img" aria-label="{text(project["alt"][locale])}"><span>{text(label)}</span></div>'
    return f'<div class="project-image {image_class}" role="img" aria-label="{text(project["alt"][locale])}"><span>{text(label)}</span></div>'


def project_card(project: dict, locale: str) -> str:
    return f'''<a class="project-card" href="{detail_file(project["slug"], locale)}" data-category="{text(project["category"])}">{project_visual(project, locale)}<div class="project-meta"><span>{text(project["label"][locale])}</span><span>{text(project_year(project, locale))}</span></div><h3>{text(project["title"][locale])}</h3><p class="project-summary">{text(project["summary"][locale])}</p><span class="project-link">{text(t(locale, "view_project"))} {ARROW}</span></a>'''


def service_card(service: dict, locale: str) -> str:
    return f'''<article class="service-card"><h3>{text(service["title"][locale])}</h3><p>{text(service["summary"][locale])}</p><p class="service-tools"><span>{text(t(locale, "service_tools_label"))}</span>{text(service["tools"][locale])}</p></article>'''


def process_step(number: str, title: str, copy: str) -> str:
    return f'''<article class="process-step"><span class="process-number" aria-hidden="true">{text(number)}</span><h3>{text(title)}</h3><p>{text(copy)}</p></article>'''


def award_card(award: dict, locale: str) -> str:
    title = award["title"][locale]
    alt_prefix = "Certificate: " if locale == "en" else "Sertifikat: "
    return f'''<button class="award-card" type="button" data-certificate="assets/images/{award["image"]}.webp" data-certificate-title="{text(title)}" aria-label="{text(t(locale, "award_button_label") + title)}"><div class="award-image"><img src="assets/images/{award["image"]}.webp" alt="{text(alt_prefix + title)}" width="800" height="560" loading="lazy"></div><div class="award-content"><span class="award-year">{text(award["year"])}</span><h3>{text(title)}</h3><p>{text(award["description"][locale])}</p><span class="project-link">{text(t(locale, "view_certificate"))} {ARROW}</span></div></button>'''


def experience_item(period: str, title: str, organization: str, detail: str, kind: str) -> str:
    detail_html = f'<p>{text(detail)}</p>' if detail else ""
    return f'''<article class="experience-item"><p class="experience-period">{text(period)}</p><div class="experience-detail"><h3>{text(title)}</h3><p>{text(organization)}</p>{detail_html}</div><span class="experience-type">{text(kind)}</span></article>'''


def home_main(locale: str) -> str:
    hero_cv = "assets/documents/CV-Aliyus-Hedri-EN.pdf" if locale == "en" else "assets/documents/CV-Aliyus-Hedri.pdf"
    services = "".join(service_card(service, locale) for service in SERVICES)
    project_cards = "".join(project_card(project, locale) for project in PROJECTS)
    awards = "".join(award_card(award, locale) for award in AWARDS)
    steps = "".join(
        [
            process_step("01", t(locale, "step_brief_title"), t(locale, "step_brief_text")),
            process_step("02", t(locale, "step_scope_title"), t(locale, "step_scope_text")),
            process_step("03", t(locale, "step_build_title"), t(locale, "step_build_text")),
        ]
    )
    if locale == "en":
        experience = "".join(
            [
                experience_item("30 Jun–9 Aug 2025", "Mechatronics Engineering Intern", "PT Arthatronic Studio Teknologi", t(locale, "internship_detail"), t(locale, "industry")),
                experience_item("2024–2025", "EIRRG Coordinator", "Electronics & Intelligence Robotics Research Group", t(locale, "eirrg_detail"), t(locale, "leadership")),
                experience_item("2023–2025", "Computer Basics Laboratory Assistant", "Telkom University", t(locale, "lab_detail"), t(locale, "laboratory")),
                experience_item("2023", "PKKMB Committee", "Telkom University", t(locale, "pkkmb_detail"), t(locale, "organization")),
            ]
        )
        education = "".join(
            [
                experience_item(t(locale, "in_progress"), "Electrical Engineering", t(locale, "master_context"), "", t(locale, "education_type")),
                experience_item("2022–2026", "Bachelor of Electrical Engineering", t(locale, "bachelor_context"), t(locale, "bachelor_detail"), t(locale, "education_type")),
            ]
        )
    else:
        experience = "".join(
            [
                experience_item("30 Jun–9 Agu 2025", "Magang Mechatronics Engineer", "PT Arthatronic Studio Teknologi", t(locale, "internship_detail"), t(locale, "industry")),
                experience_item("2024–2025", "Koordinator EIRRG", "Electronics & Intelligence Robotics Research Group", t(locale, "eirrg_detail"), t(locale, "leadership")),
                experience_item("2023–2025", "Asisten Laboratorium Dasar Komputer", "Telkom University", t(locale, "lab_detail"), t(locale, "laboratory")),
                experience_item("2023", "Panitia PKKMB", "Telkom University", t(locale, "pkkmb_detail"), t(locale, "organization")),
            ]
        )
        education = "".join(
            [
                experience_item(t(locale, "in_progress"), "Teknik Elektro", t(locale, "master_context"), "", t(locale, "education_type")),
                experience_item("2022–2026", "S1 Teknik Elektro", t(locale, "bachelor_context"), t(locale, "bachelor_detail"), t(locale, "education_type")),
            ]
        )

    copy_username_label = t(locale, "copy_username")
    copy_email_label = t(locale, "copy_email")
    return f'''<main id="main">
<section class="hero container" aria-labelledby="hero-title"><div class="hero-copy"><p class="intro-line">{text(t(locale, "role"))}</p><h1 id="hero-title">Aliyus<br>Hedri</h1><p class="hero-description">{text(t(locale, "hero_description"))}</p><div class="hero-actions"><a class="button button-primary" href="#contact">{text(t(locale, "discuss_project"))} {ARROW}</a><a class="button button-secondary" href="#projects">{text(t(locale, "explore_projects"))} {ARROW}</a><a class="hero-cv-link" href="{hero_cv}" download>{text(t(locale, "download_cv"))} {DOWNLOAD}</a></div><p class="hero-location">{text(t(locale, "location"))}</p></div><figure class="hero-portrait"><img src="assets/images/aliyus.webp" alt="{text(t(locale, "portrait_alt"))}" width="1334" height="1179" fetchpriority="high"><figcaption class="portrait-caption"><strong>Aliyus Hedri</strong><span>{text(t(locale, "portrait_caption"))}</span></figcaption></figure></section>
<div class="container hero-footnote"><span>{text(t(locale, "focus_robotics"))}</span><span>{text(t(locale, "focus_slam"))}</span><span>{text(t(locale, "focus_embedded"))}</span><span>{text(t(locale, "focus_iot"))}</span></div>

<section class="services-section section container" id="services" aria-labelledby="services-title"><div class="section-heading"><h2 id="services-title">{text(t(locale, "services_heading"))}</h2><p>{text(t(locale, "services_intro"))}</p></div><div class="service-grid">{services}</div></section>

<section class="section container" id="projects" aria-labelledby="projects-title"><div class="section-heading"><h2 id="projects-title">{text(t(locale, "selected_projects"))}</h2><p>{text(t(locale, "projects_intro"))}</p></div><div class="project-filters" role="group" aria-label="{text(t(locale, "filter_label"))}"><button class="filter-button" type="button" data-filter="all" aria-pressed="true">{text(t(locale, "all_projects"))}</button><button class="filter-button" type="button" data-filter="robotics" aria-pressed="false">{text(t(locale, "filter_robotics"))}</button><button class="filter-button" type="button" data-filter="embedded" aria-pressed="false">{text(t(locale, "filter_embedded"))}</button><button class="filter-button" type="button" data-filter="iot" aria-pressed="false">{text(t(locale, "filter_iot"))}</button><button class="filter-button" type="button" data-filter="software" aria-pressed="false">{text(t(locale, "filter_software"))}</button><button class="filter-button" type="button" data-filter="ai" aria-pressed="false">{text(t(locale, "filter_ai"))}</button></div><p id="filter-status" class="sr-only" role="status" aria-live="polite">{text(t(locale, "projects_shown"))}</p><div class="project-grid">{project_cards}</div></section>

<section class="process-section section" id="how-work" aria-labelledby="how-work-title"><div class="container"><div class="section-heading"><h2 id="how-work-title">{text(t(locale, "how_work_heading"))}</h2><p>{text(t(locale, "how_work_intro"))}</p></div><div class="process-grid">{steps}</div></div></section>

<section class="about-section" id="about" aria-labelledby="about-title"><div class="container about-grid"><div class="about-copy"><h2 id="about-title">{text(t(locale, "about_heading"))}</h2><p>{text(t(locale, "about_p1"))}</p><p>{text(t(locale, "about_p2"))}</p><p>{text(t(locale, "about_p3"))}</p><a class="text-link" href="{home_href(locale, "cv")}">{text(t(locale, "see_cv"))} {ARROW}</a></div><div class="expertise-list"><div class="expertise-item"><h3>{text(t(locale, "expertise_robotics"))}</h3><p>{text(t(locale, "expertise_robotics_text"))}</p></div><div class="expertise-item"><h3>{text(t(locale, "expertise_embedded"))}</h3><p>{text(t(locale, "expertise_embedded_text"))}</p></div><div class="expertise-item"><h3>{text(t(locale, "expertise_iot"))}</h3><p>{text(t(locale, "expertise_iot_text"))}</p></div></div></div></section>

<section class="section container" id="experience" aria-labelledby="experience-title"><div class="section-heading"><h2 id="experience-title">{text(t(locale, "experience_heading"))}</h2><p>{text(t(locale, "experience_intro"))}</p></div><div class="experience-list">{experience}</div></section>

<section class="section compact-section container" id="education" aria-labelledby="education-title"><div class="section-heading"><h2 id="education-title">{text(t(locale, "education_heading"))}</h2><p>{text(t(locale, "education_intro"))}</p></div><div class="experience-list">{education}</div></section>

<section class="container research-block" id="research" aria-labelledby="research-title"><div class="research-copy"><h2 id="research-title">{text(t(locale, "research_heading"))}</h2><p>{text(t(locale, "research_p1"))}</p><p>{text(t(locale, "research_p2"))}</p></div><aside class="research-note"><span class="research-symbol" aria-hidden="true">3D</span><h3>{text(t(locale, "target_label"))}</h3><p>{text(t(locale, "research_note"))}</p></aside></section>

<section class="section award-section" id="awards" aria-labelledby="awards-title"><div class="container"><div class="section-heading"><h2 id="awards-title">{text(t(locale, "awards_heading"))}</h2><p>{text(t(locale, "awards_intro"))}</p></div><div class="award-grid">{awards}</div><p class="additional-award">{text(t(locale, "additional_award"))}</p></div></section>

<section class="cv-section container" id="cv" aria-labelledby="cv-title"><div class="section-heading"><h2 id="cv-title">{text(t(locale, "cv_heading"))}</h2><p>{text(t(locale, "cv_intro"))}</p></div><div class="cv-actions"><a class="button button-primary" href="assets/documents/CV-Aliyus-Hedri-EN.pdf" download>{text(t(locale, "download_english_cv"))} {DOWNLOAD}</a><a class="button button-secondary" href="assets/documents/CV-Aliyus-Hedri.pdf" download>{text(t(locale, "download_indonesian_cv"))} {DOWNLOAD}</a></div></section>

<section class="contact-section" id="contact" aria-labelledby="contact-title"><div class="container contact-inner"><div class="contact-copy"><h2 id="contact-title">{text(t(locale, "contact_heading"))}<span aria-hidden="true">.</span></h2><p>{text(t(locale, "contact_intro"))}</p></div><div class="contact-channels"><div class="contact-primary"><div class="contact-card contact-username" aria-label="{text(t(locale, "contact_whatsapp"))}"><span class="contact-symbol" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.5 8.5 0 0 1-12.6 7.4L3 21l1.9-5.4A8.5 8.5 0 1 1 21 11.5Z"/><path d="M8 8c0 4 4 8 8 8l1-3-3-1-1 1-2-2 1-1-1-3Z"/></svg></span><span class="contact-card-label">{text(t(locale, "whatsapp"))}<small>@aliyushedri</small><small>{text(t(locale, "find_username"))}</small></span><button class="copy-contact" type="button" data-copy="username" data-copy-value="@aliyushedri" data-copy-success="{text(t(locale, "copy_username_status"))}" data-copy-failed="{text(t(locale, "copy_failed_status"))}" aria-label="{text(copy_username_label)}"><span aria-hidden="true">{text(t(locale, "copy_action"))}</span></button><span class="copy-status" data-copy-status="username" role="status" aria-live="polite"></span></div><div class="contact-card contact-email-card"><span class="contact-symbol" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="3"/><path d="m3 7 9 6 9-6"/></svg></span><span class="contact-card-label">{text(t(locale, "gmail"))}<small>aliyus.hedri@gmail.com</small></span><a class="contact-email-link" href="https://mail.google.com/mail/?view=cm&amp;fs=1&amp;to=aliyus.hedri%40gmail.com" target="_blank" rel="noopener" aria-label="{text(t(locale, "contact_gmail"))}">{text(t(locale, "open_gmail"))} {EXTERNAL}</a><button class="copy-contact" type="button" data-copy="email" data-copy-value="aliyus.hedri@gmail.com" data-copy-success="{text(t(locale, "copy_email_status"))}" data-copy-failed="{text(t(locale, "copy_failed_status"))}" aria-label="{text(copy_email_label)}"><span aria-hidden="true">{text(t(locale, "copy_action"))}</span></button><span class="copy-status" data-copy-status="email" role="status" aria-live="polite"></span></div></div><div class="contact-socials"><a href="https://www.instagram.com/aliyushedri" target="_blank" rel="noopener" aria-label="{text(t(locale, "contact_instagram"))}">{text(t(locale, "instagram"))}{EXTERNAL}</a><a href="https://www.linkedin.com/in/aliyushedri/" target="_blank" rel="noopener" aria-label="{text(t(locale, "contact_linkedin"))}">{text(t(locale, "linkedin"))}{EXTERNAL}</a><a href="https://github.com/aliyushedri" target="_blank" rel="noopener" aria-label="{text(t(locale, "contact_github"))}">{text(t(locale, "github"))}{EXTERNAL}</a></div></div></div></section>
</main>'''


def certificate_button(project: dict, locale: str) -> str:
    certificate = project.get("certificate")
    if not certificate:
        return ""
    title = project["certificate_title"][locale]
    return f'<button class="button button-secondary certificate-button" type="button" data-certificate="assets/images/{certificate["image"]}.webp" data-certificate-title="{text(title)}">{text(t(locale, "certificate_proof"))} {ARROW}</button>'


def project_detail_main(project: dict, locale: str) -> str:
    gallery_data = project.get("gallery_id" if locale == "id" else "gallery", project.get("gallery", []))
    gallery = "".join(
        f'<figure><img src="assets/images/{text(image)}.webp" alt="{text(caption)}" width="1000" height="1000" loading="lazy"><figcaption>{text(caption)}</figcaption></figure>'
        for image, caption in gallery_data
    )
    sections = "".join(
        f'<section><h2>{text(title)}</h2><p>{text(copy)}</p></section>'
        for title, copy in project["sections"][locale]
    )
    gallery_html = f'<section class="detail-gallery" aria-label="{text(t(locale, "project_documentation"))}">{gallery}</section>' if gallery else ""
    external = ""
    if project.get("external_link"):
        external = f'<a class="button button-secondary project-external-link" href="{text(project["external_link"])}" target="_blank" rel="noopener">{text(project["external_label"][locale])} {EXTERNAL}</a>'
    return f'''<main id="main" class="project-detail container"><a class="back-link" href="{home_href(locale, "projects")}">← {text(t(locale, "back_projects"))}</a><div class="detail-heading"><p class="detail-category">{text(project["label"][locale])} · {text(project_year(project, locale))}</p><h1>{text(project["title"][locale])}</h1><p class="detail-lead">{text(project["lead"][locale])}</p></div>{project_visual(project, locale, detail=True)}<div class="detail-layout"><div class="detail-body">{sections}{certificate_button(project, locale)}{external}</div><aside class="detail-facts"><h2>{text(t(locale, "project_documentation"))}</h2><dl><dt>{text(t(locale, "detail_scope"))}</dt><dd>{text(project["role"][locale])}</dd><dt>{text(t(locale, "detail_period"))}</dt><dd>{text(project_year(project, locale))}</dd><dt>{text(t(locale, "detail_tools"))}</dt><dd>{text(project["tools"][locale])}</dd><dt>{text(t(locale, "detail_result"))}</dt><dd>{text(project["result"][locale])}</dd></dl></aside></div>{gallery_html}<div class="detail-bottom"><a class="button button-primary" href="{home_href(locale, "projects")}">{text(t(locale, "other_projects"))} {ARROW}</a><a class="text-link" href="https://mail.google.com/mail/?view=cm&amp;fs=1&amp;to=aliyus.hedri%40gmail.com" target="_blank" rel="noopener">{text(t(locale, "discuss_project"))} {EXTERNAL}</a></div></main>'''


def build_home(locale: str) -> None:
    title = t(locale, "page_title")
    description = t(locale, "page_description")
    body = header(locale) + home_main(locale) + footer(locale) + certificate_dialog(locale)
    canonical_path = "/" if locale == "en" else "/id/"
    alternate_paths = {"en": "/", "id": "/id/", "x-default": "/"}
    html = document(locale, title, description, body, canonical_path, alternate_paths)
    # Keep the old Indonesian entry point for bookmarks; app.js redirects it.
    (ROOT / home_file(locale)).write_text(html, encoding="utf-8")
    if locale == "id":
        # Nested output needs parent-relative asset, page, and dialog-image URLs.
        # Local anchors remain on the Indonesian page.
        def parent_relative(match: re.Match) -> str:
            attribute, url = match.groups()
            if url.startswith(("#", "/")) or ":" in url:
                return match.group(0)
            return f'{attribute}="../{url}"'

        html = re.sub(r'(href|src|data-language-target|data-certificate)="([^"\n]+)"', parent_relative, html)
        destination = ROOT / "id" / "index.html"
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(html, encoding="utf-8")


def build_project(project: dict, locale: str) -> None:
    title = f'{project["title"][locale]} | Aliyus Hedri'
    body = header(locale, project["slug"]) + project_detail_main(project, locale) + footer(locale) + certificate_dialog(locale)
    english_path = f'/{detail_file(project["slug"], "en")}'
    indonesian_path = f'/{detail_file(project["slug"], "id")}'
    canonical_path = english_path if locale == "en" else indonesian_path
    alternate_paths = {"en": english_path, "id": indonesian_path, "x-default": english_path}
    image = project.get("image")
    og_image_path = f'/assets/images/{image}.webp' if image else "/assets/images/aliyus.webp"
    html = document(locale, title, project["summary"][locale], body, canonical_path, alternate_paths, og_image_path)
    (ROOT / detail_file(project["slug"], locale)).write_text(html, encoding="utf-8")


def main() -> None:
    for locale in ("en", "id"):
        build_home(locale)
        for project in PROJECTS:
            build_project(project, locale)
    print(f"Generated bilingual home pages and {len(PROJECTS) * 2} project pages.")


if __name__ == "__main__":
    main()
