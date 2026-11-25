<p align="center">
  <img src="assets/banner.svg" alt="Vasava Sanjeeth Solleti — Digital Forensics &amp; Incident Response" width="100%">
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/sanjeeth-solleti/"><img src="assets/btn-linkedin.svg" alt="LinkedIn" height="38"></a>
  <a href="mailto:vasavasanjeeth@gmail.com"><img src="assets/btn-email.svg" alt="Email" height="38"></a>
  <a href="https://github.com/sanjeeth-solleti?tab=repositories"><img src="assets/btn-repos.svg" alt="All Repositories" height="38"></a>
  <img src="assets/btn-ceh.svg" alt="CEH Certified" height="38">
</p>

<p align="center">
  <img src="assets/stats.svg" alt="TCS DFIR Analyst · WFT Enterprise Platform · MSTeams_Parser Suite · DuckDB Columnar Core" width="100%">
</p>

<br>

## Executive Profile

Digital Forensics &amp; Incident Response (**DFIR**) Analyst at **Tata Consultancy Services (TCS)**, specializing in enterprise Windows endpoint forensics, deep triage, cloud collaboration evidence, and end-to-end attack timeline reconstruction.

Forensic investigations routinely encounter critical failure points where standard commercial suites slow down or stop short—unflushed registry transactions locked in volatile `.LOG` files, high-volume event streams exceeding millions of rows, or undocumented IndexedDB and LevelDB messaging stores. My focus centers on building forensically sound, deterministic engines that ingest raw disk containers, replay transactions, and correlate cross-source telemetry into unshakeable, defensible chronologies.

| Domain | Technical Scope &amp; Forensic Focus |
| :--- | :--- |
| **Endpoint Forensics** | Windows 10 / 11 / Server · Disk containers (`.E01`, `.RAW`, `.VHDX`, `.VMDK`) · Low-level NTFS (`$MFT`, `$LogFile`, `$UsnJrnl`) |
| **Registry Integrity** | Automated dirty transaction log replay (`.LOG1` / `.LOG2` via RLA) · Multi-hive correlation (`SAM`, `SYSTEM`, `SOFTWARE`, `NTUSER`) |
| **Execution Triage** | PECmd (Prefetch) · AppCompatCache (Shimcache) · Amcache · UserAssist · BAM/DAM · SRUM metrics |
| **Collaboration &amp; Cloud** | Microsoft Teams (LevelDB/IndexedDB) · Discord · Slack · OneDrive sync database · Google Drive metadata |
| **Browser Forensics** | Chromium SQLite + WAL recovery (Chrome/Edge/Brave) · Firefox `places.sqlite` (PRTime conversion) |
| **Threat Hunting** | Compiled Rust YARA-X scanning · RapidOCR on carved artifacts · LOLBins &amp; webshell detection |
| **Analytical Stack** | Python 3.10+ · DuckDB Columnar Engine · FastAPI · React 18 / TypeScript · AG Grid · Cytoscape |

<br>

## DFIR Dual-Engine Architecture

<p align="center">
  <img src="assets/map.svg" alt="DFIR Dual-Engine Architecture: WFT Platform and MSTeams_Parser evidence intake, dirty hive replay, and cross-source timeline correlation." width="100%">
</p>

<br>

## Flagship DFIR Workstations & Tooling

<p align="center">
  <a href="https://github.com/sanjeeth-solleti/WFT"><img src="assets/card-wft.svg" alt="WFT — Windows Forensic Examination Platform" width="49%"></a>
  <a href="https://github.com/sanjeeth-solleti/MSTeams_Parser"><img src="assets/card-msteams.svg" alt="MSTeams_Parser — Microsoft Teams Forensic Suite" width="49%"></a>
</p>

<br>

### 1. [WFT — Windows Forensic Examination Platform](https://github.com/sanjeeth-solleti/WFT)

An enterprise-grade Windows Digital Forensics and Incident Response platform engineered for comprehensive investigation (**Process + Examine**). WFT integrates virtual file system disk mounting, automated dirty registry transaction replay, external CLI toolchain orchestration, custom non-EZ parsers, YARA-X scanning, and RapidOCR into an unified analytics workstation.

