"""
generate_assets.py
Generates ultra-modern, publication-grade DFIR SVG assets for Sanjeeth Solleti's GitHub profile.
Aesthetic inspired by Linear / Vercel / Raycast and https://github.com/akhil-dara:
- Project-centric design strictly featuring Sanjeeth's 2 authentic tools: WFT and MSTeams_Parser.
- Side-by-side SVG cards (1280x640) with real embedded screenshots and concise DFIR explanations.
- Attractive SVG keyframe animations: pulsing ambient glow, live radar ping, and animated time card telemetry.
- Zero technology skills badge tables, zero retro-terminal tropes, zero text collisions.
"""

import os
import io
import base64
import xml.etree.ElementTree as ET
from PIL import Image

ASSETS_DIR = r"C:\Users\SANJEETH\Desktop\sanjeeth-solleti\assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

# Remove map.svg if it exists (architecture diagram is being removed per task)
map_path = os.path.join(ASSETS_DIR, "map.svg")
if os.path.exists(map_path):
    try:
        os.remove(map_path)
        print("[REMOVED] map.svg deleted")
    except Exception as e:
        print(f"[WARN] Could not delete map.svg: {e}")

def validate_and_save(filename, svg_content):
    path = os.path.join(ASSETS_DIR, filename)
    clean_svg = svg_content.strip()
    try:
        ET.fromstring(clean_svg)
    except ET.ParseError as e:
        print(f"ERROR validating {filename}: {e}")
        # Print lines around the error for quick debugging
        lines = clean_svg.split("\n")
        for i, line in enumerate(lines[:50]):
            print(f"{i+1:3d}: {line}")
        raise
    with open(path, "w", encoding="utf-8") as f:
        f.write(clean_svg)
    print(f"[OK] {filename} generated & validated ({len(clean_svg)} bytes)")


# ==============================================================================
# SCREENSHOT PROCESSING (Compress and Encode to Base64 JPEG)
# ==============================================================================

# 1. WFT Dashboard Screenshot
wft_src = r"C:\Users\SANJEETH\Desktop\WFT\docs\screenshots\01_dashboard.png"
im_wft = Image.open(wft_src).convert("RGB")
wft_w = 1100
wft_h = int(wft_w * im_wft.height / im_wft.width)
im_wft_resized = im_wft.resize((wft_w, wft_h), Image.Resampling.LANCZOS)
buf_wft = io.BytesIO()
im_wft_resized.save(buf_wft, format="JPEG", quality=86)
b64_wft = base64.b64encode(buf_wft.getvalue()).decode("ascii")

# 2. MSTeams Screenshot
ms_src = r"C:\Users\SANJEETH\Desktop\teams_shot.png"
im_ms = Image.open(ms_src).convert("RGB")
ms_w = 1100
ms_h = int(ms_w * im_ms.height / im_ms.width)
im_ms_resized = im_ms.resize((ms_w, ms_h), Image.Resampling.LANCZOS)
buf_ms = io.BytesIO()
im_ms_resized.save(buf_ms, format="JPEG", quality=86)
b64_ms = base64.b64encode(buf_ms.getvalue()).decode("ascii")


