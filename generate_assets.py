"""
generate_assets.py
Generates bespoke, unique forensic SVG assets for Sanjeeth Solleti's GitHub profile.
Eliminates copied templates, angled polygon cuts, and cyberpunk glitch tropes.
Focuses strictly on Sanjeeth's identity and his two real tools: WFT and MSTeams_Parser.
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
# 1. BANNER.SVG (1000 x 300) — Bespoke DFIR Command Station Header
# ==============================================================================
banner_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 300" width="1000" height="300" role="img" aria-label="Vasava Sanjeeth Solleti — Digital Forensics and Incident Response Analyst at TCS">
  <defs>
    <linearGradient id="bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080D1A"/>
      <stop offset="50%" stop-color="#0F172A"/>
      <stop offset="100%" stop-color="#060913"/>
    </linearGradient>
    <radialGradient id="cyan-glow" cx="20%" cy="30%" r="65%">
      <stop offset="0%" stop-color="#0284C7" stop-opacity="0.20"/>
      <stop offset="100%" stop-color="#080D1A" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="purple-glow" cx="80%" cy="70%" r="60%">
      <stop offset="0%" stop-color="#7C3AED" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#060913" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="header-accent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0284C7" stop-opacity="0.1"/>
      <stop offset="25%" stop-color="#38BDF8" stop-opacity="0.95"/>
      <stop offset="75%" stop-color="#818CF8" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#0284C7" stop-opacity="0.1"/>
    </linearGradient>
    <pattern id="dot-grid" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="0.8" fill="#334155" opacity="0.35"/>
    </pattern>
  </defs>

  <style>
    .pulse-live { animation: plive 2.2s ease-in-out infinite; }
    @keyframes plive { 0%,100% { opacity: 1; } 50% { opacity: 0.35; } }
  </style>

  <!-- Frame Background -->
  <rect width="1000" height="300" rx="14" fill="url(#bg-grad)"/>
  <rect width="1000" height="300" rx="14" fill="url(#cyan-glow)"/>
  <rect width="1000" height="300" rx="14" fill="url(#purple-glow)"/>
  <rect width="1000" height="300" rx="14" fill="url(#dot-grid)"/>
  <rect x="0.5" y="0.5" width="999" height="299" rx="14" fill="none" stroke="#1E293B" stroke-width="1"/>
  <rect x="12" y="1" width="976" height="2.5" fill="url(#header-accent)"/>

  <!-- Top Status Bar -->
  <circle class="pulse-live" cx="36" cy="30" r="4.5" fill="#10B981"/>
  <text x="48" y="34" font-family="'Segoe UI', -apple-system, sans-serif" font-size="11" font-weight="700" fill="#94A3B8" letter-spacing="1.5">FORENSIC OPERATIONS <tspan fill="#475569">//</tspan> TATA CONSULTANCY SERVICES</text>
  <text x="964" y="34" text-anchor="end" font-family="'Segoe UI', -apple-system, sans-serif" font-size="10.5" font-weight="600" fill="#94A3B8" letter-spacing="1">DEFENSIBLE CHAIN-OF-CUSTODY &#x2022; VERIFIED HASH</text>
  <line x1="30" y1="48" x2="970" y2="48" stroke="#1E293B" stroke-width="1"/>

  <!-- Left Content (bounded safely within x=36 to x=610) -->
  <rect x="36" y="66" width="220" height="22" rx="11" fill="#0C1E3A" stroke="#1D4ED8" stroke-width="1"/>
  <text x="146" y="81" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="10" font-weight="700" fill="#38BDF8" letter-spacing="1.4">ENTERPRISE DFIR ANALYST</text>

  <text x="36" y="126" font-family="'Segoe UI', -apple-system, 'SF Pro Display', sans-serif" font-size="36" font-weight="800" fill="#FFFFFF" letter-spacing="1.5">VASAVA SANJEETH SOLLETI</text>
  <text x="36" y="154" font-family="'Segoe UI', sans-serif" font-size="14.5" font-weight="600" fill="#38BDF8">DFIR Analyst @ TCS <tspan fill="#475569">|</tspan> Windows Forensics &amp; Engine Architect</text>
  <text x="36" y="180" font-family="'Segoe UI', sans-serif" font-size="12.5" fill="#CBD5E1">Reconstructing attack chronologies across raw disks, dirty hives, &amp; cloud apps.</text>

  <!-- Capability Pills on Left -->
  <g transform="translate(36, 206)">
    <rect x="0" y="0" width="132" height="26" rx="6" fill="#0B1E38" stroke="#1D4ED8" stroke-width="1"/>
    <text x="66" y="17" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="10.5" font-weight="600" fill="#93C5FD">&#x2B21; WFT Platform</text>

    <rect x="140" y="0" width="148" height="26" rx="6" fill="#1C1035" stroke="#7C3AED" stroke-width="1"/>
    <text x="214" y="17" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="10.5" font-weight="600" fill="#C4B5FD">&#x2B22; MSTeams_Parser</text>

    <rect x="296" y="0" width="144" height="26" rx="6" fill="#241804" stroke="#D97706" stroke-width="1"/>
    <text x="368" y="17" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="10.5" font-weight="600" fill="#FCD34D">&#x26A1; DuckDB Core</text>

    <rect x="448" y="0" width="130" height="26" rx="6" fill="#062117" stroke="#059669" stroke-width="1"/>
    <text x="513" y="17" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="10.5" font-weight="600" fill="#6EE7B7">&#x1F6E1; CEH Certified</text>
  </g>

  <!-- Right Side Forensic Specification Card (Starts at x=640, width=324, zero overlap) -->
  <g transform="translate(640, 66)">
    <rect width="324" height="166" rx="10" fill="#0A1224" stroke="#1E293B" stroke-width="1.2"/>
    <rect width="324" height="30" rx="10" fill="#0E1A33"/>
    <rect y="26" width="324" height="4" fill="#0E1A33"/>
    <circle cx="16" cy="15" r="3.5" fill="#38BDF8"/>
    <text x="28" y="19" font-family="'Segoe UI', sans-serif" font-size="10" font-weight="700" fill="#E2E8F0" letter-spacing="1.2">SPECIALIZED INVESTIGATIVE SCOPE</text>
    
    <g font-family="'Segoe UI', sans-serif" font-size="11" fill="#CBD5E1" transform="translate(16, 50)">
      <text x="0" y="0"><tspan fill="#38BDF8">&#x25AA;</tspan> Native VFS Ingestion <tspan fill="#94A3B8">(E01, RAW, VHDX, VMDK)</tspan></text>
      <text x="0" y="22"><tspan fill="#38BDF8">&#x25AA;</tspan> Automated Dirty Registry Replay <tspan fill="#94A3B8">(RLA)</tspan></text>
      <text x="0" y="44"><tspan fill="#38BDF8">&#x25AA;</tspan> Sub-Ms Columnar Super-Timelines <tspan fill="#94A3B8">(DuckDB)</tspan></text>
      <text x="0" y="66"><tspan fill="#A855F7">&#x25AA;</tspan> Collaboration Stores <tspan fill="#94A3B8">(Teams IndexedDB/LevelDB)</tspan></text>
      <text x="0" y="88"><tspan fill="#10B981">&#x25AA;</tspan> Compiled Threat Triage <tspan fill="#94A3B8">(Rust YARA-X + RapidOCR)</tspan></text>
    </g>
  </g>

  <!-- Bottom Telemetry Bar -->
  <line x1="30" y1="256" x2="970" y2="256" stroke="#1E293B" stroke-width="1"/>
  <circle class="pulse-live" cx="36" cy="276" r="3" fill="#00E5FF"/>
  <text x="46" y="280" font-family="'Segoe UI', sans-serif" font-size="10.5" fill="#94A3B8">ACTIVE RESEARCH: Dirty Registry Replay &#x2022; IndexedDB Forensics &#x2022; Multi-Source Attack Chronologies</text>
  <text x="964" y="280" text-anchor="end" font-family="'Segoe UI', sans-serif" font-size="10.5" font-weight="600" fill="#94A3B8">HYDERABAD, INDIA</text>
</svg>"""

