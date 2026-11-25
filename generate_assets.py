"""
generate_assets.py
Generates ultra-modern, high-end DFIR SVG assets for Sanjeeth Solleti's GitHub profile.
Aesthetic inspired by Linear / Vercel / Raycast:
- Sleek dark theme (#080C16, #0D1424, #0F172A)
- Smooth radial ambient glows (electric cyan #00D2FF / #38BDF8, indigo #6366F1, violet #A855F7)
- Multi-stop gradient borders with glassmorphism styling
- Crisp, modern typography with balanced hierarchy and tracking
- Clean pill badges with micro-indicators
- Zero retro-terminal tropes, zero clunky borders, zero overlapping text
- Strictly features Sanjeeth's two genuine tools: WFT and MSTeams_Parser
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
# 1. BANNER.SVG (1000 x 300) — Modern Linear-Style Executive DFIR Banner
# ==============================================================================
banner_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 300" width="1000" height="300" role="img" aria-label="Vasava Sanjeeth Solleti — Digital Forensics &amp; Incident Response Analyst at TCS">
  <defs>
    <!-- Background Dark Gradient -->
    <linearGradient id="hero-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080C16"/>
      <stop offset="45%" stop-color="#0C1322"/>
      <stop offset="100%" stop-color="#070A12"/>
    </linearGradient>

    <!-- Ambient Cyan Radial Glow (Top Left) -->
    <radialGradient id="hero-cyan-glow" cx="15%" cy="10%" r="65%">
      <stop offset="0%" stop-color="#00D2FF" stop-opacity="0.16"/>
      <stop offset="50%" stop-color="#0284C7" stop-opacity="0.05"/>
      <stop offset="100%" stop-color="#080C16" stop-opacity="0"/>
    </radialGradient>

    <!-- Ambient Indigo/Purple Glow (Bottom Right) -->
    <radialGradient id="hero-indigo-glow" cx="88%" cy="85%" r="60%">
      <stop offset="0%" stop-color="#6366F1" stop-opacity="0.15"/>
      <stop offset="50%" stop-color="#7C3AED" stop-opacity="0.05"/>
      <stop offset="100%" stop-color="#070A12" stop-opacity="0"/>
    </radialGradient>

    <!-- Glowing Top Border Accent -->
    <linearGradient id="hero-border-accent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00D2FF" stop-opacity="0"/>
      <stop offset="20%" stop-color="#00D2FF" stop-opacity="0.8"/>
      <stop offset="55%" stop-color="#6366F1" stop-opacity="0.8"/>
      <stop offset="85%" stop-color="#A855F7" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#A855F7" stop-opacity="0"/>
    </linearGradient>

    <!-- Refined Glass Stroke -->
    <linearGradient id="hero-frame-stroke" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.35"/>
      <stop offset="40%" stop-color="#1E293B" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#334155" stop-opacity="0.3"/>
    </linearGradient>

    <!-- Widget Glass Stroke -->
    <linearGradient id="widget-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#1E293B" stop-opacity="0.6"/>
    </linearGradient>

    <!-- Modern Minimalist Grid Pattern -->
    <pattern id="modern-grid" width="28" height="28" patternUnits="userSpaceOnUse">
      <path d="M 28 0 L 0 0 0 28" fill="none" stroke="#334155" stroke-width="0.6" stroke-opacity="0.2"/>
      <circle cx="0" cy="0" r="1" fill="#38BDF8" fill-opacity="0.2"/>
    </pattern>
  </defs>

  <style>
    .pulse-dot { animation: pulseAnim 2.4s ease-in-out infinite; }
    @keyframes pulseAnim { 0%, 100% { opacity: 1; transform: scale(1); } 50% { opacity: 0.45; transform: scale(0.92); } }
    .text-title { font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-weight: 800; letter-spacing: -0.5px; }
    .text-body { font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
  </style>

  <!-- Frame Background with Ambient Lighting -->
  <rect width="1000" height="300" rx="16" fill="url(#hero-bg)"/>
  <rect width="1000" height="300" rx="16" fill="url(#hero-cyan-glow)"/>
  <rect width="1000" height="300" rx="16" fill="url(#hero-indigo-glow)"/>
  <rect width="1000" height="300" rx="16" fill="url(#modern-grid)"/>
  <rect x="0.5" y="0.5" width="999" height="299" rx="16" fill="none" stroke="url(#hero-frame-stroke)" stroke-width="1"/>
  
  <!-- Sleek Top Glow Horizon -->
  <rect x="20" y="1" width="960" height="2" rx="1" fill="url(#hero-border-accent)"/>

  <!-- Top Status Bar -->
  <g transform="translate(36, 20)">
    <!-- TCS Pill Badge (Spacious, Single text element to eliminate overlap) -->
    <rect x="0" y="0" width="310" height="24" rx="12" fill="#0E1E38" stroke="#1D4ED8" stroke-width="0.8" stroke-opacity="0.8"/>
    <circle class="pulse-dot" cx="12" cy="12" r="3.5" fill="#10B981"/>
    <text x="24" y="16" class="text-body" font-size="10" font-weight="700" fill="#38BDF8" letter-spacing="1">TATA CONSULTANCY SERVICES <tspan fill="#64748B" font-weight="400">|</tspan> <tspan fill="#94A3B8" font-weight="600">DFIR OPERATIONS</tspan></text>

    <!-- Defensible Chain Chip on Right -->
    <text x="928" y="16" text-anchor="end" class="text-body" font-size="10" font-weight="600" fill="#94A3B8" letter-spacing="0.8">DEFENSIBLE CHAIN-OF-CUSTODY &#x2022; CRYPTOGRAPHICALLY SOUND</text>
  </g>

  <!-- Thin Horizontal Horizon Line -->
  <line x1="36" y1="52" x2="964" y2="52" stroke="#1E293B" stroke-width="0.8" stroke-opacity="0.7"/>

  <!-- Left Main Content Block -->
  <g transform="translate(36, 72)">
    <!-- Role Sub-eyebrow with glow -->
    <text x="0" y="14" class="text-body" font-size="10.5" font-weight="700" fill="#38BDF8" letter-spacing="1.8">ENTERPRISE DIGITAL FORENSICS &amp; INCIDENT RESPONSE</text>
    
    <!-- Primary Identity Headline -->
    <text x="0" y="52" class="text-title" font-size="34" fill="#FFFFFF">Vasava Sanjeeth Solleti</text>
    
    <!-- Role Description -->
    <text x="0" y="78" class="text-body" font-size="14" font-weight="600" fill="#E2E8F0">
      DFIR Analyst @ TCS <tspan fill="#475569" font-weight="400">|</tspan> Windows Forensics &amp; Engine Architect
    </text>
    
    <text x="0" y="102" class="text-body" font-size="12.5" fill="#94A3B8">
      Reconstructing complex attack chronologies across raw disk images, dirty hives, &amp; cloud collaboration stores.
    </text>

    <!-- Modern Feature Capability Pills -->
    <g transform="translate(0, 126)">
      <!-- Pill 1: WFT -->
      <rect x="0" y="0" width="138" height="28" rx="8" fill="#0C1F3F" stroke="#2563EB" stroke-width="0.9"/>
      <circle cx="14" cy="14" r="3" fill="#38BDF8"/>
      <text x="24" y="18" class="text-body" font-size="10.5" font-weight="700" fill="#BAE6FD">WFT Platform</text>
      <text x="98" y="18" class="text-body" font-size="9" font-weight="500" fill="#60A5FA">DuckDB</text>

      <!-- Pill 2: MSTeams -->
      <rect x="146" y="0" width="158" height="28" rx="8" fill="#1C1138" stroke="#7C3AED" stroke-width="0.9"/>
      <circle cx="160" cy="14" r="3" fill="#C084FC"/>
      <text x="170" y="18" class="text-body" font-size="10.5" font-weight="700" fill="#E9D5FF">MSTeams_Parser</text>
      <text x="264" y="18" class="text-body" font-size="9" font-weight="500" fill="#C084FC">DFIR</text>

      <!-- Pill 3: CEH Certified -->
      <rect x="312" y="0" width="132" height="28" rx="8" fill="#09221B" stroke="#059669" stroke-width="0.9"/>
      <circle cx="326" cy="14" r="3" fill="#34D399"/>
      <text x="336" y="18" class="text-body" font-size="10.5" font-weight="700" fill="#A7F3D0">CEH Certified</text>
      <text x="412" y="18" class="text-body" font-size="9" font-weight="500" fill="#6EE7B7">v12</text>

      <!-- Pill 4: Analytical Core -->
      <rect x="452" y="0" width="136" height="28" rx="8" fill="#261A05" stroke="#D97706" stroke-width="0.9"/>
      <circle cx="466" cy="14" r="3" fill="#FBBF24"/>
      <text x="476" y="18" class="text-body" font-size="10.5" font-weight="700" fill="#FDE68A">Columnar Core</text>
      <text x="556" y="18" class="text-body" font-size="9" font-weight="500" fill="#FCD34D">&lt;1ms</text>
    </g>
  </g>

  <!-- Right Side: Sleek Glassmorphism Widget (x=634 to 964, w=330, h=170) -->
  <g transform="translate(634, 70)">
    <!-- Glass Panel Fill with subtle gradient -->
    <rect width="330" height="170" rx="12" fill="#0D1627" fill-opacity="0.85" stroke="url(#widget-border)" stroke-width="1"/>
    
    <!-- Widget Header Bar -->
    <rect width="330" height="32" rx="12" fill="#111E36" fill-opacity="0.9"/>
    <rect y="28" width="330" height="4" fill="#111E36" fill-opacity="0.9"/>
    
    <circle cx="16" cy="16" r="3.5" fill="#38BDF8"/>
    <text x="28" y="20" class="text-body" font-size="10" font-weight="700" fill="#BAE6FD" letter-spacing="1.2">SPECIALIZED INVESTIGATIVE SCOPE</text>

    <!-- Scope Items with modern iconography -->
    <g transform="translate(16, 52)" class="text-body" font-size="11">
      <!-- Item 1 -->
      <g transform="translate(0, 0)">
        <rect x="0" y="-10" width="18" height="18" rx="4" fill="#0C203E"/>
        <text x="9" y="3" text-anchor="middle" font-size="10" font-weight="bold" fill="#38BDF8">&#x25C7;</text>
        <text x="26" y="3" fill="#E2E8F0" font-weight="600">Native VFS Ingestion <tspan fill="#94A3B8" font-size="10" font-weight="normal">(E01, RAW, VHDX, VMDK)</tspan></text>
      </g>
      <!-- Item 2 -->
      <g transform="translate(0, 26)">
        <rect x="0" y="-10" width="18" height="18" rx="4" fill="#0C203E"/>
        <text x="9" y="3" text-anchor="middle" font-size="10" font-weight="bold" fill="#38BDF8">&#x25C7;</text>
        <text x="26" y="3" fill="#E2E8F0" font-weight="600">Dirty Registry Replay <tspan fill="#94A3B8" font-size="10" font-weight="normal">(Automated RLA Commit)</tspan></text>
      </g>
      <!-- Item 3 -->
      <g transform="translate(0, 52)">
        <rect x="0" y="-10" width="18" height="18" rx="4" fill="#0C203E"/>
        <text x="9" y="3" text-anchor="middle" font-size="10" font-weight="bold" fill="#38BDF8">&#x25C7;</text>
        <text x="26" y="3" fill="#E2E8F0" font-weight="600">Sub-Ms Super-Timelines <tspan fill="#94A3B8" font-size="10" font-weight="normal">(DuckDB Engine)</tspan></text>
      </g>
      <!-- Item 4 -->
      <g transform="translate(0, 78)">
        <rect x="0" y="-10" width="18" height="18" rx="4" fill="#201138"/>
        <text x="9" y="3" text-anchor="middle" font-size="10" font-weight="bold" fill="#C084FC">&#x25C7;</text>
        <text x="26" y="3" fill="#E2E8F0" font-weight="600">Collab Forensics <tspan fill="#C084FC" font-size="10" font-weight="normal">(Teams Level/IndexedDB)</tspan></text>
      </g>
    </g>
  </g>

  <!-- Bottom Telemetry Bar -->
  <line x1="36" y1="262" x2="964" y2="262" stroke="#1E293B" stroke-width="0.8" stroke-opacity="0.7"/>
  <g transform="translate(36, 280)">
    <circle class="pulse-dot" cx="4" cy="-3" r="3" fill="#00D2FF"/>
    <text x="16" y="0" class="text-body" font-size="10.5" font-weight="500" fill="#94A3B8">
      ACTIVE RESEARCH: <tspan fill="#E2E8F0">Dirty Registry Replay</tspan> &#x2022; <tspan fill="#E2E8F0">IndexedDB Messaging Stores</tspan> &#x2022; <tspan fill="#E2E8F0">Multi-Timestamp Attack Chronologies</tspan>
    </text>
    <text x="928" y="0" text-anchor="end" class="text-body" font-size="10.5" font-weight="600" fill="#94A3B8">
      HYDERABAD, INDIA
    </text>
  </g>
</svg>"""

