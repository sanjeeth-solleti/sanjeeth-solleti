"""
generate_assets.py
Generates ultra-modern, publication-grade DFIR SVG assets for Sanjeeth Solleti's GitHub profile.
Features:
- Cohesive, unified Electric Cyan / Deep Obsidian theme (no mixed/rainbow colors).
- Executive hero name banner (banner.svg).
- Unified action buttons (btn-linkedin.svg, btn-email.svg, btn-repos.svg, btn-ceh.svg).
- The DFIR Lab philosophy card (intro.svg).
- Side-by-side screenshot project cards (card-wft.svg, card-msteams.svg).
- Yellow scrolling tape removed completely.
"""

import os
import io
import base64
import xml.etree.ElementTree as ET
from PIL import Image

ASSETS_DIR = r"C:\Users\SANJEETH\Desktop\sanjeeth-solleti\assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

# Remove tape.svg if it exists (yellow scrolling tape removed per task)
tape_path = os.path.join(ASSETS_DIR, "tape.svg")
if os.path.exists(tape_path):
    try:
        os.remove(tape_path)
        print("[REMOVED] tape.svg deleted")
    except Exception as e:
        print(f"[WARN] Could not delete tape.svg: {e}")

# Remove map.svg if it exists
map_path = os.path.join(ASSETS_DIR, "map.svg")
if os.path.exists(map_path):
    try:
        os.remove(map_path)
        print("[REMOVED] map.svg deleted")
    except Exception as e:
        print(f"[WARN] Could not delete map.svg: {e}")

# Remove stats.svg if it exists
stats_path = os.path.join(ASSETS_DIR, "stats.svg")
if os.path.exists(stats_path):
    try:
        os.remove(stats_path)
        print("[REMOVED] stats.svg deleted")
    except Exception as e:
        print(f"[WARN] Could not delete stats.svg: {e}")