# ==============================================================================
# 2. STATS.SVG (1000 x 96) — Operational Telemetry & Capabilities HUD
# ==============================================================================
stats_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 96" width="1000" height="96" role="img" aria-label="Forensic Telemetry: TCS DFIR Analyst, WFT Platform, MSTeams_Parser, DuckDB Columnar Core">
  <defs>
    <linearGradient id="sgrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080D1A"/>
      <stop offset="50%" stop-color="#0F172A"/>
      <stop offset="100%" stop-color="#0A1122"/>
    </linearGradient>
  </defs>

  <rect width="1000" height="96" rx="12" fill="url(#sgrad)"/>
  <rect x="0.5" y="0.5" width="999" height="95" rx="12" fill="none" stroke="#1E293B" stroke-width="1"/>

  <!-- Station 1: Organization & Role -->
  <g transform="translate(125, 0)">
    <text x="0" y="26" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="9.5" font-weight="700" fill="#38BDF8" letter-spacing="1.4">ENTERPRISE DFIR</text>
    <text x="0" y="55" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="22" font-weight="800" fill="#FFFFFF">TCS</text>
    <text x="0" y="76" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="10.5" fill="#CBD5E1">Tata Consultancy Services</text>
  </g>

  <!-- Divider 1 -->
  <line x1="250" y1="18" x2="250" y2="78" stroke="#1E293B" stroke-width="1"/>
  <circle cx="250" cy="48" r="2.5" fill="#38BDF8"/>

  <!-- Station 2: WFT Platform -->
  <g transform="translate(375, 0)">
    <text x="0" y="26" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="9.5" font-weight="700" fill="#34D399" letter-spacing="1.4">PRIMARY PLATFORM</text>
    <text x="0" y="55" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="22" font-weight="800" fill="#FFFFFF">WFT</text>
    <text x="0" y="76" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="10.5" fill="#CBD5E1">Windows Forensics Suite</text>
  </g>

  <!-- Divider 2 -->
  <line x1="500" y1="18" x2="500" y2="78" stroke="#1E293B" stroke-width="1"/>
  <circle cx="500" cy="48" r="2.5" fill="#34D399"/>

  <!-- Station 3: MSTeams_Parser -->
  <g transform="translate(625, 0)">
    <text x="0" y="26" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="9.5" font-weight="700" fill="#C084FC" letter-spacing="1.4">COLLABORATION DFIR</text>
    <text x="0" y="55" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="20" font-weight="800" fill="#FFFFFF">MSTeams</text>
    <text x="0" y="76" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="10.5" fill="#CBD5E1">IndexedDB / LevelDB Suite</text>
  </g>

  <!-- Divider 3 -->
  <line x1="750" y1="18" x2="750" y2="78" stroke="#1E293B" stroke-width="1"/>
  <circle cx="750" cy="48" r="2.5" fill="#C084FC"/>

  <!-- Station 4: Engine Backbone -->
  <g transform="translate(875, 0)">
    <text x="0" y="26" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="9.5" font-weight="700" fill="#FBBF24" letter-spacing="1.4">ANALYTIC CORE</text>
    <text x="0" y="55" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="22" font-weight="800" fill="#FFFFFF">DuckDB</text>
    <text x="0" y="76" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="10.5" fill="#CBD5E1">Zero-Copy Super-Timeline</text>
  </g>
