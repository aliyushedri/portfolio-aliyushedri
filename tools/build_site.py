"""Generate the bilingual static portfolio using only Python's standard library."""

from html import escape
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]

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
        "category": "robotics vision",
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
                    "I led Team ARJUNA. The documented work covered the robot platform, balance system, perception, and integration required for the competition.",
                ),
                (
                    "Documented outcome",
                    "Team ARJUNA became a finalist in the 2024 Kontes Robot Indonesia, Kontes Robot SAR Indonesia division. The finalist certificate is available as an image below.",
                ),
            ],
            "id": [
                (
                    "Ruang lingkup proyek",
                    "Proyek ini mencakup robot berkaki enam dengan keseimbangan otomatis berbasis IMU dan deteksi objek real-time menggunakan YOLOv8 untuk navigasi otonom.",
                ),
                (
                    "Peran saya",
                    "Saya memimpin Tim ARJUNA. Pekerjaan yang terdokumentasi mencakup platform robot, sistem keseimbangan, persepsi, dan integrasi untuk kompetisi.",
                ),
                (
                    "Hasil yang terdokumentasi",
                    "Tim ARJUNA menjadi finalis Kontes Robot Indonesia 2024 pada divisi Kontes Robot SAR Indonesia. Sertifikat finalis tersedia sebagai gambar di bawah.",
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
                    "Documented outcome",
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
                    "Hasil yang terdokumentasi",
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
            "en": "Nawa Majika interactive installation documented during an internship",
            "id": "Dokumentasi instalasi interaktif Nawa Majika saat magang",
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
            "en": "Installation documentation from an internship at PT Arthatronic Studio Teknologi.",
            "id": "Dokumentasi instalasi dari pengalaman magang di PT Arthatronic Studio Teknologi.",
        },
        "role": {
            "en": "Mechatronics Engineer Intern",
            "id": "Mechatronics Engineer Intern",
        },
        "tools": {
            "en": "Mechatronics and device integration",
            "id": "Mekatronika dan integrasi perangkat",
        },
        "result": {
            "en": "Internship project documentation",
            "id": "Dokumentasi proyek magang",
        },
        "lead": {
            "en": "Documentation from an internship where physical devices formed part of interactive installations.",
            "id": "Dokumentasi pengalaman magang dengan perangkat fisik sebagai bagian dari instalasi interaktif.",
        },
        "sections": {
            "en": [
                (
                    "Internship context",
                    "I was a Mechatronics Engineer Intern at PT Arthatronic Studio Teknologi from 30 June to 9 August 2025.",
                ),
                (
                    "Available documentation",
                    "The photographs document the Nawa Majika installation, interactive lantern devices, and the Skyward project during the internship.",
                ),
                (
                    "Contribution boundary",
                    "The supplied CV and project records do not specify individual implementation deliverables. This page therefore presents the internship context and the available installation documentation.",
                ),
            ],
            "id": [
                (
                    "Konteks magang",
                    "Saya menjalani magang sebagai Mechatronics Engineer di PT Arthatronic Studio Teknologi pada 30 Juni–9 Agustus 2025.",
                ),
                (
                    "Dokumentasi yang tersedia",
                    "Foto-foto mendokumentasikan instalasi Nawa Majika, perangkat lentera interaktif, dan proyek Skyward selama magang.",
                ),
                (
                    "Batas kontribusi",
                    "CV dan catatan proyek yang tersedia tidak menjelaskan keluaran implementasi individual. Halaman ini menyajikan konteks magang dan dokumentasi instalasi yang tersedia.",
                ),
            ],
        },
        "gallery": [
            ("lantern", "Interactive lantern device from the Nawa Majika project"),
            ("lantern-detail", "Detail of the Nawa Majika lantern device"),
            ("skyward", "Skyward project device documentation"),
        ],
        "gallery_id": [
            ("lantern", "Perangkat lentera interaktif dari proyek Nawa Majika"),
            ("lantern-detail", "Detail perangkat lentera Nawa Majika"),
            ("skyward", "Dokumentasi perangkat proyek Skyward"),
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
                    "Documentation",
                    "The project ran from February to June 2025. The available photographs show the physical prototype, water container, and sensor installation.",
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
                    "Dokumentasi",
                    "Proyek berlangsung pada Februari–Juni 2025. Foto yang tersedia memperlihatkan prototipe fisik, wadah air, dan pemasangan sensor.",
                ),
            ],
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