def validate_and_save(filename, svg_content):
    path = os.path.join(ASSETS_DIR, filename)
    clean_svg = svg_content.strip()
    try:
        ET.fromstring(clean_svg)
    except ET.ParseError as e:
        print(f"ERROR validating {filename}: {e}")
        lines = clean_svg.split("\n")
        for i, line in enumerate(lines[:60]):
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
# 1. BANNER.SVG (1280 x 300) — Executive DFIR Hero Banner & Name Card
# ==============================================================================
banner_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 300" width="1280" height="300" role="img" aria-label="Vasava Sanjeeth Solleti — Digital Forensics &amp; Incident Response Analyst at TCS">
  <defs>
    <linearGradient id="bg-canvas" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#05070E"/>
      <stop offset="50%" stop-color="#090E1D"/>
      <stop offset="100%" stop-color="#05070E"/>
    </linearGradient>

    <radialGradient id="nebula-cyan" cx="15%" cy="30%" r="65%">
      <stop offset="0%" stop-color="#00D2FF" stop-opacity="0.16"/>
      <stop offset="50%" stop-color="#0284C7" stop-opacity="0.04"/>
      <stop offset="100%" stop-color="#05070E" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="frame-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.5"/>
      <stop offset="40%" stop-color="#1E293B" stop-opacity="0.6"/>
      <stop offset="80%" stop-color="#0284C7" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#0F172A" stop-opacity="0.8"/>
    </linearGradient>

    <linearGradient id="top-specular" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00D2FF" stop-opacity="0"/>
      <stop offset="20%" stop-color="#38BDF8" stop-opacity="0.8"/>
      <stop offset="80%" stop-color="#0284C7" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#00D2FF" stop-opacity="0"/>
    </linearGradient>

    <linearGradient id="name-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="60%" stop-color="#F0F9FF"/>
      <stop offset="100%" stop-color="#BAE6FD"/>
    </linearGradient>

    <linearGradient id="hud-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080E1C" stop-opacity="0.92"/>
      <stop offset="100%" stop-color="#050914" stop-opacity="0.96"/>
    </linearGradient>

    <pattern id="dot-grid" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="0.9" fill="#1E293B" fill-opacity="0.35"/>
    </pattern>

    <clipPath id="banner-clip"><rect width="1280" height="300" rx="16"/></clipPath>
  </defs>

  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    .font-mono { font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; }
    .pulse-glow { animation: pglow 2.5s ease-in-out infinite; }
    @keyframes pglow { 0%, 100% { opacity: 1; } 50% { opacity: 0.35; } }
  </style>

  <g clip-path="url(#banner-clip)">
    <rect width="1280" height="300" rx="16" fill="url(#bg-canvas)"/>
    <rect width="1280" height="300" rx="16" fill="url(#nebula-cyan)"/>
    <rect width="1280" height="300" rx="16" fill="url(#dot-grid)"/>
    <rect x="0.5" y="0.5" width="1279" height="299" rx="16" fill="none" stroke="url(#frame-border)" stroke-width="1"/>

    <line x1="24" y1="1" x2="1256" y2="1" stroke="url(#top-specular)" stroke-width="2" stroke-linecap="round"/>

    <!-- TOP TELEMETRY BAR -->
    <g transform="translate(48, 20)">
      <rect x="0" y="0" width="350" height="26" rx="13" fill="#091322" stroke="#0284C7" stroke-width="0.75"/>
      <circle class="pulse-glow" cx="14" cy="13" r="3.5" fill="#38BDF8"/>
      <text x="26" y="17" class="font-sans" font-size="10.5" font-weight="700" fill="#38BDF8" letter-spacing="1">TATA CONSULTANCY SERVICES <tspan fill="#475569" font-weight="400">|</tspan> <tspan fill="#94A3B8" font-weight="600">DFIR OPERATIONS</tspan></text>

      <g transform="translate(814, 0)">
        <rect x="0" y="0" width="370" height="26" rx="13" fill="#091322" stroke="#0284C7" stroke-width="0.75"/>
        <circle cx="14" cy="13" r="3.5" fill="#38BDF8"/>
        <text x="26" y="17" class="font-sans" font-size="10" font-weight="700" fill="#BAE6FD" letter-spacing="0.8">DEFENSIBLE CHAIN-OF-CUSTODY <tspan fill="#475569" font-weight="400">|</tspan> <tspan fill="#94A3B8" font-weight="600">SHA-256 SOUND</tspan></text>
      </g>
    </g>

    <line x1="48" y1="58" x2="1232" y2="58" stroke="#1E293B" stroke-width="0.8"/>

    <!-- LEFT HERO CONTENT -->
    <g transform="translate(48, 76)">
      <text x="0" y="16" class="font-mono" font-size="11.5" font-weight="700" fill="#38BDF8" letter-spacing="2">DIGITAL FORENSICS &amp; INCIDENT RESPONSE ANALYST</text>

      <text x="0" y="58" class="font-sans" font-size="40" font-weight="800" fill="url(#name-grad)" letter-spacing="-0.5">Vasava Sanjeeth Solleti</text>

      <text x="0" y="90" class="font-sans" font-size="16" font-weight="600" fill="#E2E8F0">
        DFIR Analyst @ TCS <tspan fill="#475569" font-weight="400">|</tspan> Windows Endpoint &amp; Collaboration Forensics Engine Architect
      </text>

      <text x="0" y="116" class="font-sans" font-size="13" fill="#94A3B8">
        Reconstructing attack chronologies across raw disk images, dirty hives, &amp; IndexedDB stores.
      </text>

      <!-- Badges Row (Unified theme) -->
      <g transform="translate(0, 138)">
        <g transform="translate(0, 0)">
          <rect width="134" height="26" rx="13" fill="#091322" stroke="#0284C7" stroke-width="0.8"/>
          <circle cx="13" cy="13" r="3" fill="#38BDF8"/>
          <text x="23" y="17" class="font-mono" font-size="10.5" font-weight="700" fill="#BAE6FD">WFT Platform</text>
        </g>

        <g transform="translate(144, 0)">
          <rect width="148" height="26" rx="13" fill="#091322" stroke="#0284C7" stroke-width="0.8"/>
          <circle cx="13" cy="13" r="3" fill="#38BDF8"/>
          <text x="23" y="17" class="font-mono" font-size="10.5" font-weight="700" fill="#BAE6FD">MSTeams_Parser</text>
        </g>

        <g transform="translate(302, 0)">
          <rect width="134" height="26" rx="13" fill="#091322" stroke="#0284C7" stroke-width="0.8"/>
          <circle cx="13" cy="13" r="3" fill="#38BDF8"/>
          <text x="23" y="17" class="font-mono" font-size="10.5" font-weight="700" fill="#BAE6FD">CEH Certified</text>
        </g>

        <g transform="translate(446, 0)">
          <rect width="130" height="26" rx="13" fill="#091322" stroke="#0284C7" stroke-width="0.8"/>
          <circle cx="13" cy="13" r="3" fill="#38BDF8"/>
          <text x="23" y="17" class="font-mono" font-size="10.5" font-weight="700" fill="#BAE6FD">DuckDB Core</text>
        </g>
      </g>
    </g>

    <!-- RIGHT DFIR HUD WIDGET -->
    <g transform="translate(784, 74)">
      <rect width="448" height="162" rx="12" fill="url(#hud-bg)" stroke="#1E3A8A" stroke-width="1"/>
      
      <rect width="448" height="32" rx="12" fill="#0B162C"/>
      <rect y="24" width="448" height="8" fill="#0B162C"/>

      <circle cx="18" cy="16" r="3.5" fill="#38BDF8"/>
      <text x="32" y="20" class="font-mono" font-size="10.5" font-weight="700" fill="#BAE6FD" letter-spacing="1.2">SPECIALIZED INVESTIGATION SCOPE</text>

      <g transform="translate(18, 50)" class="font-sans" font-size="12">
        <g transform="translate(0, 0)">
          <rect x="0" y="-8" width="22" height="22" rx="5" fill="#0B1A33" stroke="#0284C7" stroke-width="0.6"/>
          <path d="M5 2 H17 M5 6 H17" stroke="#38BDF8" stroke-width="1.3" stroke-linecap="round"/>
          <circle cx="14" cy="-1" r="1.2" fill="#38BDF8"/>
          <circle cx="14" cy="3" r="1.2" fill="#38BDF8"/>
          <text x="32" y="7" fill="#F1F5F9" font-weight="600">Native VFS Ingestion <tspan fill="#64748B">|</tspan> <tspan fill="#94A3B8" font-size="11" font-weight="400">E01, RAW, VHDX, VMDK</tspan></text>
        </g>

        <g transform="translate(0, 34)">
          <rect x="0" y="-8" width="22" height="22" rx="5" fill="#0B1A33" stroke="#0284C7" stroke-width="0.6"/>
          <path d="M5 -1 C5 -3 17 -3 17 -1 C17 1 5 1 5 -1 Z M5 3 C5 5 17 5 17 3 M5 7 C5 9 17 9 17 7" fill="none" stroke="#38BDF8" stroke-width="1.3"/>
          <text x="32" y="7" fill="#F1F5F9" font-weight="600">Dirty Registry Replay <tspan fill="#64748B">|</tspan> <tspan fill="#94A3B8" font-size="11" font-weight="400">Automated RLA Commit</tspan></text>
        </g>

        <g transform="translate(0, 68)">
          <rect x="0" y="-8" width="22" height="22" rx="5" fill="#0B1A33" stroke="#0284C7" stroke-width="0.6"/>
          <path d="M5 -1 H17 V7 H11 L7 10 V7 H5 Z" fill="none" stroke="#38BDF8" stroke-width="1.3"/>
          <text x="32" y="7" fill="#F1F5F9" font-weight="600">Collaboration Forensics <tspan fill="#64748B">|</tspan> <tspan fill="#94A3B8" font-size="11" font-weight="400">Teams LevelDB / IndexedDB</tspan></text>
        </g>
      </g>
    </g>

    <!-- BOTTOM TELEMETRY FOOTER -->
    <line x1="48" y1="256" x2="1232" y2="256" stroke="#1E293B" stroke-width="0.8"/>
    <g transform="translate(48, 278)">
      <circle class="pulse-glow" cx="4" cy="-3" r="3.5" fill="#38BDF8"/>
      <text x="18" y="0" class="font-sans" font-size="11.5" font-weight="500" fill="#94A3B8">
        ACTIVE RESEARCH: <tspan fill="#E2E8F0">Dirty Registry Replay</tspan> &#x2022; <tspan fill="#E2E8F0">IndexedDB Messaging Stores</tspan> &#x2022; <tspan fill="#E2E8F0">Sub-Millisecond Super-Timelines</tspan>
      </text>
      <text x="1184" y="0" text-anchor="end" class="font-mono" font-size="11" font-weight="600" fill="#94A3B8">
        HYDERABAD, INDIA
      </text>
    </g>
  </g>