# ==============================================================================
# 1. BANNER.SVG (1000 x 300) — Executive Modern DFIR Hero Banner
# ==============================================================================
banner_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 300" width="1000" height="300" role="img" aria-label="Vasava Sanjeeth Solleti — Digital Forensics &amp; Incident Response Analyst at TCS">
  <defs>
    <linearGradient id="bg-canvas" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050811"/>
      <stop offset="40%" stop-color="#090E1D"/>
      <stop offset="100%" stop-color="#05070E"/>
    </linearGradient>

    <radialGradient id="nebula-cyan" cx="12%" cy="15%" r="65%">
      <stop offset="0%" stop-color="#00D2FF" stop-opacity="0.18"/>
      <stop offset="45%" stop-color="#0284C7" stop-opacity="0.06"/>
      <stop offset="100%" stop-color="#050811" stop-opacity="0"/>
    </radialGradient>

    <radialGradient id="nebula-indigo" cx="88%" cy="85%" r="60%">
      <stop offset="0%" stop-color="#6366F1" stop-opacity="0.18"/>
      <stop offset="50%" stop-color="#7C3AED" stop-opacity="0.05"/>
      <stop offset="100%" stop-color="#05070E" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="frame-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.45"/>
      <stop offset="35%" stop-color="#1E293B" stop-opacity="0.6"/>
      <stop offset="70%" stop-color="#6366F1" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#0F172A" stop-opacity="0.8"/>
    </linearGradient>

    <linearGradient id="top-specular" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00D2FF" stop-opacity="0"/>
      <stop offset="15%" stop-color="#00D2FF" stop-opacity="0.9"/>
      <stop offset="50%" stop-color="#6366F1" stop-opacity="0.8"/>
      <stop offset="85%" stop-color="#A855F7" stop-opacity="0.7"/>
      <stop offset="100%" stop-color="#A855F7" stop-opacity="0"/>
    </linearGradient>

    <linearGradient id="name-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="60%" stop-color="#F0F9FF"/>
      <stop offset="100%" stop-color="#BAE6FD"/>
    </linearGradient>

    <linearGradient id="widget-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0B1325" stop-opacity="0.85"/>
      <stop offset="100%" stop-color="#080E1C" stop-opacity="0.92"/>
    </linearGradient>

    <linearGradient id="widget-stroke" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#1E3A8A" stop-opacity="0.25"/>
    </linearGradient>

    <pattern id="dot-grid" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="0.9" fill="#334155" fill-opacity="0.25"/>
    </pattern>
  </defs>

  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    .pulse-glow { animation: pglow 2.4s ease-in-out infinite; }
    @keyframes pglow { 0%, 100% { opacity: 1; transform: scale(1); } 50% { opacity: 0.45; transform: scale(0.9); } }
  </style>

  <rect width="1000" height="300" rx="16" fill="url(#bg-canvas)"/>
  <rect width="1000" height="300" rx="16" fill="url(#nebula-cyan)"/>
  <rect width="1000" height="300" rx="16" fill="url(#nebula-indigo)"/>
  <rect width="1000" height="300" rx="16" fill="url(#dot-grid)"/>
  <rect x="0.5" y="0.5" width="999" height="299" rx="16" fill="none" stroke="url(#frame-border)" stroke-width="1"/>

  <line x1="20" y1="1" x2="980" y2="1" stroke="url(#top-specular)" stroke-width="1.8" stroke-linecap="round"/>

  <!-- TOP TELEMETRY BAR -->
  <g transform="translate(36, 18)">
    <rect x="0" y="0" width="300" height="24" rx="12" fill="#0C1B33" stroke="#1D4ED8" stroke-width="0.75" stroke-opacity="0.8"/>
    <circle class="pulse-glow" cx="12" cy="12" r="3.5" fill="#10B981"/>
    <text x="24" y="16" class="font-sans" font-size="10" font-weight="700" fill="#38BDF8" letter-spacing="1">TATA CONSULTANCY SERVICES <tspan fill="#64748B" font-weight="400">|</tspan> <tspan fill="#94A3B8" font-weight="600">DFIR OPERATIONS</tspan></text>

    <g transform="translate(628, 0)">
      <rect x="0" y="0" width="300" height="24" rx="12" fill="#0C1B33" stroke="#1D4ED8" stroke-width="0.75" stroke-opacity="0.8"/>
      <circle cx="12" cy="12" r="3.5" fill="#38BDF8"/>
      <text x="24" y="16" class="font-sans" font-size="9.5" font-weight="700" fill="#BAE6FD" letter-spacing="0.8">DEFENSIBLE CHAIN-OF-CUSTODY <tspan fill="#64748B" font-weight="400">|</tspan> <tspan fill="#94A3B8" font-weight="600">SHA-256</tspan></text>
    </g>
  </g>

  <line x1="36" y1="52" x2="964" y2="52" stroke="#1E293B" stroke-width="0.8" stroke-opacity="0.7"/>

  <!-- LEFT HERO CONTENT -->
  <g transform="translate(36, 72)">
    <text x="0" y="14" class="font-sans" font-size="10.5" font-weight="700" fill="#38BDF8" letter-spacing="1.6">ENTERPRISE DIGITAL FORENSICS &amp; INCIDENT RESPONSE</text>

    <text x="0" y="52" class="font-sans" font-size="34" font-weight="800" fill="url(#name-grad)" letter-spacing="-0.5">Vasava Sanjeeth Solleti</text>

    <text x="0" y="78" class="font-sans" font-size="13.5" font-weight="600" fill="#E2E8F0">
      DFIR Analyst @ TCS <tspan fill="#475569" font-weight="400">|</tspan> Windows Forensics &amp; High-Throughput Engine Architect
    </text>

    <text x="0" y="101" class="font-sans" font-size="11.5" fill="#94A3B8">
      Reconstructing complex attack chronologies across raw disk images, dirty hives, &amp; cloud collaboration stores.
    </text>

    <g transform="translate(0, 124)">
      <!-- Pill 1: WFT Platform -->
      <g transform="translate(0, 0)">
        <rect width="130" height="26" rx="8" fill="#0A1C36" stroke="#0284C7" stroke-width="0.8"/>
        <circle cx="12" cy="13" r="3" fill="#38BDF8"/>
        <text x="22" y="17" class="font-sans" font-size="10" font-weight="700" fill="#BAE6FD">WFT Workstation</text>
      </g>

      <!-- Pill 2: MSTeams_Parser -->
      <g transform="translate(138, 0)">
        <rect width="132" height="26" rx="8" fill="#180F30" stroke="#7C3AED" stroke-width="0.8"/>
        <circle cx="12" cy="13" r="3" fill="#C084FC"/>
        <text x="22" y="17" class="font-sans" font-size="10" font-weight="700" fill="#E9D5FF">MSTeams_Parser</text>
      </g>

      <!-- Pill 3: CEH Certified -->
      <g transform="translate(278, 0)">
        <rect width="116" height="26" rx="8" fill="#08201A" stroke="#059669" stroke-width="0.8"/>
        <circle cx="12" cy="13" r="3" fill="#34D399"/>
        <text x="22" y="17" class="font-sans" font-size="10" font-weight="700" fill="#A7F3D0">CEH Certified</text>
      </g>

      <!-- Pill 4: DuckDB Core -->
      <g transform="translate(402, 0)">
        <rect width="116" height="26" rx="8" fill="#241705" stroke="#D97706" stroke-width="0.8"/>
        <circle cx="12" cy="13" r="3" fill="#FBBF24"/>
        <text x="22" y="17" class="font-sans" font-size="10" font-weight="700" fill="#FDE68A">DuckDB Core</text>
      </g>
    </g>
  </g>

  <!-- RIGHT GLASS TERMINAL WIDGET -->
  <g transform="translate(620, 68)">
    <rect width="344" height="174" rx="12" fill="url(#widget-bg)" stroke="url(#widget-stroke)" stroke-width="1"/>
    
    <rect width="344" height="30" rx="12" fill="#0F1B33" fill-opacity="0.9"/>
    <rect y="26" width="344" height="4" fill="#0F1B33" fill-opacity="0.9"/>

    <circle cx="16" cy="15" r="3.5" fill="#EF4444" fill-opacity="0.8"/>
    <circle cx="28" cy="15" r="3.5" fill="#F59E0B" fill-opacity="0.8"/>
    <circle cx="40" cy="15" r="3.5" fill="#10B981" fill-opacity="0.8"/>

    <text x="56" y="19" class="font-sans" font-size="10" font-weight="700" fill="#BAE6FD" letter-spacing="1.2">SPECIALIZED INVESTIGATIVE SCOPE</text>

    <g transform="translate(16, 48)" class="font-sans" font-size="11">
      <g transform="translate(0, 0)">
        <rect x="0" y="-8" width="22" height="20" rx="5" fill="#0A1F3B" stroke="#1D4ED8" stroke-width="0.6"/>
        <path d="M4 2 H18 M4 6 H18" stroke="#38BDF8" stroke-width="1.2" stroke-linecap="round"/>
        <circle cx="15" cy="0" r="1" fill="#38BDF8"/>
        <circle cx="15" cy="4" r="1" fill="#38BDF8"/>
        <text x="30" y="6" fill="#F1F5F9" font-weight="600">Native VFS Ingestion <tspan fill="#94A3B8" font-size="10" font-weight="400">(E01, RAW, VHDX, VMDK)</tspan></text>
      </g>

      <g transform="translate(0, 27)">
        <rect x="0" y="-8" width="22" height="20" rx="5" fill="#0A1F3B" stroke="#1D4ED8" stroke-width="0.6"/>
        <path d="M5 -1 C5 -3 17 -3 17 -1 C17 1 5 1 5 -1 Z M5 2 C5 4 17 4 17 2 M5 5 C5 7 17 7 17 5" fill="none" stroke="#38BDF8" stroke-width="1.2"/>
        <text x="30" y="6" fill="#F1F5F9" font-weight="600">Dirty Registry Replay <tspan fill="#94A3B8" font-size="10" font-weight="400">(Automated RLA Commit)</tspan></text>
      </g>

      <g transform="translate(0, 54)">
        <rect x="0" y="-8" width="22" height="20" rx="5" fill="#0A1F3B" stroke="#1D4ED8" stroke-width="0.6"/>
        <path d="M12 -4 L8 2 H13 L10 8 L15 1 H11 Z" fill="#38BDF8"/>
        <text x="30" y="6" fill="#F1F5F9" font-weight="600">Sub-Ms Super-Timelines <tspan fill="#94A3B8" font-size="10" font-weight="400">(DuckDB Engine)</tspan></text>
      </g>

      <g transform="translate(0, 81)">
        <rect x="0" y="-8" width="22" height="20" rx="5" fill="#1C0F33" stroke="#7C3AED" stroke-width="0.6"/>
        <path d="M5 -1 H17 V6 H11 L7 9 V6 H5 Z" fill="none" stroke="#C084FC" stroke-width="1.2"/>
        <text x="30" y="6" fill="#F1F5F9" font-weight="600">Collab Forensics <tspan fill="#C084FC" font-size="10" font-weight="400">(Teams Level/IndexedDB)</tspan></text>
      </g>
    </g>
  </g>

  <!-- BOTTOM TELEMETRY FOOTER -->
  <line x1="36" y1="262" x2="964" y2="262" stroke="#1E293B" stroke-width="0.8" stroke-opacity="0.7"/>
  <g transform="translate(36, 280)">
    <circle class="pulse-glow" cx="4" cy="-3" r="3" fill="#00D2FF"/>
    <text x="16" y="0" class="font-sans" font-size="10.5" font-weight="500" fill="#94A3B8">
      ACTIVE RESEARCH: <tspan fill="#E2E8F0">Dirty Registry Replay</tspan> &#x2022; <tspan fill="#E2E8F0">IndexedDB Messaging Stores</tspan> &#x2022; <tspan fill="#E2E8F0">Multi-Timestamp Attack Chronologies</tspan>
    </text>
    <text x="928" y="0" text-anchor="end" class="font-sans" font-size="10.5" font-weight="600" fill="#94A3B8">
      HYDERABAD, INDIA
    </text>
  </g>