</svg>"""

# ==============================================================================
# 3. ACTION BUTTONS (215 x 44 each) — Modern Interactive Hardware Action Badges
# ==============================================================================

# Button: LinkedIn
btn_linkedin = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 215 44" width="215" height="44" role="img" aria-label="LinkedIn Profile">
  <rect x="0.5" y="0.5" width="214" height="43" rx="10" fill="#0A1224" stroke="#1E293B" stroke-width="1"/>
  <path d="M12 1 H203" stroke="#0A66C2" stroke-width="1.5" stroke-opacity="0.5"/>
  <rect x="13" y="11" width="22" height="22" rx="4" fill="#0A66C2"/>
  <text x="24" y="27" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="800" fill="#FFFFFF">in</text>
  <text x="44" y="27" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="700" fill="#E2E8F0" letter-spacing="1">LINKEDIN</text>
  <text x="198" y="27" text-anchor="end" font-family="sans-serif" font-size="13" font-weight="bold" fill="#38BDF8">&#x2197;</text>
</svg>"""

# Button: Email
btn_email = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 215 44" width="215" height="44" role="img" aria-label="Direct Email">
  <rect x="0.5" y="0.5" width="214" height="43" rx="10" fill="#0A1224" stroke="#1E293B" stroke-width="1"/>
  <path d="M12 1 H203" stroke="#059669" stroke-width="1.5" stroke-opacity="0.5"/>
  <rect x="13" y="11" width="22" height="22" rx="4" fill="#065F46"/>
  <path d="M17 17 L24 22 L31 17 M17 17 H31 V27 H17 Z" fill="none" stroke="#6EE7B7" stroke-width="1.4" stroke-linejoin="round"/>
  <text x="44" y="27" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="700" fill="#E2E8F0" letter-spacing="1">EMAIL CONTACT</text>
  <text x="198" y="27" text-anchor="end" font-family="sans-serif" font-size="13" font-weight="bold" fill="#34D399">&#x2197;</text>