</svg>"""


# ==============================================================================
# 2. ACTION BUTTONS (195 x 42 each) — Unified Electric Cyan / Deep Obsidian
# ==============================================================================
btn_linkedin = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 195 42" width="195" height="42" role="img" aria-label="LinkedIn Profile">
  <defs>
    <linearGradient id="btn-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#08101E"/>
      <stop offset="100%" stop-color="#0C172B"/>
    </linearGradient>
    <linearGradient id="btn-border" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0284C7" stop-opacity="0.7"/>
      <stop offset="100%" stop-color="#1D4ED8" stop-opacity="0.5"/>
    </linearGradient>
  </defs>
  <rect x="0.5" y="0.5" width="194" height="41" rx="10" fill="url(#btn-bg)" stroke="url(#btn-border)" stroke-width="1"/>
  <line x1="12" y1="1" x2="183" y2="1" stroke="#38BDF8" stroke-width="1.6" stroke-linecap="round"/>

  <g transform="translate(14, 11)">
    <rect width="20" height="20" rx="4" fill="#0C203B" stroke="#0284C7" stroke-width="0.6"/>
    <circle cx="6" cy="6" r="1.5" fill="#38BDF8"/>
    <rect x="4.5" y="9" width="3" height="7" fill="#38BDF8"/>
    <path d="M10 9 H12.8 V10.2 C13.3 9.4 14.2 9 15.3 9 C17.4 9 18.2 10.3 18.2 12.4 V16 H15.4 V12.8 C15.4 11.8 15 11.2 14.1 11.2 C13.3 11.2 12.8 11.7 12.8 12.6 V16 H10 Z" fill="#38BDF8"/>
  </g>

  <text x="44" y="26" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="700" fill="#F1F5F9" letter-spacing="1">LINKEDIN</text>
  
  <path d="M174 24 L179 19 M179 19 H175 M179 19 V23" stroke="#38BDF8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
</svg>"""

btn_email = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 195 42" width="195" height="42" role="img" aria-label="Direct Email">
  <defs>
    <linearGradient id="btn-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#08101E"/>
      <stop offset="100%" stop-color="#0C172B"/>
    </linearGradient>
    <linearGradient id="btn-border" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0284C7" stop-opacity="0.7"/>
      <stop offset="100%" stop-color="#1D4ED8" stop-opacity="0.5"/>
    </linearGradient>
  </defs>
  <rect x="0.5" y="0.5" width="194" height="41" rx="10" fill="url(#btn-bg)" stroke="url(#btn-border)" stroke-width="1"/>
  <line x1="12" y1="1" x2="183" y2="1" stroke="#38BDF8" stroke-width="1.6" stroke-linecap="round"/>

  <g transform="translate(14, 11)">
    <rect width="20" height="20" rx="4" fill="#0C203B" stroke="#0284C7" stroke-width="0.6"/>
    <path d="M3.5 5.5 H16.5 V14.5 H3.5 Z" fill="none" stroke="#38BDF8" stroke-width="1.3"/>
    <path d="M4 6.5 L10 11 L16 6.5" fill="none" stroke="#38BDF8" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/>
  </g>

  <text x="44" y="26" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="700" fill="#F1F5F9" letter-spacing="1">EMAIL CONTACT</text>

  <path d="M174 24 L179 19 M179 19 H175 M179 19 V23" stroke="#38BDF8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
</svg>"""

btn_repos = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 195 42" width="195" height="42" role="img" aria-label="All GitHub Repositories">
  <defs>
    <linearGradient id="btn-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#08101E"/>
      <stop offset="100%" stop-color="#0C172B"/>
    </linearGradient>
    <linearGradient id="btn-border" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0284C7" stop-opacity="0.7"/>
      <stop offset="100%" stop-color="#1D4ED8" stop-opacity="0.5"/>
    </linearGradient>
  </defs>
  <rect x="0.5" y="0.5" width="194" height="41" rx="10" fill="url(#btn-bg)" stroke="url(#btn-border)" stroke-width="1"/>
  <line x1="12" y1="1" x2="183" y2="1" stroke="#38BDF8" stroke-width="1.6" stroke-linecap="round"/>

  <g transform="translate(14, 11)">
    <rect width="20" height="20" rx="4" fill="#0C203B" stroke="#0284C7" stroke-width="0.6"/>
    <path d="M4 6 H8.5 L10.5 8 H16 V14.5 H4 Z" fill="none" stroke="#38BDF8" stroke-width="1.3" stroke-linejoin="round"/>
  </g>

  <text x="44" y="26" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="700" fill="#F1F5F9" letter-spacing="1">REPOSITORIES</text>

  <path d="M174 24 L179 19 M179 19 H175 M179 19 V23" stroke="#38BDF8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
</svg>"""

btn_ceh = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 195 42" width="195" height="42" role="img" aria-label="CEH Certified Ethical Hacker">
  <defs>
    <linearGradient id="btn-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#08101E"/>
      <stop offset="100%" stop-color="#0C172B"/>
    </linearGradient>
    <linearGradient id="btn-border" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0284C7" stop-opacity="0.7"/>
      <stop offset="100%" stop-color="#1D4ED8" stop-opacity="0.5"/>
    </linearGradient>
  </defs>
  <rect x="0.5" y="0.5" width="194" height="41" rx="10" fill="url(#btn-bg)" stroke="url(#btn-border)" stroke-width="1"/>
  <line x1="12" y1="1" x2="183" y2="1" stroke="#38BDF8" stroke-width="1.6" stroke-linecap="round"/>

  <g transform="translate(14, 11)">
    <rect width="20" height="20" rx="4" fill="#0C203B" stroke="#0284C7" stroke-width="0.6"/>
    <path d="M10 4 L15.5 6.5 V10.5 C15.5 13.5 10 16 10 16 C10 16 4.5 13.5 4.5 10.5 V6.5 Z" fill="none" stroke="#38BDF8" stroke-width="1.3"/>
    <path d="M8 10 L9.5 11.5 L12.5 8" fill="none" stroke="#38BDF8" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
  </g>

  <text x="44" y="26" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="700" fill="#F1F5F9" letter-spacing="1">CEH CERTIFIED</text>

  <path d="M174 21 L177 24 L182 18" stroke="#38BDF8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