TRANSLATIONS = {
    "en": {
        "skip": "Skip to main content",
        "home": "Aliyus Hedri, home",
        "open_menu": "Open navigation menu",
        "close_menu": "Close navigation menu",
        "nav_label": "Main navigation",
        "projects": "Projects",
        "about": "About",
        "experience": "Experience",
        "education": "Education",
        "research": "Research",
        "awards": "Awards & certificates",
        "cv_short": "CV",
        "contact": "Contact",
        "language_label": "Language selection",
        "switch_language": "Switch to Bahasa Indonesia",
        "role": "Robotics & Embedded Systems",
        "hero_description": "Electrical Engineering master's student at Telkom University working across robotics, SLAM, embedded systems, IoT, and AI.",
        "location": "Bandung, West Java, Indonesia",
        "explore_projects": "View selected projects",
        "download_cv": "Download CV",
        "focus_robotics": "Robotics",
        "focus_slam": "SLAM",
        "focus_embedded": "Embedded systems",
        "focus_iot": "Internet of Things",
        "portrait_alt": "Aliyus Hedri wearing a Telkom University jacket",
        "portrait_caption": "Master by Research · Electrical Engineering",
        "selected_projects": "Selected projects",
        "projects_intro": "Documented projects across robotics, embedded systems, IoT, and mechatronics from 2023 to 2025.",
        "filter_label": "Filter projects by field",
        "all_projects": "All projects",
        "filter_robotics": "Robotics",
        "filter_embedded": "Embedded",
        "filter_iot": "IoT",
        "projects_shown": "4 projects shown",
        "view_project": "View project",
        "about_heading": "About",
        "about_p1": "I am an Electrical Engineering master's student in Telkom University's Master by Research program. My documented work covers robotics, SLAM, embedded systems, IoT, and AI.",
        "about_p2": "Project records include leading Team ARJUNA, building monitoring prototypes, and an internship as a Mechatronics Engineer. The pages identify the documented scope and outcomes for each project.",
        "see_cv": "See curriculum vitae",
        "expertise_robotics": "Robotics and perception",
        "expertise_robotics_text": "ROS2, SLAM, sensor fusion, mobile and legged robots, YOLOv8, and OpenCV.",
        "expertise_embedded": "Embedded systems and sensors",
        "expertise_embedded_text": "C/C++, ESP32, STM32, Raspberry Pi, IMU, camera, distance, and environmental sensors.",
        "expertise_iot": "IoT and software",
        "expertise_iot_text": "Python, MQTT, HTTP/REST API, Wi-Fi, Git, Linux, and MATLAB/Simulink.",
        "experience_heading": "Experience",
        "experience_intro": "Industry, laboratory, and organizational roles recorded in the CV.",
        "industry": "Industry",
        "leadership": "Leadership",
        "laboratory": "Laboratory",
        "organization": "Organization",
        "internship_detail": "The CV records this internship period; the supplied documents do not list specific individual deliverables.",
        "eirrg_detail": "Coordinator for the Electronics & Intelligence Robotics Research Group.",
        "lab_detail": "Computer Basics Laboratory Assistant at Telkom University.",
        "pkkmb_detail": "Committee member for Telkom University's PKKMB in 2023.",
        "education_heading": "Education",
        "education_intro": "Formal education recorded in the CV.",
        "in_progress": "In progress",
        "master_context": "Master by Research · Telkom University",
        "bachelor_context": "Telkom University · GPA 3.8",
        "bachelor_detail": "APERTI BUMN 2022 scholarship recipient.",
        "school_context": "Science track",
        "school_detail": "Graduated with good standing.",
        "education_type": "Education",
        "research_heading": "Research",
        "research_p1": "My current master's research focuses on LiDAR-inertial odometry and SLAM for mobile robots.",
        "research_p2": "A 2026 AGV project adapts FAST-LIO to four low-cost RGB-D Kinect V1 cameras and distributes computation between an STM32 and a Mini PC on ROS2 Jazzy.",
        "target_label": "Design target",
        "research_note": "RMSE ≤10 cm is listed as a design target for the AGV project; it is not a reported experimental result.",
        "awards_heading": "Awards & certificates",
        "awards_intro": "Selected competition and academic recognition recorded in the certificates and CV.",
        "view_certificate": "View certificate",
        "award_button_label": "View certificate: ",
        "additional_award": "Additional record: participant in PIMNAS 2025, PKM-KI1, with TIRNARA.",
        "cv_heading": "Curriculum vitae",
        "cv_intro": "Download the current curriculum vitae in English or Bahasa Indonesia.",
        "download_english_cv": "Download English CV",
        "download_indonesian_cv": "Download Bahasa Indonesia CV",
        "contact_heading": "Contact",
        "contact_intro": "For opportunities and collaboration in robotics, embedded systems, IoT, or related research.",
        "whatsapp": "WhatsApp",
        "gmail": "Gmail",
        "instagram": "Instagram",
        "linkedin": "LinkedIn",
        "github": "GitHub",
        "contact_whatsapp": "WhatsApp: @aliyushedri",
        "contact_gmail": "Gmail: aliyus.hedri@gmail.com",
        "contact_instagram": "Instagram: aliyushedri",
        "contact_linkedin": "LinkedIn: aliyushedri",
        "contact_github": "GitHub: aliyushedri",
        "back_to_top": "Back to top",
        "footer_location": "Based in Bandung, Indonesia.",
        "back_projects": "Back to projects",
        "other_projects": "View other projects",
        "discuss_project": "Contact me about this project",
        "detail_scope": "Role / context",
        "detail_period": "Period",
        "detail_tools": "Technology / field",
        "detail_result": "Outcome / output",
        "project_documentation": "Project documentation",
        "close_certificate": "Close certificate dialog",
        "certificate_alt": "Certificate preview",
        "certificate_proof": "View certificate",
        "page_title": "Aliyus Hedri | Robotics & Embedded Systems",
        "page_description": "Portfolio of Aliyus Hedri, an Electrical Engineering master's student working on robotics, SLAM, embedded systems, IoT, and AI.",
    },
    "id": {
        "skip": "Lewati ke konten utama",
        "home": "Aliyus Hedri, beranda",
        "open_menu": "Buka menu navigasi",
        "close_menu": "Tutup menu navigasi",
        "nav_label": "Navigasi utama",
        "projects": "Proyek",
        "about": "Tentang",
        "experience": "Pengalaman",
        "education": "Pendidikan",
        "research": "Riset",
        "awards": "Penghargaan & sertifikat",
        "cv_short": "CV",
        "contact": "Kontak",
        "language_label": "Pilihan bahasa",
        "switch_language": "Beralih ke bahasa Inggris",
        "role": "Robotika & Embedded Systems",
        "hero_description": "Mahasiswa S2 Teknik Elektro di Telkom University dengan fokus pada robotika, SLAM, embedded systems, IoT, dan AI.",
        "location": "Bandung, Jawa Barat, Indonesia",
        "explore_projects": "Lihat proyek pilihan",
        "download_cv": "Unduh CV",
        "focus_robotics": "Robotika",
        "focus_slam": "SLAM",
        "focus_embedded": "Embedded systems",
        "focus_iot": "Internet of Things",
        "portrait_alt": "Aliyus Hedri mengenakan jaket Telkom University",
        "portrait_caption": "Master by Research · Teknik Elektro",
        "selected_projects": "Proyek pilihan",
        "projects_intro": "Proyek terdokumentasi di bidang robotika, embedded systems, IoT, dan mekatronika dari 2023 hingga 2025.",
        "filter_label": "Filter proyek berdasarkan bidang",
        "all_projects": "Semua proyek",
        "filter_robotics": "Robotika",
        "filter_embedded": "Embedded",
        "filter_iot": "IoT",
        "projects_shown": "4 proyek ditampilkan",
        "view_project": "Lihat proyek",
        "about_heading": "Tentang",
        "about_p1": "Saya adalah mahasiswa S2 Teknik Elektro pada program Master by Research di Telkom University. Pekerjaan yang terdokumentasi mencakup robotika, SLAM, embedded systems, IoT, dan AI.",
        "about_p2": "Catatan proyek mencakup kepemimpinan Tim ARJUNA, pembuatan prototipe monitoring, dan pengalaman magang sebagai Mechatronics Engineer. Setiap halaman menjelaskan ruang lingkup dan hasil yang terdokumentasi.",
        "see_cv": "Lihat curriculum vitae",
        "expertise_robotics": "Robotika dan persepsi",
        "expertise_robotics_text": "ROS2, SLAM, sensor fusion, robot bergerak dan robot berkaki, YOLOv8, serta OpenCV.",
        "expertise_embedded": "Embedded systems dan sensor",
        "expertise_embedded_text": "C/C++, ESP32, STM32, Raspberry Pi, IMU, kamera, sensor jarak, dan sensor lingkungan.",
        "expertise_iot": "IoT dan perangkat lunak",
        "expertise_iot_text": "Python, MQTT, HTTP/REST API, Wi-Fi, Git, Linux, dan MATLAB/Simulink.",
        "experience_heading": "Pengalaman",
        "experience_intro": "Peran di industri, laboratorium, dan organisasi yang tercatat di CV.",
        "industry": "Industri",
        "leadership": "Kepemimpinan",
        "laboratory": "Laboratorium",
        "organization": "Organisasi",
        "internship_detail": "CV mencatat periode magang ini; dokumen yang tersedia tidak merinci keluaran implementasi individual.",
        "eirrg_detail": "Koordinator Electronics & Intelligence Robotics Research Group.",
        "lab_detail": "Asisten Laboratorium Dasar Komputer di Telkom University.",
        "pkkmb_detail": "Panitia PKKMB Telkom University pada 2023.",
        "education_heading": "Pendidikan",
        "education_intro": "Pendidikan formal yang tercatat di CV.",
        "in_progress": "Sedang berjalan",
        "master_context": "Master by Research · Telkom University",
        "bachelor_context": "Telkom University · IPK 3,8",
        "bachelor_detail": "Penerima Beasiswa APERTI BUMN 2022.",
        "school_context": "Jurusan IPA",
        "school_detail": "Lulus dengan predikat baik.",
        "education_type": "Pendidikan",
        "research_heading": "Riset",
        "research_p1": "Riset magister saya saat ini berfokus pada LiDAR-inertial odometry dan SLAM untuk robot bergerak.",
        "research_p2": "Proyek AGV 2026 mengadaptasi FAST-LIO untuk empat kamera RGB-D Kinect V1 berbiaya rendah dan membagi komputasi antara STM32 dan Mini PC pada ROS2 Jazzy.",
        "target_label": "Target desain",
        "research_note": "RMSE ≤10 cm tercantum sebagai target desain proyek AGV; angka ini bukan hasil eksperimen yang dilaporkan.",
        "awards_heading": "Penghargaan & sertifikat",
        "awards_intro": "Pilihan penghargaan kompetisi dan akademik yang tercatat pada sertifikat dan CV.",
        "view_certificate": "Lihat sertifikat",
        "award_button_label": "Lihat sertifikat: ",
        "additional_award": "Catatan tambahan: peserta PIMNAS 2025, PKM-KI1, melalui TIRNARA.",
        "cv_heading": "Curriculum vitae",
        "cv_intro": "Unduh curriculum vitae terbaru dalam bahasa Inggris atau Bahasa Indonesia.",
        "download_english_cv": "Unduh CV bahasa Inggris",
        "download_indonesian_cv": "Unduh CV Bahasa Indonesia",
        "contact_heading": "Kontak",
        "contact_intro": "Untuk peluang dan kolaborasi di bidang robotika, embedded systems, IoT, atau riset terkait.",
        "whatsapp": "WhatsApp",
        "gmail": "Gmail",
        "instagram": "Instagram",
        "linkedin": "LinkedIn",
        "github": "GitHub",
        "contact_whatsapp": "WhatsApp: @aliyushedri",
        "contact_gmail": "Gmail: aliyus.hedri@gmail.com",
        "contact_instagram": "Instagram: aliyushedri",
        "contact_linkedin": "LinkedIn: aliyushedri",
        "contact_github": "GitHub: aliyushedri",
        "back_to_top": "Kembali ke atas",
        "footer_location": "Berbasis di Bandung, Indonesia.",
        "back_projects": "Kembali ke proyek",
        "other_projects": "Lihat proyek lainnya",
        "discuss_project": "Hubungi saya tentang proyek ini",
        "detail_scope": "Peran / konteks",
        "detail_period": "Periode",
        "detail_tools": "Teknologi / bidang",
        "detail_result": "Hasil / keluaran",
        "project_documentation": "Dokumentasi proyek",
        "close_certificate": "Tutup dialog sertifikat",
        "certificate_alt": "Pratinjau sertifikat",
        "certificate_proof": "Lihat sertifikat",
        "page_title": "Aliyus Hedri | Robotika & Embedded Systems",
        "page_description": "Portfolio Aliyus Hedri, mahasiswa S2 Teknik Elektro dengan pekerjaan di bidang robotika, SLAM, embedded systems, IoT, dan AI.",
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
<nav class="desktop-nav" id="navigation" aria-label="{text(t(locale, "nav_label"))}"><a href="{home_href(locale, "projects")}">{text(t(locale, "projects"))}</a><a href="{home_href(locale, "about")}">{text(t(locale, "about"))}</a><a href="{home_href(locale, "experience")}">{text(t(locale, "experience"))}</a><a href="{home_href(locale, "awards")}">{text(t(locale, "awards"))}</a><a href="{home_href(locale, "cv")}">{text(t(locale, "cv_short"))}</a><a class="nav-contact" href="{home_href(locale, "contact")}">{text(t(locale, "contact"))} {EXTERNAL}</a></nav>
</div></header>'''


def footer(locale: str) -> str:
    return f'''<footer class="site-footer"><div class="container footer-inner"><span>© 2026 Aliyus Hedri</span><span>{text(t(locale, "footer_location"))}</span><a href="#main">{text(t(locale, "back_to_top"))} ↑</a></div></footer>'''


def certificate_dialog(locale: str) -> str:
    return f'''<dialog id="certificate-dialog" class="certificate-dialog" aria-labelledby="certificate-title"><button class="dialog-close" type="button" aria-label="{text(t(locale, "close_certificate"))}">{CROSS}</button><h2 id="certificate-title"></h2><img id="certificate-image" alt=""></dialog>'''


def document(locale: str, title: str, description: str, body: str) -> str:
    return f'''<!doctype html>
<html lang="{locale}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="theme-color" content="#14263d"><meta name="description" content="{text(description)}"><title>{text(title)}</title><link rel="icon" type="image/png" href="assets/images/logo.png"><link rel="preload" href="assets/fonts/manrope-latin.woff2" as="font" type="font/woff2" crossorigin><link rel="stylesheet" href="styles.css"><script src="app.js" defer></script></head><body data-locale="{locale}">{body}</body></html>'''


def project_card(project: dict, locale: str) -> str:
    return f'''<a class="project-card" href="{detail_file(project["slug"], locale)}" data-category="{text(project["category"])}"><div class="project-image image-{project["image"]}"><img src="assets/images/{project["image"]}.webp" alt="{text(project["alt"][locale])}" width="1200" height="900" loading="lazy"></div><div class="project-meta"><span>{text(project["label"][locale])}</span><span>{text(project["year"])}</span></div><h3>{text(project["title"][locale])}</h3><p class="project-summary">{text(project["summary"][locale])}</p><span class="project-link">{text(t(locale, "view_project"))} {ARROW}</span></a>'''


def award_card(award: dict, locale: str) -> str:
    title = award["title"][locale]
    alt_prefix = "Certificate: " if locale == "en" else "Sertifikat: "
    return f'''<button class="award-card" type="button" data-certificate="assets/images/{award["image"]}.webp" data-certificate-title="{text(title)}" aria-label="{text(t(locale, "award_button_label") + title)}"><div class="award-image"><img src="assets/images/{award["image"]}.webp" alt="{text(alt_prefix + title)}" width="800" height="560" loading="lazy"></div><div class="award-content"><span class="award-year">{text(award["year"])}</span><h3>{text(title)}</h3><p>{text(award["description"][locale])}</p><span class="project-link">{text(t(locale, "view_certificate"))} {ARROW}</span></div></button>'''


def experience_item(period: str, title: str, organization: str, detail: str, kind: str) -> str:
    detail_html = f'<p>{text(detail)}</p>' if detail else ""
    return f'''<article class="experience-item"><p class="experience-period">{text(period)}</p><div class="experience-detail"><h3>{text(title)}</h3><p>{text(organization)}</p>{detail_html}</div><span class="experience-type">{text(kind)}</span></article>'''


def home_main(locale: str) -> str:
    hero_cv = "assets/documents/CV-Aliyus-Hedri-EN.pdf" if locale == "en" else "assets/documents/CV-Aliyus-Hedri.pdf"
    project_cards = "".join(project_card(project, locale) for project in PROJECTS)
    awards = "".join(award_card(award, locale) for award in AWARDS)
    if locale == "en":
        experience = "".join(
            [
                experience_item("30 Jun–9 Aug 2025", "Mechatronics Engineer Intern", "PT Arthatronic Studio Teknologi", t(locale, "internship_detail"), t(locale, "industry")),
                experience_item("2024–2025", "EIRRG Coordinator", "Electronics & Intelligence Robotics Research Group", t(locale, "eirrg_detail"), t(locale, "leadership")),
                experience_item("2023–2025", "Computer Basics Laboratory Assistant", "Telkom University", t(locale, "lab_detail"), t(locale, "laboratory")),
                experience_item("2023", "PKKMB Committee", "Telkom University", t(locale, "pkkmb_detail"), t(locale, "organization")),
            ]
        )
        education = "".join(
            [
                experience_item(t(locale, "in_progress"), "Electrical Engineering", t(locale, "master_context"), "", t(locale, "education_type")),
                experience_item("2022–2026", "Bachelor of Electrical Engineering", t(locale, "bachelor_context"), t(locale, "bachelor_detail"), t(locale, "education_type")),
                experience_item("2019–2022", "SMA Negeri Plus Provinsi Riau", t(locale, "school_context"), t(locale, "school_detail"), t(locale, "education_type")),
            ]
        )
    else:
        experience = "".join(
            [
                experience_item("30 Jun–9 Agu 2025", "Mechatronics Engineer Intern", "PT Arthatronic Studio Teknologi", t(locale, "internship_detail"), t(locale, "industry")),
                experience_item("2024–2025", "Koordinator EIRRG", "Electronics & Intelligence Robotics Research Group", t(locale, "eirrg_detail"), t(locale, "leadership")),
                experience_item("2023–2025", "Asisten Laboratorium Dasar Komputer", "Telkom University", t(locale, "lab_detail"), t(locale, "laboratory")),
                experience_item("2023", "Panitia PKKMB", "Telkom University", t(locale, "pkkmb_detail"), t(locale, "organization")),
            ]
        )
        education = "".join(
            [
                experience_item(t(locale, "in_progress"), "Teknik Elektro", t(locale, "master_context"), "", t(locale, "education_type")),
                experience_item("2022–2026", "S1 Teknik Elektro", t(locale, "bachelor_context"), t(locale, "bachelor_detail"), t(locale, "education_type")),
                experience_item("2019–2022", "SMA Negeri Plus Provinsi Riau", t(locale, "school_context"), t(locale, "school_detail"), t(locale, "education_type")),
            ]
        )

    return f'''<main id="main">
<section class="hero container" aria-labelledby="hero-title"><div class="hero-copy"><p class="intro-line">{text(t(locale, "role"))}</p><h1 id="hero-title">Aliyus<br>Hedri</h1><p class="hero-description">{text(t(locale, "hero_description"))}</p><div class="hero-actions"><a class="button button-primary" href="#projects">{text(t(locale, "explore_projects"))} {ARROW}</a><a class="button button-secondary" href="{hero_cv}" download>{text(t(locale, "download_cv"))} {DOWNLOAD}</a></div><p class="hero-location">{text(t(locale, "location"))}</p></div><figure class="hero-portrait"><img src="assets/images/aliyus.webp" alt="{text(t(locale, "portrait_alt"))}" width="1334" height="1179" fetchpriority="high"><figcaption class="portrait-caption"><strong>Aliyus Hedri</strong><span>{text(t(locale, "portrait_caption"))}</span></figcaption></figure></section>
<div class="container hero-footnote"><span>{text(t(locale, "focus_robotics"))}</span><span>{text(t(locale, "focus_slam"))}</span><span>{text(t(locale, "focus_embedded"))}</span><span>{text(t(locale, "focus_iot"))}</span></div>

<section class="section container" id="projects" aria-labelledby="projects-title"><div class="section-heading"><h2 id="projects-title">{text(t(locale, "selected_projects"))}</h2><p>{text(t(locale, "projects_intro"))}</p></div><div class="project-filters" role="group" aria-label="{text(t(locale, "filter_label"))}"><button class="filter-button" type="button" data-filter="all" aria-pressed="true">{text(t(locale, "all_projects"))}</button><button class="filter-button" type="button" data-filter="robotics" aria-pressed="false">{text(t(locale, "filter_robotics"))}</button><button class="filter-button" type="button" data-filter="embedded" aria-pressed="false">{text(t(locale, "filter_embedded"))}</button><button class="filter-button" type="button" data-filter="iot" aria-pressed="false">{text(t(locale, "filter_iot"))}</button></div><p id="filter-status" class="sr-only" role="status" aria-live="polite">{text(t(locale, "projects_shown"))}</p><div class="project-grid">{project_cards}</div></section>

<section class="about-section" id="about" aria-labelledby="about-title"><div class="container about-grid"><div class="about-copy"><h2 id="about-title">{text(t(locale, "about_heading"))}</h2><p>{text(t(locale, "about_p1"))}</p><p>{text(t(locale, "about_p2"))}</p><a class="text-link" href="{home_href(locale, "cv")}">{text(t(locale, "see_cv"))} {ARROW}</a></div><div class="expertise-list"><div class="expertise-item"><h3>{text(t(locale, "expertise_robotics"))}</h3><p>{text(t(locale, "expertise_robotics_text"))}</p></div><div class="expertise-item"><h3>{text(t(locale, "expertise_embedded"))}</h3><p>{text(t(locale, "expertise_embedded_text"))}</p></div><div class="expertise-item"><h3>{text(t(locale, "expertise_iot"))}</h3><p>{text(t(locale, "expertise_iot_text"))}</p></div></div></div></section>

<section class="section container" id="experience" aria-labelledby="experience-title"><div class="section-heading"><h2 id="experience-title">{text(t(locale, "experience_heading"))}</h2><p>{text(t(locale, "experience_intro"))}</p></div><div class="experience-list">{experience}</div></section>

<section class="section container" id="education" aria-labelledby="education-title"><div class="section-heading"><h2 id="education-title">{text(t(locale, "education_heading"))}</h2><p>{text(t(locale, "education_intro"))}</p></div><div class="experience-list">{education}</div></section>

<section class="container research-block" id="research" aria-labelledby="research-title"><div class="research-copy"><h2 id="research-title">{text(t(locale, "research_heading"))}</h2><p>{text(t(locale, "research_p1"))}</p><p>{text(t(locale, "research_p2"))}</p></div><aside class="research-note"><span class="research-symbol" aria-hidden="true">3D</span><h3>{text(t(locale, "target_label"))}</h3><p>{text(t(locale, "research_note"))}</p></aside></section>

<section class="section award-section" id="awards" aria-labelledby="awards-title"><div class="container"><div class="section-heading"><h2 id="awards-title">{text(t(locale, "awards_heading"))}</h2><p>{text(t(locale, "awards_intro"))}</p></div><div class="award-grid">{awards}</div><p class="additional-award">{text(t(locale, "additional_award"))}</p></div></section>

<section class="cv-section container" id="cv" aria-labelledby="cv-title"><div class="section-heading"><h2 id="cv-title">{text(t(locale, "cv_heading"))}</h2><p>{text(t(locale, "cv_intro"))}</p></div><div class="cv-actions"><a class="button button-primary" href="assets/documents/CV-Aliyus-Hedri-EN.pdf" download>{text(t(locale, "download_english_cv"))} {DOWNLOAD}</a><a class="button button-secondary" href="assets/documents/CV-Aliyus-Hedri.pdf" download>{text(t(locale, "download_indonesian_cv"))} {DOWNLOAD}</a></div></section>

<section class="contact-section" id="contact" aria-labelledby="contact-title"><div class="container contact-inner"><div class="contact-copy"><h2 id="contact-title">{text(t(locale, "contact_heading"))}<span aria-hidden="true">.</span></h2><p>{text(t(locale, "contact_intro"))}</p></div><div class="contact-channels"><div class="contact-primary"><div class="contact-card contact-username" aria-label="{text(t(locale, "contact_whatsapp"))}"><span class="contact-symbol" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.5 8.5 0 0 1-12.6 7.4L3 21l1.9-5.4A8.5 8.5 0 1 1 21 11.5Z"/><path d="M8 8c0 4 4 8 8 8l1-3-3-1-1 1-2-2 1-1-1-3Z"/></svg></span><span class="contact-card-label">{text(t(locale, "whatsapp"))}<small>@aliyushedri</small><small>{text("Find me by username in WhatsApp" if locale == "en" else "Cari username ini di WhatsApp")}</small></span></div><a class="contact-card" href="https://mail.google.com/mail/?view=cm&amp;fs=1&amp;to=aliyus.hedri%40gmail.com" target="_blank" rel="noopener" aria-label="{text(t(locale, "contact_gmail"))}"><span class="contact-symbol" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="3"/><path d="m3 7 9 6 9-6"/></svg></span><span class="contact-card-label">{text(t(locale, "gmail"))}<small>aliyus.hedri@gmail.com</small></span>{EXTERNAL}</a></div><div class="contact-socials"><a href="https://www.instagram.com/aliyushedri" target="_blank" rel="noopener" aria-label="{text(t(locale, "contact_instagram"))}">{text(t(locale, "instagram"))}{EXTERNAL}</a><a href="https://www.linkedin.com/in/aliyushedri/" target="_blank" rel="noopener" aria-label="{text(t(locale, "contact_linkedin"))}">{text(t(locale, "linkedin"))}{EXTERNAL}</a><a href="https://github.com/aliyushedri" target="_blank" rel="noopener" aria-label="{text(t(locale, "contact_github"))}">{text(t(locale, "github"))}{EXTERNAL}</a></div></div></div></section>
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
    return f'''<main id="main" class="project-detail container"><a class="back-link" href="{home_href(locale, "projects")}">← {text(t(locale, "back_projects"))}</a><div class="detail-heading"><p class="detail-category">{text(project["label"][locale])} · {text(project["year"])}</p><h1>{text(project["title"][locale])}</h1><p class="detail-lead">{text(project["lead"][locale])}</p></div><figure class="detail-cover image-{project["image"]}"><img src="assets/images/{project["image"]}.webp" alt="{text(project["alt"][locale])}" width="1500" height="1000" fetchpriority="high"></figure><div class="detail-layout"><div class="detail-body">{sections}{certificate_button(project, locale)}</div><aside class="detail-facts"><h2>{text(t(locale, "project_documentation"))}</h2><dl><dt>{text(t(locale, "detail_scope"))}</dt><dd>{text(project["role"][locale])}</dd><dt>{text(t(locale, "detail_period"))}</dt><dd>{text(project["year"])}</dd><dt>{text(t(locale, "detail_tools"))}</dt><dd>{text(project["tools"][locale])}</dd><dt>{text(t(locale, "detail_result"))}</dt><dd>{text(project["result"][locale])}</dd></dl></aside></div>{gallery_html}<div class="detail-bottom"><a class="button button-primary" href="{home_href(locale, "projects")}">{text(t(locale, "other_projects"))} {ARROW}</a><a class="text-link" href="https://mail.google.com/mail/?view=cm&amp;fs=1&amp;to=aliyus.hedri%40gmail.com" target="_blank" rel="noopener">{text(t(locale, "discuss_project"))} {EXTERNAL}</a></div></main>'''


def build_home(locale: str) -> None:
    title = t(locale, "page_title")
    description = t(locale, "page_description")
    body = header(locale) + home_main(locale) + footer(locale) + certificate_dialog(locale)
    html = document(locale, title, description, body)
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
    (ROOT / detail_file(project["slug"], locale)).write_text(document(locale, title, project["summary"][locale], body), encoding="utf-8")


def main() -> None:
    for locale in ("en", "id"):
        build_home(locale)
        for project in PROJECTS:
            build_project(project, locale)
    print("Generated bilingual home pages and 8 project pages.")


if __name__ == "__main__":
    main()
