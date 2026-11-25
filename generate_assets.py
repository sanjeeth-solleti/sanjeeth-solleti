"""
generate_assets.py
Generates bespoke, unique forensic SVG assets for Sanjeeth Solleti's GitHub profile.
Eliminates copied templates, angled polygon cuts, and cyberpunk glitch tropes.
Focuses strictly on Sanjeeth's identity and his two real tools: WFT and MSTeams_Parser.
"""
import os
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
    <linearGradient id="bgrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080D1A"/>
      <stop offset="50%" stop-color="#0B1528"/>
      <stop offset="100%" stop-color="#060A14"/>
    </linearGradient>
    <radialGradient id="topglow" cx="50%" cy="0%" r="70%">
      <stop offset="0%" stop-color="#0284C7" stop-opacity="0.22"/>
      <stop offset="100%" stop-color="#080D1A" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="toprule" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0284C7" stop-opacity="0.1"/>
      <stop offset="35%" stop-color="#38BDF8" stop-opacity="0.95"/>
      <stop offset="65%" stop-color="#00E5FF" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#0284C7" stop-opacity="0.1"/>
    </linearGradient>
    <pattern id="gridpat" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="0.75" fill="#334155" opacity="0.4"/>
    </pattern>
  </defs>

  <style>
    .pulse-live { animation: plive 2.2s ease-in-out infinite; }
    @keyframes plive { 0%,100% { opacity: 1; } 50% { opacity: 0.3; } }
  </style>

  <!-- Frame Background -->
  <rect width="1000" height="300" rx="14" fill="url(#bgrad)"/>
  <rect width="1000" height="300" rx="14" fill="url(#topglow)"/>
  <rect width="1000" height="300" rx="14" fill="url(#gridpat)"/>
  <rect x="0.5" y="0.5" width="999" height="299" rx="14" fill="none" stroke="#1E293B" stroke-width="1"/>
  <rect x="10" y="1" width="980" height="2" fill="url(#toprule)"/>

  <!-- Top Status / Telemetry Bar -->
  <circle class="pulse-live" cx="36" cy="30" r="4.5" fill="#10B981"/>
  <text x="48" y="34" font-family="'Segoe UI', -apple-system, sans-serif" font-size="11" font-weight="700" fill="#94A3B8" letter-spacing="1.5">FORENSIC OPERATIONS <tspan fill="#334155">//</tspan> TATA CONSULTANCY SERVICES</text>
  <text x="964" y="34" text-anchor="end" font-family="'Segoe UI', -apple-system, sans-serif" font-size="10.5" font-weight="600" fill="#64748B" letter-spacing="1">DEFENSIBLE CHAIN-OF-CUSTODY &#x2022; VERIFIED HASH</text>
  <line x1="30" y1="48" x2="970" y2="48" stroke="#1E293B" stroke-width="1"/>

  <!-- Left Main Identity Content -->
  <rect x="36" y="66" width="236" height="22" rx="11" fill="#0C1E3A" stroke="#1D4ED8" stroke-width="1"/>
  <text x="154" y="81" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="10" font-weight="700" fill="#38BDF8" letter-spacing="1.4">ENTERPRISE DFIR SPECIALIST</text>

  <text x="36" y="128" font-family="'Segoe UI', -apple-system, 'SF Pro Display', sans-serif" font-size="40" font-weight="800" fill="#FFFFFF" letter-spacing="2">VASAVA SANJEETH SOLLETI</text>
  <text x="36" y="158" font-family="'Segoe UI', sans-serif" font-size="15" font-weight="600" fill="#38BDF8">Digital Forensics &amp; Incident Response Analyst <tspan fill="#475569">|</tspan> Windows Forensics &amp; Tool Architect</text>
  <text x="36" y="186" font-family="'Segoe UI', sans-serif" font-size="13" fill="#94A3B8">Reconstructing ground-truth attack chronologies across raw disk images, dirty hives, memory, and cloud stores.</text>

  <!-- Feature Capability Pills -->
  <g transform="translate(36, 212)">
    <!-- Pill 1: WFT -->
    <rect x="0" y="0" width="138" height="26" rx="6" fill="#0B1E38" stroke="#1D4ED8" stroke-width="1"/>
    <text x="69" y="17" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="10.5" font-weight="600" fill="#93C5FD">&#x2B21; WFT Platform</text>

    <!-- Pill 2: MSTeams -->
    <rect x="146" y="0" width="154" height="26" rx="6" fill="#1C1035" stroke="#7C3AED" stroke-width="1"/>
    <text x="223" y="17" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="10.5" font-weight="600" fill="#C4B5FD">&#x2B22; MSTeams_Parser</text>

    <!-- Pill 3: DuckDB -->
    <rect x="308" y="0" width="158" height="26" rx="6" fill="#241804" stroke="#D97706" stroke-width="1"/>
    <text x="387" y="17" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="10.5" font-weight="600" fill="#FCD34D">&#x26A1; DuckDB Columnar</text>

    <!-- Pill 4: CEH -->
    <rect x="474" y="0" width="136" height="26" rx="6" fill="#062117" stroke="#059669" stroke-width="1"/>
    <text x="542" y="17" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="10.5" font-weight="600" fill="#6EE7B7">&#x1F6E1; CEH Certified</text>
  </g>

  <!-- Right Side Decorative Forensic Card -->
  <g transform="translate(696, 66)">
    <rect width="268" height="136" rx="10" fill="#0A1224" stroke="#1E293B" stroke-width="1"/>
    <rect width="268" height="28" rx="10" fill="#0E1A33"/>
    <rect y="24" width="268" height="4" fill="#0E1A33"/>
    <circle cx="16" cy="14" r="3.5" fill="#38BDF8"/>
    <text x="28" y="18" font-family="'Segoe UI', sans-serif" font-size="10" font-weight="700" fill="#E2E8F0" letter-spacing="1">FORENSIC CAPABILITY SPEC</text>
    
    <g font-family="'Segoe UI', sans-serif" font-size="10.5" fill="#94A3B8" transform="translate(16, 46)">
      <text x="0" y="0">&#x25AA; Native VFS Dissect Intake (E01/RAW)</text>
      <text x="0" y="20">&#x25AA; RLA Automated Dirty Hive Replay</text>
      <text x="0" y="40">&#x25AA; Zero-Copy DuckDB Timeline Engine</text>
      <text x="0" y="60">&#x25AA; YARA-X Rust Scanning &amp; RapidOCR</text>
      <text x="0" y="80">&#x25AA; LevelDB &amp; IndexedDB Evidence Suite</text>
    </g>
  </g>

  <!-- Bottom Terminal Bar -->
  <line x1="30" y1="260" x2="970" y2="260" stroke="#1E293B" stroke-width="1"/>
  <circle class="pulse-live" cx="36" cy="278" r="3" fill="#00E5FF"/>
  <text x="46" y="282" font-family="'Segoe UI', sans-serif" font-size="10.5" fill="#64748B">ACTIVE RESEARCH: Dirty Registry Recovery &#x2022; IndexedDB Forensics &#x2022; Multi-Source Attack Chronologies</text>
  <text x="964" y="282" text-anchor="end" font-family="'Segoe UI', sans-serif" font-size="10.5" fill="#475569">HYDERABAD, INDIA</text>