</svg>"""

# Button: Repositories
btn_repos = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 215 44" width="215" height="44" role="img" aria-label="All GitHub Repositories">
  <rect x="0.5" y="0.5" width="214" height="43" rx="10" fill="#0A1224" stroke="#1E293B" stroke-width="1"/>
  <path d="M12 1 H203" stroke="#D97706" stroke-width="1.5" stroke-opacity="0.5"/>
  <rect x="13" y="11" width="22" height="22" rx="4" fill="#78350F"/>
  <path d="M18 16 H24 L26 18 H30 V26 H18 Z" fill="none" stroke="#FCD34D" stroke-width="1.4" stroke-linejoin="round"/>
  <text x="44" y="27" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="700" fill="#E2E8F0" letter-spacing="1">REPOSITORIES</text>
  <text x="198" y="27" text-anchor="end" font-family="sans-serif" font-size="13" font-weight="bold" fill="#FBBF24">&#x2197;</text>
</svg>"""

# Button: CEH Certified
btn_ceh = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 215 44" width="215" height="44" role="img" aria-label="CEH Certified Ethical Hacker">
  <rect x="0.5" y="0.5" width="214" height="43" rx="10" fill="#0A1224" stroke="#1E293B" stroke-width="1"/>
  <path d="M12 1 H203" stroke="#7C3AED" stroke-width="1.5" stroke-opacity="0.5"/>
  <rect x="13" y="11" width="22" height="22" rx="4" fill="#4C1D95"/>
  <path d="M24 15 L30 18 V23 C30 27 24 30 24 30 C24 30 18 27 18 23 V18 Z" fill="none" stroke="#C4B5FD" stroke-width="1.4"/>
  <text x="44" y="27" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="700" fill="#E2E8F0" letter-spacing="1">CEH CERTIFIED</text>
  <text x="198" y="27" text-anchor="end" font-family="sans-serif" font-size="12" font-weight="bold" fill="#A78BFA">&#x2713;</text>