# ==============================================================================
# 2. STATS.SVG (1000 x 96) — Sleek Glassmorphism Highlights HUD
# ==============================================================================
stats_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 96" width="1000" height="96" role="img" aria-label="Operational Telemetry: TCS DFIR Analyst, WFT Platform, MSTeams_Parser Suite, DuckDB Columnar Core">
  <defs>
    <linearGradient id="hud-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080C16"/>
      <stop offset="50%" stop-color="#0E1628"/>
      <stop offset="100%" stop-color="#090E1B"/>
    </linearGradient>
    <linearGradient id="hud-border" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.3"/>
      <stop offset="35%" stop-color="#818CF8" stop-opacity="0.3"/>
      <stop offset="70%" stop-color="#C084FC" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#34D399" stop-opacity="0.3"/>
    </linearGradient>
  </defs>

  <style>
    .hud-title { font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 21px; font-weight: 800; fill: #FFFFFF; }
    .hud-sub { font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 10.5px; fill: #94A3B8; }
    .hud-tag { font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 9.5px; font-weight: 700; letter-spacing: 1.3px; }
  </style>

  <!-- HUD Container Frame -->
  <rect width="1000" height="96" rx="14" fill="url(#hud-bg)"/>
  <rect x="0.5" y="0.5" width="999" height="95" rx="14" fill="none" stroke="url(#hud-border)" stroke-width="1"/>

  <!-- Station 1: Organization & Role (Center x=125) -->
  <g transform="translate(125, 0)">
    <text x="0" y="26" text-anchor="middle" class="hud-tag" fill="#38BDF8">ENTERPRISE DFIR</text>
    <text x="0" y="55" text-anchor="middle" class="hud-title">TCS</text>
    <text x="0" y="75" text-anchor="middle" class="hud-sub">Tata Consultancy Services</text>
  </g>

  <!-- Divider 1 -->
  <line x1="250" y1="18" x2="250" y2="78" stroke="#1E293B" stroke-width="1"/>
  <circle cx="250" cy="48" r="2.5" fill="#38BDF8" fill-opacity="0.6"/>

  <!-- Station 2: WFT Flagship Platform (Center x=375) -->
  <g transform="translate(375, 0)">
    <text x="0" y="26" text-anchor="middle" class="hud-tag" fill="#60A5FA">HOST FORENSICS</text>
    <text x="0" y="55" text-anchor="middle" class="hud-title">WFT</text>
    <text x="0" y="75" text-anchor="middle" class="hud-sub">Windows Forensics Workstation</text>
  </g>

  <!-- Divider 2 -->
  <line x1="500" y1="18" x2="500" y2="78" stroke="#1E293B" stroke-width="1"/>
  <circle cx="500" cy="48" r="2.5" fill="#818CF8" fill-opacity="0.6"/>

  <!-- Station 3: MSTeams Collaboration Suite (Center x=625) -->
  <g transform="translate(625, 0)">
    <text x="0" y="26" text-anchor="middle" class="hud-tag" fill="#C084FC">COLLAB DFIR</text>
    <text x="0" y="55" text-anchor="middle" class="hud-title">MSTeams</text>
    <text x="0" y="75" text-anchor="middle" class="hud-sub">IndexedDB &amp; LevelDB Suite</text>
  </g>

  <!-- Divider 3 -->
  <line x1="750" y1="18" x2="750" y2="78" stroke="#1E293B" stroke-width="1"/>
  <circle cx="750" cy="48" r="2.5" fill="#C084FC" fill-opacity="0.6"/>

  <!-- Station 4: Analytical Core (Center x=875) -->
  <g transform="translate(875, 0)">
    <text x="0" y="26" text-anchor="middle" class="hud-tag" fill="#34D399">ANALYTIC CORE</text>
    <text x="0" y="55" text-anchor="middle" class="hud-title">DuckDB</text>
    <text x="0" y="75" text-anchor="middle" class="hud-sub">Zero-Copy Super-Timeline</text>
  </g>
</svg>"""

# ==============================================================================
# 3. ACTION BUTTONS (215 x 44 each) — Contemporary Glass Hardware Badges
# ==============================================================================

# Button: LinkedIn
btn_linkedin = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 215 44" width="215" height="44" role="img" aria-label="LinkedIn Profile">
  <defs>
    <linearGradient id="btn-li-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0A1428"/>
      <stop offset="100%" stop-color="#0E1B36"/>
    </linearGradient>
  </defs>
  <rect x="0.5" y="0.5" width="214" height="43" rx="10" fill="url(#btn-li-grad)" stroke="#1D4ED8" stroke-width="1" stroke-opacity="0.6"/>
  <line x1="12" y1="1" x2="203" y2="1" stroke="#0A66C2" stroke-width="1.8" stroke-linecap="round"/>
  
  <!-- LinkedIn Icon -->
  <rect x="14" y="11" width="22" height="22" rx="4" fill="#0A66C2"/>
  <text x="25" y="27" text-anchor="middle" font-family="system-ui, sans-serif" font-size="13" font-weight="800" fill="#FFFFFF">in</text>
  
  <text x="46" y="27" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" fill="#F1F5F9" letter-spacing="1">LINKEDIN</text>
  <text x="198" y="27" text-anchor="end" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#38BDF8">&#x2197;</text>
</svg>"""

# Button: Email
btn_email = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 215 44" width="215" height="44" role="img" aria-label="Direct Email">
  <defs>
    <linearGradient id="btn-em-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#081A16"/>
      <stop offset="100%" stop-color="#0D2620"/>
    </linearGradient>
  </defs>
  <rect x="0.5" y="0.5" width="214" height="43" rx="10" fill="url(#btn-em-grad)" stroke="#059669" stroke-width="1" stroke-opacity="0.6"/>
  <line x1="12" y1="1" x2="203" y2="1" stroke="#10B981" stroke-width="1.8" stroke-linecap="round"/>
  
  <!-- Email Icon -->
  <rect x="14" y="11" width="22" height="22" rx="4" fill="#065F46"/>
  <path d="M18 17 L25 22 L32 17 M18 17 H32 V27 H18 Z" fill="none" stroke="#6EE7B7" stroke-width="1.4" stroke-linejoin="round"/>
  
  <text x="46" y="27" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" fill="#F1F5F9" letter-spacing="1">EMAIL CONTACT</text>
  <text x="198" y="27" text-anchor="end" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#34D399">&#x2197;</text>
</svg>"""

# Button: Repositories
btn_repos = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 215 44" width="215" height="44" role="img" aria-label="All GitHub Repositories">
  <defs>
    <linearGradient id="btn-rp-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#141126"/>
      <stop offset="100%" stop-color="#1B1736"/>
    </linearGradient>
  </defs>
  <rect x="0.5" y="0.5" width="214" height="43" rx="10" fill="url(#btn-rp-grad)" stroke="#6366F1" stroke-width="1" stroke-opacity="0.6"/>
  <line x1="12" y1="1" x2="203" y2="1" stroke="#818CF8" stroke-width="1.8" stroke-linecap="round"/>
  
  <!-- Repo Folder Icon -->
  <rect x="14" y="11" width="22" height="22" rx="4" fill="#3730A3"/>
  <path d="M19 16 H24 L26 18 H31 V26 H19 Z" fill="none" stroke="#A5B4FC" stroke-width="1.4" stroke-linejoin="round"/>
  
  <text x="46" y="27" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" fill="#F1F5F9" letter-spacing="1">REPOSITORIES</text>
  <text x="198" y="27" text-anchor="end" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" fill="#A5B4FC">&#x2197;</text>
</svg>"""

# Button: CEH Certified
btn_ceh = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 215 44" width="215" height="44" role="img" aria-label="CEH Certified Ethical Hacker">
  <defs>
    <linearGradient id="btn-ceh-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#190F2C"/>
      <stop offset="100%" stop-color="#24153E"/>
    </linearGradient>
  </defs>
  <rect x="0.5" y="0.5" width="214" height="43" rx="10" fill="url(#btn-ceh-grad)" stroke="#8B5CF6" stroke-width="1" stroke-opacity="0.6"/>
  <line x1="12" y1="1" x2="203" y2="1" stroke="#A855F7" stroke-width="1.8" stroke-linecap="round"/>
  
  <!-- Shield Icon -->
  <rect x="14" y="11" width="22" height="22" rx="4" fill="#581C87"/>
  <path d="M25 15 L30 18 V23 C30 27 25 29.5 25 29.5 C25 29.5 20 27 20 23 V18 Z" fill="none" stroke="#D8B4FE" stroke-width="1.4"/>
  
  <text x="46" y="27" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" fill="#F1F5F9" letter-spacing="1">CEH CERTIFIED</text>
  <text x="198" y="27" text-anchor="end" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#C084FC">&#x2713;</text>
</svg>"""

# ==============================================================================
# 4. FLAGSHIP TOOL CARDS (485 x 270 each) — ONLY Sanjeeth's 2 Real Tools
# ==============================================================================

# Card 1: WFT (Windows Forensic Examination Platform)
card_wft = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 485 270" width="485" height="270" role="img" aria-label="WFT — Windows Forensic Examination Platform">
  <defs>
    <linearGradient id="wft-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080E1C"/>
      <stop offset="50%" stop-color="#0C152B"/>
      <stop offset="100%" stop-color="#070B16"/>
    </linearGradient>
    <radialGradient id="wft-glow" cx="15%" cy="15%" r="65%">
      <stop offset="0%" stop-color="#00D2FF" stop-opacity="0.14"/>
      <stop offset="60%" stop-color="#1D4ED8" stop-opacity="0.04"/>
      <stop offset="100%" stop-color="#080E1C" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="wft-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.5"/>
      <stop offset="50%" stop-color="#1E3A8A" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#1E293B" stop-opacity="0.4"/>
    </linearGradient>
  </defs>

  <style>
    .pulse-wft { animation: pwft 2.4s ease-in-out infinite; }
    @keyframes pwft { 0%,100% { opacity: 1; } 50% { opacity: 0.4; } }
  </style>

  <!-- Card Frame -->
  <rect width="485" height="270" rx="14" fill="url(#wft-bg)"/>
  <rect width="485" height="270" rx="14" fill="url(#wft-glow)"/>
  <rect x="0.5" y="0.5" width="484" height="269" rx="14" fill="none" stroke="url(#wft-border)" stroke-width="1"/>
  
  <!-- Glowing Top Accent -->
  <line x1="16" y1="1" x2="469" y2="1" stroke="#38BDF8" stroke-width="1.8" stroke-linecap="round"/>

  <!-- Top Header Bar -->
  <g transform="translate(24, 20)">
    <circle class="pulse-wft" cx="4" cy="5" r="3.5" fill="#00D2FF"/>
    <text x="14" y="9" font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="700" fill="#38BDF8" letter-spacing="1.4">FLAGSHIP DFIR WORKSTATION</text>
    
    <!-- Version Pill -->
    <rect x="345" y="-3" width="92" height="20" rx="6" fill="#0E2344" stroke="#1D4ED8" stroke-width="0.8"/>
    <text x="391" y="11" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#93C5FD">v1.0 ACTIVE</text>
  </g>

  <!-- Title & Subtitle -->
  <text x="24" y="66" font-family="system-ui, -apple-system, sans-serif" font-size="21" font-weight="800" fill="#FFFFFF">WFT — Windows Forensics</text>
  <text x="24" y="85" font-family="system-ui, sans-serif" font-size="12" font-weight="500" fill="#94A3B8">Enterprise "Process + Examine" Digital Forensics Platform</text>
  
  <!-- Sleek Separator -->
  <line x1="24" y1="98" x2="461" y2="98" stroke="#1E293B" stroke-width="0.8"/>

  <!-- Core Forensic Highlights -->
  <g font-family="system-ui, -apple-system, sans-serif" font-size="11" fill="#E2E8F0" transform="translate(24, 118)">
    <g transform="translate(0, 0)">
      <circle cx="4" cy="-4" r="2.5" fill="#38BDF8"/>
      <text x="14" y="0"><tspan font-weight="700" fill="#FFFFFF">DuckDB Columnar Core:</tspan> <tspan fill="#CBD5E1">Sub-millisecond unpivoted super-timeline</tspan></text>
    </g>
    <g transform="translate(0, 20)">
      <circle cx="4" cy="-4" r="2.5" fill="#38BDF8"/>
      <text x="14" y="0"><tspan font-weight="700" fill="#FFFFFF">Dirty Registry Replay:</tspan> <tspan fill="#CBD5E1">Automated RLA .LOG1/.LOG2 transaction commit</tspan></text>
    </g>
    <g transform="translate(0, 40)">
      <circle cx="4" cy="-4" r="2.5" fill="#38BDF8"/>
      <text x="14" y="0"><tspan font-weight="700" fill="#FFFFFF">Native VFS Intake:</tspan> <tspan fill="#CBD5E1">Direct E01, RAW, VHDX, VMDK mount via dissect</tspan></text>
    </g>
    <g transform="translate(0, 60)">
      <circle cx="4" cy="-4" r="2.5" fill="#38BDF8"/>
      <text x="14" y="0"><tspan font-weight="700" fill="#FFFFFF">Threat Hunting &amp; Carving:</tspan> <tspan fill="#CBD5E1">Rust YARA-X scanning + RapidOCR triage</tspan></text>
    </g>
  </g>

  <!-- Divider before pills -->
  <line x1="24" y1="198" x2="461" y2="198" stroke="#1E293B" stroke-width="0.8"/>

  <!-- Modern Tech Stack Pills -->
  <g transform="translate(24, 208)">
    <rect x="0" y="0" width="62" height="22" rx="6" fill="#0C203E" stroke="#1D4ED8" stroke-width="0.6"/>
    <text x="31" y="15" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" fill="#93C5FD">DuckDB</text>

    <rect x="68" y="0" width="58" height="22" rx="6" fill="#0C203E" stroke="#1D4ED8" stroke-width="0.6"/>
    <text x="97" y="15" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" fill="#93C5FD">FastAPI</text>

    <rect x="132" y="0" width="64" height="22" rx="6" fill="#0C203E" stroke="#1D4ED8" stroke-width="0.6"/>
    <text x="164" y="15" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" fill="#93C5FD">React 18</text>

    <rect x="202" y="0" width="70" height="22" rx="6" fill="#0C203E" stroke="#1D4ED8" stroke-width="0.6"/>
    <text x="237" y="15" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" fill="#93C5FD">Cytoscape</text>

    <rect x="278" y="0" width="60" height="22" rx="6" fill="#0C203E" stroke="#1D4ED8" stroke-width="0.6"/>
    <text x="308" y="15" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" fill="#93C5FD">YARA-X</text>

    <rect x="344" y="0" width="62" height="22" rx="6" fill="#0C203E" stroke="#1D4ED8" stroke-width="0.6"/>
    <text x="375" y="15" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" fill="#93C5FD">AG Grid</text>
  </g>

  <!-- Bottom Link Bar -->
  <g transform="translate(24, 252)">
    <text x="0" y="0" font-family="'SFMono-Regular', Consolas, monospace" font-size="10" fill="#64748B">github.com/sanjeeth-solleti/WFT</text>
    <text x="437" y="0" text-anchor="end" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#38BDF8">Explore Repository &#x2192;</text>
  </g>
</svg>"""

# Card 2: MSTeams_Parser (Microsoft Teams DFIR Forensic Suite)
card_msteams = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 485 270" width="485" height="270" role="img" aria-label="MSTeams_Parser — Microsoft Teams DFIR Forensic Suite">
  <defs>
    <linearGradient id="ms-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#110B22"/>
      <stop offset="50%" stop-color="#181032"/>
      <stop offset="100%" stop-color="#0A0614"/>
    </linearGradient>
    <radialGradient id="ms-glow" cx="15%" cy="15%" r="65%">
      <stop offset="0%" stop-color="#A855F7" stop-opacity="0.16"/>
      <stop offset="60%" stop-color="#6B21A8" stop-opacity="0.04"/>
      <stop offset="100%" stop-color="#110B22" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="ms-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#C084FC" stop-opacity="0.5"/>
      <stop offset="50%" stop-color="#7C3AED" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#1E293B" stop-opacity="0.4"/>
    </linearGradient>
  </defs>

  <style>
    .pulse-ms { animation: pms 2.4s ease-in-out infinite; }
    @keyframes pms { 0%,100% { opacity: 1; } 50% { opacity: 0.4; } }
  </style>

  <!-- Card Frame -->
  <rect width="485" height="270" rx="14" fill="url(#ms-bg)"/>
  <rect width="485" height="270" rx="14" fill="url(#ms-glow)"/>
  <rect x="0.5" y="0.5" width="484" height="269" rx="14" fill="none" stroke="url(#ms-border)" stroke-width="1"/>
  
  <!-- Glowing Top Accent -->
  <line x1="16" y1="1" x2="469" y2="1" stroke="#A855F7" stroke-width="1.8" stroke-linecap="round"/>

  <!-- Top Header Bar -->
  <g transform="translate(24, 20)">
    <circle class="pulse-ms" cx="4" cy="5" r="3.5" fill="#A855F7"/>
    <text x="14" y="9" font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="700" fill="#C084FC" letter-spacing="1.4">COLLABORATION DFIR SUITE</text>
    
    <!-- Air-gapped badge -->
    <rect x="317" y="-3" width="120" height="20" rx="6" fill="#291142" stroke="#7C3AED" stroke-width="0.8"/>
    <text x="377" y="11" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#E9D5FF">AIR-GAPPED 127.0.0.1</text>
  </g>

  <!-- Title & Subtitle -->
  <text x="24" y="66" font-family="system-ui, -apple-system, sans-serif" font-size="21" font-weight="800" fill="#FFFFFF">MSTeams_Parser</text>
  <text x="24" y="85" font-family="system-ui, sans-serif" font-size="12" font-weight="500" fill="#94A3B8">Standalone Microsoft Teams DFIR Forensic Suite</text>
  
  <!-- Sleek Separator -->
  <line x1="24" y1="98" x2="461" y2="98" stroke="#25163D" stroke-width="0.8"/>

  <!-- Core Forensic Highlights -->
  <g font-family="system-ui, -apple-system, sans-serif" font-size="11" fill="#E2E8F0" transform="translate(24, 118)">
    <g transform="translate(0, 0)">
      <circle cx="4" cy="-4" r="2.5" fill="#C084FC"/>
      <text x="14" y="0"><tspan font-weight="700" fill="#FFFFFF">Multi-Source Ingestion:</tspan> <tspan fill="#CBD5E1">Decodes New &amp; Classic IndexedDB &amp; LevelDB</tspan></text>
    </g>
    <g transform="translate(0, 20)">
      <circle cx="4" cy="-4" r="2.5" fill="#C084FC"/>
      <text x="14" y="0"><tspan font-weight="700" fill="#FFFFFF">Deep Normalization:</tspan> <tspan fill="#CBD5E1">Base64 Adaptive Cards, call logs &amp; meeting events</tspan></text>
    </g>
    <g transform="translate(0, 40)">
      <circle cx="4" cy="-4" r="2.5" fill="#C084FC"/>
      <text x="14" y="0"><tspan font-weight="700" fill="#FFFFFF">Identity Correlator:</tspan> <tspan fill="#CBD5E1">Resolves 8:orgid GUIDs to employee records</tspan></text>
    </g>
    <g transform="translate(0, 60)">
      <circle cx="4" cy="-4" r="2.5" fill="#C084FC"/>
      <text x="14" y="0"><tspan font-weight="700" fill="#FFFFFF">Forensic Media Carver:</tspan> <tspan fill="#CBD5E1">Magic-byte image recovery &amp; noise suppression</tspan></text>
    </g>
  </g>

  <!-- Divider before pills -->
  <line x1="24" y1="198" x2="461" y2="198" stroke="#25163D" stroke-width="0.8"/>

  <!-- Modern Tech Stack Pills -->
  <g transform="translate(24, 208)">
    <rect x="0" y="0" width="62" height="22" rx="6" fill="#24103C" stroke="#7C3AED" stroke-width="0.6"/>
    <text x="31" y="15" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" fill="#E9D5FF">LevelDB</text>

    <rect x="68" y="0" width="72" height="22" rx="6" fill="#24103C" stroke="#7C3AED" stroke-width="0.6"/>
    <text x="104" y="15" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" fill="#E9D5FF">IndexedDB</text>

    <rect x="146" y="0" width="84" height="22" rx="6" fill="#24103C" stroke="#7C3AED" stroke-width="0.6"/>
    <text x="188" y="15" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" fill="#E9D5FF">dfindexeddb</text>

    <rect x="236" y="0" width="68" height="22" rx="6" fill="#24103C" stroke="#7C3AED" stroke-width="0.6"/>
    <text x="270" y="15" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" fill="#E9D5FF">cramjam</text>

    <rect x="310" y="0" width="86" height="22" rx="6" fill="#24103C" stroke="#7C3AED" stroke-width="0.6"/>
    <text x="353" y="15" text-anchor="middle" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" fill="#E9D5FF">HTML Viewer</text>
  </g>

  <!-- Bottom Link Bar -->
  <g transform="translate(24, 252)">
    <text x="0" y="0" font-family="'SFMono-Regular', Consolas, monospace" font-size="10" fill="#64748B">github.com/sanjeeth-solleti/MSTeams_Parser</text>
    <text x="437" y="0" text-anchor="end" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#C084FC">Explore Repository &#x2192;</text>
  </g>
</svg>"""

# ==============================================================================
# 5. MAP.SVG (1000 x 340) — Contemporary DFIR Architecture Pipeline
# ==============================================================================
map_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 340" width="1000" height="340" role="img" aria-label="DFIR Dual-Engine Forensic Pipeline Architecture: WFT Platform and MSTeams_Parser Synthesis">
  <defs>
    <!-- Background Gradient -->
    <linearGradient id="map-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080C16"/>
      <stop offset="50%" stop-color="#0B1322"/>
      <stop offset="100%" stop-color="#070A12"/>
    </linearGradient>

    <!-- Outer Border Stroke -->
    <linearGradient id="map-border" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.3"/>
      <stop offset="50%" stop-color="#818CF8" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#10B981" stop-opacity="0.3"/>
    </linearGradient>

    <!-- WFT Flow Arrow Gradient -->
    <linearGradient id="arrow-cyan" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#38BDF8" stop-opacity="1"/>
    </linearGradient>

    <!-- MSTeams Flow Arrow Gradient -->
    <linearGradient id="arrow-purple" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#A855F7" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#A855F7" stop-opacity="1"/>
    </linearGradient>
  </defs>

  <style>
    .arch-title { font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
    .pulse-dot-c { animation: pcyan 2s ease-in-out infinite; }
    .pulse-dot-p { animation: ppurple 2s ease-in-out infinite; }
    @keyframes pcyan { 0%,100% { opacity: 1; } 50% { opacity: 0.35; } }
    @keyframes ppurple { 0%,100% { opacity: 1; } 50% { opacity: 0.35; } }
  </style>

  <!-- Canvas Frame -->
  <rect width="1000" height="340" rx="16" fill="url(#map-bg)"/>
  <rect x="0.5" y="0.5" width="999" height="339" rx="16" fill="none" stroke="url(#map-border)" stroke-width="1"/>

  <!-- Architecture Header Bar (Single text element to avoid overlap) -->
  <g transform="translate(36, 24)">
    <text x="0" y="10" class="arch-title" font-size="11" font-weight="700" fill="#38BDF8" letter-spacing="1.2">DFIR DUAL-ENGINE ARCHITECTURE <tspan fill="#475569" font-weight="400">//</tspan> <tspan fill="#94A3B8" font-weight="600">DETERMINISTIC INGESTION &#x2022; DIRTY HIVE REPLAY &#x2022; DEFENSIBLE SYNTHESIS</tspan></text>
    <text x="928" y="10" text-anchor="end" class="arch-title" font-size="10.5" font-weight="600" fill="#94A3B8">TCS FORENSIC OPERATIONS</text>
  </g>
  <line x1="36" y1="46" x2="964" y2="46" stroke="#1E293B" stroke-width="0.8"/>

  <!-- ==================== TRACK 1: HOST & ENDPOINT FORENSICS (WFT) ==================== -->
  <g transform="translate(36, 62)">
    <!-- Track Header Chip -->
    <rect x="0" y="0" width="270" height="22" rx="6" fill="#0C203E" stroke="#1D4ED8" stroke-width="0.8"/>
    <circle class="pulse-dot-c" cx="12" cy="11" r="3" fill="#38BDF8"/>
    <text x="24" y="15" class="arch-title" font-size="9.5" font-weight="700" fill="#BAE6FD" letter-spacing="1">TRACK 1: HOST &amp; DISK FORENSICS (WFT)</text>

    <!-- Stage 1.1: Evidence Intake -->
    <g transform="translate(0, 32)">
      <rect width="190" height="78" rx="10" fill="#0A152A" stroke="#1E3A8A" stroke-width="0.9"/>
      <text x="95" y="24" text-anchor="middle" class="arch-title" font-size="11.5" font-weight="700" fill="#FFFFFF">1. Disk Evidence Intake</text>
      <text x="95" y="44" text-anchor="middle" class="arch-title" font-size="10.5" fill="#94A3B8">E01, RAW, VHDX, VMDK</text>
      <text x="95" y="64" text-anchor="middle" class="arch-title" font-size="10" font-weight="600" fill="#38BDF8">Native Dissect VFS Mount</text>
    </g>

    <!-- Flow Connector 1 -> 2 -->
    <path d="M190 71 H228" stroke="url(#arrow-cyan)" stroke-width="1.8"/>
    <polygon points="230,71 223,67.5 223,74.5" fill="#38BDF8"/>

    <!-- Stage 1.2: Dirty Registry Replay -->
    <g transform="translate(232, 32)">
      <rect width="190" height="78" rx="10" fill="#0A152A" stroke="#1E3A8A" stroke-width="0.9"/>
      <text x="95" y="24" text-anchor="middle" class="arch-title" font-size="11.5" font-weight="700" fill="#FFFFFF">2. Registry Integrity</text>
      <text x="95" y="44" text-anchor="middle" class="arch-title" font-size="10.5" fill="#94A3B8">RLA .LOG1/.LOG2 Replay</text>
      <text x="95" y="64" text-anchor="middle" class="arch-title" font-size="10" font-weight="600" fill="#38BDF8">Transaction Log Commit</text>
    </g>

    <!-- Flow Connector 2 -> 3 -->
    <path d="M422 71 H460" stroke="url(#arrow-cyan)" stroke-width="1.8"/>
    <polygon points="462,71 455,67.5 455,74.5" fill="#38BDF8"/>

    <!-- Stage 1.3: Super-Timeline & Triage Engine -->
    <g transform="translate(464, 32)">
      <rect width="190" height="78" rx="10" fill="#0F2447" stroke="#2563EB" stroke-width="1.2"/>
      <text x="95" y="24" text-anchor="middle" class="arch-title" font-size="11.5" font-weight="800" fill="#38BDF8">3. WFT Analytic Core</text>
      <text x="95" y="44" text-anchor="middle" class="arch-title" font-size="10.5" font-weight="600" fill="#FFFFFF">DuckDB Columnar Core</text>
      <text x="95" y="64" text-anchor="middle" class="arch-title" font-size="10" font-weight="600" fill="#93C5FD">Sub-Ms Timeline · YARA-X</text>
    </g>

    <!-- Connector Track 1 -> Synthesis Core (Cleanly reaches Dossier at x=734) -->
    <path d="M654 71 H730" stroke="url(#arrow-cyan)" stroke-width="1.8"/>
    <polygon points="732,71 724,67.5 724,74.5" fill="#38BDF8"/>
  </g>

  <!-- ==================== TRACK 2: COLLABORATION FORENSICS (MSTEAMS) ==================== -->
  <g transform="translate(36, 192)">
    <!-- Track Header Chip -->
    <rect x="0" y="0" width="290" height="22" rx="6" fill="#1C1138" stroke="#7C3AED" stroke-width="0.8"/>
    <circle class="pulse-dot-p" cx="12" cy="11" r="3" fill="#C084FC"/>
    <text x="24" y="15" class="arch-title" font-size="9.5" font-weight="700" fill="#E9D5FF" letter-spacing="1">TRACK 2: COLLABORATION FORENSICS (MSTEAMS)</text>

    <!-- Stage 2.1: Store Ingestion -->
    <g transform="translate(0, 32)">
      <rect width="190" height="78" rx="10" fill="#140D26" stroke="#4C1D95" stroke-width="0.9"/>
      <text x="95" y="24" text-anchor="middle" class="arch-title" font-size="11.5" font-weight="700" fill="#FFFFFF">1. Messaging Intake</text>
      <text x="95" y="44" text-anchor="middle" class="arch-title" font-size="10.5" fill="#94A3B8">IndexedDB &amp; LevelDB Stores</text>
      <text x="95" y="64" text-anchor="middle" class="arch-title" font-size="10" font-weight="600" fill="#C084FC">New &amp; Classic Teams Cache</text>
    </g>

    <!-- Flow Connector 1 -> 2 -->
    <path d="M190 71 H228" stroke="url(#arrow-purple)" stroke-width="1.8"/>
    <polygon points="230,71 223,67.5 223,74.5" fill="#A855F7"/>

    <!-- Stage 2.2: Payload Normalization -->
    <g transform="translate(232, 32)">
      <rect width="190" height="78" rx="10" fill="#140D26" stroke="#4C1D95" stroke-width="0.9"/>
      <text x="95" y="24" text-anchor="middle" class="arch-title" font-size="11.5" font-weight="700" fill="#FFFFFF">2. Event Normalization</text>
      <text x="95" y="44" text-anchor="middle" class="arch-title" font-size="10.5" fill="#94A3B8">Base64 Adaptive Cards &amp; Calls</text>
      <text x="95" y="64" text-anchor="middle" class="arch-title" font-size="10" font-weight="600" fill="#C084FC">8:orgid GUID &#x2192; Directory Name</text>
    </g>

    <!-- Flow Connector 2 -> 3 -->
    <path d="M422 71 H460" stroke="url(#arrow-purple)" stroke-width="1.8"/>
    <polygon points="462,71 455,67.5 455,74.5" fill="#A855F7"/>

    <!-- Stage 2.3: MSTeams Engine & Carve -->
    <g transform="translate(464, 32)">
      <rect width="190" height="78" rx="10" fill="#2E1254" stroke="#7C3AED" stroke-width="1.2"/>
      <text x="95" y="24" text-anchor="middle" class="arch-title" font-size="11.5" font-weight="800" fill="#C084FC">3. MSTeams Parser</text>
      <text x="95" y="44" text-anchor="middle" class="arch-title" font-size="10.5" font-weight="600" fill="#FFFFFF">Air-Gapped 127.0.0.1</text>
      <text x="95" y="64" text-anchor="middle" class="arch-title" font-size="10" font-weight="600" fill="#E9D5FF">Magic-Byte Media Carving</text>
    </g>

    <!-- Connector Track 2 -> Synthesis Core (Cleanly reaches Dossier at x=734) -->
    <path d="M654 71 H730" stroke="url(#arrow-purple)" stroke-width="1.8"/>
    <polygon points="732,71 724,67.5 724,74.5" fill="#A855F7"/>
  </g>

  <!-- ==================== SYNTHESIS OUTPUT NODE (Right) ==================== -->
  <g transform="translate(734, 76)">
    <!-- Outer Glass Container -->
    <rect width="230" height="236" rx="12" fill="#0C152B" stroke="#1E293B" stroke-width="1.2"/>
    <rect width="230" height="32" rx="12" fill="#102042"/>
    <rect y="28" width="230" height="4" fill="#102042"/>
    
    <circle cx="16" cy="16" r="3.5" fill="#10B981"/>
    <text x="28" y="20" class="arch-title" font-size="10.5" font-weight="700" fill="#FFFFFF" letter-spacing="1">DEFENSIBLE DFIR DOSSIER</text>

    <!-- Feature Checklist -->
    <g class="arch-title" font-size="11" fill="#E2E8F0" transform="translate(16, 56)">
      <!-- Item 1 -->
      <g transform="translate(0, 0)">
        <text x="0" y="0" font-weight="bold" fill="#38BDF8">&#x2714;</text>
        <text x="18" y="0">Master UTC Super-Timeline</text>
        <text x="18" y="16" font-size="9.5" fill="#94A3B8">Cross-source chronologies</text>
      </g>
      <!-- Item 2 -->
      <g transform="translate(0, 36)">
        <text x="0" y="0" font-weight="bold" fill="#38BDF8">&#x2714;</text>
        <text x="18" y="0">Cytoscape Entity Graph</text>
        <text x="18" y="16" font-size="9.5" fill="#94A3B8">Relational binary/IP nodes</text>
      </g>
      <!-- Item 3 -->
      <g transform="translate(0, 72)">
        <text x="0" y="0" font-weight="bold" fill="#C084FC">&#x2714;</text>
        <text x="18" y="0">Offline HTML Chat Viewer</text>
        <text x="18" y="16" font-size="9.5" fill="#94A3B8">Decoded conversation dossiers</text>
      </g>
      <!-- Item 4 -->
      <g transform="translate(0, 108)">
        <text x="0" y="0" font-weight="bold" fill="#C084FC">&#x2714;</text>
        <text x="18" y="0">Court-Ready CSV Exports</text>
        <text x="18" y="16" font-size="9.5" fill="#94A3B8">UTF-8 BOM standardized</text>
      </g>
      <!-- Item 5 -->
      <g transform="translate(0, 144)">
        <text x="0" y="0" font-weight="bold" fill="#10B981">&#x2714;</text>
        <text x="18" y="0">SHA-256 Audit Hashes</text>
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