</svg>"""

# ==============================================================================
# 2. ACTION BUTTONS (195 x 42 each)
# ==============================================================================
btn_linkedin = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 195 42" width="195" height="42" role="img" aria-label="LinkedIn Profile">
  <defs>
    <linearGradient id="li-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0A1428"/>
      <stop offset="100%" stop-color="#0D1C38"/>
    </linearGradient>
    <linearGradient id="li-border" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0284C7" stop-opacity="0.7"/>
      <stop offset="100%" stop-color="#1D4ED8" stop-opacity="0.5"/>
    </linearGradient>
  </defs>
  <rect x="0.5" y="0.5" width="194" height="41" rx="10" fill="url(#li-bg)" stroke="url(#li-border)" stroke-width="1"/>
  <line x1="12" y1="1" x2="183" y2="1" stroke="#38BDF8" stroke-width="1.6" stroke-linecap="round"/>

  <g transform="translate(14, 11)">
    <rect width="20" height="20" rx="4" fill="#0A66C2"/>
    <circle cx="6" cy="6" r="1.5" fill="#FFFFFF"/>
    <rect x="4.5" y="9" width="3" height="7" fill="#FFFFFF"/>
    <path d="M10 9 H12.8 V10.2 C13.3 9.4 14.2 9 15.3 9 C17.4 9 18.2 10.3 18.2 12.4 V16 H15.4 V12.8 C15.4 11.8 15 11.2 14.1 11.2 C13.3 11.2 12.8 11.7 12.8 12.6 V16 H10 Z" fill="#FFFFFF"/>
  </g>

  <text x="44" y="26" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="700" fill="#F1F5F9" letter-spacing="1">LINKEDIN</text>
  
  <path d="M174 24 L179 19 M179 19 H175 M179 19 V23" stroke="#38BDF8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
</svg>"""

btn_email = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 195 42" width="195" height="42" role="img" aria-label="Direct Email">
  <defs>
    <linearGradient id="em-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#081816"/>
      <stop offset="100%" stop-color="#0C2622"/>
    </linearGradient>
    <linearGradient id="em-border" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#059669" stop-opacity="0.7"/>
      <stop offset="100%" stop-color="#10B981" stop-opacity="0.5"/>
    </linearGradient>
  </defs>
  <rect x="0.5" y="0.5" width="194" height="41" rx="10" fill="url(#em-bg)" stroke="url(#em-border)" stroke-width="1"/>
  <line x1="12" y1="1" x2="183" y2="1" stroke="#34D399" stroke-width="1.6" stroke-linecap="round"/>

  <g transform="translate(14, 11)">
    <rect width="20" height="20" rx="4" fill="#065F46"/>
    <path d="M3.5 5.5 H16.5 V14.5 H3.5 Z" fill="none" stroke="#6EE7B7" stroke-width="1.3"/>
    <path d="M4 6.5 L10 11 L16 6.5" fill="none" stroke="#6EE7B7" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/>
  </g>

  <text x="44" y="26" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="700" fill="#F1F5F9" letter-spacing="1">EMAIL CONTACT</text>

  <path d="M174 24 L179 19 M179 19 H175 M179 19 V23" stroke="#34D399" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
</svg>"""

btn_repos = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 195 42" width="195" height="42" role="img" aria-label="All GitHub Repositories">
  <defs>
    <linearGradient id="rp-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#121026"/>
      <stop offset="100%" stop-color="#1B1738"/>
    </linearGradient>
    <linearGradient id="rp-border" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#6366F1" stop-opacity="0.7"/>
      <stop offset="100%" stop-color="#4F46E5" stop-opacity="0.5"/>
    </linearGradient>
  </defs>
  <rect x="0.5" y="0.5" width="194" height="41" rx="10" fill="url(#rp-bg)" stroke="url(#rp-border)" stroke-width="1"/>
  <line x1="12" y1="1" x2="183" y2="1" stroke="#818CF8" stroke-width="1.6" stroke-linecap="round"/>

  <g transform="translate(14, 11)">
    <rect width="20" height="20" rx="4" fill="#312E81"/>
    <path d="M4 6 H8.5 L10.5 8 H16 V14.5 H4 Z" fill="none" stroke="#A5B4FC" stroke-width="1.3" stroke-linejoin="round"/>
  </g>

  <text x="44" y="26" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="700" fill="#F1F5F9" letter-spacing="1">REPOSITORIES</text>

  <path d="M174 24 L179 19 M179 19 H175 M179 19 V23" stroke="#818CF8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
</svg>"""

btn_ceh = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 195 42" width="195" height="42" role="img" aria-label="CEH Certified Ethical Hacker">
  <defs>
    <linearGradient id="ceh-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#180E29"/>
      <stop offset="100%" stop-color="#24153E"/>
    </linearGradient>
    <linearGradient id="ceh-border" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#8B5CF6" stop-opacity="0.7"/>
      <stop offset="100%" stop-color="#7C3AED" stop-opacity="0.5"/>
    </linearGradient>
  </defs>
  <rect x="0.5" y="0.5" width="194" height="41" rx="10" fill="url(#ceh-bg)" stroke="url(#ceh-border)" stroke-width="1"/>
  <line x1="12" y1="1" x2="183" y2="1" stroke="#C084FC" stroke-width="1.6" stroke-linecap="round"/>

  <g transform="translate(14, 11)">
    <rect width="20" height="20" rx="4" fill="#581C87"/>
    <path d="M10 4 L15.5 6.5 V10.5 C15.5 13.5 10 16 10 16 C10 16 4.5 13.5 4.5 10.5 V6.5 Z" fill="none" stroke="#D8B4FE" stroke-width="1.3"/>
    <path d="M8 10 L9.5 11.5 L12.5 8" fill="none" stroke="#D8B4FE" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
  </g>

  <text x="44" y="26" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="700" fill="#F1F5F9" letter-spacing="1">CEH CERTIFIED</text>

  <path d="M174 21 L177 24 L182 18" stroke="#C084FC" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