</svg>"""

# ==============================================================================
# 4. FLAGSHIP TOOL CARDS (485 x 260 each) — ONLY Sanjeeth's 2 Real Tools
# ==============================================================================

# Card 1: WFT (Windows Forensic Examination Platform)
card_wft = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 485 260" width="485" height="260" role="img" aria-label="WFT — Windows Forensic Examination Platform">
  <defs>
    <linearGradient id="wftgrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080E1C"/>
      <stop offset="100%" stop-color="#060A14"/>
    </linearGradient>
  </defs>

  <style>
    .pulse-wft { animation: pwft 2s ease-in-out infinite; }
    @keyframes pwft { 0%,100% { opacity: 1; } 50% { opacity: 0.3; } }
  </style>

  <!-- Frame Background -->
  <rect width="485" height="260" rx="14" fill="url(#wftgrad)"/>
  <rect x="0.5" y="0.5" width="484" height="259" rx="14" fill="none" stroke="#1D4ED8" stroke-width="1.2"/>
  <path d="M14 1 H471" stroke="#00E5FF" stroke-width="2"/>

  <!-- Top Header Bar -->
  <circle class="pulse-wft" cx="24" cy="24" r="4" fill="#00E5FF"/>
  <text x="36" y="28" font-family="'Segoe UI', sans-serif" font-size="10" font-weight="700" fill="#38BDF8" letter-spacing="1.5">FLAGSHIP DFIR WORKSTATION</text>
  
  <rect x="385" y="14" width="80" height="20" rx="4" fill="#0E2342" stroke="#1D4ED8" stroke-width="1"/>
  <text x="425" y="28" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="9" font-weight="700" fill="#93C5FD">v1.0 ACTIVE</text>

  <!-- Title & Subtitle -->
  <text x="24" y="62" font-family="'Segoe UI', -apple-system, sans-serif" font-size="20" font-weight="800" fill="#FFFFFF">WFT — Windows Forensics</text>
  <text x="24" y="80" font-family="'Segoe UI', sans-serif" font-size="11.5" fill="#CBD5E1">Enterprise "Process + Examine" Digital Forensics Platform</text>
  <line x1="24" y1="92" x2="461" y2="92" stroke="#1E293B" stroke-width="1"/>

  <!-- Core Highlights -->
  <g font-family="'Segoe UI', sans-serif" font-size="11" fill="#E2E8F0">
    <text x="24" y="112"><tspan fill="#38BDF8">&#x25B8;</tspan> <tspan font-weight="700" fill="#FFFFFF">DuckDB Columnar Core:</tspan> Sub-millisecond unpivoted super-timeline</text>
    <text x="24" y="132"><tspan fill="#38BDF8">&#x25B8;</tspan> <tspan font-weight="700" fill="#FFFFFF">Dirty Registry Replay:</tspan> Automated RLA .LOG1/.LOG2 transaction commit</text>
    <text x="24" y="152"><tspan fill="#38BDF8">&#x25B8;</tspan> <tspan font-weight="700" fill="#FFFFFF">Native VFS Intake:</tspan> Direct E01, RAW, VHDX, VMDK mounting via dissect</text>
    <text x="24" y="172"><tspan fill="#38BDF8">&#x25B8;</tspan> <tspan font-weight="700" fill="#FFFFFF">Threat Hunting &amp; Carving:</tspan> Rust YARA-X scanning + RapidOCR triage</text>
  </g>

  <!-- Divider before tags -->
  <line x1="24" y1="188" x2="461" y2="188" stroke="#1E293B" stroke-width="1"/>

  <!-- Tech Stack Pills -->
  <g transform="translate(24, 198)">
    <rect x="0" y="0" width="60" height="20" rx="4" fill="#0C1D38"/><text x="30" y="14" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="9.5" font-weight="600" fill="#93C5FD">DuckDB</text>
    <rect x="66" y="0" width="56" height="20" rx="4" fill="#0C1D38"/><text x="94" y="14" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="9.5" font-weight="600" fill="#93C5FD">FastAPI</text>
    <rect x="128" y="0" width="62" height="20" rx="4" fill="#0C1D38"/><text x="159" y="14" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="9.5" font-weight="600" fill="#93C5FD">React 18</text>
    <rect x="196" y="0" width="68" height="20" rx="4" fill="#0C1D38"/><text x="230" y="14" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="9.5" font-weight="600" fill="#93C5FD">Cytoscape</text>
    <rect x="270" y="0" width="58" height="20" rx="4" fill="#0C1D38"/><text x="299" y="14" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="9.5" font-weight="600" fill="#93C5FD">YARA-X</text>
    <rect x="334" y="0" width="60" height="20" rx="4" fill="#0C1D38"/><text x="364" y="14" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="9.5" font-weight="600" fill="#93C5FD">AG Grid</text>
  </g>

  <!-- Bottom Link Line -->
  <text x="24" y="242" font-family="'Cascadia Code', Consolas, monospace" font-size="10" fill="#94A3B8">github.com/sanjeeth-solleti/WFT</text>
  <text x="461" y="242" text-anchor="end" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="700" fill="#38BDF8">Explore Repository &#x2197;</text>
</svg>"""

