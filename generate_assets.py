"""
generate_assets.py
Generates all forensic SVG assets for Sanjeeth Solleti's GitHub profile.
"""
import os
import xml.etree.ElementTree as ET

ASSETS_DIR = r"C:\Users\SANJEETH\Desktop\sanjeeth-solleti\assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

def validate_and_save(filename, svg_content):
    path = os.path.join(ASSETS_DIR, filename)
    try:
        ET.fromstring(svg_content)
    except ET.ParseError as e:
        print(f"ERROR validating {filename}: {e}")
        raise
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg_content.strip())
    print(f"[OK] {filename} generated & validated ({len(svg_content)} bytes)")

# ==========================================
# 1. BANNER.SVG (1000 x 380)
# ==========================================
banner_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 380" width="1000" height="380" role="img" aria-label="Vasava Sanjeeth Solleti — DFIR. Digital forensics, incident response, tool building. deleted != gone. dirty hives != lost evidence.">
  <style>
    .g1 { animation: glitch 7s infinite steps(1); }
    .g2 { animation: glitch2 7s infinite steps(1); }
    .blink { animation: blink 1.1s infinite steps(1); }
    .pulse { animation: pulse 2s ease-in-out infinite; }
    @keyframes glitch { 0%,88%,100% { opacity:0; transform:translate(0,0) } 89% { opacity:.9; transform:translate(-4px,1px) } 91% { opacity:.9; transform:translate(3px,-2px) } 93% { opacity:0 } }
    @keyframes glitch2 { 0%,88%,100% { opacity:0; transform:translate(0,0) } 90% { opacity:.6; transform:translate(4px,2px) } 92% { opacity:.6; transform:translate(-3px,0) } 93% { opacity:0 } }
    @keyframes blink { 0%,50% { opacity:1 } 51%,100% { opacity:0 } }
    @keyframes pulse { 0%,100% { opacity:1 } 50% { opacity:.25 } }
  </style>
  <defs>
    <radialGradient id="glow" cx="50%" cy="42%" r="60%">
      <stop offset="0%" stop-color="#1FA8FF" stop-opacity="0.16"/>
      <stop offset="100%" stop-color="#1FA8FF" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="rule" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#1FA8FF" stop-opacity="0"/>
      <stop offset="50%" stop-color="#1FA8FF" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#1FA8FF" stop-opacity="0"/>
    </linearGradient>
    <pattern id="scan" width="4" height="4" patternUnits="userSpaceOnUse">
      <rect width="4" height="1" fill="#FFFFFF" opacity="0.03"/>
    </pattern>
    <clipPath id="frame"><rect width="1000" height="380" rx="14"/></clipPath>
  </defs>

  <g clip-path="url(#frame)">
    <rect width="1000" height="380" fill="#05080F"/>
    <rect width="1000" height="380" fill="url(#glow)"/>
    <rect width="1000" height="380" fill="url(#scan)"/>
    <rect x="0" y="0" width="1000" height="2" fill="url(#rule)"/>

    <!-- Subtle forensic hex watermark in background -->
    <g font-family="'Cascadia Code', 'JetBrains Mono', Consolas, monospace" font-size="11" fill="#132035" opacity="0.65">
      <text x="32" y="88">00000000  46 49 4C 45 30 00 03 00  FILE0... ($MFT)</text>
      <text x="32" y="108">00000010  01 00 00 00 38 00 01 00  ....8...</text>
      <text x="32" y="128">00000030  10 00 00 00 60 00 00 00  ....`... ($SI)</text>
      <text x="720" y="88">00000000  52 45 47 46 01 00 00 00  REGF (Hive)</text>
      <text x="720" y="108">00000020  44 49 52 54 59 5F 4C 4F  RLA REPLAY</text>
      <text x="720" y="128">00000040  30 00 00 00 78 00 00 00  0...x... ($FN)</text>
    </g>
  </g>
  <rect x="0.5" y="0.5" width="999" height="379" rx="14" fill="none" stroke="#1A2740"/>

  <!-- Corner status bar -->
  <g font-family="'Cascadia Code', 'JetBrains Mono', ui-monospace, Consolas, monospace" font-size="11" letter-spacing="2">
    <circle class="pulse" cx="36" cy="36" r="4" fill="#1FA8FF"/>
    <text x="48" y="40" fill="#8495B2">ACQUIRING &amp; TRIAGING</text>
    <text x="964" y="40" text-anchor="end" fill="#5A6A88">DFIR // TCS</text>
  </g>

  <!-- Wordmark with cyberpunk glitch effect -->
  <g font-family="'Segoe UI', -apple-system, 'Helvetica Neue', Arial, sans-serif" font-size="56" font-weight="800" letter-spacing="9" text-anchor="middle">
    <text class="g1" x="504" y="156" fill="#1FA8FF">VASAVA SANJEETH SOLLETI</text>
    <text class="g2" x="504" y="156" fill="#FF3D8B" opacity="0">VASAVA SANJEETH SOLLETI</text>
    <text x="504" y="156" fill="#EAF4FF">VASAVA SANJEETH SOLLETI</text>
  </g>

  <!-- Role tag between rules -->
  <rect x="310" y="188" width="120" height="1" fill="#0E3A66"/>
  <text x="500" y="193" text-anchor="middle" font-family="'Cascadia Code', 'JetBrains Mono', ui-monospace, Consolas, monospace" font-size="13" letter-spacing="6" fill="#1FA8FF">DFIR ANALYST</text>
  <rect x="570" y="188" width="120" height="1" fill="#0E3A66"/>

  <text x="500" y="230" text-anchor="middle" font-family="'Cascadia Code', 'JetBrains Mono', ui-monospace, Consolas, monospace" font-size="11.5" letter-spacing="3.5" fill="#8495B2">DIGITAL FORENSICS  ·  INCIDENT RESPONSE  ·  TOOL ARCHITECT</text>
  <text x="500" y="268" text-anchor="middle" font-family="'Cascadia Code', 'JetBrains Mono', ui-monospace, Consolas, monospace" font-size="16" fill="#EAF4FF">deleted <tspan fill="#1FA8FF">&#x2260;</tspan> gone  ·  dirty hives <tspan fill="#1FA8FF">&#x2260;</tspan> lost evidence<tspan class="blink" fill="#1FA8FF">&#x258C;</tspan></text>

  <!-- Status bar -->
  <rect x="32" y="306" width="936" height="1" fill="#1A2740"/>
  <rect x="496" y="302.5" width="7" height="7" fill="#1FA8FF" transform="rotate(45 499.5 306)"/>
  <g font-family="'Cascadia Code', 'JetBrains Mono', ui-monospace, Consolas, monospace" font-size="10.5" letter-spacing="2">
    <circle class="pulse" cx="38" cy="340" r="3.5" fill="#1FA8FF"/>
    <text x="50" y="344" fill="#8495B2">OPEN TO DFIR CONVERSATIONS<tspan class="blink" fill="#1FA8FF">_</tspan></text>
    <text x="964" y="344" text-anchor="end" fill="#5A6A88">WINDOWS · DUCKDB · TEAMS · EVENT LOGS · YARA-X · CEH</text>
  </g>
</svg>"""

# ==========================================
# 2. STATS.SVG (1000 x 84)
# ==========================================
stats_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 84" width="1000" height="84" role="img" aria-label="WFT Enterprise Platform · 50+ Forensic Artifacts Parsed · DuckDB Columnar Core · CEH Certified">
  <defs>
    <pattern id="statscan" width="4" height="4" patternUnits="userSpaceOnUse">
      <rect width="4" height="1" fill="#FFFFFF" opacity="0.025"/>
    </pattern>
    <clipPath id="sround"><rect width="1000" height="84" rx="12"/></clipPath>
  </defs>

  <g clip-path="url(#sround)">
    <rect width="1000" height="84" fill="#0A1020"/>
    <rect width="1000" height="84" fill="url(#statscan)"/>
  </g>
  <rect x="0.5" y="0.5" width="999" height="83" rx="12" fill="none" stroke="#1A2740"/>

  <g font-family="'Cascadia Code', 'JetBrains Mono', ui-monospace, Consolas, monospace">
    <!-- Col 1: WFT Platform -->
    <g transform="translate(125,0)">
      <text x="0" y="39" text-anchor="middle" font-family="'Segoe UI', -apple-system, sans-serif" font-size="28" font-weight="800" fill="#1FA8FF">WFT</text>
      <text x="0" y="62" text-anchor="middle" font-size="9.5" font-weight="600" fill="#8495B2" letter-spacing="2">ENTERPRISE DFIR SUITE</text>
    </g>

    <rect x="250" y="16" width="1" height="52" fill="#1A2740"/>

    <!-- Col 2: Artifacts -->
    <g transform="translate(375,0)">
      <text x="0" y="39" text-anchor="middle" font-family="'Segoe UI', -apple-system, sans-serif" font-size="28" font-weight="800" fill="#3FB950">50+</text>
      <text x="0" y="62" text-anchor="middle" font-size="9.5" font-weight="600" fill="#8495B2" letter-spacing="2">ARTIFACTS PARSED</text>
    </g>

    <rect x="500" y="16" width="1" height="52" fill="#1A2740"/>

    <!-- Col 3: Engine -->
    <g transform="translate(625,0)">
      <text x="0" y="39" text-anchor="middle" font-family="'Segoe UI', -apple-system, sans-serif" font-size="26" font-weight="800" fill="#F2C94C">DuckDB</text>
      <text x="0" y="62" text-anchor="middle" font-size="9.5" font-weight="600" fill="#8495B2" letter-spacing="2">COLUMNAR CORE</text>
    </g>

    <rect x="750" y="16" width="1" height="52" fill="#1A2740"/>

    <!-- Col 4: Certification -->
    <g transform="translate(875,0)">
      <text x="0" y="39" text-anchor="middle" font-family="'Segoe UI', -apple-system, sans-serif" font-size="28" font-weight="800" fill="#A371F7">CEH</text>
      <text x="0" y="62" text-anchor="middle" font-size="9.5" font-weight="600" fill="#8495B2" letter-spacing="2">CERTIFIED ETHICAL HACKER</text>
    </g>
  </g>
</svg>"""

# ==========================================
# 3. ACTION BUTTONS (220 x 44)
# ==========================================
def make_btn(label, accent_color, diamond_color="#1FA8FF"):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 44" width="220" height="44" role="img" aria-label="{label}">
  <path d="M8 0.5 H208 L219.5 12 V36 Q219.5 43.5 212 43.5 H8 Q0.5 43.5 0.5 36 V8 Q0.5 0.5 8 0.5 Z" fill="#0A1020" stroke="#1A2740"/>
  <path d="M208 0.5 L219.5 12" stroke="{accent_color}" stroke-width="2"/>
  <rect x="18" y="18" width="7" height="7" fill="{diamond_color}" transform="rotate(45 21.5 21.5)"/>
  <text x="36" y="27" font-family="'Cascadia Code', 'JetBrains Mono', ui-monospace, Consolas, monospace" font-size="11.5" font-weight="700" letter-spacing="2.2" fill="#EAF4FF">{label}</text>
  <text x="202" y="27" text-anchor="end" font-family="'Cascadia Code', 'JetBrains Mono', ui-monospace, Consolas, monospace" font-size="11" fill="{accent_color}">&#x2192;</text>
</svg>"""

btn_linkedin = make_btn("LINKEDIN", "#1FA8FF", "#1FA8FF")
btn_email = make_btn("EMAIL", "#2EA043", "#2EA043")
btn_repos = make_btn("ALL REPOSITORIES", "#E3B341", "#E3B341")
btn_ceh = make_btn("CEH CERTIFIED", "#A371F7", "#A371F7")

# ==========================================
# 4. EVIDENCE FLOW MAP.SVG (1000 x 380)
# ==========================================
map_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 380" width="1000" height="380" role="img" aria-label="Evidence map: RAW forensics intake flows through WFT and MSTeams_Parser into super-timelines and case reports.">
  <style>
    .flow { animation: flow 1.6s linear infinite; }
    .pulse { animation: pulse 2s ease-in-out infinite; }
    @keyframes flow { to { stroke-dashoffset: -32; } }
    @keyframes pulse { 0%,100% { opacity:1 } 50% { opacity:.3 } }
  </style>
  <defs>
    <pattern id="mapscan" width="4" height="4" patternUnits="userSpaceOnUse">
      <rect width="4" height="1" fill="#FFFFFF" opacity="0.025"/>
    </pattern>
    <clipPath id="mframe"><rect width="1000" height="380" rx="14"/></clipPath>
  </defs>

  <g clip-path="url(#mframe)">
    <rect width="1000" height="380" fill="#05080F"/>
    <rect width="1000" height="380" fill="url(#mapscan)"/>
  </g>
  <rect x="0.5" y="0.5" width="999" height="379" rx="14" fill="none" stroke="#1A2740"/>

  <!-- Header line -->
  <text x="500" y="34" text-anchor="middle" font-family="'Cascadia Code', 'JetBrains Mono', Consolas, monospace" font-size="11" letter-spacing="4" fill="#5A6A88">FORENSIC EVIDENCE &amp; ENGINE ARCHITECTURE</text>
  <text x="140" y="34" text-anchor="middle" font-family="'Cascadia Code', 'JetBrains Mono', Consolas, monospace" font-size="10" letter-spacing="2.5" fill="#8495B2">EVIDENCE SOURCES</text>
  <text x="860" y="34" text-anchor="middle" font-family="'Cascadia Code', 'JetBrains Mono', Consolas, monospace" font-size="10" letter-spacing="2.5" fill="#8495B2">CORRELATED PRODUCTS</text>

  <!-- Left: Evidence Sources (5 boxes) -->
  <!-- Box 1 -->
  <rect x="30" y="60" width="220" height="46" rx="6" fill="#0A1020" stroke="#1A2740"/>
  <circle class="pulse" cx="46" cy="83" r="3.5" fill="#1FA8FF"/>
  <text x="58" y="79" font-family="'Cascadia Code', Consolas, monospace" font-size="11" font-weight="700" fill="#EAF4FF">E01 / RAW / VHDX</text>
  <text x="58" y="94" font-family="'Segoe UI', sans-serif" font-size="9.5" fill="#8495B2">Native dissect.target VFS</text>

  <!-- Box 2 -->
  <rect x="30" y="118" width="220" height="46" rx="6" fill="#0A1020" stroke="#1A2740"/>
  <circle class="pulse" cx="46" cy="141" r="3.5" fill="#1FA8FF"/>
  <text x="58" y="137" font-family="'Cascadia Code', Consolas, monospace" font-size="11" font-weight="700" fill="#EAF4FF">NTFS $MFT / $J / Log</text>
  <text x="58" y="152" font-family="'Segoe UI', sans-serif" font-size="9.5" fill="#8495B2">MFTECmd deep file records</text>

  <!-- Box 3 -->
  <rect x="30" y="176" width="220" height="46" rx="6" fill="#0A1020" stroke="#1A2740"/>
  <circle class="pulse" cx="46" cy="199" r="3.5" fill="#1FA8FF"/>
  <text x="58" y="195" font-family="'Cascadia Code', Consolas, monospace" font-size="11" font-weight="700" fill="#EAF4FF">Dirty Registry Logs</text>
  <text x="58" y="210" font-family="'Segoe UI', sans-serif" font-size="9.5" fill="#8495B2">RLA .LOG1/.LOG2 transaction replay</text>

  <!-- Box 4 -->
  <rect x="30" y="234" width="220" height="46" rx="6" fill="#0A1020" stroke="#1A2740"/>
  <circle class="pulse" cx="46" cy="257" r="3.5" fill="#A371F7"/>
  <text x="58" y="253" font-family="'Cascadia Code', Consolas, monospace" font-size="11" font-weight="700" fill="#EAF4FF">Teams LevelDB / IdxDB</text>
  <text x="58" y="268" font-family="'Segoe UI', sans-serif" font-size="9.5" fill="#8495B2">dfindexeddb + cramjam parser</text>

  <!-- Box 5 -->
  <rect x="30" y="292" width="220" height="46" rx="6" fill="#0A1020" stroke="#1A2740"/>
  <circle class="pulse" cx="46" cy="315" r="3.5" fill="#3FB950"/>
  <text x="58" y="311" font-family="'Cascadia Code', Consolas, monospace" font-size="11" font-weight="700" fill="#EAF4FF">Browser &amp; Cloud Sync</text>
  <text x="58" y="326" font-family="'Segoe UI', sans-serif" font-size="9.5" fill="#8495B2">Chromium WAL &amp; OneDrive DB</text>

  <!-- Connecting Flow Lines (Left to Center) -->
  <path d="M250 83 C330 83, 330 150, 410 150" fill="none" stroke="#1A2740" stroke-width="1.5"/>
  <path class="flow" style="animation-delay:-0.0s" d="M250 83 C330 83, 330 150, 410 150" fill="none" stroke="#1FA8FF" stroke-width="1.5" stroke-dasharray="3 13" stroke-linecap="round"/>

  <path d="M250 141 C330 141, 330 150, 410 150" fill="none" stroke="#1A2740" stroke-width="1.5"/>
  <path class="flow" style="animation-delay:-0.3s" d="M250 141 C330 141, 330 150, 410 150" fill="none" stroke="#1FA8FF" stroke-width="1.5" stroke-dasharray="3 13" stroke-linecap="round"/>

  <path d="M250 199 C330 199, 330 160, 410 160" fill="none" stroke="#1A2740" stroke-width="1.5"/>
  <path class="flow" style="animation-delay:-0.6s" d="M250 199 C330 199, 330 160, 410 160" fill="none" stroke="#1FA8FF" stroke-width="1.5" stroke-dasharray="3 13" stroke-linecap="round"/>

  <path d="M250 257 C330 257, 330 290, 410 290" fill="none" stroke="#1A2740" stroke-width="1.5"/>
  <path class="flow" style="animation-delay:-0.9s" d="M250 257 C330 257, 330 290, 410 290" fill="none" stroke="#A371F7" stroke-width="1.5" stroke-dasharray="3 13" stroke-linecap="round"/>

  <path d="M250 315 C330 315, 330 180, 410 180" fill="none" stroke="#1A2740" stroke-width="1.5"/>
  <path class="flow" style="animation-delay:-1.2s" d="M250 315 C330 315, 330 180, 410 180" fill="none" stroke="#3FB950" stroke-width="1.5" stroke-dasharray="3 13" stroke-linecap="round"/>

  <!-- Center: Forensic Engines (2 Primary Engines) -->
  <!-- Center 1: WFT Platform (Main Engine) -->
  <rect x="410" y="80" width="180" height="135" rx="8" fill="#071A30" stroke="#0E3A66" stroke-width="1.5"/>
  <rect x="410" y="80" width="180" height="4" rx="2" fill="#1FA8FF"/>
  <text x="500" y="105" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="15" font-weight="700" fill="#EAF4FF">WFT Platform</text>
  <text x="500" y="122" text-anchor="middle" font-family="'Cascadia Code', Consolas, monospace" font-size="9" fill="#1FA8FF">ENTERPRISE WORKBENCH</text>
  <rect x="424" y="132" width="152" height="1" fill="#0E3A66"/>
  <text x="430" y="148" font-family="'Cascadia Code', Consolas, monospace" font-size="9" fill="#8495B2">&#x25AA; DuckDB Columnar</text>
  <text x="430" y="163" font-family="'Cascadia Code', Consolas, monospace" font-size="9" fill="#8495B2">&#x25AA; RLA Registry Replay</text>
  <text x="430" y="178" font-family="'Cascadia Code', Consolas, monospace" font-size="9" fill="#8495B2">&#x25AA; EZ Tools &amp; YARA-X</text>
  <text x="430" y="193" font-family="'Cascadia Code', Consolas, monospace" font-size="9" fill="#8495B2">&#x25AA; RapidOCR Carving</text>

  <!-- Center 2: MSTeams_Parser -->
  <rect x="410" y="240" width="180" height="100" rx="8" fill="#140C24" stroke="#3D2068" stroke-width="1.5"/>
  <rect x="410" y="240" width="180" height="4" rx="2" fill="#A371F7"/>
  <text x="500" y="265" text-anchor="middle" font-family="'Segoe UI', sans-serif" font-size="14" font-weight="700" fill="#EAF4FF">MSTeams_Parser</text>
  <text x="500" y="280" text-anchor="middle" font-family="'Cascadia Code', Consolas, monospace" font-size="9" fill="#A371F7">COLLABORATION DFIR</text>
  <rect x="424" y="288" width="152" height="1" fill="#3D2068"/>
  <text x="430" y="304" font-family="'Cascadia Code', Consolas, monospace" font-size="9" fill="#8495B2">&#x25AA; LevelDB &amp; Adaptive Cards</text>
  <text x="430" y="319" font-family="'Cascadia Code', Consolas, monospace" font-size="9" fill="#8495B2">&#x25AA; Contact GUID &amp; Magic Carve</text>

  <!-- Connecting Flow Lines (Center to Right) -->
  <path d="M590 120 C670 120, 670 83, 750 83" fill="none" stroke="#1A2740" stroke-width="1.5"/>
  <path class="flow" style="animation-delay:-0.2s" d="M590 120 C670 120, 670 83, 750 83" fill="none" stroke="#1FA8FF" stroke-width="1.5" stroke-dasharray="3 13" stroke-linecap="round"/>

  <path d="M590 145 C670 145, 670 141, 750 141" fill="none" stroke="#1A2740" stroke-width="1.5"/>
  <path class="flow" style="animation-delay:-0.5s" d="M590 145 C670 145, 670 141, 750 141" fill="none" stroke="#1FA8FF" stroke-width="1.5" stroke-dasharray="3 13" stroke-linecap="round"/>

  <path d="M590 280 C670 280, 670 215, 750 215" fill="none" stroke="#1A2740" stroke-width="1.5"/>
  <path class="flow" style="animation-delay:-0.8s" d="M590 280 C670 280, 670 215, 750 215" fill="none" stroke="#A371F7" stroke-width="1.5" stroke-dasharray="3 13" stroke-linecap="round"/>

  <path d="M590 180 C670 180, 670 290, 750 290" fill="none" stroke="#1A2740" stroke-width="1.5"/>
  <path class="flow" style="animation-delay:-1.1s" d="M590 180 C670 180, 670 290, 750 290" fill="none" stroke="#3FB950" stroke-width="1.5" stroke-dasharray="3 13" stroke-linecap="round"/>

  <!-- Right: Correlated Products (4 boxes) -->
  <!-- Box 1 -->
  <rect x="750" y="60" width="220" height="46" rx="6" fill="#0A1020" stroke="#1A2740"/>
  <text x="765" y="79" font-family="'Cascadia Code', Consolas, monospace" font-size="11" font-weight="700" fill="#EAF4FF">Master Super-Timeline</text>
  <text x="765" y="94" font-family="'Segoe UI', sans-serif" font-size="9.5" fill="#8495B2">Unpivoted UTC attack sequence</text>

  <!-- Box 2 -->
  <rect x="750" y="118" width="220" height="46" rx="6" fill="#0A1020" stroke="#1A2740"/>
  <text x="765" y="137" font-family="'Cascadia Code', Consolas, monospace" font-size="11" font-weight="700" fill="#EAF4FF">Cytoscape Entity Graph</text>
  <text x="765" y="152" font-family="'Segoe UI', sans-serif" font-size="9.5" fill="#8495B2">Executable, IP, hash correlation</text>

  <!-- Box 3 -->
  <rect x="750" y="192" width="220" height="46" rx="6" fill="#0A1020" stroke="#1A2740"/>
  <text x="765" y="211" font-family="'Cascadia Code', Consolas, monospace" font-size="11" font-weight="700" fill="#EAF4FF">Teams Case Viewer</text>
  <text x="765" y="226" font-family="'Segoe UI', sans-serif" font-size="9.5" fill="#8495B2">Offline chat, calls &amp; carved media</text>

  <!-- Box 4 -->
  <rect x="750" y="267" width="220" height="46" rx="6" fill="#0A1020" stroke="#1A2740"/>
  <text x="765" y="286" font-family="'Cascadia Code', Consolas, monospace" font-size="11" font-weight="700" fill="#EAF4FF">Evidentiary Reports</text>
  <text x="765" y="301" font-family="'Segoe UI', sans-serif" font-size="9.5" fill="#8495B2">Court-ready Excel CSVs &amp; HTML</text>

  <!-- Bottom status line -->
  <text x="500" y="360" text-anchor="middle" font-family="'Cascadia Code', Consolas, monospace" font-size="10" fill="#5A6A88">&#x25B6; DETERMINISTIC EXTRACTION &#x25B6; READ-ONLY VFS &#x25B6; REPRODUCIBLE TIMELINES</text>
</svg>"""

# ==========================================
# 5. CYBER CARDS (480 x 170 each)
# ==========================================
# Card 1: WFT
card_wft = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 170" width="480" height="170" role="img" aria-label="WFT — Windows Forensic Examination Platform">
  <style>
    .pulse { animation: pulse 2s ease-in-out infinite; }
    @keyframes pulse { 0%,100% { opacity:1 } 50% { opacity:.2 } }
  </style>
  <defs>
    <pattern id="wftscan" width="4" height="4" patternUnits="userSpaceOnUse">
      <rect width="4" height="1" fill="#FFFFFF" opacity="0.035"/>
    </pattern>
    <clipPath id="cwft"><path d="M12 0.5 H458 L479.5 22 V158 Q479.5 169.5 468 169.5 H12 Q0.5 169.5 0.5 158 V12 Q0.5 0.5 12 0.5 Z"/></clipPath>
  </defs>
  <g clip-path="url(#cwft)">
    <rect width="480" height="170" fill="#0A1020"/>
    <rect width="480" height="170" fill="url(#wftscan)"/>
  </g>
  <path d="M12 0.5 H458 L479.5 22 V158 Q479.5 169.5 468 169.5 H12 Q0.5 169.5 0.5 158 V12 Q0.5 0.5 12 0.5 Z" fill="none" stroke="#1A2740"/>
  <path d="M458 0.5 L479.5 22" stroke="#1FA8FF" stroke-width="2"/>

  <circle class="pulse" cx="28" cy="33" r="4" fill="#1FA8FF"/>
  <text x="42" y="37" font-family="'Cascadia Code', 'JetBrains Mono', Consolas, monospace" font-size="10.5" letter-spacing="2.2" fill="#1FA8FF">FLAGSHIP · DFIR SUITE</text>
  <text x="444" y="37" text-anchor="end" font-family="'Cascadia Code', Consolas, monospace" font-size="10.5" fill="#5A6A88">01</text>

  <text x="28" y="74" font-family="'Segoe UI', -apple-system, sans-serif" font-size="22" font-weight="700" fill="#EAF4FF">WFT — Windows Forensics</text>
  <text x="28" y="98" font-family="'Segoe UI', -apple-system, sans-serif" font-size="13" fill="#C3CEE0">DuckDB columnar core, automated RLA dirty registry replay,</text>
  <text x="28" y="117" font-family="'Segoe UI', -apple-system, sans-serif" font-size="13" fill="#8495B2">50+ EZ &amp; non-EZ parsers, super-timeline &amp; entity graph.</text>

  <rect x="28" y="130" width="424" height="1" fill="#1A2740"/>
  <text x="28" y="146" font-family="'Cascadia Code', Consolas, monospace" font-size="11" fill="#8495B2">github.com/sanjeeth-solleti/WFT</text>
  <text x="452" y="146" text-anchor="end" font-family="'Cascadia Code', Consolas, monospace" font-size="12" fill="#1FA8FF">&#x2192;</text>
</svg>"""

# Card 2: MSTeams_Parser
card_msteams = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 170" width="480" height="170" role="img" aria-label="MSTeams_Parser — Microsoft Teams Forensic Suite">
  <style>
    .pulse { animation: pulse 2s ease-in-out infinite; }
    @keyframes pulse { 0%,100% { opacity:1 } 50% { opacity:.2 } }
  </style>
  <defs>
    <pattern id="msscan" width="4" height="4" patternUnits="userSpaceOnUse">
      <rect width="4" height="1" fill="#FFFFFF" opacity="0.035"/>
    </pattern>
    <clipPath id="cms"><path d="M12 0.5 H458 L479.5 22 V158 Q479.5 169.5 468 169.5 H12 Q0.5 169.5 0.5 158 V12 Q0.5 0.5 12 0.5 Z"/></clipPath>
  </defs>
  <g clip-path="url(#cms)">
    <rect width="480" height="170" fill="#0A1020"/>
    <rect width="480" height="170" fill="url(#msscan)"/>
  </g>
  <path d="M12 0.5 H458 L479.5 22 V158 Q479.5 169.5 468 169.5 H12 Q0.5 169.5 0.5 158 V12 Q0.5 0.5 12 0.5 Z" fill="none" stroke="#1A2740"/>
  <path d="M458 0.5 L479.5 22" stroke="#A371F7" stroke-width="2"/>

  <circle class="pulse" cx="28" cy="33" r="4" fill="#A371F7"/>
  <text x="42" y="37" font-family="'Cascadia Code', 'JetBrains Mono', Consolas, monospace" font-size="10.5" letter-spacing="2.2" fill="#A371F7">COLLABORATION · DFIR</text>
  <text x="444" y="37" text-anchor="end" font-family="'Cascadia Code', Consolas, monospace" font-size="10.5" fill="#5A6A88">02</text>

  <text x="28" y="74" font-family="'Segoe UI', -apple-system, sans-serif" font-size="22" font-weight="700" fill="#EAF4FF">MSTeams_Parser</text>
  <text x="28" y="98" font-family="'Segoe UI', -apple-system, sans-serif" font-size="13" fill="#C3CEE0">LevelDB &amp; IndexedDB parser, Base64 Adaptive Cards,</text>
  <text x="28" y="117" font-family="'Segoe UI', -apple-system, sans-serif" font-size="13" fill="#8495B2">calls/meetings, GUID resolution &amp; offline media carving.</text>

  <rect x="28" y="130" width="424" height="1" fill="#1A2740"/>
  <text x="28" y="146" font-family="'Cascadia Code', Consolas, monospace" font-size="11" fill="#8495B2">github.com/sanjeeth-solleti/MSTeams_Parser</text>
  <text x="452" y="146" text-anchor="end" font-family="'Cascadia Code', Consolas, monospace" font-size="12" fill="#A371F7">&#x2192;</text>
</svg>"""

# Card 3: WFT Super-Timeline Engine
card_supertimeline = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 170" width="480" height="170" role="img" aria-label="WFT Super-Timeline — Zero-Copy Columnar Analytics">
  <style>
    .pulse { animation: pulse 2s ease-in-out infinite; }
    @keyframes pulse { 0%,100% { opacity:1 } 50% { opacity:.2 } }
  </style>
  <defs>
    <pattern id="stscan" width="4" height="4" patternUnits="userSpaceOnUse">
      <rect width="4" height="1" fill="#FFFFFF" opacity="0.035"/>
    </pattern>
    <clipPath id="cst"><path d="M12 0.5 H458 L479.5 22 V158 Q479.5 169.5 468 169.5 H12 Q0.5 169.5 0.5 158 V12 Q0.5 0.5 12 0.5 Z"/></clipPath>
  </defs>
  <g clip-path="url(#cst)">
    <rect width="480" height="170" fill="#0A1020"/>
    <rect width="480" height="170" fill="url(#stscan)"/>
  </g>
  <path d="M12 0.5 H458 L479.5 22 V158 Q479.5 169.5 468 169.5 H12 Q0.5 169.5 0.5 158 V12 Q0.5 0.5 12 0.5 Z" fill="none" stroke="#1A2740"/>
  <path d="M458 0.5 L479.5 22" stroke="#F2C94C" stroke-width="2"/>

  <circle class="pulse" cx="28" cy="33" r="4" fill="#F2C94C"/>
  <text x="42" y="37" font-family="'Cascadia Code', 'JetBrains Mono', Consolas, monospace" font-size="10.5" letter-spacing="2.2" fill="#F2C94C">ANALYTICAL CORE · TIMELINE</text>
  <text x="444" y="37" text-anchor="end" font-family="'Cascadia Code', Consolas, monospace" font-size="10.5" fill="#5A6A88">03</text>

  <text x="28" y="74" font-family="'Segoe UI', -apple-system, sans-serif" font-size="22" font-weight="700" fill="#EAF4FF">WFT Super-Timeline Core</text>
  <text x="28" y="98" font-family="'Segoe UI', -apple-system, sans-serif" font-size="13" fill="#C3CEE0">Zero-copy DuckDB unpivots all artifact timestamps across</text>
  <text x="28" y="117" font-family="'Segoe UI', -apple-system, sans-serif" font-size="13" fill="#8495B2">500,000+ records into sub-millisecond attack chronologies.</text>

  <rect x="28" y="130" width="424" height="1" fill="#1A2740"/>
  <text x="28" y="146" font-family="'Cascadia Code', Consolas, monospace" font-size="11" fill="#8495B2">sanjeeth-solleti/WFT #super-timeline</text>
  <text x="452" y="146" text-anchor="end" font-family="'Cascadia Code', Consolas, monospace" font-size="12" fill="#F2C94C">&#x2192;</text>
</svg>"""

# Card 4: Threat Hunting & Visual Inspection
card_threathunt = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 170" width="480" height="170" role="img" aria-label="YARA-X &amp; RapidOCR — Threat Hunting &amp; Inspection">
  <style>
    .pulse { animation: pulse 2s ease-in-out infinite; }
    @keyframes pulse { 0%,100% { opacity:1 } 50% { opacity:.2 } }
  </style>
  <defs>
    <pattern id="thscan" width="4" height="4" patternUnits="userSpaceOnUse">
      <rect width="4" height="1" fill="#FFFFFF" opacity="0.035"/>
    </pattern>
    <clipPath id="cth"><path d="M12 0.5 H458 L479.5 22 V158 Q479.5 169.5 468 169.5 H12 Q0.5 169.5 0.5 158 V12 Q0.5 0.5 12 0.5 Z"/></clipPath>
  </defs>
  <g clip-path="url(#cth)">
    <rect width="480" height="170" fill="#0A1020"/>
    <rect width="480" height="170" fill="url(#thscan)"/>
  </g>
  <path d="M12 0.5 H458 L479.5 22 V158 Q479.5 169.5 468 169.5 H12 Q0.5 169.5 0.5 158 V12 Q0.5 0.5 12 0.5 Z" fill="none" stroke="#1A2740"/>
  <path d="M458 0.5 L479.5 22" stroke="#3FB950" stroke-width="2"/>

  <circle class="pulse" cx="28" cy="33" r="4" fill="#3FB950"/>
  <text x="42" y="37" font-family="'Cascadia Code', 'JetBrains Mono', Consolas, monospace" font-size="10.5" letter-spacing="2.2" fill="#3FB950">THREAT HUNTING · TRIAGE</text>
  <text x="444" y="37" text-anchor="end" font-family="'Cascadia Code', Consolas, monospace" font-size="10.5" fill="#5A6A88">04</text>

  <text x="28" y="74" font-family="'Segoe UI', -apple-system, sans-serif" font-size="22" font-weight="700" fill="#EAF4FF">YARA-X &amp; RapidOCR</text>
  <text x="28" y="98" font-family="'Segoe UI', -apple-system, sans-serif" font-size="13" fill="#C3CEE0">Compiled YARA-X rule engine for webshells/LOLBins,</text>
  <text x="28" y="117" font-family="'Segoe UI', -apple-system, sans-serif" font-size="13" fill="#8495B2">RapidOCR text extraction &amp; 16-byte dual Hex inspector.</text>

  <rect x="28" y="130" width="424" height="1" fill="#1A2740"/>
  <text x="28" y="146" font-family="'Cascadia Code', Consolas, monospace" font-size="11" fill="#8495B2">sanjeeth-solleti/WFT #threat-hunting</text>
  <text x="452" y="146" text-anchor="end" font-family="'Cascadia Code', Consolas, monospace" font-size="12" fill="#3FB950">&#x2192;</text>
</svg>"""

# ==========================================
# Run Validation and Output
# ==========================================
validate_and_save("banner.svg", banner_svg)
validate_and_save("stats.svg", stats_svg)
validate_and_save("btn-linkedin.svg", btn_linkedin)
validate_and_save("btn-email.svg", btn_email)
validate_and_save("btn-repos.svg", btn_repos)
validate_and_save("btn-ceh.svg", btn_ceh)
validate_and_save("map.svg", map_svg)
validate_and_save("card-wft.svg", card_wft)
validate_and_save("card-msteams.svg", card_msteams)
validate_and_save("card-supertimeline.svg", card_supertimeline)
validate_and_save("card-threathunt.svg", card_threathunt)

# Remove unwanted foreign card if exists
privesc_path = os.path.join(ASSETS_DIR, "card-privesc.svg")
if os.path.exists(privesc_path):
    os.remove(privesc_path)
    print(f"[REMOVED] Foreign asset {privesc_path} deleted successfully.")