</svg>"""


# ==============================================================================
# 3. INTRO.SVG (1280 x 260) — DFIR Lab Philosophy & Defensible Tenets Card
# ==============================================================================
intro_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 260" width="1280" height="260" role="img" aria-label="The DFIR Lab — Open source tools engineered for the gaps where standard forensic suites stop short.">
  <defs>
    <linearGradient id="bg-intro" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#060A14"/>
      <stop offset="50%" stop-color="#090E1F"/>
      <stop offset="100%" stop-color="#05070E"/>
    </linearGradient>

    <radialGradient id="gl-intro" cx="15%" cy="20%" r="65%">
      <stop offset="0%" stop-color="#00D2FF" stop-opacity="0.22"/>
      <stop offset="60%" stop-color="#0284C7" stop-opacity="0.04"/>
      <stop offset="100%" stop-color="#060A14" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="intro-border" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.45"/>
      <stop offset="50%" stop-color="#6366F1" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#10B981" stop-opacity="0.4"/>
    </linearGradient>

    <linearGradient id="hi-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38BDF8"/>
      <stop offset="50%" stop-color="#818CF8"/>
      <stop offset="100%" stop-color="#34D399"/>
    </linearGradient>

    <pattern id="dt-intro" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1.1" fill="#1E293B" fill-opacity="0.5"/>
    </pattern>

    <filter id="sh-chip" x="-10%" y="-10%" width="120%" height="130%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    .font-mono { font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; }
    .pulse-glow { animation: pglow 6s ease-in-out infinite; }
    @keyframes pglow { 0%, 100% { opacity: 0.7; } 50% { opacity: 1; } }
  </style>

  <rect width="1280" height="260" rx="16" fill="url(#bg-intro)"/>
  <rect class="pulse-glow" width="1280" height="260" rx="16" fill="url(#gl-intro)"/>
  <rect width="1280" height="260" rx="16" fill="url(#dt-intro)"/>
  <rect x="0.5" y="0.5" width="1279" height="259" rx="16" fill="none" stroke="url(#intro-border)" stroke-width="1"/>

  <!-- Specular top edge -->
  <line x1="20" y1="1" x2="1260" y2="1" stroke="#38BDF8" stroke-width="1.8" stroke-linecap="round"/>

  <!-- LEFT HERO NARRATIVE -->
  <g transform="translate(56, 42)">
    <text x="0" y="16" class="font-mono" font-size="12" font-weight="700" fill="#38BDF8" letter-spacing="2">THE DFIR LAB</text>
    <rect x="0" y="24" width="44" height="3" rx="1.5" fill="#38BDF8"/>

    <text x="0" y="78" class="font-sans" font-size="28" font-weight="800" fill="#F8FAFC" letter-spacing="-0.3">
      Forensic suites are built for standard casework.
    </text>

    <text x="0" y="118" class="font-sans" font-size="28" font-weight="800" fill="url(#hi-grad)" letter-spacing="-0.3">
      These engines are engineered for the critical gaps.
    </text>

    <text x="0" y="156" class="font-sans" font-size="14.5" fill="#94A3B8">
      Deterministic open-source tooling for dirty registry replay, LevelDB messaging, &amp; sub-millisecond super-timelines.
    </text>
  </g>

  <!-- RIGHT TENET PILLARS (3 Glassmorphic Chips) -->
  <g transform="translate(820, 24)">
    <!-- Pillar 1: Read-Only VFS -->
    <g transform="translate(0, 0)">
      <rect width="404" height="60" rx="12" fill="#0A1830" stroke="#0284C7" stroke-width="0.75" filter="url(#sh-chip)"/>
      <rect x="12" y="14" width="32" height="32" rx="8" fill="#0C2448" stroke="#38BDF8" stroke-width="0.8"/>
      <!-- Lock / VFS icon -->
      <path d="M24 24 H32 V36 H24 Z M26 24 V21 C26 19.5 27 18 28 18 C29 18 30 19.5 30 21 V24" fill="none" stroke="#38BDF8" stroke-width="1.3" stroke-linecap="round"/>
      <text x="56" y="29" class="font-mono" font-size="11.5" font-weight="700" fill="#38BDF8" letter-spacing="1">READ-ONLY VFS INTAKE</text>
      <text x="56" y="46" class="font-sans" font-size="12" fill="#94A3B8">Mounted immutable via dissect; disk containers never modified.</text>
    </g>

    <!-- Pillar 2: Dirty Log Replay -->
    <g transform="translate(0, 72)">
      <rect width="404" height="60" rx="12" fill="#141032" stroke="#6366F1" stroke-width="0.75" filter="url(#sh-chip)"/>
      <rect x="12" y="14" width="32" height="32" rx="8" fill="#1E194D" stroke="#818CF8" stroke-width="0.8"/>
      <!-- Circular commit arrows -->
      <path d="M24 30 A5 5 0 1 1 32 30" fill="none" stroke="#818CF8" stroke-width="1.4"/>
      <path d="M32 27 L32 30 L29 30" fill="none" stroke="#818CF8" stroke-width="1.4" stroke-linecap="round"/>
      <text x="56" y="29" class="font-mono" font-size="11.5" font-weight="700" fill="#818CF8" letter-spacing="1">DIRTY LOG REPLAY</text>
      <text x="56" y="46" class="font-sans" font-size="12" fill="#94A3B8">Mandatory automated RLA transaction commit before hive analysis.</text>
    </g>

    <!-- Pillar 3: Columnar Speed -->
    <g transform="translate(0, 144)">
      <rect width="404" height="60" rx="12" fill="#071E19" stroke="#059669" stroke-width="0.75" filter="url(#sh-chip)"/>
      <rect x="12" y="14" width="32" height="32" rx="8" fill="#0A3228" stroke="#34D399" stroke-width="0.8"/>
      <!-- Lightning bolt icon -->
      <path d="M29 20 L24 28 H30 L27 36 L33 26 H27 Z" fill="#34D399"/>
      <text x="56" y="29" class="font-mono" font-size="11.5" font-weight="700" fill="#34D399" letter-spacing="1">COLUMNAR SPEED</text>
      <text x="56" y="46" class="font-sans" font-size="12" fill="#94A3B8">Sub-millisecond analytical queries across 500K+ records via DuckDB.</text>
    </g>
  </g>
</svg>"""