</svg>"""


# ==============================================================================
# 3. INTRO.SVG (1280 x 260) — DFIR Lab Philosophy & Tenets (Unified Palette)
# ==============================================================================
intro_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 260" width="1280" height="260" role="img" aria-label="The DFIR Lab — Open source tools engineered for the gaps where standard forensic suites stop short.">
  <defs>
    <linearGradient id="bg-intro" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#060A14"/>
      <stop offset="50%" stop-color="#090E1F"/>
      <stop offset="100%" stop-color="#05070E"/>
    </linearGradient>

    <radialGradient id="gl-intro" cx="15%" cy="20%" r="65%">
      <stop offset="0%" stop-color="#00D2FF" stop-opacity="0.20"/>
      <stop offset="60%" stop-color="#0284C7" stop-opacity="0.04"/>
      <stop offset="100%" stop-color="#060A14" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="intro-border" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.45"/>
      <stop offset="50%" stop-color="#1E3A8A" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#0284C7" stop-opacity="0.4"/>
    </linearGradient>

    <linearGradient id="hi-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="50%" stop-color="#7DD3FC"/>
      <stop offset="100%" stop-color="#38BDF8"/>
    </linearGradient>

    <pattern id="dt-intro" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1.1" fill="#1E293B" fill-opacity="0.45"/>
    </pattern>

    <filter id="sh-chip" x="-10%" y="-10%" width="120%" height="130%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.4"/>
    </filter>

    <clipPath id="intro-clip"><rect width="1280" height="260" rx="16"/></clipPath>
  </defs>

  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    .font-mono { font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; }
    .pulse-glow { animation: pglow 6s ease-in-out infinite; }
    @keyframes pglow { 0%, 100% { opacity: 0.7; } 50% { opacity: 1; } }
  </style>

  <g clip-path="url(#intro-clip)">
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

    <!-- RIGHT TENET PILLARS (3 Glassmorphic Chips - Unified Palette) -->
    <g transform="translate(820, 24)">
      <!-- Pillar 1: Read-Only VFS -->
      <g transform="translate(0, 0)">
        <rect width="404" height="60" rx="12" fill="#0A1830" stroke="#0284C7" stroke-width="0.75" filter="url(#sh-chip)"/>
        <rect x="12" y="14" width="32" height="32" rx="8" fill="#0C2448" stroke="#38BDF8" stroke-width="0.8"/>
        <path d="M24 24 H32 V36 H24 Z M26 24 V21 C26 19.5 27 18 28 18 C29 18 30 19.5 30 21 V24" fill="none" stroke="#38BDF8" stroke-width="1.3" stroke-linecap="round"/>
        <text x="56" y="29" class="font-mono" font-size="11.5" font-weight="700" fill="#38BDF8" letter-spacing="1">READ-ONLY VFS INTAKE</text>
        <text x="56" y="46" class="font-sans" font-size="12" fill="#94A3B8">Mounted immutable via dissect; disk containers never modified.</text>
      </g>

      <!-- Pillar 2: Dirty Log Replay -->
      <g transform="translate(0, 72)">
        <rect width="404" height="60" rx="12" fill="#0A1830" stroke="#0284C7" stroke-width="0.75" filter="url(#sh-chip)"/>
        <rect x="12" y="14" width="32" height="32" rx="8" fill="#0C2448" stroke="#38BDF8" stroke-width="0.8"/>
        <path d="M24 30 A5 5 0 1 1 32 30" fill="none" stroke="#38BDF8" stroke-width="1.4"/>
        <path d="M32 27 L32 30 L29 30" fill="none" stroke="#38BDF8" stroke-width="1.4" stroke-linecap="round"/>
        <text x="56" y="29" class="font-mono" font-size="11.5" font-weight="700" fill="#38BDF8" letter-spacing="1">DIRTY LOG REPLAY</text>
        <text x="56" y="46" class="font-sans" font-size="12" fill="#94A3B8">Mandatory automated RLA transaction commit before hive analysis.</text>
      </g>

      <!-- Pillar 3: Columnar Speed -->
      <g transform="translate(0, 144)">
        <rect width="404" height="60" rx="12" fill="#0A1830" stroke="#0284C7" stroke-width="0.75" filter="url(#sh-chip)"/>
        <rect x="12" y="14" width="32" height="32" rx="8" fill="#0C2448" stroke="#38BDF8" stroke-width="0.8"/>
        <path d="M29 20 L24 28 H30 L27 36 L33 26 H27 Z" fill="#38BDF8"/>
        <text x="56" y="29" class="font-mono" font-size="11.5" font-weight="700" fill="#38BDF8" letter-spacing="1">COLUMNAR SPEED</text>
        <text x="56" y="46" class="font-sans" font-size="12" fill="#94A3B8">Sub-millisecond analytical queries across 500K+ records via DuckDB.</text>
      </g>
    </g>
  </g>
</svg>"""