# Card 2: MSTeams_Parser (Microsoft Teams DFIR Forensic Suite)
card_msteams = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 485 260" width="485" height="260" role="img" aria-label="MSTeams_Parser — Microsoft Teams DFIR Forensic Suite">
  <defs>
    <linearGradient id="msgrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#110A24"/>
      <stop offset="100%" stop-color="#080612"/>
    </linearGradient>
  </defs>

  <style>
    .pulse-ms { animation: pms 2s ease-in-out infinite; }
    @keyframes pms { 0%,100% { opacity: 1; } 50% { opacity: 0.3; } }
  </style>

  <!-- Frame Background -->
  <rect width="485" height="260" rx="14" fill="url(#msgrad)"/>
  <rect x="0.5" y="0.5" width="484" height="259" rx="14" fill="none" stroke="#7C3AED" stroke-width="1.2"/>
  <path d="M14 1 H471" stroke="#A855F7" stroke-width="2"/>

  <!-- Top Header Bar -->
  <circle class="pulse-ms" cx="24" cy="24" r="4" fill="#A855F7"/>
  <text x="36" y="28" font-family="'Segoe UI', sans-serif" font-size="10" font-weight="700" fill="#C084FC" letter-spacing="1.5">COLLABORATION DFIR SUITE</text>

  <rect x="352" y="14" width="113" height="20" rx="4" fill="#24103C" stroke="#7C3AED" stroke-width="1"/>
  <text x="408" y="28" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="9" font-weight="700" fill="#E9D5FF">AIR-GAPPED 127.0.0.1</text>

  <!-- Title & Subtitle -->
  <text x="24" y="62" font-family="'Segoe UI', -apple-system, sans-serif" font-size="20" font-weight="800" fill="#FFFFFF">MSTeams_Parser</text>
  <text x="24" y="80" font-family="'Segoe UI', sans-serif" font-size="11.5" fill="#CBD5E1">Standalone Microsoft Teams DFIR Forensic Extraction Suite</text>
  <line x1="24" y1="92" x2="461" y2="92" stroke="#2E1B4E" stroke-width="1"/>

  <!-- Core Highlights -->
  <g font-family="'Segoe UI', sans-serif" font-size="11" fill="#E2E8F0">
    <text x="24" y="112"><tspan fill="#C084FC">&#x25B8;</tspan> <tspan font-weight="700" fill="#FFFFFF">Multi-Source Ingestion:</tspan> Decodes New &amp; Classic IndexedDB &amp; LevelDB</text>
    <text x="24" y="132"><tspan fill="#C084FC">&#x25B8;</tspan> <tspan font-weight="700" fill="#FFFFFF">Deep Normalization:</tspan> Base64 Adaptive Cards, calls &amp; meeting events</text>
    <text x="24" y="152"><tspan fill="#C084FC">&#x25B8;</tspan> <tspan font-weight="700" fill="#FFFFFF">Identity Correlator:</tspan> Resolves 8:orgid GUIDs to employee records</text>
    <text x="24" y="172"><tspan fill="#C084FC">&#x25B8;</tspan> <tspan font-weight="700" fill="#FFFFFF">Forensic Media Carver:</tspan> Magic-byte image recovery &amp; noise suppression</text>
  </g>

  <!-- Divider before tags -->
  <line x1="24" y1="188" x2="461" y2="188" stroke="#2E1B4E" stroke-width="1"/>

  <!-- Tech Stack Pills -->
  <g transform="translate(24, 198)">
    <rect x="0" y="0" width="58" height="20" rx="4" fill="#24103C"/><text x="29" y="14" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="9.5" font-weight="600" fill="#E9D5FF">LevelDB</text>
    <rect x="64" y="0" width="70" height="20" rx="4" fill="#24103C"/><text x="99" y="14" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="9.5" font-weight="600" fill="#E9D5FF">IndexedDB</text>
    <rect x="140" y="0" width="82" height="20" rx="4" fill="#24103C"/><text x="181" y="14" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="9.5" font-weight="600" fill="#E9D5FF">dfindexeddb</text>
    <rect x="228" y="0" width="64" height="20" rx="4" fill="#24103C"/><text x="260" y="14" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="9.5" font-weight="600" fill="#E9D5FF">cramjam</text>
    <rect x="298" y="0" width="82" height="20" rx="4" fill="#24103C"/><text x="339" y="14" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="9.5" font-weight="600" fill="#E9D5FF">HTML Viewer</text>
  </g>

  <!-- Bottom Link Line -->
  <text x="24" y="242" font-family="'Cascadia Code', Consolas, monospace" font-size="10" fill="#94A3B8">github.com/sanjeeth-solleti/MSTeams_Parser</text>
  <text x="461" y="242" text-anchor="end" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="700" fill="#C084FC">Explore Repository &#x2197;</text>