</svg>"""

# ==============================================================================
# 2. STATS.SVG (1000 x 96) — Operational Telemetry & Capabilities HUD
# ==============================================================================
stats_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 96" width="1000" height="96" role="img" aria-label="Forensic Telemetry: TCS DFIR Analyst, WFT Platform, MSTeams_Parser, DuckDB Columnar Core">
  <defs>
    <linearGradient id="sgrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080D1A"/>
      <stop offset="100%" stop-color="#0B1326"/>
    </linearGradient>
  </defs>

  <rect width="1000" height="96" rx="12" fill="url(#sgrad)"/>
  <rect x="0.5" y="0.5" width="999" height="95" rx="12" fill="none" stroke="#1E293B" stroke-width="1"/>

  <!-- Station 1: Organization & Role -->
  <g transform="translate(125, 0)">
    <text x="0" y="27" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="9.5" font-weight="700" fill="#38BDF8" letter-spacing="1.2">ENTERPRISE DFIR</text>
    <text x="0" y="55" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="22" font-weight="800" fill="#FFFFFF">TCS</text>
    <text x="0" y="76" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="10.5" fill="#94A3B8">Tata Consultancy Services</text>
  </g>

  <!-- Divider 1 -->
  <line x1="250" y1="18" x2="250" y2="78" stroke="#1E293B" stroke-width="1"/>
  <circle cx="250" cy="48" r="2.5" fill="#38BDF8"/>

  <!-- Station 2: WFT Platform -->
  <g transform="translate(375, 0)">
    <text x="0" y="27" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="9.5" font-weight="700" fill="#34D399" letter-spacing="1.2">PRIMARY WORKSTATION</text>
    <text x="0" y="55" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="22" font-weight="800" fill="#FFFFFF">WFT</text>
    <text x="0" y="76" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="10.5" fill="#94A3B8">Process + Examine DFIR</text>
  </g>

  <!-- Divider 2 -->
  <line x1="500" y1="18" x2="500" y2="78" stroke="#1E293B" stroke-width="1"/>
  <circle cx="500" cy="48" r="2.5" fill="#34D399"/>

  <!-- Station 3: MSTeams_Parser -->
  <g transform="translate(625, 0)">
    <text x="0" y="27" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="9.5" font-weight="700" fill="#C084FC" letter-spacing="1.2">SPECIALIZED SUITE</text>
    <text x="0" y="55" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="20" font-weight="800" fill="#FFFFFF">MSTeams</text>
    <text x="0" y="76" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="10.5" fill="#94A3B8">IndexedDB / LevelDB Suite</text>
  </g>

  <!-- Divider 3 -->
  <line x1="750" y1="18" x2="750" y2="78" stroke="#1E293B" stroke-width="1"/>
  <circle cx="750" cy="48" r="2.5" fill="#C084FC"/>

  <!-- Station 4: Engine Backbone -->
  <g transform="translate(875, 0)">
    <text x="0" y="27" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="9.5" font-weight="700" fill="#FBBF24" letter-spacing="1.2">ANALYTICAL CORE</text>
    <text x="0" y="55" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="22" font-weight="800" fill="#FFFFFF">DuckDB</text>
    <text x="0" y="76" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="10.5" fill="#94A3B8">Zero-Copy Columnar Engine</text>
  </g>
</svg>"""