# ==============================================================================
# 4. CARD-WFT.SVG (1280 x 640) — WFT Side-by-Side Card (Electric Cyan / Obsidian)
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
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.55"/>
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
      <circle cx="2" cy="2" r="1.1" fill="#1E293B" fill-opacity="0.45"/>
    </pattern>

    <!-- Drop Shadow for Window Frame -->
    <filter id="sh-wbox" x="-10%" y="-10%" width="125%" height="125%">
      <feDropShadow dx="0" dy="16" stdDeviation="22" flood-color="#000000" flood-opacity="0.75"/>
    </filter>

    <!-- Card Outer Clip -->
    <clipPath id="cc-wft"><rect width="1280" height="640" rx="20"/></clipPath>

    <!-- Screenshot Viewport Clip -->
    <clipPath id="wc-wft">
      <rect x="548" y="108" width="692" height="434" rx="2"/>
    </clipPath>
  </defs>

  <style>
    .font-sans {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }}
    .font-mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; }}
    
    /* Animations */
    .pulse-ambient {{ animation: pamb 6s ease-in-out infinite; }}
    .live-dot {{ animation: ldot 2s cubic-bezier(0.4, 0, 0.6, 1) infinite; }}
    .radar-ring {{ animation: rring 2.4s cubic-bezier(0, 0.2, 0.8, 1) infinite; transform-origin: 88px 288px; }}
    
    @keyframes pamb {{ 0%, 100% {{ opacity: 0.65; }} 50% {{ opacity: 1; }} }}
    @keyframes ldot {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0.35; }} }}
    @keyframes rring {{ 0% {{ r: 3; opacity: 1; }} 100% {{ r: 16; opacity: 0; }} }}
    
    @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} }}
  </style>

  <g clip-path="url(#cc-wft)">
    <!-- Canvas Surface -->
    <rect width="1280" height="640" rx="20" fill="url(#bg-wft)"/>
    <rect class="pulse-ambient" width="1280" height="640" rx="20" fill="url(#gl-wft)"/>
    <rect width="1280" height="640" rx="20" fill="url(#dt-wft)"/>
    <rect x="0.5" y="0.5" width="1279" height="639" rx="20" fill="none" stroke="url(#border-wft)" stroke-width="1"/>

    <!-- Top Specular Highlight Line -->
    <line x1="20" y1="1" x2="1260" y2="1" stroke="#38BDF8" stroke-width="2" stroke-linecap="round"/>

    <!-- ==================== LEFT COLUMN: DFIR SPECIFICATIONS ==================== -->
    <g>
      <!-- Category & Index Tag -->
      <text x="64" y="66" class="font-mono" font-size="12" font-weight="700" fill="#38BDF8" letter-spacing="2">TOOL 01 / 02 &#x2022; ENTERPRISE WINDOWS FORENSICS</text>
      <rect x="64" y="78" width="44" height="3" rx="1.5" fill="#38BDF8"/>

      <!-- Tech Chips Row -->
      <g transform="translate(64, 98)">
        <rect x="0" y="0" width="136" height="26" rx="13" fill="#0A2244" stroke="#0284C7" stroke-width="0.8"/>
        <text x="68" y="17" text-anchor="middle" class="font-mono" font-size="10.5" font-weight="700" fill="#93C5FD">dissect.target VFS</text>

        <rect x="144" y="0" width="112" height="26" rx="13" fill="#0A2244" stroke="#0284C7" stroke-width="0.8"/>
        <text x="200" y="17" text-anchor="middle" class="font-mono" font-size="10.5" font-weight="700" fill="#93C5FD">DuckDB Core</text>

        <rect x="264" y="0" width="128" height="26" rx="13" fill="#0A2244" stroke="#0284C7" stroke-width="0.8"/>
        <text x="328" y="17" text-anchor="middle" class="font-mono" font-size="10.5" font-weight="700" fill="#93C5FD">RLA Log Commit</text>

        <rect x="400" y="0" width="76" height="26" rx="13" fill="#0A2244" stroke="#0284C7" stroke-width="0.8"/>
        <text x="438" y="17" text-anchor="middle" class="font-mono" font-size="10.5" font-weight="700" fill="#93C5FD">YARA-X</text>
      </g>

      <!-- Main Title & Tagline -->
      <text x="62" y="176" class="font-sans" font-size="52" font-weight="800" fill="url(#wft-title)" letter-spacing="-0.5">WFT</text>
      <text x="64" y="210" class="font-sans" font-size="19" font-weight="700" fill="#E2E8F0">Windows Forensic Examination Platform</text>
      <text x="64" y="234" class="font-sans" font-size="14.5" fill="#94A3B8">Raw container intake to sub-millisecond super-timelines.</text>

      <!-- ANIMATED TIME CARD / TELEMETRY HUD WIDGET -->
      <g>
        <rect x="64" y="256" width="450" height="64" rx="10" fill="#08172E" stroke="#1D4ED8" stroke-width="0.8"/>
        <!-- Radar Status Indicator -->
        <circle class="live-dot" cx="88" cy="288" r="4.5" fill="#38BDF8">
          <animate attributeName="opacity" values="1;0.35;1" dur="2s" repeatCount="indefinite"/>
        </circle>
        <circle class="radar-ring" cx="88" cy="288" r="4.5" fill="none" stroke="#38BDF8" stroke-width="1.2">
          <animate attributeName="r" values="3;16" dur="2.4s" repeatCount="indefinite"/>
          <animate attributeName="opacity" values="1;0" dur="2.4s" repeatCount="indefinite"/>
        </circle>
        
        <text x="108" y="281" class="font-mono" font-size="11" font-weight="700" fill="#38BDF8" letter-spacing="1">TIME CARD &amp; SUPER-TIMELINE HUD</text>
        <text x="108" y="300" class="font-sans" font-size="12" fill="#F1F5F9">UTC &#177;00:00 &#x2022; <tspan font-weight="700" fill="#38BDF8">524,198 Records</tspan> Parsed in 0.72s</text>

        <!-- Animated Sweeping Timeline Bar -->
        <line x1="64" y1="319" x2="160" y2="319" stroke="#38BDF8" stroke-width="1.6">
          <animate attributeName="x1" values="64;414;64" dur="4s" repeatCount="indefinite"/>
          <animate attributeName="x2" values="160;514;160" dur="4s" repeatCount="indefinite"/>
        </line>
      </g>

      <!-- 4 Core Forensic Feature Points -->
      <g>
        <!-- Point 1: DuckDB Columnar Core -->
        <g transform="translate(64, 342)">
          <rect width="22" height="22" rx="6" fill="#0A2244" stroke="#0284C7" stroke-width="0.8"/>
          <path d="M6 11 L10 15 L16 7" fill="none" stroke="#38BDF8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          <text x="34" y="12" class="font-sans" font-size="15.5" font-weight="700" fill="#FFFFFF">Zero-Copy DuckDB Columnar Core</text>
          <text x="34" y="29" class="font-sans" font-size="13" fill="#94A3B8">Sub-ms SQL queries across 500,000+ events with unpivoted filters</text>
        </g>

        <!-- Point 2: Dirty Registry Replay -->
        <g transform="translate(64, 398)">
          <rect width="22" height="22" rx="6" fill="#0A2244" stroke="#0284C7" stroke-width="0.8"/>
          <path d="M6 11 L10 15 L16 7" fill="none" stroke="#38BDF8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          <text x="34" y="12" class="font-sans" font-size="15.5" font-weight="700" fill="#FFFFFF">Mandatory Dirty Registry Replay</text>
          <text x="34" y="29" class="font-sans" font-size="13" fill="#94A3B8">Automated RLA commit for volatile .LOG1/.LOG2 logs before hive analysis</text>
        </g>

        <!-- Point 3: Direct VFS Intake -->
        <g transform="translate(64, 454)">
          <rect width="22" height="22" rx="6" fill="#0A2244" stroke="#0284C7" stroke-width="0.8"/>
          <path d="M6 11 L10 15 L16 7" fill="none" stroke="#38BDF8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          <text x="34" y="12" class="font-sans" font-size="15.5" font-weight="700" fill="#FFFFFF">Native VFS Multi-Format Intake</text>
          <text x="34" y="29" class="font-sans" font-size="13" fill="#94A3B8">Direct read-only mounting of .E01, .RAW, .VHDX, and .VMDK containers</text>
        </g>

        <!-- Point 4: Threat Hunting & OCR -->
        <g transform="translate(64, 510)">
          <rect width="22" height="22" rx="6" fill="#0A2244" stroke="#0284C7" stroke-width="0.8"/>
          <path d="M6 11 L10 15 L16 7" fill="none" stroke="#38BDF8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          <text x="34" y="12" class="font-sans" font-size="15.5" font-weight="700" fill="#FFFFFF">Threat Hunting &amp; RapidOCR Triage</text>
          <text x="34" y="29" class="font-sans" font-size="13" fill="#94A3B8">Compiled Rust YARA-X rules + OCR text extraction from carved images</text>
        </g>
      </g>

      <!-- Footer Stats Metrics Bar -->
      <g transform="translate(64, 584)">
        <text class="font-mono" font-size="12" fill="#8B949E">
          29-stage ingest  &#x2022;  500K+ rows/sec  &#x2022;  dissect VFS  &#x2022;  Cytoscape graph
        </text>
      </g>
    </g>

    <!-- ==================== RIGHT COLUMN: REAL APPLICATION WINDOW ==================== -->
    <g>
      <!-- Window Outer Shell with Drop Shadow -->
      <rect x="548" y="70" width="692" height="504" rx="12" fill="#0A1122" stroke="#1E3A8A" stroke-width="1.2" filter="url(#sh-wbox)"/>

      <!-- Mac-Style Titlebar -->
      <rect x="548" y="70" width="692" height="38" rx="12" fill="#0D182E"/>
      <rect x="548" y="96" width="692" height="12" fill="#0D182E"/>

      <!-- Window Dots -->
      <circle cx="568" cy="89" r="4.5" fill="#EF4444" fill-opacity="0.9"/>
      <circle cx="583" cy="89" r="4.5" fill="#F59E0B" fill-opacity="0.9"/>
      <circle cx="598" cy="89" r="4.5" fill="#10B981" fill-opacity="0.9"/>

      <!-- Centered Window Title -->
      <text x="894" y="93" text-anchor="middle" class="font-sans" font-size="11.5" font-weight="600" fill="#94A3B8">
        WFT — Windows Forensic Examination Platform
      </text>

      <!-- Right Live Session Indicator -->
      <g transform="translate(1106, 79)">
        <rect width="124" height="20" rx="10" fill="#081E38" stroke="#0284C7" stroke-width="0.8"/>
        <circle class="live-dot" cx="12" cy="10" r="3" fill="#38BDF8"/>
        <text x="22" y="13.5" class="font-mono" font-size="9" font-weight="700" fill="#BAE6FD">LIVE DUCKDB CORE</text>
      </g>

      <!-- Viewport with REAL Embedded Screenshot -->
      <image href="data:image/jpeg;base64,{b64_wft}" xlink:href="data:image/jpeg;base64,{b64_wft}" x="548" y="108" width="692" height="434" preserveAspectRatio="xMidYMin slice" clip-path="url(#wc-wft)"/>
      <rect x="548" y="108" width="692" height="434" fill="none" stroke="#1E293B" stroke-width="0.5"/>

      <!-- Floating Bottom Telemetry Glass HUD -->
      <g transform="translate(560, 488)">
        <rect width="668" height="42" rx="8" fill="#071328" fill-opacity="0.94" stroke="#0284C7" stroke-width="0.8"/>
        <circle class="live-dot" cx="16" cy="21" r="3.5" fill="#38BDF8"/>
        <text x="28" y="24" class="font-mono" font-size="10" font-weight="700" fill="#BAE6FD">CONTAINER: Windows10_Forensic.E01 <tspan fill="#64748B">[VFS MOUNTED &#x2022; READ ONLY]</tspan></text>
        <text x="654" y="24" text-anchor="end" class="font-mono" font-size="9.5" font-weight="600" fill="#38BDF8">524,198 ARTIFACTS PARSED (0.72s) &#x2022; SHA-256 VERIFIED</text>
      </g>

      <!-- Window Bottom Status Bar -->
      <g transform="translate(548, 542)">
        <line x1="0" y1="0" x2="692" y2="0" stroke="#1E293B" stroke-width="0.8"/>
        <rect y="0" width="692" height="32" rx="0" fill="#08101E"/>
        <rect y="20" width="692" height="12" rx="12" fill="#08101E"/>

        <g transform="translate(16, 20)" class="font-mono" font-size="9.5" fill="#64748B">
          <text x="0" y="0"><tspan fill="#38BDF8">&#x25CF;</tspan> VFS: ACTIVE</text>
          <text x="120" y="0"><tspan fill="#38BDF8">&#x25CF;</tspan> AG GRID: VIRTUALIZED</text>
          <text x="280" y="0"><tspan fill="#38BDF8">&#x25CF;</tspan> CYTOSCAPE: READY</text>
          <text x="480" y="0"><tspan fill="#38BDF8">&#x25CF;</tspan> ENGINE: DUCKDB v1.0</text>
        </g>
      </g>
    </g>
  </g>
</svg>"""


# ==============================================================================
# 5. CARD-MSTEAMS.SVG (1280 x 640) — MSTeams_Parser Card (Electric Cyan / Obsidian)
# ==============================================================================
card_msteams_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1280 640" width="1280" height="640" role="img" aria-label="MSTeams_Parser — Microsoft Teams DFIR Forensic Suite with LevelDB and IndexedDB Parsing">
  <defs>
    <!-- Background Canvas -->
    <linearGradient id="bg-ms" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050811"/>
      <stop offset="50%" stop-color="#080E1C"/>
      <stop offset="100%" stop-color="#05070E"/>
    </linearGradient>

    <!-- Glowing Nebula -->
    <radialGradient id="gl-ms" cx="15%" cy="20%" r="65%">
      <stop offset="0%" stop-color="#00D2FF" stop-opacity="0.22"/>
      <stop offset="55%" stop-color="#1D4ED8" stop-opacity="0.05"/>
      <stop offset="100%" stop-color="#050811" stop-opacity="0"/>
    </radialGradient>

    <!-- Border Stroke -->
    <linearGradient id="border-ms" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.55"/>
      <stop offset="45%" stop-color="#1E3A8A" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#1E293B" stop-opacity="0.4"/>
    </linearGradient>

    <!-- Title Gradient -->
    <linearGradient id="ms-title" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="60%" stop-color="#F0F9FF"/>
      <stop offset="100%" stop-color="#BAE6FD"/>
    </linearGradient>

    <!-- Dot Grid Pattern -->
    <pattern id="dt-ms" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1.1" fill="#1E293B" fill-opacity="0.45"/>
    </pattern>

    <!-- Drop Shadow for Window Frame -->
    <filter id="sh-msbox" x="-10%" y="-10%" width="125%" height="125%">
      <feDropShadow dx="0" dy="16" stdDeviation="22" flood-color="#000000" flood-opacity="0.75"/>
    </filter>

    <!-- Card Outer Clip -->
    <clipPath id="cc-ms"><rect width="1280" height="640" rx="20"/></clipPath>

    <!-- Screenshot Viewport Clip -->
    <clipPath id="wc-ms">
      <rect x="548" y="108" width="692" height="434" rx="2"/>
    </clipPath>
  </defs>

  <style>
    .font-sans {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }}
    .font-mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; }}
    
    /* Animations */
    .pulse-ambient {{ animation: pamb 6s ease-in-out infinite; }}
    .live-dot {{ animation: ldot 2s cubic-bezier(0.4, 0, 0.6, 1) infinite; }}
    .radar-ring {{ animation: rring 2.4s cubic-bezier(0, 0.2, 0.8, 1) infinite; transform-origin: 88px 288px; }}
    
    @keyframes pamb {{ 0%, 100% {{ opacity: 0.65; }} 50% {{ opacity: 1; }} }}
    @keyframes ldot {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0.35; }} }}
    @keyframes rring {{ 0% {{ r: 3; opacity: 1; }} 100% {{ r: 16; opacity: 0; }} }}
    
    @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} }}
  </style>

  <g clip-path="url(#cc-ms)">
    <!-- Canvas Surface -->
    <rect width="1280" height="640" rx="20" fill="url(#bg-ms)"/>
    <rect class="pulse-ambient" width="1280" height="640" rx="20" fill="url(#gl-ms)"/>
    <rect width="1280" height="640" rx="20" fill="url(#dt-ms)"/>
    <rect x="0.5" y="0.5" width="1279" height="639" rx="20" fill="none" stroke="url(#border-ms)" stroke-width="1"/>

    <!-- Top Specular Highlight Line -->
    <line x1="20" y1="1" x2="1260" y2="1" stroke="#38BDF8" stroke-width="2" stroke-linecap="round"/>

    <!-- ==================== LEFT COLUMN: DFIR SPECIFICATIONS ==================== -->
    <g>
      <!-- Category & Index Tag -->
      <text x="64" y="66" class="font-mono" font-size="12" font-weight="700" fill="#38BDF8" letter-spacing="2">TOOL 02 / 02 &#x2022; COLLABORATION DFIR SUITE</text>
      <rect x="64" y="78" width="44" height="3" rx="1.5" fill="#38BDF8"/>

      <!-- Tech Chips Row -->
      <g transform="translate(64, 98)">
        <rect x="0" y="0" width="144" height="26" rx="13" fill="#0A2244" stroke="#0284C7" stroke-width="0.8"/>
        <text x="72" y="17" text-anchor="middle" class="font-mono" font-size="10.5" font-weight="700" fill="#93C5FD">LevelDB / IndexedDB</text>

        <rect x="152" y="0" width="104" height="26" rx="13" fill="#0A2244" stroke="#0284C7" stroke-width="0.8"/>
        <text x="204" y="17" text-anchor="middle" class="font-mono" font-size="10.5" font-weight="700" fill="#93C5FD">dfindexeddb</text>

        <rect x="264" y="0" width="90" height="26" rx="13" fill="#0A2244" stroke="#0284C7" stroke-width="0.8"/>
        <text x="309" y="17" text-anchor="middle" class="font-mono" font-size="10.5" font-weight="700" fill="#93C5FD">cramjam</text>

        <rect x="362" y="0" width="100" height="26" rx="13" fill="#0A2244" stroke="#0284C7" stroke-width="0.8"/>
        <text x="412" y="17" text-anchor="middle" class="font-mono" font-size="10.5" font-weight="700" fill="#93C5FD">Air-Gapped</text>
      </g>

      <!-- Main Title & Tagline -->
      <text x="62" y="176" class="font-sans" font-size="52" font-weight="800" fill="url(#ms-title)" letter-spacing="-0.5">MSTeams_Parser</text>
      <text x="64" y="210" class="font-sans" font-size="19" font-weight="700" fill="#E2E8F0">Microsoft Teams Forensic Analysis Suite</text>
      <text x="64" y="234" class="font-sans" font-size="14.5" fill="#94A3B8">Reconstruct enterprise Teams chats, calls, meetings, &amp; media.</text>

      <!-- ANIMATED TIME CARD / TELEMETRY HUD WIDGET -->
      <g>
        <rect x="64" y="256" width="450" height="64" rx="10" fill="#08172E" stroke="#1D4ED8" stroke-width="0.8"/>
        <!-- Radar Status Indicator -->
        <circle class="live-dot" cx="88" cy="288" r="4.5" fill="#38BDF8">
          <animate attributeName="opacity" values="1;0.35;1" dur="2s" repeatCount="indefinite"/>
        </circle>
        <circle class="radar-ring" cx="88" cy="288" r="4.5" fill="none" stroke="#38BDF8" stroke-width="1.2">
          <animate attributeName="r" values="3;16" dur="2.4s" repeatCount="indefinite"/>
          <animate attributeName="opacity" values="1;0" dur="2.4s" repeatCount="indefinite"/>
        </circle>
        
        <text x="108" y="281" class="font-mono" font-size="11" font-weight="700" fill="#38BDF8" letter-spacing="1">AIR-GAPPED TIME CARD &amp; FORENSIC DAEMON</text>
        <text x="108" y="300" class="font-sans" font-size="12" fill="#F1F5F9">Strict 127.0.0.1 &#x2022; <tspan font-weight="700" fill="#38BDF8">Dual UTC &amp; IST (+05:30)</tspan> Timestamps</text>

        <!-- Animated Sweeping Timeline Bar -->
        <line x1="64" y1="319" x2="160" y2="319" stroke="#38BDF8" stroke-width="1.6">
          <animate attributeName="x1" values="64;414;64" dur="4s" repeatCount="indefinite"/>
          <animate attributeName="x2" values="160;514;160" dur="4s" repeatCount="indefinite"/>
        </line>
      </g>

      <!-- 4 Core Forensic Feature Points -->
      <g>
        <!-- Point 1: Multi-Source Ingestion -->
        <g transform="translate(64, 342)">
          <rect width="22" height="22" rx="6" fill="#0A2244" stroke="#0284C7" stroke-width="0.8"/>
          <path d="M6 11 L10 15 L16 7" fill="none" stroke="#38BDF8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          <text x="34" y="12" class="font-sans" font-size="15.5" font-weight="700" fill="#FFFFFF">Multi-Source LevelDB &amp; IndexedDB Intake</text>
          <text x="34" y="29" class="font-sans" font-size="13" fill="#94A3B8">Ingests New Teams (%LOCALAPPDATA% EBWebView) &amp; Classic stores</text>
        </g>

        <!-- Point 2: Adaptive Card Normalization -->
        <g transform="translate(64, 398)">
          <rect width="22" height="22" rx="6" fill="#0A2244" stroke="#0284C7" stroke-width="0.8"/>
          <path d="M6 11 L10 15 L16 7" fill="none" stroke="#38BDF8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          <text x="34" y="12" class="font-sans" font-size="15.5" font-weight="700" fill="#FFFFFF">Adaptive Card &amp; Event Normalization</text>
          <text x="34" y="29" class="font-sans" font-size="13" fill="#94A3B8">Unpacks Base64 JSON cards, call durations, meeting logs, &amp; roles</text>
        </g>

        <!-- Point 3: Identity Resolution -->
        <g transform="translate(64, 454)">
          <rect width="22" height="22" rx="6" fill="#0A2244" stroke="#0284C7" stroke-width="0.8"/>
          <path d="M6 11 L10 15 L16 7" fill="none" stroke="#38BDF8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          <text x="34" y="12" class="font-sans" font-size="15.5" font-weight="700" fill="#FFFFFF">Identity &amp; Internal GUID Resolution</text>
          <text x="34" y="29" class="font-sans" font-size="13" fill="#94A3B8">Resolves internal 8:orgid GUIDs to corporate employees &amp; emails</text>
        </g>

        <!-- Point 4: Media Carver -->
        <g transform="translate(64, 510)">
          <rect width="22" height="22" rx="6" fill="#0A2244" stroke="#0284C7" stroke-width="0.8"/>
          <path d="M6 11 L10 15 L16 7" fill="none" stroke="#38BDF8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          <text x="34" y="12" class="font-sans" font-size="15.5" font-weight="700" fill="#FFFFFF">Magic-Byte Media &amp; Attachment Carver</text>
          <text x="34" y="29" class="font-sans" font-size="13" fill="#94A3B8">Carves cached images while filtering UI telemetry noise (&lt; 3.5 KB)</text>
        </g>
      </g>

      <!-- Footer Stats Metrics Bar -->
      <g transform="translate(64, 584)">
        <text class="font-mono" font-size="12" fill="#8B949E">
          5-step pipeline  &#x2022;  magic-byte carver  &#x2022;  dual UTC/IST  &#x2022;  HTML dossier
        </text>
      </g>
    </g>

    <!-- ==================== RIGHT COLUMN: REAL APPLICATION WINDOW ==================== -->
    <g>
      <!-- Window Outer Shell with Drop Shadow -->
      <rect x="548" y="70" width="692" height="504" rx="12" fill="#0A1122" stroke="#1E3A8A" stroke-width="1.2" filter="url(#sh-msbox)"/>

      <!-- Mac-Style Titlebar -->
      <rect x="548" y="70" width="692" height="38" rx="12" fill="#0D182E"/>
      <rect x="548" y="96" width="692" height="12" fill="#0D182E"/>

      <!-- Window Dots -->
      <circle cx="568" cy="89" r="4.5" fill="#EF4444" fill-opacity="0.9"/>
      <circle cx="583" cy="89" r="4.5" fill="#F59E0B" fill-opacity="0.9"/>
      <circle cx="598" cy="89" r="4.5" fill="#10B981" fill-opacity="0.9"/>

      <!-- Centered Window Title -->
      <text x="894" y="93" text-anchor="middle" class="font-sans" font-size="11.5" font-weight="600" fill="#94A3B8">
        MSTeams_Parser — Desktop Forensic Viewer &amp; Dossier
      </text>

      <!-- Right Live Session Indicator -->
      <g transform="translate(1106, 79)">
        <rect width="124" height="20" rx="10" fill="#081E38" stroke="#0284C7" stroke-width="0.8"/>
        <circle class="live-dot" cx="12" cy="10" r="3" fill="#38BDF8"/>
        <text x="22" y="13.5" class="font-mono" font-size="9" font-weight="700" fill="#BAE6FD">AIR-GAPPED 127.0.0.1</text>
      </g>

      <!-- Viewport with REAL Embedded Screenshot -->
      <image href="data:image/jpeg;base64,{b64_ms}" xlink:href="data:image/jpeg;base64,{b64_ms}" x="548" y="108" width="692" height="434" preserveAspectRatio="xMidYMin slice" clip-path="url(#wc-ms)"/>
      <rect x="548" y="108" width="692" height="434" fill="none" stroke="#1E293B" stroke-width="0.5"/>

      <!-- Floating Bottom Telemetry Glass HUD -->
      <g transform="translate(560, 488)">
        <rect width="668" height="42" rx="8" fill="#071328" fill-opacity="0.94" stroke="#0284C7" stroke-width="0.8"/>
        <circle class="live-dot" cx="16" cy="21" r="3.5" fill="#38BDF8"/>
        <text x="28" y="24" class="font-mono" font-size="10" font-weight="700" fill="#BAE6FD">TARGET: EBWebView\\WV2Profile_tfw\\IndexedDB <tspan fill="#64748B">[LevelDB / JSON]</tspan></text>
        <text x="654" y="24" text-anchor="end" class="font-mono" font-size="9.5" font-weight="600" fill="#38BDF8">HTML DOSSIER &#x2022; UTF-8 BOM CSVs &#x2022; ZIP MEDIA</text>
      </g>

      <!-- Window Bottom Status Bar -->
      <g transform="translate(548, 542)">
        <line x1="0" y1="0" x2="692" y2="0" stroke="#1E293B" stroke-width="0.8"/>
        <rect y="0" width="692" height="32" rx="0" fill="#08101E"/>
        <rect y="20" width="692" height="12" rx="12" fill="#08101E"/>

        <g transform="translate(16, 20)" class="font-mono" font-size="9.5" fill="#64748B">
          <text x="0" y="0"><tspan fill="#38BDF8">&#x25CF;</tspan> PIPELINE: 5-STEP</text>
          <text x="130" y="0"><tspan fill="#38BDF8">&#x25CF;</tspan> CARVER: MAGIC-BYTE</text>
          <text x="300" y="0"><tspan fill="#38BDF8">&#x25CF;</tspan> TIMESTAMPS: DUAL UTC/IST</text>
          <text x="500" y="0"><tspan fill="#38BDF8">&#x25CF;</tspan> CONFIDENTIALITY: LOCALHOST</text>
        </g>
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