- **Zero-Copy DuckDB Columnar Core:** In-process columnar analytical database delivering sub-millisecond queries, live multi-timestamp super-timelines unpivoted across all artifacts, and zero-latency filtering over 500,000+ forensic records.
- **Native Evidence Intake &amp; VFS:** Direct mounting and forensic extraction from `.E01`, `.Ex01`, `.VHDX`, `.VHD`, `.VMDK`, `.RAW`, `.DD`, and `.ISO` disk containers via native `dissect.target` VFS, as well as live triage folders.
- **Automated Registry Integrity:** Mandatory automated dirty registry transaction log replay (`.LOG1` / `.LOG2` via RLA) before hive analysis to ensure no unflushed forensic transactions are lost.
- **Full Eric Zimmerman Toolchain Orchestration:** Seamless batch processing with PECmd (Prefetch), MFTECmd ($MFT, $J, $LogFile), EvtxECmd (Event Logs), RECmd (Batch Registry), LECmd (LNK Shortcuts), JLECmd (Jump Lists), AmcacheParser, AppCompatCacheParser (Shimcache), SBECmd (ShellBags), SrumECmd (SRUM metrics), WxTCmd (ActivitiesCache), and SQLECmd.
- **Non-EZ Native Forensic Parsers:**
  - *Browsers:* Chromium (Chrome, Edge, Brave) and Firefox databases with full WAL recovery for History, Downloads, and Login Data.
  - *Collaboration:* Microsoft Teams, Discord, and Slack IndexedDB / LevelDB message parsing.
  - *Cloud Sync:* OneDrive (`SyncEngineDatabase.db`) and Google Drive synced metadata.
  - *USB Device Correlator:* Multi-hive correlation cross-referencing `setupapi.dev.log` with `SYSTEM` (`USBSTOR`, `MountedDevices`) and `SOFTWARE` (`EMDMgmt`) to reconstruct end-to-end device connection histories.
  - *Document &amp; MOTW Parser:* Metadata extraction with Mark-of-the-Web (`Zone.Identifier`) zone parsing.
- **Threat Hunting &amp; Inspection:** Rust-based compiled YARA-X rule engine scanning for webshells, beacons, and LOLBins, accompanied by RapidOCR text extraction from carved screenshots, receipts, and images.
- **Examiner UI:** Virtualized AG Grid with dynamic bookmarks, FTK Imager-style NTFS directory browser, interactive Cytoscape network entity graph linking IPs, binaries, and accounts, plus an integrated 16-byte dual Hex/ASCII inspector.

<br>

### 2. [MSTeams_Parser — Microsoft Teams DFIR Forensic Suite](https://github.com/sanjeeth-solleti/MSTeams_Parser)

A standalone DFIR suite engineered for parsing, reconstructing, and analyzing Microsoft Teams communication artifacts from raw forensic disk images and live triage extractions.

- **Air-Gapped Forensic Safety:** Embedded server binds strictly to `127.0.0.1`. Absolutely no data leaves the workstation, upholding forensic confidentiality.
- **Multi-Source Ingestion Pipeline:** Ingests New Teams (`%LOCALAPPDATA%\Packages\MSTeams_8wekyb3d8bbwe\...\IndexedDB`) and Classic Teams (`%APPDATA%\Microsoft\Teams\IndexedDB`), raw LevelDB files with `dfindexeddb` & `cramjam`, pre-parsed UTF-16 JSON dumps, and candidate CSV logs.
- **Message Normalization &amp; Event Parsing:** Unpacks raw XML/JSON markup into intelligible timelines: Base64 JSON Adaptive Cards, call started/ended events with participant lists and durations, meeting policy updates, member role changes, and file shares.
- **Identity &amp; Contact Resolution:** Resolves internal GUIDs (`8:orgid:<guid>`) to real employee names, emails, job roles, and corporate directory records.
- **Carving &amp; Telemetry Suppression:** Carves cached images and attachments, identifying file headers via magic bytes while automatically filtering UI telemetry, emojis, and noise (< 3.5 KB).
- **Examiner Reporting:** Standalone HTML chat viewer, Excel-ready CSV summaries (UTF-8 BOM), ZIP media bundle, audit log, and dual UTC/IST timestamps.

<br>

## Field Kit & Technical Arsenal

<table>
<tr><td width="22%"><b>Forensic Suites</b></td><td>