# ==============================================================================
# 4. CARD-WFT.SVG (1280 x 640) — WFT Side-by-Side Card with Real Screenshot
# ==============================================================================
card_wft_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1280 640" width="1280" height="640" role="img" aria-label="WFT — Windows Forensic Examination Platform with DuckDB Columnar Core and dissect.target VFS">
  <defs>
    <!-- Background Canvas -->
    <linearGradient id="bg-wft" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050811"/>
      <stop offset="50%" stop-color="#080E1C"/>
      <stop offset="100%" stop-color="#05070E"/>
    </linearGradient>

    <!-- Glowing Nebula -->
    <radialGradient id="gl-wft" cx="15%" cy="20%" r="65%">
      <stop offset="0%" stop-color="#00D2FF" stop-opacity="0.22"/>
      <stop offset="55%" stop-color="#1D4ED8" stop-opacity="0.05"/>
      <stop offset="100%" stop-color="#050811" stop-opacity="0"/>
    </radialGradient>

    <!-- Border Stroke -->
    <linearGradient id="border-wft" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.5"/>
      <stop offset="45%" stop-color="#1E3A8A" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#1E293B" stop-opacity="0.4"/>
    </linearGradient>

    <!-- Title Gradient -->
    <linearGradient id="wft-title" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="60%" stop-color="#F0F9FF"/>
      <stop offset="100%" stop-color="#BAE6FD"/>
    </linearGradient>

    <!-- Dot Grid Pattern -->
    <pattern id="dt-wft" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1.1" fill="#1E293B" fill-opacity="0.4"/>
    </pattern>

    <!-- Drop Shadow for Window Frame -->
    <filter id="sh-wbox" x="-10%" y="-10%" width="125%" height="125%">
      <feDropShadow dx="0" dy="16" stdDeviation="22" flood-color="#000000" flood-opacity="0.75"/>
    </filter>

    <!-- Screenshot Viewport Clip -->
    <clipPath id="clip-wft-vp">
      <rect x="548" y="94" width="684" height="434" rx="2"/>
    </clipPath>
  </defs>

  <style>
    .font-sans {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }}
    .font-mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; }}
    
    /* Animations */
    .pulse-ambient {{ animation: pamb 6s ease-in-out infinite; }}
    .live-dot {{ animation: ldot 2s cubic-bezier(0.4, 0, 0.6, 1) infinite; }}
    .radar-ring {{ animation: rring 2.4s cubic-bezier(0, 0.2, 0.8, 1) infinite; transform-origin: 24px 26px; }}
    .timeline-cursor {{ animation: tcur 4s ease-in-out infinite alternate; }}
    
    @keyframes pamb {{ 0%, 100% {{ opacity: 0.65; }} 50% {{ opacity: 1; }} }}
    @keyframes ldot {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0.35; }} }}
    @keyframes rring {{ 0% {{ r: 3; opacity: 1; }} 100% {{ r: 15; opacity: 0; }} }}
    @keyframes tcur {{ 0% {{ transform: translateX(0); }} 100% {{ transform: translateX(380px); }} }}
    
    @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} }}
  </style>

  <!-- Canvas Surface -->
  <rect width="1280" height="640" rx="16" fill="url(#bg-wft)"/>
  <rect class="pulse-ambient" width="1280" height="640" rx="16" fill="url(#gl-wft)"/>
  <rect width="1280" height="640" rx="16" fill="url(#dt-wft)"/>
  <rect x="0.5" y="0.5" width="1279" height="639" rx="16" fill="none" stroke="url(#border-wft)" stroke-width="1"/>

  <!-- Top Specular Highlight Line -->
  <line x1="20" y1="1" x2="1260" y2="1" stroke="#38BDF8" stroke-width="2" stroke-linecap="round"/>

  <!-- ==================== LEFT SIDE: DETAILED SPECIFICATIONS ==================== -->
  <g transform="translate(48, 42)">
    <!-- Category & Index Tag -->
    <text x="0" y="16" class="font-mono" font-size="11.5" font-weight="700" fill="#38BDF8" letter-spacing="2">TOOL 01 / 02 &#x2022; ENTERPRISE WINDOWS FORENSICS</text>
    <rect x="0" y="24" width="46" height="3" rx="1.5" fill="#38BDF8"/>

    <!-- Tech Chips Row -->
    <g transform="translate(0, 36)">
      <g transform="translate(0, 0)">
        <rect width="124" height="24" rx="7" fill="#0A2244" stroke="#0284C7" stroke-width="0.8"/>
        <text x="62" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="700" fill="#93C5FD">DuckDB Core</text>
      </g>
      <g transform="translate(132, 0)">
        <rect width="138" height="24" rx="7" fill="#0A2244" stroke="#0284C7" stroke-width="0.8"/>
        <text x="69" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="700" fill="#93C5FD">dissect.target VFS</text>
      </g>
      <g transform="translate(278, 0)">
        <rect width="116" height="24" rx="7" fill="#0A2244" stroke="#0284C7" stroke-width="0.8"/>
        <text x="58" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="700" fill="#93C5FD">RLA Log Commit</text>
      </g>
    </g>

    <!-- Main Title & Headline -->
    <text x="0" y="98" class="font-sans" font-size="44" font-weight="800" fill="url(#wft-title)" letter-spacing="-0.5">WFT</text>
    <text x="0" y="124" class="font-sans" font-size="16" font-weight="600" fill="#CBD5E1">Windows Forensic Examination Platform</text>
    <text x="0" y="144" class="font-sans" font-size="12" fill="#94A3B8">Enterprise "Process + Examine" workstation ingesting raw containers to sub-ms timelines.</text>

    <!-- Animated Time Card / Live Telemetry HUD Widget -->
    <g transform="translate(0, 162)">
      <rect width="470" height="66" rx="10" fill="#08172E" stroke="#1D4ED8" stroke-width="0.8"/>
      <!-- Radar Status Indicator -->
      <circle class="live-dot" cx="24" cy="26" r="4.5" fill="#10B981">
        <animate attributeName="opacity" values="1;0.35;1" dur="2s" repeatCount="indefinite"/>
      </circle>
      <circle class="radar-ring" cx="24" cy="26" r="4.5" fill="none" stroke="#10B981" stroke-width="1.2">
        <animate attributeName="r" values="3;15" dur="2.4s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="1;0" dur="2.4s" repeatCount="indefinite"/>
      </circle>
      
      <text x="44" y="24" class="font-mono" font-size="10.5" font-weight="700" fill="#38BDF8" letter-spacing="1">SUPER-TIMELINE ENGINE: 500,000+ RECORDS</text>
      <text x="44" y="42" class="font-sans" font-size="11" fill="#E2E8F0">Zero-Copy In-Process Columnar &#x2022; Sub-0.8ms Query Latency</text>
      <text x="44" y="56" class="font-mono" font-size="9.5" fill="#94A3B8">CORRELATION DELTA: UTC &#177;00:00 &#x2022; Sub-Second Artifact Sync</text>
    </g>

    <!-- 4 Core Forensic Feature Points -->
    <g transform="translate(0, 246)">
      <!-- Point 1: DuckDB Columnar Core -->
      <g transform="translate(0, 0)">
        <rect width="24" height="24" rx="6" fill="#0A2244" stroke="#0284C7" stroke-width="0.8"/>
        <!-- Lightning bolt -->
        <path d="M14 4 L9 13 H15 L12 21 L18 11 H13 Z" fill="#38BDF8"/>
        <text x="36" y="13" class="font-sans" font-size="13.5" font-weight="700" fill="#FFFFFF">Zero-Copy DuckDB Columnar Core</text>
        <text x="36" y="28" class="font-sans" font-size="11.5" fill="#94A3B8">Sub-ms super-timeline across 500,000+ events with unpivoted filtering.</text>
      </g>

      <!-- Point 2: Dirty Registry Replay -->
      <g transform="translate(0, 48)">
        <rect width="24" height="24" rx="6" fill="#0A2244" stroke="#0284C7" stroke-width="0.8"/>
        <!-- Replay arrows -->
        <path d="M7 12 A5 5 0 1 1 17 12" fill="none" stroke="#38BDF8" stroke-width="1.4"/>
        <path d="M17 9 L17 12 L14 12" fill="none" stroke="#38BDF8" stroke-width="1.4" stroke-linecap="round"/>
        <text x="36" y="13" class="font-sans" font-size="13.5" font-weight="700" fill="#FFFFFF">Mandatory Dirty Registry Replay</text>
        <text x="36" y="28" class="font-sans" font-size="11.5" fill="#94A3B8">Automated RLA commit for volatile .LOG1/.LOG2 logs before hive analysis.</text>
      </g>

      <!-- Point 3: Direct VFS Intake -->
      <g transform="translate(0, 96)">
        <rect width="24" height="24" rx="6" fill="#0A2244" stroke="#0284C7" stroke-width="0.8"/>
        <!-- Disk drive icon -->
        <path d="M5 8 H19 V16 H5 Z" fill="none" stroke="#38BDF8" stroke-width="1.2"/>
        <line x1="5" y1="12" x2="19" y2="12" stroke="#38BDF8" stroke-width="0.8"/>
        <circle cx="16" cy="14" r="1" fill="#38BDF8"/>
        <text x="36" y="13" class="font-sans" font-size="13.5" font-weight="700" fill="#FFFFFF">Native VFS Multi-Format Intake</text>
        <text x="36" y="28" class="font-sans" font-size="11.5" fill="#94A3B8">Direct mounting of .E01, .RAW, .VHDX, and .VMDK containers via dissect.</text>
      </g>

      <!-- Point 4: Threat Hunting & OCR -->
      <g transform="translate(0, 144)">
        <rect width="24" height="24" rx="6" fill="#0A2244" stroke="#0284C7" stroke-width="0.8"/>
        <!-- Crosshair icon -->
        <circle cx="12" cy="12" r="6" fill="none" stroke="#38BDF8" stroke-width="1.2"/>
        <line x1="12" y1="3" x2="12" y2="21" stroke="#38BDF8" stroke-width="0.8"/>
        <line x1="3" y1="12" x2="21" y2="12" stroke="#38BDF8" stroke-width="0.8"/>
        <text x="36" y="13" class="font-sans" font-size="13.5" font-weight="700" fill="#FFFFFF">Threat Hunting &amp; RapidOCR Triage</text>
        <text x="36" y="28" class="font-sans" font-size="11.5" fill="#94A3B8">Compiled Rust YARA-X rules + OCR text extraction from carved images.</text>
      </g>
    </g>

    <!-- Pipeline Schematic Flow -->
    <g transform="translate(0, 470)">
      <text x="0" y="0" class="font-mono" font-size="10" fill="#64748B">
        dissect VFS <tspan fill="#38BDF8">&#x2192;</tspan> RLA Dirty Replay <tspan fill="#38BDF8">&#x2192;</tspan> DuckDB Columnar <tspan fill="#38BDF8">&#x2192;</tspan> Cytoscape Graph
      </text>
    </g>

    <!-- Footer Repo CTA Link -->
    <g transform="translate(0, 502)">
      <text x="0" y="0" class="font-mono" font-size="11" fill="#64748B">github.com/sanjeeth-solleti/WFT</text>
      <text x="470" y="0" text-anchor="end" class="font-sans" font-size="12" font-weight="700" fill="#38BDF8">Explore WFT Repository &#x2192;</text>
    </g>
  </g>

  <!-- ==================== RIGHT SIDE: REAL APPLICATION WINDOW ==================== -->
  <g transform="translate(546, 42)">
    <!-- Window Outer Shell with Drop Shadow -->
    <rect width="688" height="552" rx="12" fill="#0A1122" stroke="#1E3A8A" stroke-width="1.2" filter="url(#sh-wbox)"/>

    <!-- Mac-Style Titlebar -->
    <rect width="688" height="38" rx="12" fill="#0D182E"/>
    <rect y="30" width="688" height="8" fill="#0D182E"/>

    <!-- Window Dots -->
    <circle cx="20" cy="19" r="4.5" fill="#EF4444" fill-opacity="0.9"/>
    <circle cx="35" cy="19" r="4.5" fill="#F59E0B" fill-opacity="0.9"/>
    <circle cx="50" cy="19" r="4.5" fill="#10B981" fill-opacity="0.9"/>

    <!-- Centered Window Title -->
    <text x="344" y="23" text-anchor="middle" class="font-sans" font-size="11" font-weight="600" fill="#94A3B8">
      WFT — Windows Forensic Examination Platform
    </text>

    <!-- Right Live Session Indicator -->
    <g transform="translate(534, 9)">
      <rect width="138" height="20" rx="10" fill="#064E3B" stroke="#059669" stroke-width="0.8"/>
      <circle class="live-dot" cx="12" cy="10" r="3" fill="#34D399"/>
      <text x="22" y="13.5" class="font-mono" font-size="9" font-weight="700" fill="#A7F3D0">LIVE DUCKDB CORE</text>
    </g>

    <!-- Viewport with REAL Embedded Screenshot -->
    <g transform="translate(2, 38)">
      <image href="data:image/jpeg;base64,{b64_wft}" xlink:href="data:image/jpeg;base64,{b64_wft}" x="0" y="0" width="684" height="476" preserveAspectRatio="xMidYMid slice" clip-path="url(#clip-wft-vp)"/>
      <rect x="0" y="0" width="684" height="476" fill="none" stroke="#1E293B" stroke-width="0.5"/>
    </g>

    <!-- Floating Bottom Telemetry Glass HUD (Over Screenshot) -->
    <g transform="translate(14, 456)">
      <rect width="660" height="42" rx="8" fill="#071328" fill-opacity="0.92" stroke="#0284C7" stroke-width="0.8"/>
      <circle class="live-dot" cx="16" cy="21" r="3.5" fill="#34D399"/>
      <text x="28" y="24" class="font-mono" font-size="10" font-weight="700" fill="#A7F3D0">CONTAINER: Windows10_Forensic.E01 <tspan fill="#64748B">[VFS MOUNTED &#x2022; READ ONLY]</tspan></text>
      <text x="646" y="24" text-anchor="end" class="font-mono" font-size="9.5" font-weight="600" fill="#BAE6FD">524,198 ARTIFACTS PARSED (0.72s) &#x2022; SHA-256 VERIFIED</text>
    </g>

    <!-- Window Bottom Status Bar -->
    <g transform="translate(0, 518)">
      <line x1="0" y1="0" x2="688" y2="0" stroke="#1E293B" stroke-width="0.8"/>
      <rect y="0" width="688" height="34" rx="0" fill="#08101E"/>
      <rect y="22" width="688" height="12" rx="12" fill="#08101E"/>

      <g transform="translate(16, 21)" class="font-mono" font-size="9.5" fill="#64748B">
        <text x="0" y="0"><tspan fill="#10B981">&#x25CF;</tspan> VFS: ACTIVE</text>
        <text x="120" y="0"><tspan fill="#38BDF8">&#x25CF;</tspan> AG GRID: VIRTUALIZED</text>
        <text x="280" y="0"><tspan fill="#818CF8">&#x25CF;</tspan> CYTOSCAPE: GRAPH READY</text>
        <text x="480" y="0"><tspan fill="#F59E0B">&#x25CF;</tspan> ENGINE: DUCKDB v1.0</text>
      </g>
    </g>
  </g>
</svg>"""


# ==============================================================================
# 5. CARD-MSTEAMS.SVG (1280 x 640) — MSTeams_Parser Side-by-Side Card
# ==============================================================================
card_msteams_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1280 640" width="1280" height="640" role="img" aria-label="MSTeams_Parser — Microsoft Teams DFIR Forensic Suite with LevelDB and IndexedDB Parsing">
  <defs>
    <!-- Background Canvas -->
    <linearGradient id="bg-ms" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090514"/>
      <stop offset="50%" stop-color="#130B24"/>
      <stop offset="100%" stop-color="#07040E"/>
    </linearGradient>

    <!-- Glowing Nebula -->
    <radialGradient id="gl-ms" cx="15%" cy="20%" r="65%">
      <stop offset="0%" stop-color="#A855F7" stop-opacity="0.22"/>
      <stop offset="55%" stop-color="#6B21A8" stop-opacity="0.05"/>
      <stop offset="100%" stop-color="#090514" stop-opacity="0"/>
    </radialGradient>

    <!-- Border Stroke -->
    <linearGradient id="border-ms" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#C084FC" stop-opacity="0.5"/>
      <stop offset="45%" stop-color="#7C3AED" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#1E293B" stop-opacity="0.4"/>
    </linearGradient>

    <!-- Title Gradient -->
    <linearGradient id="ms-title" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="60%" stop-color="#FAF5FF"/>
      <stop offset="100%" stop-color="#E9D5FF"/>
    </linearGradient>

    <!-- Dot Grid Pattern -->
    <pattern id="dt-ms" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1.1" fill="#2E1B4E" fill-opacity="0.5"/>
    </pattern>

    <!-- Drop Shadow for Window Frame -->
    <filter id="sh-msbox" x="-10%" y="-10%" width="125%" height="125%">
      <feDropShadow dx="0" dy="16" stdDeviation="22" flood-color="#000000" flood-opacity="0.75"/>
    </filter>

    <!-- Screenshot Viewport Clip -->
    <clipPath id="clip-ms-vp">
      <rect x="548" y="94" width="684" height="434" rx="2"/>
    </clipPath>
  </defs>

  <style>
    .font-sans {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }}
    .font-mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; }}
    
    /* Animations */
    .pulse-ambient {{ animation: pamb 6s ease-in-out infinite; }}
    .live-dot-purple {{ animation: ldotp 2s cubic-bezier(0.4, 0, 0.6, 1) infinite; }}
    .radar-ring-purple {{ animation: rringp 2.4s cubic-bezier(0, 0.2, 0.8, 1) infinite; transform-origin: 24px 26px; }}
    
    @keyframes pamb {{ 0%, 100% {{ opacity: 0.65; }} 50% {{ opacity: 1; }} }}
    @keyframes ldotp {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0.35; }} }}
    @keyframes rringp {{ 0% {{ r: 3; opacity: 1; }} 100% {{ r: 15; opacity: 0; }} }}
    
    @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} }}
  </style>

  <!-- Canvas Surface -->
  <rect width="1280" height="640" rx="16" fill="url(#bg-ms)"/>
  <rect class="pulse-ambient" width="1280" height="640" rx="16" fill="url(#gl-ms)"/>
  <rect width="1280" height="640" rx="16" fill="url(#dt-ms)"/>
  <rect x="0.5" y="0.5" width="1279" height="639" rx="16" fill="none" stroke="url(#border-ms)" stroke-width="1"/>

  <!-- Top Specular Highlight Line -->
  <line x1="20" y1="1" x2="1260" y2="1" stroke="#A855F7" stroke-width="2" stroke-linecap="round"/>

  <!-- ==================== LEFT SIDE: DETAILED SPECIFICATIONS ==================== -->
  <g transform="translate(48, 42)">
    <!-- Category & Index Tag -->
    <text x="0" y="16" class="font-mono" font-size="11.5" font-weight="700" fill="#C084FC" letter-spacing="2">TOOL 02 / 02 &#x2022; COLLABORATION DFIR SUITE</text>
    <rect x="0" y="24" width="46" height="3" rx="1.5" fill="#C084FC"/>

    <!-- Tech Chips Row -->
    <g transform="translate(0, 36)">
      <g transform="translate(0, 0)">
        <rect width="138" height="24" rx="7" fill="#24103C" stroke="#7C3AED" stroke-width="0.8"/>
        <text x="69" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="700" fill="#E9D5FF">LevelDB / IndexedDB</text>
      </g>
      <g transform="translate(146, 0)">
        <rect width="98" height="24" rx="7" fill="#24103C" stroke="#7C3AED" stroke-width="0.8"/>
        <text x="49" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="700" fill="#E9D5FF">dfindexeddb</text>
      </g>
      <g transform="translate(252, 0)">
        <rect width="84" height="24" rx="7" fill="#24103C" stroke="#7C3AED" stroke-width="0.8"/>
        <text x="42" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="700" fill="#E9D5FF">cramjam</text>
      </g>
      <g transform="translate(344, 0)">
        <rect width="112" height="24" rx="7" fill="#24103C" stroke="#7C3AED" stroke-width="0.8"/>
        <text x="56" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="700" fill="#E9D5FF">Air-Gapped</text>
      </g>
    </g>

    <!-- Main Title & Headline -->
    <text x="0" y="98" class="font-sans" font-size="44" font-weight="800" fill="url(#ms-title)" letter-spacing="-0.5">MSTeams_Parser</text>
    <text x="0" y="124" class="font-sans" font-size="16" font-weight="600" fill="#E9D5FF">Microsoft Teams Forensic Analysis Suite</text>
    <text x="0" y="144" class="font-sans" font-size="12" fill="#94A3B8">Reconstruct enterprise Teams chats, calls, meetings, &amp; media from LevelDB stores.</text>

    <!-- Animated Time Card / Live Telemetry HUD Widget -->
    <g transform="translate(0, 162)">
      <rect width="470" height="66" rx="10" fill="#1A0D30" stroke="#7C3AED" stroke-width="0.8"/>
      <!-- Radar Status Indicator -->
      <circle class="live-dot-purple" cx="24" cy="26" r="4.5" fill="#C084FC">
        <animate attributeName="opacity" values="1;0.35;1" dur="2s" repeatCount="indefinite"/>
      </circle>
      <circle class="radar-ring-purple" cx="24" cy="26" r="4.5" fill="none" stroke="#C084FC" stroke-width="1.2">
        <animate attributeName="r" values="3;15" dur="2.4s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="1;0" dur="2.4s" repeatCount="indefinite"/>
      </circle>
      
      <text x="44" y="24" class="font-mono" font-size="10.5" font-weight="700" fill="#C084FC" letter-spacing="1">AIR-GAPPED FORENSIC DAEMON: 127.0.0.1</text>
      <text x="44" y="42" class="font-sans" font-size="11" fill="#F3E8FF">Strict Localhost Binding &#x2022; Zero External Data Transmission</text>
      <text x="44" y="56" class="font-mono" font-size="9.5" fill="#D8B4FE">TIMESTAMPS: DUAL UTC &amp; IST (UTC+05:30) &#x2022; Millisecond Resolution</text>
    </g>

    <!-- 4 Core Forensic Feature Points -->
    <g transform="translate(0, 246)">
      <!-- Point 1: Multi-Source Ingestion -->
      <g transform="translate(0, 0)">
        <rect width="24" height="24" rx="6" fill="#281144" stroke="#7C3AED" stroke-width="0.8"/>
        <!-- Box icon -->
        <path d="M6 8 L12 5 L18 8 L12 11 Z" fill="none" stroke="#C084FC" stroke-width="1.1"/>
        <path d="M6 8 V16 L12 19 V11 M18 8 V16 L12 19" fill="none" stroke="#C084FC" stroke-width="1.1"/>
        <text x="36" y="13" class="font-sans" font-size="13.5" font-weight="700" fill="#FFFFFF">Multi-Source LevelDB &amp; IndexedDB Intake</text>
        <text x="36" y="28" class="font-sans" font-size="11.5" fill="#94A3B8">Ingests New Teams (%LOCALAPPDATA% EBWebView) &amp; Classic stores.</text>
      </g>

      <!-- Point 2: Adaptive Card Normalization -->
      <g transform="translate(0, 48)">
        <rect width="24" height="24" rx="6" fill="#281144" stroke="#7C3AED" stroke-width="0.8"/>
        <!-- Code / card icon -->
        <path d="M6 7 H14 L18 11 V17 H6 Z" fill="none" stroke="#C084FC" stroke-width="1.1"/>
        <line x1="9" y1="11" x2="15" y2="11" stroke="#C084FC" stroke-width="0.8"/>
        <line x1="9" y1="14" x2="13" y2="14" stroke="#C084FC" stroke-width="0.8"/>
        <text x="36" y="13" class="font-sans" font-size="13.5" font-weight="700" fill="#FFFFFF">Adaptive Card &amp; Event Normalization</text>
        <text x="36" y="28" class="font-sans" font-size="11.5" fill="#94A3B8">Unpacks Base64 JSON cards, call durations, meeting logs, &amp; role changes.</text>
      </g>

      <!-- Point 3: Identity Resolution -->
      <g transform="translate(0, 96)">
        <rect width="24" height="24" rx="6" fill="#281144" stroke="#7C3AED" stroke-width="0.8"/>
        <!-- User icon -->
        <circle cx="12" cy="9" r="3.2" fill="none" stroke="#C084FC" stroke-width="1.1"/>
        <path d="M6 18 C6 14.5 9 14 12 14 C15 14 18 14.5 18 18" fill="none" stroke="#C084FC" stroke-width="1.1"/>
        <text x="36" y="13" class="font-sans" font-size="13.5" font-weight="700" fill="#FFFFFF">Identity &amp; Internal GUID Resolution</text>
        <text x="36" y="28" class="font-sans" font-size="11.5" fill="#94A3B8">Resolves internal 8:orgid GUIDs to corporate employees, emails, &amp; roles.</text>
      </g>

      <!-- Point 4: Media Carver -->
      <g transform="translate(0, 144)">
        <rect width="24" height="24" rx="6" fill="#281144" stroke="#7C3AED" stroke-width="0.8"/>
        <!-- Media / photo icon -->
        <rect x="5" y="6" width="14" height="12" rx="2" fill="none" stroke="#C084FC" stroke-width="1.1"/>
        <circle cx="9" cy="10" r="1.2" fill="#C084FC"/>
        <path d="M6 16 L10 12 L13 15 L15 13 L18 16" fill="none" stroke="#C084FC" stroke-width="1"/>
        <text x="36" y="13" class="font-sans" font-size="13.5" font-weight="700" fill="#FFFFFF">Magic-Byte Media &amp; Attachment Carver</text>
        <text x="36" y="28" class="font-sans" font-size="11.5" fill="#94A3B8">Carves cached images while filtering UI telemetry noise (&lt; 3.5 KB).</text>
      </g>
    </g>

    <!-- Pipeline Schematic Flow -->
    <g transform="translate(0, 470)">
      <text x="0" y="0" class="font-mono" font-size="10" fill="#64748B">
        IndexedDB/LevelDB <tspan fill="#C084FC">&#x2192;</tspan> Base64 Decode <tspan fill="#C084FC">&#x2192;</tspan> GUID Resolution <tspan fill="#C084FC">&#x2192;</tspan> HTML Dossier
      </text>
    </g>

    <!-- Footer Repo CTA Link -->
    <g transform="translate(0, 502)">
      <text x="0" y="0" class="font-mono" font-size="11" fill="#64748B">github.com/sanjeeth-solleti/MSTeams_Parser</text>
      <text x="470" y="0" text-anchor="end" class="font-sans" font-size="12" font-weight="700" fill="#C084FC">Explore MSTeams_Parser Repository &#x2192;</text>
    </g>
  </g>

  <!-- ==================== RIGHT SIDE: REAL APPLICATION WINDOW ==================== -->
  <g transform="translate(546, 42)">
    <!-- Window Outer Shell with Drop Shadow -->
    <rect width="688" height="552" rx="12" fill="#110820" stroke="#7C3AED" stroke-width="1.2" filter="url(#sh-msbox)"/>

    <!-- Mac-Style Titlebar -->
    <rect width="688" height="38" rx="12" fill="#180C30"/>
    <rect y="30" width="688" height="8" fill="#180C30"/>

    <!-- Window Dots -->
    <circle cx="20" cy="19" r="4.5" fill="#EF4444" fill-opacity="0.9"/>
    <circle cx="35" cy="19" r="4.5" fill="#F59E0B" fill-opacity="0.9"/>
    <circle cx="50" cy="19" r="4.5" fill="#10B981" fill-opacity="0.9"/>

    <!-- Centered Window Title -->
    <text x="344" y="23" text-anchor="middle" class="font-sans" font-size="11" font-weight="600" fill="#C084FC">
      MSTeams_Parser — Desktop Forensic Viewer &amp; Dossier
    </text>

    <!-- Right Live Session Indicator -->
    <g transform="translate(534, 9)">
      <rect width="138" height="20" rx="10" fill="#2E1065" stroke="#7C3AED" stroke-width="0.8"/>
      <circle class="live-dot-purple" cx="12" cy="10" r="3" fill="#C084FC"/>
      <text x="22" y="13.5" class="font-mono" font-size="9" font-weight="700" fill="#E9D5FF">AIR-GAPPED 127.0.0.1</text>
    </g>

    <!-- Viewport with REAL Embedded Screenshot -->
    <g transform="translate(2, 38)">
      <image href="data:image/jpeg;base64,{b64_ms}" xlink:href="data:image/jpeg;base64,{b64_ms}" x="0" y="0" width="684" height="476" preserveAspectRatio="xMidYMid slice" clip-path="url(#clip-ms-vp)"/>
      <rect x="0" y="0" width="684" height="476" fill="none" stroke="#25163D" stroke-width="0.5"/>
    </g>

    <!-- Floating Bottom Telemetry Glass HUD (Over Screenshot) -->
    <g transform="translate(14, 456)">
      <rect width="660" height="42" rx="8" fill="#150A28" fill-opacity="0.94" stroke="#7C3AED" stroke-width="0.8"/>
      <circle class="live-dot-purple" cx="16" cy="21" r="3.5" fill="#C084FC"/>
      <text x="28" y="24" class="font-mono" font-size="10" font-weight="700" fill="#E9D5FF">TARGET: EBWebView\\WV2Profile_tfw\\IndexedDB <tspan fill="#64748B">[LevelDB / JSON]</tspan></text>
      <text x="646" y="24" text-anchor="end" class="font-mono" font-size="9.5" font-weight="600" fill="#D8B4FE">HTML DOSSIER &#x2022; UTF-8 BOM CSVs &#x2022; ZIP MEDIA</text>
    </g>

    <!-- Window Bottom Status Bar -->
    <g transform="translate(0, 518)">
      <line x1="0" y1="0" x2="688" y2="0" stroke="#2A1646" stroke-width="0.8"/>
      <rect y="0" width="688" height="34" rx="0" fill="#130824"/>
      <rect y="22" width="688" height="12" rx="12" fill="#130824"/>

      <g transform="translate(16, 21)" class="font-mono" font-size="9.5" fill="#64748B">
        <text x="0" y="0"><tspan fill="#A855F7">&#x25CF;</tspan> PIPELINE: 5-STEP</text>
        <text x="130" y="0"><tspan fill="#C084FC">&#x25CF;</tspan> CARVER: MAGIC-BYTE</text>
        <text x="300" y="0"><tspan fill="#38BDF8">&#x25CF;</tspan> TIMESTAMPS: DUAL UTC/IST</text>
        <text x="500" y="0"><tspan fill="#34D399">&#x25CF;</tspan> CONFIDENTIALITY: LOCALHOST</text>
      </g>
    </g>
  </g>
</svg>"""

if __name__ == "__main__":
    validate_and_save("banner.svg", banner_svg)
    validate_and_save("btn-linkedin.svg", btn_linkedin)
    validate_and_save("btn-email.svg", btn_email)
    validate_and_save("btn-repos.svg", btn_repos)
    validate_and_save("btn-ceh.svg", btn_ceh)
    validate_and_save("intro.svg", intro_svg)
    validate_and_save("card-wft.svg", card_wft_svg)
    validate_and_save("card-msteams.svg", card_msteams_svg)
    print("\n[SUCCESS] All modern project assets generated & validated!")
