"""
generate_assets.py
Generates ultra-modern, publication-grade DFIR SVG assets for Sanjeeth Solleti's GitHub profile.
Aesthetic inspired by Linear / Vercel / Raycast:
- Deep obsidian & slate canvas (#050811, #080D1A, #0B132B)
- Multi-layered soft ambient glows (electric cyan #00D2FF, royal indigo #6366F1, radiant violet #A855F7, emerald #10B981)
- Luminous gradient borders, top-edge horizon specular highlights, and glassmorphic panels
- Refined typography with metallic gradient headlines and high-contrast metadata
- Hardware-grade glass pill badges with authentic vector iconography
- Bespoke DFIR iconography for each feature highlight
- Defensible, deterministic DFIR pipeline visualization with curved/orthogonal flow connectors
- Strictly features Sanjeeth's two genuine tools: WFT and MSTeams_Parser
- Zero retro-terminal tropes, zero clunky borders, zero overlapping text
"""
import os
import re
import xml.etree.ElementTree as ET

ASSETS_DIR = r"C:\Users\SANJEETH\Desktop\sanjeeth-solleti\assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

def validate_and_save(filename, svg_content):
    path = os.path.join(ASSETS_DIR, filename)
    clean_svg = svg_content.strip()
    try:
        ET.fromstring(clean_svg)
    except ET.ParseError as e:
        print(f"ERROR validating {filename}: {e}")
        raise
    with open(path, "w", encoding="utf-8") as f:
        f.write(clean_svg)
    print(f"[OK] {filename} generated & validated ({len(clean_svg)} bytes)")