</svg>"""

# ==============================================================================
# 5. MAP.SVG (1000 x 320) — High-Resolution Bespoke Dual-Engine Schematic
# ==============================================================================
map_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 320" width="1000" height="320" role="img" aria-label="DFIR Dual-Engine Forensic Pipeline Architecture: WFT Platform and MSTeams_Parser Synthesis">
  <defs>
    <linearGradient id="mapbg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080D1A"/>
      <stop offset="50%" stop-color="#0F172A"/>
      <stop offset="100%" stop-color="#060913"/>
    </linearGradient>
  </defs>

  <rect width="1000" height="320" rx="14" fill="url(#mapbg)"/>
  <rect x="0.5" y="0.5" width="999" height="319" rx="14" fill="none" stroke="#1E293B" stroke-width="1"/>

  <!-- Architecture Header -->
  <text x="36" y="32" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="700" fill="#38BDF8" letter-spacing="1.5">DFIR DUAL-ENGINE FORENSIC ARCHITECTURE <tspan fill="#475569">//</tspan> PIPELINE OVERVIEW</text>
  <text x="964" y="32" text-anchor="end" font-family="'Segoe UI', sans-serif" font-size="10.5" font-weight="600" fill="#94A3B8">Deterministic Ingestion &#x2022; Dirty Hive Recovery &#x2022; Defensible Synthesis</text>
  <line x1="30" y1="46" x2="970" y2="46" stroke="#1E293B" stroke-width="1"/>

  <!-- ==================== TRACK 1: WFT (Host / Endpoint) ==================== -->
  <!-- Label -->
  <rect x="36" y="60" width="260" height="22" rx="4" fill="#0C1D38" stroke="#1D4ED8" stroke-width="1"/>
  <text x="166" y="75" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="9.5" font-weight="700" fill="#93C5FD" letter-spacing="1">TRACK 1: HOST &amp; DISK FORENSICS (WFT)</text>

  <!-- Stage 1.1: Evidence Intake -->
  <g transform="translate(36, 92)">
    <rect width="190" height="74" rx="8" fill="#0A1428" stroke="#1E3A8A" stroke-width="1"/>
    <text x="95" y="24" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="11.5" font-weight="700" fill="#FFFFFF">1. Disk Evidence Intake</text>
    <text x="95" y="44" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="11" fill="#94A3B8">E01, RAW, VHDX, VMDK</text>
    <text x="95" y="62" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="10.5" font-weight="600" fill="#38BDF8">Native Dissect VFS Mount</text>
  </g>

  <!-- Bus Arrow 1 -> 2 -->
  <path d="M226 129 H260" stroke="#38BDF8" stroke-width="1.5" stroke-dasharray="3 3"/>
  <polygon points="262,129 256,126 256,132" fill="#38BDF8"/>

  <!-- Stage 1.2: Dirty Registry Replay -->
  <g transform="translate(264, 92)">
    <rect width="190" height="74" rx="8" fill="#0A1428" stroke="#1E3A8A" stroke-width="1"/>
    <text x="95" y="24" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="11.5" font-weight="700" fill="#FFFFFF">2. Registry Integrity</text>
    <text x="95" y="44" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="11" fill="#94A3B8">RLA .LOG1/.LOG2 Replay</text>
    <text x="95" y="62" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="10.5" font-weight="600" fill="#38BDF8">Transaction Log Commit</text>
  </g>

  <!-- Bus Arrow 2 -> 3 -->
  <path d="M454 129 H488" stroke="#38BDF8" stroke-width="1.5" stroke-dasharray="3 3"/>
  <polygon points="490,129 484,126 484,132" fill="#38BDF8"/>

  <!-- Stage 1.3: Super-Timeline & Triage Engine -->
  <g transform="translate(492, 92)">
    <rect width="190" height="74" rx="8" fill="#0F284E" stroke="#2563EB" stroke-width="1.4"/>
    <text x="95" y="24" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="11.5" font-weight="800" fill="#38BDF8">3. WFT Analytic Core</text>
    <text x="95" y="44" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="11" fill="#FFFFFF">DuckDB Columnar Core</text>
    <text x="95" y="62" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="10.5" font-weight="600" fill="#93C5FD">Sub-Ms Timeline · YARA-X</text>
  </g>

  <!-- Connector Track 1 -> Synthesis Node -->
  <path d="M682 129 H728" stroke="#38BDF8" stroke-width="1.6"/>
  <polygon points="730,129 724,126 724,132" fill="#38BDF8"/>

  <!-- ==================== TRACK 2: MSTEAMS (Collaboration / Cloud) ==================== -->
  <!-- Label -->
  <rect x="36" y="180" width="280" height="22" rx="4" fill="#1C1035" stroke="#7C3AED" stroke-width="1"/>
  <text x="176" y="195" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="9.5" font-weight="700" fill="#C4B5FD" letter-spacing="1">TRACK 2: COLLABORATION FORENSICS (MSTEAMS)</text>

  <!-- Stage 2.1: Store Ingestion -->
  <g transform="translate(36, 212)">
    <rect width="190" height="74" rx="8" fill="#140C24" stroke="#4C1D95" stroke-width="1"/>
    <text x="95" y="24" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="11.5" font-weight="700" fill="#FFFFFF">1. Messaging Intake</text>
    <text x="95" y="44" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="11" fill="#94A3B8">IndexedDB &amp; LevelDB Stores</text>
    <text x="95" y="62" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="10.5" font-weight="600" fill="#C084FC">New &amp; Classic Teams Cache</text>
  </g>

  <!-- Bus Arrow 1 -> 2 -->
  <path d="M226 249 H260" stroke="#A855F7" stroke-width="1.5" stroke-dasharray="3 3"/>
  <polygon points="262,249 256,246 256,252" fill="#A855F7"/>

  <!-- Stage 2.2: Payload Normalization -->
  <g transform="translate(264, 212)">
    <rect width="190" height="74" rx="8" fill="#140C24" stroke="#4C1D95" stroke-width="1"/>
    <text x="95" y="24" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="11.5" font-weight="700" fill="#FFFFFF">2. Event Normalization</text>
    <text x="95" y="44" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="11" fill="#94A3B8">Base64 Adaptive Cards &amp; Calls</text>
    <text x="95" y="62" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="10.5" font-weight="600" fill="#C084FC">8:orgid GUID &#x2192; Directory Name</text>
  </g>

  <!-- Bus Arrow 2 -> 3 -->
  <path d="M454 249 H488" stroke="#A855F7" stroke-width="1.5" stroke-dasharray="3 3"/>
  <polygon points="490,249 484,246 484,252" fill="#A855F7"/>

  <!-- Stage 2.3: MSTeams Engine & Carve -->
  <g transform="translate(492, 212)">
    <rect width="190" height="74" rx="8" fill="#2E1254" stroke="#7C3AED" stroke-width="1.4"/>
    <text x="95" y="24" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="11.5" font-weight="800" fill="#C084FC">3. MSTeams Parser</text>
    <text x="95" y="44" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="11" fill="#FFFFFF">Air-Gapped 127.0.0.1</text>
    <text x="95" y="62" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="10.5" font-weight="600" fill="#E9D5FF">Magic-Byte Media Carving</text>
  </g>

  <!-- Connector Track 2 -> Synthesis Node -->
  <path d="M682 249 H728" stroke="#A855F7" stroke-width="1.6"/>
  <polygon points="730,249 724,246 724,252" fill="#A855F7"/>

  <!-- ==================== SYNTHESIS OUTPUT NODE (Right) ==================== -->
  <g transform="translate(734, 76)">
    <rect width="230" height="210" rx="10" fill="#0C152B" stroke="#1E293B" stroke-width="1.2"/>
    <rect width="230" height="30" rx="10" fill="#0F1E3E"/>
    <rect y="26" width="230" height="4" fill="#0F1E3E"/>
    <text x="115" y="20" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="10.5" font-weight="700" fill="#FFFFFF" letter-spacing="1">DEFENSIBLE DFIR DOSSIER</text>

    <g font-family="'Segoe UI', sans-serif" font-size="11" fill="#E2E8F0" transform="translate(16, 52)">
      <text x="0" y="0"><tspan fill="#38BDF8">&#x2714;</tspan> Master UTC Super-Timeline</text>
      <text x="0" y="28"><tspan fill="#38BDF8">&#x2714;</tspan> Cytoscape Entity Graph</text>
      <text x="0" y="56"><tspan fill="#C084FC">&#x2714;</tspan> Offline HTML Chat Dossier</text>
      <text x="0" y="84"><tspan fill="#C084FC">&#x2714;</tspan> Court-Ready CSV Exports</text>
      <text x="0" y="112"><tspan fill="#10B981">&#x2714;</tspan> SHA-256 Audit Hashes</text>
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
    print("[PASS] README.md verification passed: Coverage matrix removed, only 2 tools displayed.")

print("\nAll bespoke assets generated and XML validated successfully!")