# ==============================================================================
# 3. ACTION BUTTONS (215 x 44 each) — Modern Interactive Hardware Action Badges
# ==============================================================================

# Button: LinkedIn
btn_linkedin = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 215 44" width="215" height="44" role="img" aria-label="LinkedIn Profile">
  <rect x="0.5" y="0.5" width="214" height="43" rx="10" fill="#0A1224" stroke="#1E293B" stroke-width="1"/>
  <path d="M12 1 H203" stroke="#0A66C2" stroke-width="1.5" stroke-opacity="0.45"/>
  <rect x="13" y="11" width="22" height="22" rx="4" fill="#0A66C2"/>
  <text x="24" y="27" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="800" fill="#FFFFFF">in</text>
  <text x="44" y="27" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="700" fill="#E2E8F0" letter-spacing="1">LINKEDIN</text>
  <text x="198" y="27" text-anchor="end" font-family="sans-serif" font-size="13" font-weight="bold" fill="#38BDF8">&#x2197;</text>
</svg>"""

# Button: Email
btn_email = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 215 44" width="215" height="44" role="img" aria-label="Direct Email">
  <rect x="0.5" y="0.5" width="214" height="43" rx="10" fill="#0A1224" stroke="#1E293B" stroke-width="1"/>
  <path d="M12 1 H203" stroke="#059669" stroke-width="1.5" stroke-opacity="0.45"/>
  <rect x="13" y="11" width="22" height="22" rx="4" fill="#065F46"/>
  <path d="M17 17 L24 22 L31 17 M17 17 H31 V27 H17 Z" fill="none" stroke="#6EE7B7" stroke-width="1.4" stroke-linejoin="round"/>
  <text x="44" y="27" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="700" fill="#E2E8F0" letter-spacing="1">EMAIL CONTACT</text>
  <text x="198" y="27" text-anchor="end" font-family="sans-serif" font-size="13" font-weight="bold" fill="#34D399">&#x2197;</text>
</svg>"""