![Magnet AXIOM](https://img.shields.io/badge/Magnet_AXIOM-161B22?style=flat-square&labelColor=161B22&color=58A6FF)
![FTK Imager](https://img.shields.io/badge/FTK_Imager-161B22?style=flat-square&labelColor=161B22&color=58A6FF)
![EnCase](https://img.shields.io/badge/EnCase-161B22?style=flat-square&labelColor=161B22&color=58A6FF)
![Cellebrite UFED](https://img.shields.io/badge/Cellebrite_UFED-161B22?style=flat-square&labelColor=161B22&color=58A6FF)
![Volatility 3](https://img.shields.io/badge/Volatility_3-161B22?style=flat-square&labelColor=161B22&color=3FB950)
![RegRipper 4.0](https://img.shields.io/badge/RegRipper_4.0-161B22?style=flat-square&labelColor=161B22&color=3FB950)
![Eric Zimmerman Tools](https://img.shields.io/badge/Eric_Zimmerman_Tools-161B22?style=flat-square&labelColor=161B22&color=3FB950)
![DuckDB](https://img.shields.io/badge/DuckDB-161B22?style=flat-square&labelColor=161B22&color=FFF000)

</td></tr>
<tr><td><b>Detection &amp; Hunting</b></td><td>

![YARA-X](https://img.shields.io/badge/YARA--X-161B22?style=flat-square&labelColor=161B22&color=FF4500)
![Splunk](https://img.shields.io/badge/Splunk-161B22?style=flat-square&logo=splunk&logoColor=white&labelColor=161B22)
![Sysmon](https://img.shields.io/badge/Sysmon-161B22?style=flat-square&labelColor=161B22&color=58A6FF)
![RapidOCR](https://img.shields.io/badge/RapidOCR-161B22?style=flat-square&labelColor=161B22&color=7952B3)
![Sigma Rules](https://img.shields.io/badge/Sigma_Rules-161B22?style=flat-square&labelColor=161B22&color=D29922)
![Wireshark](https://img.shields.io/badge/Wireshark-161B22?style=flat-square&logo=wireshark&logoColor=white&labelColor=161B22)
![Ghidra](https://img.shields.io/badge/Ghidra-161B22?style=flat-square&labelColor=161B22&color=3FB950)
![IDA Pro](https://img.shields.io/badge/IDA_Pro-161B22?style=flat-square&labelColor=161B22&color=58A6FF)

</td></tr>
<tr><td><b>Core Disciplines</b></td><td>

![Windows Forensics](https://img.shields.io/badge/Windows_Forensics-161B22?style=flat-square&labelColor=161B22&color=0284C7)
![Endpoint Triage](https://img.shields.io/badge/Endpoint_Triage-161B22?style=flat-square&labelColor=161B22&color=0284C7)
![Incident Response](https://img.shields.io/badge/Incident_Response-161B22?style=flat-square&labelColor=161B22&color=38BDF8)
![Artifact Parser Dev](https://img.shields.io/badge/Artifact_Parser_Dev-161B22?style=flat-square&labelColor=161B22&color=7C3AED)
![Threat Hunting](https://img.shields.io/badge/Threat_Hunting-161B22?style=flat-square&labelColor=161B22&color=A855F7)
![Timeline Reconstruction](https://img.shields.io/badge/Timeline_Reconstruction-161B22?style=flat-square&labelColor=161B22&color=10B981)

</td></tr>
<tr><td><b>Code &amp; Stack</b></td><td>

![Python](https://img.shields.io/badge/Python-161B22?style=flat-square&logo=python&logoColor=3FB950&labelColor=161B22)
![FastAPI](https://img.shields.io/badge/FastAPI-161B22?style=flat-square&logo=fastapi&logoColor=009688&labelColor=161B22)
![TypeScript](https://img.shields.io/badge/TypeScript-161B22?style=flat-square&logo=typescript&logoColor=3178C6&labelColor=161B22)
![React](https://img.shields.io/badge/React_18-161B22?style=flat-square&logo=react&logoColor=61DAFB&labelColor=161B22)
![Tailwind CSS](https://img.shields.io/badge/Tailwind-161B22?style=flat-square&logo=tailwindcss&logoColor=38B2AC&labelColor=161B22)
![SQLite](https://img.shields.io/badge/SQLite-161B22?style=flat-square&logo=sqlite&logoColor=003B57&labelColor=161B22)
![PowerShell](https://img.shields.io/badge/PowerShell-161B22?style=flat-square&logo=powershell&logoColor=white&labelColor=161B22)
![Bash](https://img.shields.io/badge/Bash-161B22?style=flat-square&logo=gnubash&logoColor=white&labelColor=161B22)

</td></tr>
</table>

<br>

## Defensible Forensic Standards

In DFIR, the defensibility of conclusions relies entirely on data integrity and process reproducibility. Every investigation and parser adheres to four core principles:

1. **Read-Only Ingestion:** Evidence is never mounted with write permissions. Forensic disk containers (`.E01`, `.RAW`, `.VHDX`) are mounted through read-only VFS virtual devices with strict write-blocking.
2. **Deterministic Transaction Replay:** Registry hives are never parsed "dirty" without replaying associated `.LOG1` and `.LOG2` transaction logs first, guaranteeing that pending system transactions are properly committed.
3. **Multi-Source Corroboration:** No artifact stands alone. Execution is verified across Prefetch, Shimcache, Amcache, and Event ID 4688/Sysmon 1 to construct unshakeable timelines.
4. **Cryptographic Defensibility:** SHA-256 cryptographic hashes are computed across original containers, carved assets, and exported reports to guarantee complete chain-of-custody defensibility.

<br>

---

<p align="center">
  <sub>Open to technical discussions regarding digital forensics, artifact parser engineering, and incident response automation.</sub><br><br>
  <a href="https://www.linkedin.com/in/sanjeeth-solleti/"><img src="assets/btn-linkedin.svg" alt="LinkedIn" height="34"></a>
  <a href="mailto:vasavasanjeeth@gmail.com"><img src="assets/btn-email.svg" alt="Email" height="34"></a>
  <a href="https://github.com/sanjeeth-solleti?tab=repositories"><img src="assets/btn-repos.svg" alt="GitHub Repositories" height="34"></a>
  <br><br>
  <img src="https://komarev.com/ghpvc/?username=sanjeeth-solleti&label=PROFILE%20VIEWS&color=0284C7&style=flat-square" alt="Profile views">
</p>