# ==============================================================================
# 1. BANNER.SVG (1000 x 300) — Executive Modern DFIR Hero Banner
# ==============================================================================
banner_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 300" width="1000" height="300" role="img" aria-label="Vasava Sanjeeth Solleti — Digital Forensics &amp; Incident Response Analyst at TCS">
  <defs>
    <!-- Background Canvas -->
    <linearGradient id="bg-canvas" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050811"/>
      <stop offset="40%" stop-color="#090E1D"/>
      <stop offset="100%" stop-color="#05070E"/>
    </linearGradient>

    <!-- Top Left Cyan Nebula Glow -->
    <radialGradient id="nebula-cyan" cx="12%" cy="15%" r="65%">
      <stop offset="0%" stop-color="#00D2FF" stop-opacity="0.18"/>
      <stop offset="45%" stop-color="#0284C7" stop-opacity="0.06"/>
      <stop offset="100%" stop-color="#050811" stop-opacity="0"/>
    </radialGradient>

    <!-- Bottom Right Indigo Glow -->
    <radialGradient id="nebula-indigo" cx="88%" cy="85%" r="60%">
      <stop offset="0%" stop-color="#6366F1" stop-opacity="0.18"/>
      <stop offset="50%" stop-color="#7C3AED" stop-opacity="0.05"/>
      <stop offset="100%" stop-color="#05070E" stop-opacity="0"/>
    </radialGradient>

    <!-- Outer Frame Stroke -->
    <linearGradient id="frame-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.45"/>
      <stop offset="35%" stop-color="#1E293B" stop-opacity="0.6"/>
      <stop offset="70%" stop-color="#6366F1" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#0F172A" stop-opacity="0.8"/>
    </linearGradient>

    <!-- Top Specular Highlight Line -->
    <linearGradient id="top-specular" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00D2FF" stop-opacity="0"/>
      <stop offset="15%" stop-color="#00D2FF" stop-opacity="0.9"/>
      <stop offset="50%" stop-color="#6366F1" stop-opacity="0.8"/>
      <stop offset="85%" stop-color="#A855F7" stop-opacity="0.7"/>
      <stop offset="100%" stop-color="#A855F7" stop-opacity="0"/>
    </linearGradient>

    <!-- Luminous Name Gradient -->
    <linearGradient id="name-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="60%" stop-color="#F0F9FF"/>
      <stop offset="100%" stop-color="#BAE6FD"/>
    </linearGradient>

    <!-- Glass Widget Gradient -->
    <linearGradient id="widget-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0B1325" stop-opacity="0.85"/>
      <stop offset="100%" stop-color="#080E1C" stop-opacity="0.92"/>
    </linearGradient>

    <linearGradient id="widget-stroke" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#1E3A8A" stop-opacity="0.25"/>
    </linearGradient>

    <!-- Subtle Tech Dot Grid -->
    <pattern id="dot-grid" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="0.9" fill="#334155" fill-opacity="0.25"/>
    </pattern>
  </defs>

  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    .pulse-glow { animation: pglow 2.4s ease-in-out infinite; }
    @keyframes pglow { 0%, 100% { opacity: 1; transform: scale(1); } 50% { opacity: 0.45; transform: scale(0.9); } }
  </style>

  <!-- Canvas Surface -->
  <rect width="1000" height="300" rx="16" fill="url(#bg-canvas)"/>
  <rect width="1000" height="300" rx="16" fill="url(#nebula-cyan)"/>
  <rect width="1000" height="300" rx="16" fill="url(#nebula-indigo)"/>
  <rect width="1000" height="300" rx="16" fill="url(#dot-grid)"/>
  <rect x="0.5" y="0.5" width="999" height="299" rx="16" fill="none" stroke="url(#frame-border)" stroke-width="1"/>

  <!-- Top Edge Glow Line -->
  <line x1="20" y1="1" x2="980" y2="1" stroke="url(#top-specular)" stroke-width="1.8" stroke-linecap="round"/>

  <!-- ==================== TOP TELEMETRY BAR ==================== -->
  <g transform="translate(36, 18)">
    <!-- TCS Operations Capsule (Left) -->
    <rect x="0" y="0" width="300" height="24" rx="12" fill="#0C1B33" stroke="#1D4ED8" stroke-width="0.75" stroke-opacity="0.8"/>
    <circle class="pulse-glow" cx="12" cy="12" r="3.5" fill="#10B981"/>
    <text x="24" y="16" class="font-sans" font-size="10" font-weight="700" fill="#38BDF8" letter-spacing="1">TATA CONSULTANCY SERVICES <tspan fill="#64748B" font-weight="400">|</tspan> <tspan fill="#94A3B8" font-weight="600">DFIR OPERATIONS</tspan></text>

    <!-- Cryptographic Soundness Pill (Right) - Symmetrical, Zero overlap -->
    <g transform="translate(628, 0)">
      <rect x="0" y="0" width="300" height="24" rx="12" fill="#0C1B33" stroke="#1D4ED8" stroke-width="0.75" stroke-opacity="0.8"/>
      <circle cx="12" cy="12" r="3.5" fill="#38BDF8"/>
      <text x="24" y="16" class="font-sans" font-size="9.5" font-weight="700" fill="#BAE6FD" letter-spacing="0.8">DEFENSIBLE CHAIN-OF-CUSTODY <tspan fill="#64748B" font-weight="400">|</tspan> <tspan fill="#94A3B8" font-weight="600">SHA-256</tspan></text>
    </g>
  </g>

  <!-- Horizontal Divider Line -->
  <line x1="36" y1="52" x2="964" y2="52" stroke="#1E293B" stroke-width="0.8" stroke-opacity="0.7"/>

  <!-- ==================== LEFT HERO CONTENT ==================== -->
  <g transform="translate(36, 72)">
    <!-- Eyebrow -->
    <text x="0" y="14" class="font-sans" font-size="10.5" font-weight="700" fill="#38BDF8" letter-spacing="1.6">ENTERPRISE DIGITAL FORENSICS &amp; INCIDENT RESPONSE</text>

    <!-- Name Headline -->
    <text x="0" y="52" class="font-sans" font-size="34" font-weight="800" fill="url(#name-grad)" letter-spacing="-0.5">Vasava Sanjeeth Solleti</text>

    <!-- Role / Specialty -->
    <text x="0" y="78" class="font-sans" font-size="13.5" font-weight="600" fill="#E2E8F0">
      DFIR Analyst @ TCS <tspan fill="#475569" font-weight="400">|</tspan> Windows Forensics &amp; High-Throughput Engine Architect
    </text>

    <!-- Narrative -->
    <text x="0" y="101" class="font-sans" font-size="11.5" fill="#94A3B8">
      Reconstructing complex attack chronologies across raw disk images, dirty hives, &amp; cloud collaboration stores.
    </text>

    <!-- Modern Feature Capability Pills (Cleanly spaced within 490px, leaving 130px margin before widget) -->
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

      <!-- Pill 4: Columnar Core -->
      <g transform="translate(402, 0)">
        <rect width="116" height="26" rx="8" fill="#241705" stroke="#D97706" stroke-width="0.8"/>
        <circle cx="12" cy="13" r="3" fill="#FBBF24"/>
        <text x="22" y="17" class="font-sans" font-size="10" font-weight="700" fill="#FDE68A">DuckDB Core</text>
      </g>
    </g>
  </g>

  <!-- ==================== RIGHT GLASS TERMINAL WIDGET ==================== -->
  <g transform="translate(620, 68)">
    <!-- Container -->
    <rect width="344" height="174" rx="12" fill="url(#widget-bg)" stroke="url(#widget-stroke)" stroke-width="1"/>
    
    <!-- Header Bar -->
    <rect width="344" height="30" rx="12" fill="#0F1B33" fill-opacity="0.9"/>
    <rect y="26" width="344" height="4" fill="#0F1B33" fill-opacity="0.9"/>

    <!-- Mac/Linux Terminal Dots -->
    <circle cx="16" cy="15" r="3.5" fill="#EF4444" fill-opacity="0.8"/>
    <circle cx="28" cy="15" r="3.5" fill="#F59E0B" fill-opacity="0.8"/>
    <circle cx="40" cy="15" r="3.5" fill="#10B981" fill-opacity="0.8"/>

    <text x="56" y="19" class="font-sans" font-size="10" font-weight="700" fill="#BAE6FD" letter-spacing="1.2">SPECIALIZED INVESTIGATIVE SCOPE</text>

    <!-- Scope Rows with Vector Icons -->
    <g transform="translate(16, 48)" class="font-sans" font-size="11">
      <!-- Row 1: Hard Drive / VFS -->
      <g transform="translate(0, 0)">
        <rect x="0" y="-8" width="22" height="20" rx="5" fill="#0A1F3B" stroke="#1D4ED8" stroke-width="0.6"/>
        <path d="M4 2 H18 M4 6 H18" stroke="#38BDF8" stroke-width="1.2" stroke-linecap="round"/>
        <circle cx="15" cy="0" r="1" fill="#38BDF8"/>
        <circle cx="15" cy="4" r="1" fill="#38BDF8"/>
        <text x="30" y="6" fill="#F1F5F9" font-weight="600">Native VFS Ingestion <tspan fill="#94A3B8" font-size="10" font-weight="400">(E01, RAW, VHDX, VMDK)</tspan></text>
      </g>

      <!-- Row 2: Registry / Transaction Log -->
      <g transform="translate(0, 27)">
        <rect x="0" y="-8" width="22" height="20" rx="5" fill="#0A1F3B" stroke="#1D4ED8" stroke-width="0.6"/>
        <path d="M5 -1 C5 -3 17 -3 17 -1 C17 1 5 1 5 -1 Z M5 2 C5 4 17 4 17 2 M5 5 C5 7 17 7 17 5" fill="none" stroke="#38BDF8" stroke-width="1.2"/>
        <text x="30" y="6" fill="#F1F5F9" font-weight="600">Dirty Registry Replay <tspan fill="#94A3B8" font-size="10" font-weight="400">(Automated RLA Commit)</tspan></text>
      </g>

      <!-- Row 3: Lightning Columnar Core -->
      <g transform="translate(0, 54)">
        <rect x="0" y="-8" width="22" height="20" rx="5" fill="#0A1F3B" stroke="#1D4ED8" stroke-width="0.6"/>
        <path d="M12 -4 L8 2 H13 L10 8 L15 1 H11 Z" fill="#38BDF8"/>
        <text x="30" y="6" fill="#F1F5F9" font-weight="600">Sub-Ms Super-Timelines <tspan fill="#94A3B8" font-size="10" font-weight="400">(DuckDB Engine)</tspan></text>
      </g>

      <!-- Row 4: Teams / Collab -->
      <g transform="translate(0, 81)">
        <rect x="0" y="-8" width="22" height="20" rx="5" fill="#1C0F33" stroke="#7C3AED" stroke-width="0.6"/>
        <path d="M5 -1 H17 V6 H11 L7 9 V6 H5 Z" fill="none" stroke="#C084FC" stroke-width="1.2"/>
        <text x="30" y="6" fill="#F1F5F9" font-weight="600">Collab Forensics <tspan fill="#C084FC" font-size="10" font-weight="400">(Teams Level/IndexedDB)</tspan></text>
      </g>
    </g>
  </g>

  <!-- ==================== BOTTOM TELEMETRY FOOTER ==================== -->
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
# 2. STATS.SVG (1000 x 106) — High-End Operational Telemetry HUD
# ==============================================================================
stats_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 106" width="1000" height="106" role="img" aria-label="Operational Telemetry HUD: TCS Operations, WFT Platform, MSTeams_Parser, Defensible Evidence Integrity">
  <defs>
    <linearGradient id="hud-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050811"/>
      <stop offset="50%" stop-color="#090E1D"/>
      <stop offset="100%" stop-color="#05070E"/>
    </linearGradient>
    <linearGradient id="hud-border" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.4"/>
      <stop offset="35%" stop-color="#818CF8" stop-opacity="0.3"/>
      <stop offset="70%" stop-color="#C084FC" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#34D399" stop-opacity="0.4"/>
    </linearGradient>
    <linearGradient id="val-cyan" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#BAE6FD"/>
    </linearGradient>
    <linearGradient id="val-blue" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#93C5FD"/>
    </linearGradient>
    <linearGradient id="val-purple" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#E9D5FF"/>
    </linearGradient>
    <linearGradient id="val-emerald" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#A7F3D0"/>
    </linearGradient>
  </defs>

  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    .hud-tag { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 9.5px; font-weight: 700; letter-spacing: 1.2px; }
    .hud-val { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 19px; font-weight: 800; letter-spacing: -0.3px; }
    .hud-sub { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 10.5px; fill: #94A3B8; font-weight: 500; }
  </style>

  <!-- Frame Background -->
  <rect width="1000" height="106" rx="14" fill="url(#hud-bg)"/>
  <rect x="0.5" y="0.5" width="999" height="105" rx="14" fill="none" stroke="url(#hud-border)" stroke-width="1"/>

  <!-- Module 1: Enterprise DFIR (Center x=125) -->
  <g transform="translate(125, 0)">
    <rect x="-64" y="14" width="128" height="18" rx="9" fill="#0C203E" stroke="#1D4ED8" stroke-width="0.6"/>
    <text x="0" y="26.5" text-anchor="middle" class="hud-tag" fill="#38BDF8">ENTERPRISE DFIR</text>
    <text x="0" y="58" text-anchor="middle" class="hud-val" fill="url(#val-cyan)">TCS OPERATIONS</text>
    <text x="0" y="80" text-anchor="middle" class="hud-sub">Host &amp; Endpoint Incident Response</text>
  </g>

  <!-- Divider 1 -->
  <line x1="250" y1="20" x2="250" y2="86" stroke="#1E293B" stroke-width="1"/>
  <circle cx="250" cy="53" r="2.5" fill="#38BDF8" fill-opacity="0.7"/>

  <!-- Module 2: WFT Host Forensics (Center x=375) -->
  <g transform="translate(375, 0)">
    <rect x="-82" y="14" width="164" height="18" rx="9" fill="#0C203E" stroke="#1D4ED8" stroke-width="0.6"/>
    <text x="0" y="26.5" text-anchor="middle" class="hud-tag" fill="#60A5FA">HOST FORENSICS WORKSTATION</text>
    <text x="0" y="58" text-anchor="middle" class="hud-val" fill="url(#val-blue)">500,000+ RECORDS</text>
    <text x="0" y="80" text-anchor="middle" class="hud-sub">WFT &#x2022; Zero-Copy DuckDB Super-Timeline</text>
  </g>

  <!-- Divider 2 -->
  <line x1="500" y1="20" x2="500" y2="86" stroke="#1E293B" stroke-width="1"/>
  <circle cx="500" cy="53" r="2.5" fill="#818CF8" fill-opacity="0.7"/>

  <!-- Module 3: MSTeams Collaboration (Center x=625) -->
  <g transform="translate(625, 0)">
    <rect x="-72" y="14" width="144" height="18" rx="9" fill="#24103C" stroke="#7C3AED" stroke-width="0.6"/>
    <text x="0" y="26.5" text-anchor="middle" class="hud-tag" fill="#C084FC">COLLABORATION SUITE</text>
    <text x="0" y="58" text-anchor="middle" class="hud-val" fill="url(#val-purple)">AIR-GAPPED 127.0.0.1</text>
    <text x="0" y="80" text-anchor="middle" class="hud-sub">MSTeams &#x2022; IndexedDB &amp; LevelDB Recovery</text>
  </g>

  <!-- Divider 3 -->
  <line x1="750" y1="20" x2="750" y2="86" stroke="#1E293B" stroke-width="1"/>
  <circle cx="750" cy="53" r="2.5" fill="#C084FC" fill-opacity="0.7"/>

  <!-- Module 4: Defensible Integrity (Center x=875) -->
  <g transform="translate(875, 0)">
    <rect x="-68" y="14" width="136" height="18" rx="9" fill="#08201A" stroke="#059669" stroke-width="0.6"/>
    <text x="0" y="26.5" text-anchor="middle" class="hud-tag" fill="#34D399">EVIDENCE INTEGRITY</text>
    <text x="0" y="58" text-anchor="middle" class="hud-val" fill="url(#val-emerald)">DETERMINISTIC</text>
    <text x="0" y="80" text-anchor="middle" class="hud-sub">RLA Log Replay &#x2022; SHA-256 Defensible Hashes</text>
  </g>
</svg>"""


# ==============================================================================
# 3. ACTION BUTTONS (195 x 42 each) — Sleek Modern Hardware-Grade Glass Pills
# ==============================================================================

# Button: LinkedIn
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

  <!-- LinkedIn Vector Icon -->
  <g transform="translate(14, 11)">
    <rect width="20" height="20" rx="4" fill="#0A66C2"/>
    <circle cx="6" cy="6" r="1.5" fill="#FFFFFF"/>
    <rect x="4.5" y="9" width="3" height="7" fill="#FFFFFF"/>
    <path d="M10 9 H12.8 V10.2 C13.3 9.4 14.2 9 15.3 9 C17.4 9 18.2 10.3 18.2 12.4 V16 H15.4 V12.8 C15.4 11.8 15 11.2 14.1 11.2 C13.3 11.2 12.8 11.7 12.8 12.6 V16 H10 Z" fill="#FFFFFF"/>
  </g>

  <text x="44" y="26" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="700" fill="#F1F5F9" letter-spacing="1">LINKEDIN</text>
  
  <!-- Sleek Vector Arrow -->
  <path d="M174 24 L179 19 M179 19 H175 M179 19 V23" stroke="#38BDF8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
</svg>"""

# Button: Email
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

  <!-- Email Vector Icon -->
  <g transform="translate(14, 11)">
    <rect width="20" height="20" rx="4" fill="#065F46"/>
    <path d="M3.5 5.5 H16.5 V14.5 H3.5 Z" fill="none" stroke="#6EE7B7" stroke-width="1.3"/>
    <path d="M4 6.5 L10 11 L16 6.5" fill="none" stroke="#6EE7B7" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/>
  </g>

  <text x="44" y="26" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="700" fill="#F1F5F9" letter-spacing="1">EMAIL CONTACT</text>

  <path d="M174 24 L179 19 M179 19 H175 M179 19 V23" stroke="#34D399" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
</svg>"""

# Button: Repositories
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

  <!-- Repo Folder Vector Icon -->
  <g transform="translate(14, 11)">
    <rect width="20" height="20" rx="4" fill="#312E81"/>
    <path d="M4 6 H8.5 L10.5 8 H16 V14.5 H4 Z" fill="none" stroke="#A5B4FC" stroke-width="1.3" stroke-linejoin="round"/>
  </g>

  <text x="44" y="26" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="700" fill="#F1F5F9" letter-spacing="1">REPOSITORIES</text>

  <path d="M174 24 L179 19 M179 19 H175 M179 19 V23" stroke="#818CF8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
</svg>"""

# Button: CEH Certified
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

  <!-- Shield Vector Icon -->
  <g transform="translate(14, 11)">
    <rect width="20" height="20" rx="4" fill="#581C87"/>
    <path d="M10 4 L15.5 6.5 V10.5 C15.5 13.5 10 16 10 16 C10 16 4.5 13.5 4.5 10.5 V6.5 Z" fill="none" stroke="#D8B4FE" stroke-width="1.3"/>
    <path d="M8 10 L9.5 11.5 L12.5 8" fill="none" stroke="#D8B4FE" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
  </g>

  <text x="44" y="26" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="700" fill="#F1F5F9" letter-spacing="1">CEH CERTIFIED</text>

  <!-- Verified Checkmark -->
  <path d="M174 21 L177 24 L182 18" stroke="#C084FC" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
</svg>"""


# ==============================================================================
# 4. FLAGSHIP TOOL CARDS (485 x 285 each) — Strictly Sanjeeth's 2 Real Tools
# ==============================================================================

# Card 1: WFT (Windows Forensic Examination Platform)
card_wft = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 485 285" width="485" height="285" role="img" aria-label="WFT — Windows Forensic Examination Platform">
  <defs>
    <linearGradient id="wft-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#060A16"/>
      <stop offset="50%" stop-color="#0A1326"/>
      <stop offset="100%" stop-color="#050811"/>
    </linearGradient>
    <radialGradient id="wft-glow" cx="15%" cy="15%" r="65%">
      <stop offset="0%" stop-color="#00D2FF" stop-opacity="0.16"/>
      <stop offset="60%" stop-color="#1D4ED8" stop-opacity="0.04"/>
      <stop offset="100%" stop-color="#060A16" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="wft-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.5"/>
      <stop offset="50%" stop-color="#1E3A8A" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#1E293B" stop-opacity="0.4"/>
    </linearGradient>
    <linearGradient id="wft-title-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#93C5FD"/>
    </linearGradient>
  </defs>

  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    .pulse-wft { animation: pwft 2.4s ease-in-out infinite; }
    @keyframes pwft { 0%,100% { opacity: 1; } 50% { opacity: 0.4; } }
  </style>

  <!-- Frame Background -->
  <rect width="485" height="285" rx="14" fill="url(#wft-bg)"/>
  <rect width="485" height="285" rx="14" fill="url(#wft-glow)"/>
  <rect x="0.5" y="0.5" width="484" height="284" rx="14" fill="none" stroke="url(#wft-border)" stroke-width="1"/>

  <!-- Top Specular Highlight Accent -->
  <line x1="16" y1="1" x2="469" y2="1" stroke="#38BDF8" stroke-width="1.8" stroke-linecap="round"/>

  <!-- Header Status Bar -->
  <g transform="translate(24, 20)">
    <circle class="pulse-wft" cx="4" cy="5" r="3.5" fill="#00D2FF"/>
    <text x="14" y="9" class="font-sans" font-size="10" font-weight="700" fill="#38BDF8" letter-spacing="1.4">FLAGSHIP DFIR WORKSTATION</text>
    
    <!-- Version Tag -->
    <rect x="345" y="-3" width="92" height="20" rx="6" fill="#0C203E" stroke="#1D4ED8" stroke-width="0.8"/>
    <text x="391" y="11" text-anchor="middle" class="font-sans" font-size="9" font-weight="700" fill="#93C5FD">v1.0 ACTIVE</text>
  </g>

  <!-- Title & Subtitle -->
  <text x="24" y="66" class="font-sans" font-size="20" font-weight="800" fill="url(#wft-title-grad)">WFT — Windows Forensics</text>
  <text x="24" y="85" class="font-sans" font-size="11.5" font-weight="500" fill="#94A3B8">Enterprise "Process + Examine" Digital Forensics Platform</text>

  <!-- Telemetry Pipeline Preview Capsule -->
  <g transform="translate(24, 98)">
    <rect width="437" height="22" rx="6" fill="#08172E" stroke="#1E3A8A" stroke-width="0.75"/>
    <text x="10" y="15" class="font-sans" font-size="9" font-weight="700" fill="#38BDF8">PIPELINE:</text>
    <text x="64" y="15" class="font-sans" font-size="9" fill="#94A3B8">
      dissect.target VFS <tspan fill="#38BDF8">&#x2192;</tspan> Dirty RLA Commit <tspan fill="#38BDF8">&#x2192;</tspan> DuckDB Columnar <tspan fill="#38BDF8">&#x2192;</tspan> Cytoscape
    </text>
  </g>

  <!-- Core Highlights with Bespoke Micro-Icons -->
  <g class="font-sans" font-size="11" fill="#E2E8F0" transform="translate(24, 138)">
    <!-- Point 1: DuckDB Lightning Bolt -->
    <g transform="translate(0, 0)">
      <rect x="0" y="-9" width="16" height="16" rx="4" fill="#0A2244" stroke="#0284C7" stroke-width="0.6"/>
      <path d="M9 -7 L5 -2 H9 L7 4 L12 -1 H8 Z" fill="#38BDF8"/>
      <text x="24" y="3"><tspan font-weight="700" fill="#FFFFFF">DuckDB Columnar Core:</tspan> <tspan fill="#CBD5E1">Sub-ms unpivoted super-timeline (500K+ records)</tspan></text>
    </g>
    <!-- Point 2: Dirty Registry Replay Refresh Icon -->
    <g transform="translate(0, 21)">
      <rect x="0" y="-9" width="16" height="16" rx="4" fill="#0A2244" stroke="#0284C7" stroke-width="0.6"/>
      <path d="M5 -1 A4 4 0 1 1 11 -1" fill="none" stroke="#38BDF8" stroke-width="1.2"/>
      <path d="M11 -3 L11 -1 L9 -1" fill="none" stroke="#38BDF8" stroke-width="1.2" stroke-linecap="round"/>
      <text x="24" y="3"><tspan font-weight="700" fill="#FFFFFF">Dirty Registry Replay:</tspan> <tspan fill="#CBD5E1">Automated RLA commit for volatile .LOG1/.LOG2</tspan></text>
    </g>
    <!-- Point 3: VFS Intake Disk Icon -->
    <g transform="translate(0, 42)">
      <rect x="0" y="-9" width="16" height="16" rx="4" fill="#0A2244" stroke="#0284C7" stroke-width="0.6"/>
      <path d="M3 -4 H13 V2 H3 Z" fill="none" stroke="#38BDF8" stroke-width="1.1"/>
      <line x1="3" y1="-1" x2="13" y2="-1" stroke="#38BDF8" stroke-width="0.8"/>
      <circle cx="10.5" cy="0.5" r="0.6" fill="#38BDF8"/>
      <text x="24" y="3"><tspan font-weight="700" fill="#FFFFFF">Native VFS Intake:</tspan> <tspan fill="#CBD5E1">Direct E01, RAW, VHDX, VMDK mount via dissect</tspan></text>
    </g>
    <!-- Point 4: Threat Hunting Crosshair -->
    <g transform="translate(0, 63)">
      <rect x="0" y="-9" width="16" height="16" rx="4" fill="#0A2244" stroke="#0284C7" stroke-width="0.6"/>
      <circle cx="8" cy="-1" r="4.5" fill="none" stroke="#38BDF8" stroke-width="1"/>
      <line x1="8" y1="-7" x2="8" y2="5" stroke="#38BDF8" stroke-width="0.8"/>
      <line x1="2" y1="-1" x2="14" y2="-1" stroke="#38BDF8" stroke-width="0.8"/>
      <text x="24" y="3"><tspan font-weight="700" fill="#FFFFFF">Threat Hunting &amp; Carving:</tspan> <tspan fill="#CBD5E1">Rust YARA-X scanning + RapidOCR triage</tspan></text>
    </g>
  </g>

  <!-- Divider before pills -->
  <line x1="24" y1="216" x2="461" y2="216" stroke="#1E293B" stroke-width="0.8"/>

  <!-- Tech Stack Chips -->
  <g transform="translate(24, 226)">
    <rect x="0" y="0" width="64" height="22" rx="6" fill="#0C203E" stroke="#1D4ED8" stroke-width="0.6"/>
    <text x="32" y="15" text-anchor="middle" class="font-sans" font-size="9.5" font-weight="600" fill="#93C5FD">DuckDB</text>

    <rect x="70" y="0" width="60" height="22" rx="6" fill="#0C203E" stroke="#1D4ED8" stroke-width="0.6"/>
    <text x="100" y="15" text-anchor="middle" class="font-sans" font-size="9.5" font-weight="600" fill="#93C5FD">FastAPI</text>

    <rect x="136" y="0" width="66" height="22" rx="6" fill="#0C203E" stroke="#1D4ED8" stroke-width="0.6"/>
    <text x="169" y="15" text-anchor="middle" class="font-sans" font-size="9.5" font-weight="600" fill="#93C5FD">React 18</text>

    <rect x="208" y="0" width="72" height="22" rx="6" fill="#0C203E" stroke="#1D4ED8" stroke-width="0.6"/>
    <text x="244" y="15" text-anchor="middle" class="font-sans" font-size="9.5" font-weight="600" fill="#93C5FD">Cytoscape</text>

    <rect x="286" y="0" width="62" height="22" rx="6" fill="#0C203E" stroke="#1D4ED8" stroke-width="0.6"/>
    <text x="317" y="15" text-anchor="middle" class="font-sans" font-size="9.5" font-weight="600" fill="#93C5FD">YARA-X</text>

    <rect x="354" y="0" width="64" height="22" rx="6" fill="#0C203E" stroke="#1D4ED8" stroke-width="0.6"/>
    <text x="386" y="15" text-anchor="middle" class="font-sans" font-size="9.5" font-weight="600" fill="#93C5FD">AG Grid</text>
  </g>

  <!-- Bottom Link Bar -->
  <g transform="translate(24, 269)">
    <text x="0" y="0" font-family="'SFMono-Regular', Consolas, monospace" font-size="10" fill="#64748B">github.com/sanjeeth-solleti/WFT</text>
    <text x="437" y="0" text-anchor="end" class="font-sans" font-size="11" font-weight="700" fill="#38BDF8">Explore Repository &#x2192;</text>
  </g>
</svg>"""

# Card 2: MSTeams_Parser (Microsoft Teams DFIR Forensic Suite)
card_msteams = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 485 285" width="485" height="285" role="img" aria-label="MSTeams_Parser — Microsoft Teams DFIR Forensic Suite">
  <defs>
    <linearGradient id="ms-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0E081D"/>
      <stop offset="50%" stop-color="#150D2B"/>
      <stop offset="100%" stop-color="#090514"/>
    </linearGradient>
    <radialGradient id="ms-glow" cx="15%" cy="15%" r="65%">
      <stop offset="0%" stop-color="#A855F7" stop-opacity="0.18"/>
      <stop offset="60%" stop-color="#6B21A8" stop-opacity="0.04"/>
      <stop offset="100%" stop-color="#0E081D" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="ms-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#C084FC" stop-opacity="0.5"/>
      <stop offset="50%" stop-color="#7C3AED" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#1E293B" stop-opacity="0.4"/>
    </linearGradient>
    <linearGradient id="ms-title-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#E9D5FF"/>
    </linearGradient>
  </defs>

  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    .pulse-ms { animation: pms 2.4s ease-in-out infinite; }
    @keyframes pms { 0%,100% { opacity: 1; } 50% { opacity: 0.4; } }
  </style>

  <!-- Frame Background -->
  <rect width="485" height="285" rx="14" fill="url(#ms-bg)"/>
  <rect width="485" height="285" rx="14" fill="url(#ms-glow)"/>
  <rect x="0.5" y="0.5" width="484" height="284" rx="14" fill="none" stroke="url(#ms-border)" stroke-width="1"/>

  <!-- Top Specular Highlight Accent -->
  <line x1="16" y1="1" x2="469" y2="1" stroke="#A855F7" stroke-width="1.8" stroke-linecap="round"/>

  <!-- Header Status Bar -->
  <g transform="translate(24, 20)">
    <circle class="pulse-ms" cx="4" cy="5" r="3.5" fill="#A855F7"/>
    <text x="14" y="9" class="font-sans" font-size="10" font-weight="700" fill="#C084FC" letter-spacing="1.4">COLLABORATION DFIR SUITE</text>
    
    <!-- Air-gapped badge -->
    <rect x="317" y="-3" width="120" height="20" rx="6" fill="#291142" stroke="#7C3AED" stroke-width="0.8"/>
    <text x="377" y="11" text-anchor="middle" class="font-sans" font-size="9" font-weight="700" fill="#E9D5FF">AIR-GAPPED 127.0.0.1</text>
  </g>

  <!-- Title & Subtitle -->
  <text x="24" y="66" class="font-sans" font-size="20" font-weight="800" fill="url(#ms-title-grad)">MSTeams_Parser</text>
  <text x="24" y="85" class="font-sans" font-size="11.5" font-weight="500" fill="#94A3B8">Standalone Microsoft Teams DFIR Forensic Suite</text>

  <!-- Telemetry Pipeline Preview Capsule -->
  <g transform="translate(24, 98)">
    <rect width="437" height="22" rx="6" fill="#201138" stroke="#4C1D95" stroke-width="0.75"/>
    <text x="10" y="15" class="font-sans" font-size="9" font-weight="700" fill="#C084FC">PIPELINE:</text>
    <text x="64" y="15" class="font-sans" font-size="9" fill="#94A3B8">
      IndexedDB/LevelDB <tspan fill="#C084FC">&#x2192;</tspan> Base64 Decode <tspan fill="#C084FC">&#x2192;</tspan> 8:orgid Resolve <tspan fill="#C084FC">&#x2192;</tspan> HTML Dossier
    </text>
  </g>

  <!-- Core Highlights with Bespoke Micro-Icons -->
  <g class="font-sans" font-size="11" fill="#E2E8F0" transform="translate(24, 138)">
    <!-- Point 1: Multi-Source Package Box -->
    <g transform="translate(0, 0)">
      <rect x="0" y="-9" width="16" height="16" rx="4" fill="#281144" stroke="#7C3AED" stroke-width="0.6"/>
      <path d="M4 -5 L8 -7 L12 -5 L8 -3 Z" fill="none" stroke="#C084FC" stroke-width="1"/>
      <path d="M4 -5 V1 L8 3 V-3 M12 -5 V1 L8 3" fill="none" stroke="#C084FC" stroke-width="1"/>
      <text x="24" y="3"><tspan font-weight="700" fill="#FFFFFF">Multi-Source Ingestion:</tspan> <tspan fill="#CBD5E1">Decodes New &amp; Classic IndexedDB &amp; LevelDB</tspan></text>
    </g>
    <!-- Point 2: Normalization Code/Doc Icon -->
    <g transform="translate(0, 21)">
      <rect x="0" y="-9" width="16" height="16" rx="4" fill="#281144" stroke="#7C3AED" stroke-width="0.6"/>
      <path d="M4 -6 H10 L12 -4 V4 H4 Z" fill="none" stroke="#C084FC" stroke-width="1"/>
      <line x1="6" y1="-2" x2="10" y2="-2" stroke="#C084FC" stroke-width="0.8"/>
      <line x1="6" y1="1" x2="10" y2="1" stroke="#C084FC" stroke-width="0.8"/>
      <text x="24" y="3"><tspan font-weight="700" fill="#FFFFFF">Deep Normalization:</tspan> <tspan fill="#CBD5E1">Base64 Adaptive Cards, call logs &amp; meeting events</tspan></text>
    </g>
    <!-- Point 3: Identity User Icon -->
    <g transform="translate(0, 42)">
      <rect x="0" y="-9" width="16" height="16" rx="4" fill="#281144" stroke="#7C3AED" stroke-width="0.6"/>
      <circle cx="8" cy="-4" r="2.2" fill="none" stroke="#C084FC" stroke-width="1"/>
      <path d="M4 3 C4 0.5 6 0 8 0 C10 0 12 0.5 12 3" fill="none" stroke="#C084FC" stroke-width="1"/>
      <text x="24" y="3"><tspan font-weight="700" fill="#FFFFFF">Identity Correlator:</tspan> <tspan fill="#CBD5E1">Resolves 8:orgid GUIDs to corporate records</tspan></text>
    </g>
    <!-- Point 4: Media Carver Photo Icon -->
    <g transform="translate(0, 63)">
      <rect x="0" y="-9" width="16" height="16" rx="4" fill="#281144" stroke="#7C3AED" stroke-width="0.6"/>
      <rect x="3" y="-5" width="10" height="8" rx="1" fill="none" stroke="#C084FC" stroke-width="1"/>
      <circle cx="6" cy="-2.5" r="0.8" fill="#C084FC"/>
      <path d="M4 2 L7 -1 L9 1 L11 -1 L13 2" fill="none" stroke="#C084FC" stroke-width="0.9"/>
      <text x="24" y="3"><tspan font-weight="700" fill="#FFFFFF">Forensic Media Carver:</tspan> <tspan fill="#CBD5E1">Magic-byte image recovery &amp; noise suppression</tspan></text>
    </g>
  </g>

  <!-- Divider before pills -->
  <line x1="24" y1="216" x2="461" y2="216" stroke="#25163D" stroke-width="0.8"/>

  <!-- Tech Stack Chips -->
  <g transform="translate(24, 226)">
    <rect x="0" y="0" width="64" height="22" rx="6" fill="#24103C" stroke="#7C3AED" stroke-width="0.6"/>
    <text x="32" y="15" text-anchor="middle" class="font-sans" font-size="9.5" font-weight="600" fill="#E9D5FF">LevelDB</text>

    <rect x="70" y="0" width="74" height="22" rx="6" fill="#24103C" stroke="#7C3AED" stroke-width="0.6"/>
    <text x="107" y="15" text-anchor="middle" class="font-sans" font-size="9.5" font-weight="600" fill="#E9D5FF">IndexedDB</text>

    <rect x="150" y="0" width="86" height="22" rx="6" fill="#24103C" stroke="#7C3AED" stroke-width="0.6"/>
    <text x="193" y="15" text-anchor="middle" class="font-sans" font-size="9.5" font-weight="600" fill="#E9D5FF">dfindexeddb</text>

    <rect x="242" y="0" width="70" height="22" rx="6" fill="#24103C" stroke="#7C3AED" stroke-width="0.6"/>
    <text x="277" y="15" text-anchor="middle" class="font-sans" font-size="9.5" font-weight="600" fill="#E9D5FF">cramjam</text>

    <rect x="318" y="0" width="88" height="22" rx="6" fill="#24103C" stroke="#7C3AED" stroke-width="0.6"/>
    <text x="362" y="15" text-anchor="middle" class="font-sans" font-size="9.5" font-weight="600" fill="#E9D5FF">HTML Viewer</text>
  </g>

  <!-- Bottom Link Bar -->
  <g transform="translate(24, 269)">
    <text x="0" y="0" font-family="'SFMono-Regular', Consolas, monospace" font-size="10" fill="#64748B">github.com/sanjeeth-solleti/MSTeams_Parser</text>
    <text x="437" y="0" text-anchor="end" class="font-sans" font-size="11" font-weight="700" fill="#C084FC">Explore Repository &#x2192;</text>
  </g>
</svg>"""


# ==============================================================================
# 5. MAP.SVG (1000 x 340) — Contemporary DFIR Architecture Pipeline Schematic
# ==============================================================================
map_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 340" width="1000" height="340" role="img" aria-label="DFIR Dual-Engine Forensic Pipeline Architecture: WFT Platform and MSTeams_Parser Synthesis">
  <defs>
    <!-- Background Gradient -->
    <linearGradient id="map-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050811"/>
      <stop offset="50%" stop-color="#080E1C"/>
      <stop offset="100%" stop-color="#05070E"/>
    </linearGradient>

    <!-- Outer Border Stroke -->
    <linearGradient id="map-border" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.35"/>
      <stop offset="50%" stop-color="#818CF8" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#10B981" stop-opacity="0.35"/>
    </linearGradient>

    <!-- Arrow Cyan Gradient -->
    <linearGradient id="arrow-cyan" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#38BDF8" stop-opacity="1"/>
    </linearGradient>

    <!-- Arrow Purple Gradient -->
    <linearGradient id="arrow-purple" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#A855F7" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#A855F7" stop-opacity="1"/>
    </linearGradient>

    <!-- Dossier Frame Gradient -->
    <linearGradient id="dossier-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10B981" stop-opacity="0.6"/>
      <stop offset="50%" stop-color="#059669" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#1E293B" stop-opacity="0.5"/>
    </linearGradient>
  </defs>

  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    .pulse-dot-c { animation: pcyan 2s ease-in-out infinite; }
    .pulse-dot-p { animation: ppurple 2s ease-in-out infinite; }
    @keyframes pcyan { 0%,100% { opacity: 1; } 50% { opacity: 0.35; } }
    @keyframes ppurple { 0%,100% { opacity: 1; } 50% { opacity: 0.35; } }
  </style>

  <!-- Canvas Frame -->
  <rect width="1000" height="340" rx="16" fill="url(#map-bg)"/>
  <rect x="0.5" y="0.5" width="999" height="339" rx="16" fill="none" stroke="url(#map-border)" stroke-width="1"/>

  <!-- Architecture Header Bar -->
  <g transform="translate(36, 24)">
    <text x="0" y="10" class="font-sans" font-size="11" font-weight="700" fill="#38BDF8" letter-spacing="1.2">DFIR DUAL-ENGINE ARCHITECTURE <tspan fill="#475569" font-weight="400">//</tspan> <tspan fill="#94A3B8" font-weight="600">DETERMINISTIC INGESTION &#x2022; DIRTY HIVE REPLAY &#x2022; DEFENSIBLE SYNTHESIS</tspan></text>
    <text x="928" y="10" text-anchor="end" class="font-sans" font-size="10.5" font-weight="600" fill="#94A3B8">TCS FORENSIC OPERATIONS</text>
  </g>
  <line x1="36" y1="46" x2="964" y2="46" stroke="#1E293B" stroke-width="0.8"/>

  <!-- ==================== TRACK 1: HOST & ENDPOINT FORENSICS (WFT) ==================== -->
  <g transform="translate(36, 62)">
    <!-- Track Header Chip -->
    <rect x="0" y="0" width="270" height="22" rx="6" fill="#0C203E" stroke="#1D4ED8" stroke-width="0.8"/>
    <circle class="pulse-dot-c" cx="12" cy="11" r="3" fill="#38BDF8"/>
    <text x="24" y="15" class="font-sans" font-size="9.5" font-weight="700" fill="#BAE6FD" letter-spacing="1">TRACK 1: HOST &amp; DISK FORENSICS (WFT)</text>

    <!-- Stage 1.1: Evidence Intake -->
    <g transform="translate(0, 32)">
      <rect width="190" height="80" rx="10" fill="#0A152A" stroke="#1E3A8A" stroke-width="0.9"/>
      <rect x="12" y="10" width="56" height="14" rx="4" fill="#0C264D"/>
      <text x="40" y="20.5" text-anchor="middle" class="font-sans" font-size="8" font-weight="700" fill="#38BDF8">STAGE 01</text>
      <text x="95" y="37" text-anchor="middle" class="font-sans" font-size="11.5" font-weight="700" fill="#FFFFFF">Disk Evidence Intake</text>
      <text x="95" y="53" text-anchor="middle" class="font-sans" font-size="10" fill="#94A3B8">E01, RAW, VHDX, VMDK</text>
      <text x="95" y="69" text-anchor="middle" class="font-sans" font-size="9.5" font-weight="600" fill="#38BDF8">Native Dissect VFS Mount</text>
    </g>

    <!-- Flow Connector 1 -> 2 -->
    <path d="M190 72 H228" stroke="url(#arrow-cyan)" stroke-width="1.8"/>
    <polygon points="230,72 223,68.5 223,75.5" fill="#38BDF8"/>

    <!-- Stage 1.2: Dirty Registry Replay -->
    <g transform="translate(232, 32)">
      <rect width="190" height="80" rx="10" fill="#0A152A" stroke="#1E3A8A" stroke-width="0.9"/>
      <rect x="12" y="10" width="56" height="14" rx="4" fill="#0C264D"/>
      <text x="40" y="20.5" text-anchor="middle" class="font-sans" font-size="8" font-weight="700" fill="#38BDF8">STAGE 02</text>
      <text x="95" y="37" text-anchor="middle" class="font-sans" font-size="11.5" font-weight="700" fill="#FFFFFF">Registry Integrity</text>
      <text x="95" y="53" text-anchor="middle" class="font-sans" font-size="10" fill="#94A3B8">RLA .LOG1/.LOG2 Replay</text>
      <text x="95" y="69" text-anchor="middle" class="font-sans" font-size="9.5" font-weight="600" fill="#38BDF8">Transaction Log Commit</text>
    </g>

    <!-- Flow Connector 2 -> 3 -->
    <path d="M422 72 H460" stroke="url(#arrow-cyan)" stroke-width="1.8"/>
    <polygon points="462,72 455,68.5 455,75.5" fill="#38BDF8"/>

    <!-- Stage 1.3: Super-Timeline & Triage Engine -->
    <g transform="translate(464, 32)">
      <rect width="190" height="80" rx="10" fill="#0F2447" stroke="#2563EB" stroke-width="1.2"/>
      <rect x="12" y="10" width="56" height="14" rx="4" fill="#153366"/>
      <text x="40" y="20.5" text-anchor="middle" class="font-sans" font-size="8" font-weight="700" fill="#60A5FA">STAGE 03</text>
      <text x="95" y="37" text-anchor="middle" class="font-sans" font-size="11.5" font-weight="800" fill="#38BDF8">WFT Analytic Core</text>
      <text x="95" y="53" text-anchor="middle" class="font-sans" font-size="10" font-weight="600" fill="#FFFFFF">DuckDB Columnar Core</text>
      <text x="95" y="69" text-anchor="middle" class="font-sans" font-size="9.5" font-weight="600" fill="#93C5FD">Sub-Ms Timeline &#x2022; YARA-X</text>
    </g>

    <!-- Connector Track 1 -> Dossier -->
    <path d="M654 72 H730" stroke="url(#arrow-cyan)" stroke-width="1.8"/>
    <polygon points="732,72 724,68.5 724,75.5" fill="#38BDF8"/>
  </g>

  <!-- ==================== TRACK 2: COLLABORATION FORENSICS (MSTEAMS) ==================== -->
  <g transform="translate(36, 192)">
    <!-- Track Header Chip -->
    <rect x="0" y="0" width="290" height="22" rx="6" fill="#1C1138" stroke="#7C3AED" stroke-width="0.8"/>
    <circle class="pulse-dot-p" cx="12" cy="11" r="3" fill="#C084FC"/>
    <text x="24" y="15" class="font-sans" font-size="9.5" font-weight="700" fill="#E9D5FF" letter-spacing="1">TRACK 2: COLLABORATION FORENSICS (MSTEAMS)</text>

    <!-- Stage 2.1: Store Ingestion -->
    <g transform="translate(0, 32)">
      <rect width="190" height="80" rx="10" fill="#140D26" stroke="#4C1D95" stroke-width="0.9"/>
      <rect x="12" y="10" width="56" height="14" rx="4" fill="#29124A"/>
      <text x="40" y="20.5" text-anchor="middle" class="font-sans" font-size="8" font-weight="700" fill="#C084FC">STAGE 01</text>
      <text x="95" y="37" text-anchor="middle" class="font-sans" font-size="11.5" font-weight="700" fill="#FFFFFF">Messaging Intake</text>
      <text x="95" y="53" text-anchor="middle" class="font-sans" font-size="10" fill="#94A3B8">IndexedDB &amp; LevelDB Stores</text>
      <text x="95" y="69" text-anchor="middle" class="font-sans" font-size="9.5" font-weight="600" fill="#C084FC">New &amp; Classic Teams Cache</text>
    </g>

    <!-- Flow Connector 1 -> 2 -->
    <path d="M190 72 H228" stroke="url(#arrow-purple)" stroke-width="1.8"/>
    <polygon points="230,72 223,68.5 223,75.5" fill="#A855F7"/>

    <!-- Stage 2.2: Payload Normalization -->
    <g transform="translate(232, 32)">
      <rect width="190" height="80" rx="10" fill="#140D26" stroke="#4C1D95" stroke-width="0.9"/>
      <rect x="12" y="10" width="56" height="14" rx="4" fill="#29124A"/>
      <text x="40" y="20.5" text-anchor="middle" class="font-sans" font-size="8" font-weight="700" fill="#C084FC">STAGE 02</text>
      <text x="95" y="37" text-anchor="middle" class="font-sans" font-size="11.5" font-weight="700" fill="#FFFFFF">Event Normalization</text>
      <text x="95" y="53" text-anchor="middle" class="font-sans" font-size="10" fill="#94A3B8">Base64 Adaptive Cards &amp; Calls</text>
      <text x="95" y="69" text-anchor="middle" class="font-sans" font-size="9.5" font-weight="600" fill="#C084FC">8:orgid GUID &#x2192; Directory Name</text>
    </g>

    <!-- Flow Connector 2 -> 3 -->
    <path d="M422 72 H460" stroke="url(#arrow-purple)" stroke-width="1.8"/>
    <polygon points="462,72 455,68.5 455,75.5" fill="#A855F7"/>

    <!-- Stage 2.3: MSTeams Engine & Carve -->
    <g transform="translate(464, 32)">
      <rect width="190" height="80" rx="10" fill="#2E1254" stroke="#7C3AED" stroke-width="1.2"/>
      <rect x="12" y="10" width="56" height="14" rx="4" fill="#44177A"/>
      <text x="40" y="20.5" text-anchor="middle" class="font-sans" font-size="8" font-weight="700" fill="#E9D5FF">STAGE 03</text>
      <text x="95" y="37" text-anchor="middle" class="font-sans" font-size="11.5" font-weight="800" fill="#C084FC">MSTeams Parser</text>
      <text x="95" y="53" text-anchor="middle" class="font-sans" font-size="10" font-weight="600" fill="#FFFFFF">Air-Gapped 127.0.0.1</text>
      <text x="95" y="69" text-anchor="middle" class="font-sans" font-size="9.5" font-weight="600" fill="#E9D5FF">Magic-Byte Media Carving</text>
    </g>

    <!-- Connector Track 2 -> Dossier -->
    <path d="M654 72 H730" stroke="url(#arrow-purple)" stroke-width="1.8"/>
    <polygon points="732,72 724,68.5 724,75.5" fill="#A855F7"/>
  </g>

  <!-- ==================== SYNTHESIS OUTPUT NODE (Right) ==================== -->
  <g transform="translate(734, 76)">
    <!-- Outer Glass Container -->
    <rect width="230" height="236" rx="12" fill="#091224" stroke="url(#dossier-border)" stroke-width="1.2"/>
    <rect width="230" height="32" rx="12" fill="#0D1C38"/>
    <rect y="28" width="230" height="4" fill="#0D1C38"/>
    
    <circle cx="16" cy="16" r="3.5" fill="#10B981"/>
    <text x="28" y="20" class="font-sans" font-size="10.5" font-weight="700" fill="#FFFFFF" letter-spacing="1">DEFENSIBLE DFIR DOSSIER</text>

    <!-- Feature Checklist with Clean Vector Checkmarks -->
    <g class="font-sans" font-size="11" fill="#E2E8F0" transform="translate(16, 56)">
      <!-- Item 1 -->
      <g transform="translate(0, 0)">
        <path d="M0 -3 L4 1 L10 -5" stroke="#38BDF8" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
        <text x="18" y="0" font-weight="600">Master UTC Super-Timeline</text>
        <text x="18" y="16" font-size="9.5" fill="#94A3B8">Cross-source chronologies</text>
      </g>
      <!-- Item 2 -->
      <g transform="translate(0, 36)">
        <path d="M0 -3 L4 1 L10 -5" stroke="#38BDF8" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
        <text x="18" y="0" font-weight="600">Cytoscape Entity Graph</text>
        <text x="18" y="16" font-size="9.5" fill="#94A3B8">Relational binary/IP nodes</text>
      </g>
      <!-- Item 3 -->
      <g transform="translate(0, 72)">
        <path d="M0 -3 L4 1 L10 -5" stroke="#C084FC" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
        <text x="18" y="0" font-weight="600">Offline HTML Chat Viewer</text>
        <text x="18" y="16" font-size="9.5" fill="#94A3B8">Decoded conversation dossiers</text>
      </g>
      <!-- Item 4 -->
      <g transform="translate(0, 108)">
        <path d="M0 -3 L4 1 L10 -5" stroke="#C084FC" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
        <text x="18" y="0" font-weight="600">Court-Ready CSV Exports</text>
        <text x="18" y="16" font-size="9.5" fill="#94A3B8">UTF-8 BOM standardized</text>
      </g>
      <!-- Item 5 -->
      <g transform="translate(0, 144)">
        <path d="M0 -3 L4 1 L10 -5" stroke="#10B981" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
        <text x="18" y="0" font-weight="600">SHA-256 Audit Hashes</text>
        <text x="18" y="16" font-size="9.5" fill="#94A3B8">Verified chain of custody</text>
      </g>
    </g>
  </g>
</svg>"""


# ==============================================================================
# Generate and validate all assets
# ==============================================================================
validate_and_save("banner.svg", banner_svg)
validate_and_save("stats.svg", stats_svg)
validate_and_save("btn-linkedin.svg", btn_linkedin)
validate_and_save("btn-email.svg", btn_email)
validate_and_save("btn-repos.svg", btn_repos)
validate_and_save("btn-ceh.svg", btn_ceh)
validate_and_save("card-wft.svg", card_wft)
validate_and_save("card-msteams.svg", card_msteams)
validate_and_save("map.svg", map_svg)

# Clean up any leftover fake / foreign cards
obsolete_files = [
    "card-privesc.svg",
    "card-supertimeline.svg",
    "card-threathunt.svg"
]
for obsolete in obsolete_files:
    obs_path = os.path.join(ASSETS_DIR, obsolete)
    if os.path.exists(obs_path):
        os.remove(obs_path)
        print(f"[REMOVED] Obsolete asset deleted: {obs_path}")

# Run deep verification on README.md
readme_path = os.path.join(os.path.dirname(ASSETS_DIR), "README.md")
if os.path.exists(readme_path):
    with open(readme_path, "r", encoding="utf-8") as rf:
        readme_text = rf.read()
    if "coverage matrix" in readme_text.lower():
        raise AssertionError("Forensic Artifact Coverage Matrix detected in README.md!")
    card_refs = re.findall(r"assets/(card-[a-zA-Z0-9_\-]+)\.svg", readme_text)
    if set(card_refs) != {"card-wft", "card-msteams"}:
        raise AssertionError(f"Expected strictly card-wft and card-msteams, got: {card_refs}")
    
    # Check that all referenced assets actually exist
    all_asset_refs = re.findall(r"assets/([a-zA-Z0-9_\-]+\.svg)", readme_text)
    for asset_file in all_asset_refs:
        asset_full_path = os.path.join(ASSETS_DIR, asset_file)
        if not os.path.exists(asset_full_path):
            raise AssertionError(f"Referenced asset {asset_file} not found on disk!")
    print(f"[PASS] README.md verification passed ({len(all_asset_refs)} referenced assets verified, 0 coverage matrix, strictly genuine tools).")

print("\nAll bespoke assets generated and XML validated successfully!")