# Button: Repositories
btn_repos = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 215 44" width="215" height="44" role="img" aria-label="All GitHub Repositories">
  <rect x="0.5" y="0.5" width="214" height="43" rx="10" fill="#0A1224" stroke="#1E293B" stroke-width="1"/>
  <path d="M12 1 H203" stroke="#D97706" stroke-width="1.5" stroke-opacity="0.45"/>
  <rect x="13" y="11" width="22" height="22" rx="4" fill="#78350F"/>
  <path d="M18 16 H24 L26 18 H30 V26 H18 Z" fill="none" stroke="#FCD34D" stroke-width="1.4" stroke-linejoin="round"/>
  <text x="44" y="27" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="700" fill="#E2E8F0" letter-spacing="1">REPOSITORIES</text>
  <text x="198" y="27" text-anchor="end" font-family="sans-serif" font-size="13" font-weight="bold" fill="#FBBF24">&#x2197;</text>
</svg>"""

# Button: CEH Certified
btn_ceh = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 215 44" width="215" height="44" role="img" aria-label="CEH Certified Ethical Hacker">
  <rect x="0.5" y="0.5" width="214" height="43" rx="10" fill="#0A1224" stroke="#1E293B" stroke-width="1"/>
  <path d="M12 1 H203" stroke="#7C3AED" stroke-width="1.5" stroke-opacity="0.45"/>
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
  <text x="24" y="80" font-family="'Segoe UI', sans-serif" font-size="11.5" fill="#94A3B8">Enterprise "Process + Examine" Digital Forensics Platform</text>
  <line x1="24" y1="92" x2="461" y2="92" stroke="#1E293B" stroke-width="1"/>

  <!-- Core Highlights -->
  <g font-family="'Segoe UI', sans-serif" font-size="11" fill="#CBD5E1">
    <text x="24" y="112"><tspan fill="#38BDF8">&#x25B8;</tspan> <tspan font-weight="600" fill="#FFFFFF">DuckDB Columnar Core:</tspan> Sub-millisecond unpivoted super-timeline</text>
    <text x="24" y="132"><tspan fill="#38BDF8">&#x25B8;</tspan> <tspan font-weight="600" fill="#FFFFFF">Dirty Registry Replay:</tspan> Automated RLA .LOG1/.LOG2 transaction commit</text>
    <text x="24" y="152"><tspan fill="#38BDF8">&#x25B8;</tspan> <tspan font-weight="600" fill="#FFFFFF">Native VFS Intake:</tspan> Direct E01, RAW, VHDX, VMDK mounting via dissect</text>
    <text x="24" y="172"><tspan fill="#38BDF8">&#x25B8;</tspan> <tspan font-weight="600" fill="#FFFFFF">Threat Hunting &amp; Carving:</tspan> Rust YARA-X scanning + RapidOCR triage</text>
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
  <text x="24" y="242" font-family="'Cascadia Code', Consolas, monospace" font-size="10" fill="#64748B">github.com/sanjeeth-solleti/WFT</text>
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
  <text x="24" y="80" font-family="'Segoe UI', sans-serif" font-size="11.5" fill="#94A3B8">Standalone Microsoft Teams DFIR Forensic Extraction Suite</text>
  <line x1="24" y1="92" x2="461" y2="92" stroke="#2E1B4E" stroke-width="1"/>

  <!-- Core Highlights -->
  <g font-family="'Segoe UI', sans-serif" font-size="11" fill="#CBD5E1">
    <text x="24" y="112"><tspan fill="#C084FC">&#x25B8;</tspan> <tspan font-weight="600" fill="#FFFFFF">Multi-Source Ingestion:</tspan> Decodes New &amp; Classic IndexedDB &amp; LevelDB</text>
    <text x="24" y="132"><tspan fill="#C084FC">&#x25B8;</tspan> <tspan font-weight="600" fill="#FFFFFF">Deep Normalization:</tspan> Base64 Adaptive Cards, calls &amp; meeting events</text>
    <text x="24" y="152"><tspan fill="#C084FC">&#x25B8;</tspan> <tspan font-weight="600" fill="#FFFFFF">Identity Correlator:</tspan> Resolves 8:orgid GUIDs to employee records</text>
    <text x="24" y="172"><tspan fill="#C084FC">&#x25B8;</tspan> <tspan font-weight="600" fill="#FFFFFF">Forensic Media Carver:</tspan> Magic-byte image recovery &amp; noise suppression</text>
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
  <text x="24" y="242" font-family="'Cascadia Code', Consolas, monospace" font-size="10" fill="#64748B">github.com/sanjeeth-solleti/MSTeams_Parser</text>
  <text x="461" y="242" text-anchor="end" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="700" fill="#C084FC">Explore Repository &#x2197;</text>
</svg>"""

# ==============================================================================
# 5. MAP.SVG (1000 x 300) — Bespoke Dual-Engine Forensic Pipeline Architecture
# ==============================================================================
map_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 300" width="1000" height="300" role="img" aria-label="DFIR Dual-Engine Architecture: WFT Platform and MSTeams_Parser Evidence Pipeline">
  <defs>
    <linearGradient id="mapbg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070C18"/>
      <stop offset="100%" stop-color="#050810"/>
    </linearGradient>
  </defs>

  <rect width="1000" height="300" rx="14" fill="url(#mapbg)"/>
  <rect x="0.5" y="0.5" width="999" height="299" rx="14" fill="none" stroke="#1E293B" stroke-width="1"/>

  <!-- Architecture Header -->
  <text x="36" y="32" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="700" fill="#38BDF8" letter-spacing="1.5">DFIR DUAL-ENGINE FORENSIC ARCHITECTURE</text>
  <text x="964" y="32" text-anchor="end" font-family="'Segoe UI', sans-serif" font-size="10.5" fill="#64748B">Deterministic Intake &#x2022; Dirty Hive Recovery &#x2022; Multi-Source Evidence Synthesis</text>
  <line x1="30" y1="44" x2="970" y2="44" stroke="#1E293B" stroke-width="1"/>

  <!-- ==================== TRACK 1: WFT (Host / Endpoint) ==================== -->
  <g transform="translate(36, 60)">
    <!-- Label -->
    <rect x="0" y="0" width="190" height="20" rx="4" fill="#0C1D38" stroke="#1D4ED8" stroke-width="1"/>
    <text x="95" y="14" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="9" font-weight="700" fill="#93C5FD" letter-spacing="1">TRACK 1: HOST &amp; ENDPOINT FORENSICS</text>

    <!-- Stage 1.1: Evidence Intake -->
    <g transform="translate(0, 30)">
      <rect width="140" height="60" rx="8" fill="#0A1428" stroke="#1E3A8A" stroke-width="1"/>
      <text x="70" y="24" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="700" fill="#FFFFFF">1. Evidence Intake</text>
      <text x="70" y="42" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="9.5" fill="#94A3B8">E01 / RAW / VHDX</text>
      <text x="70" y="53" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="9" fill="#64748B">Native Dissect VFS</text>
    </g>

    <!-- Bus Arrow 1 -->
    <path d="M140 60 H165" stroke="#38BDF8" stroke-width="1.5" stroke-dasharray="3 3"/>
    <polygon points="168,60 163,57 163,63" fill="#38BDF8"/>

    <!-- Stage 1.2: Dirty Registry Replay -->
    <g transform="translate(170, 30)">
      <rect width="150" height="60" rx="8" fill="#0A1428" stroke="#1E3A8A" stroke-width="1"/>
      <text x="75" y="24" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="700" fill="#FFFFFF">2. Registry Integrity</text>
      <text x="75" y="42" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="9.5" fill="#94A3B8">RLA .LOG1/.LOG2</text>
      <text x="75" y="53" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="9" fill="#64748B">Transaction Replay</text>
    </g>

    <!-- Bus Arrow 2 -->
    <path d="M320 60 H345" stroke="#38BDF8" stroke-width="1.5" stroke-dasharray="3 3"/>
    <polygon points="348,60 343,57 343,63" fill="#38BDF8"/>

    <!-- Stage 1.3: Deep Parsers & Hunting -->
    <g transform="translate(350, 30)">
      <rect width="150" height="60" rx="8" fill="#0A1428" stroke="#1E3A8A" stroke-width="1"/>
      <text x="75" y="24" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="700" fill="#FFFFFF">3. Toolchain &amp; Triage</text>
      <text x="75" y="42" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="9.5" fill="#94A3B8">EZ Tools + Browser WAL</text>
      <text x="75" y="53" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="9" fill="#64748B">YARA-X + RapidOCR</text>
    </g>

    <!-- Bus Arrow 3 -->
    <path d="M500 60 H525" stroke="#38BDF8" stroke-width="1.5" stroke-dasharray="3 3"/>
    <polygon points="528,60 523,57 523,63" fill="#38BDF8"/>

    <!-- Stage 1.4: WFT Core -->
    <g transform="translate(530, 30)">
      <rect width="140" height="60" rx="8" fill="#0F284E" stroke="#2563EB" stroke-width="1.4"/>
      <text x="70" y="24" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="800" fill="#38BDF8">4. WFT Platform</text>
      <text x="70" y="42" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="9.5" fill="#FFFFFF">DuckDB Engine</text>
      <text x="70" y="53" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="9" fill="#93C5FD">Zero-Copy Super-Timeline</text>
    </g>

    <!-- Connector to Output -->
    <path d="M670 60 H710" stroke="#38BDF8" stroke-width="1.5"/>
    <polygon points="712,60 707,57 707,63" fill="#38BDF8"/>
  </g>

  <!-- ==================== TRACK 2: MSTEAMS (Collaboration / Cloud) ==================== -->
  <g transform="translate(36, 172)">
    <!-- Label -->
    <rect x="0" y="0" width="210" height="20" rx="4" fill="#1C1035" stroke="#7C3AED" stroke-width="1"/>
    <text x="105" y="14" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="9" font-weight="700" fill="#C4B5FD" letter-spacing="1">TRACK 2: COLLABORATION FORENSICS</text>

    <!-- Stage 2.1: Store Ingestion -->
    <g transform="translate(0, 30)">
      <rect width="140" height="60" rx="8" fill="#140C24" stroke="#4C1D95" stroke-width="1"/>
      <text x="70" y="24" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="700" fill="#FFFFFF">1. Teams Intake</text>
      <text x="70" y="42" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="9.5" fill="#94A3B8">IndexedDB &amp; LevelDB</text>
      <text x="70" y="53" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="9" fill="#64748B">New &amp; Classic Teams</text>
    </g>

    <!-- Bus Arrow 1 -->
    <path d="M140 60 H165" stroke="#A855F7" stroke-width="1.5" stroke-dasharray="3 3"/>
    <polygon points="168,60 163,57 163,63" fill="#A855F7"/>

    <!-- Stage 2.2: Payload Normalization -->
    <g transform="translate(170, 30)">
      <rect width="150" height="60" rx="8" fill="#140C24" stroke="#4C1D95" stroke-width="1"/>
      <text x="75" y="24" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="700" fill="#FFFFFF">2. Normalization</text>
      <text x="75" y="42" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="9.5" fill="#94A3B8">Adaptive Cards Base64</text>
      <text x="75" y="53" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="9" fill="#64748B">Call Logs &amp; Events</text>
    </g>

    <!-- Bus Arrow 2 -->
    <path d="M320 60 H345" stroke="#A855F7" stroke-width="1.5" stroke-dasharray="3 3"/>
    <polygon points="348,60 343,57 343,63" fill="#A855F7"/>

    <!-- Stage 2.3: Directory & Carving -->
    <g transform="translate(350, 30)">
      <rect width="150" height="60" rx="8" fill="#140C24" stroke="#4C1D95" stroke-width="1"/>
      <text x="75" y="24" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="700" fill="#FFFFFF">3. Correlation &amp; Carve</text>
      <text x="75" y="42" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="9.5" fill="#94A3B8">GUID &#x2192; Directory Name</text>
      <text x="75" y="53" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="9" fill="#64748B">Magic Bytes Media Carve</text>
    </g>

    <!-- Bus Arrow 3 -->
    <path d="M500 60 H525" stroke="#A855F7" stroke-width="1.5" stroke-dasharray="3 3"/>
    <polygon points="528,60 523,57 523,63" fill="#A855F7"/>

    <!-- Stage 2.4: MSTeams Engine -->
    <g transform="translate(530, 30)">
      <rect width="140" height="60" rx="8" fill="#2E1254" stroke="#7C3AED" stroke-width="1.4"/>
      <text x="70" y="24" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="800" fill="#C084FC">4. MSTeams Parser</text>
      <text x="70" y="42" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="9.5" fill="#FFFFFF">Air-Gapped Suite</text>
      <text x="70" y="53" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="9" fill="#E9D5FF">Standalone Extraction</text>
    </g>

    <!-- Connector to Output -->
    <path d="M670 60 H710" stroke="#A855F7" stroke-width="1.5"/>
    <polygon points="712,60 707,57 707,63" fill="#A855F7"/>
  </g>

  <!-- ==================== SYNTHESIS OUTPUT NODE (Right) ==================== -->
  <g transform="translate(750, 88)">
    <rect width="214" height="174" rx="10" fill="#0C152B" stroke="#1E293B" stroke-width="1.2"/>
    <rect width="214" height="28" rx="10" fill="#0F1E3E"/>
    <rect y="24" width="214" height="4" fill="#0F1E3E"/>
    <text x="107" y="19" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="10.5" font-weight="700" fill="#FFFFFF" letter-spacing="1">DEFENSIBLE DFIR OUTPUTS</text>

    <g font-family="'Segoe UI', sans-serif" font-size="10.5" fill="#CBD5E1" transform="translate(14, 46)">
      <text x="0" y="0"><tspan fill="#38BDF8">&#x2714;</tspan> Master UTC Super-Timeline</text>
      <text x="0" y="26"><tspan fill="#38BDF8">&#x2714;</tspan> Cytoscape Entity Graph</text>
      <text x="0" y="52"><tspan fill="#A855F7">&#x2714;</tspan> Offline HTML Chat Viewer</text>
      <text x="0" y="78"><tspan fill="#A855F7">&#x2714;</tspan> Court-Ready Evidence CSVs</text>
      <text x="0" y="104"><tspan fill="#34D399">&#x2714;</tspan> Cryptographic Audit Hashes</text>
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
import re
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
