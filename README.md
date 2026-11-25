<img src="assets/banner.svg" alt="Vasava Sanjeeth Solleti — Digital Forensics &amp; Incident Response" width="100%">

<p align="center">
  <a href="https://www.linkedin.com/in/sanjeeth-solleti/"><img src="https://img.shields.io/badge/LinkedIn-sanjeeth--solleti-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0D1117" alt="LinkedIn"></a>
  <a href="mailto:vasavasanjeeth@gmail.com"><img src="https://img.shields.io/badge/Email-reach_out-2EA043?style=for-the-badge&logo=gmail&logoColor=white&labelColor=0D1117" alt="Email"></a>
  <a href="https://github.com/sanjeeth-solleti?tab=repositories"><img src="https://img.shields.io/badge/Repos-DFIR_Tooling-388BFD?style=for-the-badge&logo=github&logoColor=white&labelColor=0D1117" alt="Repositories"></a>
  <img src="https://img.shields.io/badge/Credential-CEH_Certified-BC8CFF?style=for-the-badge&labelColor=0D1117" alt="CEH Certified">
</p>

<img src="assets/stats.svg" alt="WFT Enterprise Suite · 50+ Artifact Parsers · Windows &amp; Endpoint DFIR · CEH Certified" width="100%">

<br>

## ▍whoami

Digital Forensics &amp; Incident Response (**DFIR**) Analyst specializing in enterprise Windows forensics, endpoint triage, cloud collaboration evidence, and attack-timeline reconstruction.

Forensic investigations often encounter edge cases—corrupted or unflushed transaction logs, undocumented application databases, and high-volume event streams where standard forensic suites slow down or leave questions unanswered. When off-the-shelf tools stop short, I build dedicated, forensically sound engines to extract, correlate, and validate every byte.

```yaml
endpoint_forensics:  Windows 10 / 11 / Server · E01 / RAW / VHDX / VMDK · NTFS ($MFT, $LogFile, $UsnJrnl)
registry_integrity:  Automated transaction log replay (RLA .LOG1/.LOG2) · Multi-hive correlation (SAM, SYSTEM, SOFTWARE, NTUSER)
execution_triage:    PECmd (Prefetch) · AppCompatCache (Shimcache) · Amcache · UserAssist · BAM/DAM · SRUM
messaging_&_cloud:   Microsoft Teams (LevelDB/IndexedDB) · Discord · Slack · OneDrive · Google Drive
browser_forensics:   Chromium SQLite + WAL recovery (Chrome/Edge/Brave) · Firefox places.sqlite (PRTime)
threat_hunting:      YARA-X compiled scanning · RapidOCR on carved media · LOLBins & webshell detection
development_stack:   Python 3.10+ · DuckDB Columnar Engine · FastAPI · React 18 / TypeScript · eBPF / BCC
```

<br>

## ▍Flagship DFIR Workstations &amp; Tooling

---

### 1. [WFT — Windows Forensic Examination Platform](https://github.com/sanjeeth-solleti/WFT)

<a href="https://github.com/sanjeeth-solleti/WFT">
  <img src="assets/card-wft.svg" alt="WFT — Windows Forensic Examination Platform" width="100%">
</a>

<p align="center">
  <a href="https://github.com/sanjeeth-solleti/WFT"><img src="https://img.shields.io/badge/Platform-Windows%2010%20%7C%2011%20%7C%20Server-0078D6?style=flat-square&logo=windows&logoColor=white" alt="Windows"></a>
  <a href="https://github.com/sanjeeth-solleti/WFT"><img src="https://img.shields.io/badge/Engine-DuckDB%20Columnar-FFF000?style=flat-square&logo=duckdb&logoColor=black" alt="DuckDB"></a>
  <a href="https://github.com/sanjeeth-solleti/WFT"><img src="https://img.shields.io/badge/Backend-FastAPI%20%7C%20Python-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI"></a>
  <a href="https://github.com/sanjeeth-solleti/WFT"><img src="https://img.shields.io/badge/Frontend-React%2018%20%7C%20TS%20%7C%20Tailwind-61DAFB?style=flat-square&logo=react&logoColor=black" alt="React"></a>
  <a href="https://github.com/sanjeeth-solleti/WFT"><img src="https://img.shields.io/badge/Scanning-YARA--X-FF4500?style=flat-square" alt="YARA-X"></a>
  <a href="https://github.com/sanjeeth-solleti/WFT"><img src="https://img.shields.io/badge/OCR-RapidOCR-7952B3?style=flat-square" alt="RapidOCR"></a>
</p>

An enterprise-grade, full-featured Windows Digital Forensics and Incident Response workstation integrating evidence ingestion, virtual file system mounting, dirty registry log replay, external CLI orchestration, non-EZ forensic parsing, YARA-X scanning, and RapidOCR into an unified analytics platform.

- **Zero-Copy DuckDB Columnar Core:** In-process columnar database providing sub-millisecond queries, live multi-timestamp super-timelines unpivoted across all artifacts, and zero-latency filtering over 500,000+ records.
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
- **Examiner UI:** Virtualized AG Grid with dynamic bookmarks, interactive Cytoscape network entity graph linking IPs, binaries, and accounts, plus an integrated 16-byte dual Hex/ASCII inspector.

---

### 2. [MSTeams_Parser — Microsoft Teams Forensic Suite](https://github.com/sanjeeth-solleti/MSTeams_Parser)

<a href="https://github.com/sanjeeth-solleti/MSTeams_Parser">
  <img src="assets/card-msteams.svg" alt="MSTeams_Parser — Microsoft Teams Forensic Suite" width="100%">
</a>

<p align="center">
  <a href="https://github.com/sanjeeth-solleti/MSTeams_Parser"><img src="https://img.shields.io/badge/Language-Python%203.9+-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"></a>
  <a href="https://github.com/sanjeeth-solleti/MSTeams_Parser"><img src="https://img.shields.io/badge/Database-LevelDB%20%7C%20IndexedDB-4E73DF?style=flat-square" alt="IndexedDB"></a>
  <a href="https://github.com/sanjeeth-solleti/MSTeams_Parser"><img src="https://img.shields.io/badge/UI-Edge%2FChrome%20App%20Mode-0078D7?style=flat-square" alt="App Mode"></a>
  <a href="https://github.com/sanjeeth-solleti/MSTeams_Parser"><img src="https://img.shields.io/badge/Security-100%25%20Offline%20Isolated-success?style=flat-square" alt="Offline"></a>
  <a href="https://github.com/sanjeeth-solleti/MSTeams_Parser"><img src="https://img.shields.io/badge/Timestamps-Dual%20UTC%20%2B%20IST-blueviolet?style=flat-square" alt="Timestamps"></a>
</p>

A standalone DFIR tool designed for parsing, reconstructing, and analyzing Microsoft Teams communication artifacts from forensic images and live triage extractions.

- **Air-Gapped Forensic Safety:** Embedded server binds strictly to `127.0.0.1`. Absolutely no data leaves the workstation, upholding forensic confidentiality.
- **Multi-Source Ingestion Pipeline:** Ingests New Teams (`%LOCALAPPDATA%\Packages\MSTeams_8wekyb3d8bbwe\...\IndexedDB`) and Classic Teams (`%APPDATA%\Microsoft\Teams\IndexedDB`), raw LevelDB files with `dfindexeddb`, pre-parsed UTF-16 JSON dumps, and candidate CSV logs.
- **Message Normalization &amp; Event Parsing:** Unpacks raw XML/JSON markup into intelligible timelines: Base64 JSON Adaptive Cards, call started/ended events with participant lists and durations, meeting policy updates, member role changes, and file shares.
- **Identity &amp; Contact Resolution:** Resolves internal GUIDs (`8:orgid:<guid>`) to real user names, emails, job roles, and corporate directory records.
- **Carving &amp; Telemetry Suppression:** Carves cached images and attachments, identifying file headers via magic bytes while automatically filtering UI telemetry, emojis, and noise (< 3.5 KB).
- **Examiner Reporting:** Standalone HTML chat viewer, Excel-ready CSV summaries, ZIP media bundle, audit log, and dual UTC/IST timestamps.

---

### 3. [PrivEsc-Detector — Real-Time Linux Privilege Escalation Detector](https://github.com/fuzzzer77/PrivEsc-Detector)

<img src="assets/card-privesc.svg" alt="PrivEsc-Detector — Real-Time Linux Privilege Escalation Detector" width="100%">

<p align="center">
  <img src="https://img.shields.io/badge/Core-eBPF%20%7C%20BCC-FF6F00?style=flat-square" alt="eBPF">
  <img src="https://img.shields.io/badge/Kernel-Linux%20Tracepoints-FCC624?style=flat-square&logo=linux&logoColor=black" alt="Linux">
  <img src="https://img.shields.io/badge/Detection-10%20Deterministic%20Rules-red?style=flat-square" alt="Rules">
  <img src="https://img.shields.io/badge/Storage-SQLite%20Audit%20Log-003B57?style=flat-square&logo=sqlite&logoColor=white" alt="SQLite">
</p>

Real-time, eBPF-based detection of Linux privilege-escalation attempts watching kernel syscalls and correlating events with strict zero-false-positive detection rules.

- **Kernel Tracepoints:** Attaches directly to `setuid`, `setreuid`, `setresuid`, `setgid`, `execve`, `openat`, `chmod`, and `capset` syscalls via eBPF ring buffers.
- **Rule Engine (RULE-01 to RULE-10):** Strict defensive rules equipped with process allowlists (`sudo`, `su`, `sshd`, `dpkg`/`apt`) to eliminate noise.
- **Multi-Signal Correlation:** RULE-10 detects 2+ distinct privilege-escalation signals emitted by the same PID within a 15-second window, flagging confirmed escalation bursts.
- **Audit Persistence:** Multi-threaded worker pool, 10-minute alert deduplication window, rate limiting, and local SQLite audit logging.

<br>

## ▍Forensic Artifact Coverage Matrix

A breakdown of critical Windows, messaging, and system artifacts parsed across my forensic tooling:

| Category | Forensic Artifact | File / Source Location | Evidentiary Value |
| :--- | :--- | :--- | :--- |
| **Execution** | **Prefetch** | `C:\Windows\Prefetch\*.pf` | Execution proof, run count, volume serial, previous execution timestamps |
| **Execution** | **Shimcache** | `SYSTEM\CurrentControlSet\Control\Session Manager\AppCompatCache` | Executable presence, path verification, last modified time |
| **Execution** | **Amcache** | `C:\Windows\appcompat\Programs\Amcache.hve` | SHA-1 program hashes, unassociated file entries, execution metadata |
| **Execution** | **SRUM** | `C:\Windows\System32\sru\SRUDB.dat` | Network bytes sent/received per application, background energy usage |
| **Execution** | **BAM / DAM** | `SYSTEM\CurrentControlSet\Services\bam` | Background Activity Moderator user execution timestamps |
| **Execution** | **UserAssist** | `NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist` | ROT13 encoded GUI application execution counts and last launch dates |
| **File System** | **NTFS $MFT** | `$MFT` (Root of volume) | File record attributes, $STANDARD_INFORMATION vs $FILE_NAME timestamp comparison (timestomp detection) |
| **File System** | **USN Journal** | `$Extend\$UsnJrnl:$J` | Complete record of file creation, modification, deletion, and renaming |
| **File System** | **ShellBags** | `USRCLASS.DAT` &amp; `NTUSER.DAT` | Folder browsing history, deleted directory verification, external drive reconnaissance |
| **File System** | **LNK &amp; Jump Lists** | `Recent\`, `AutomaticDestinations\`, `CustomDestinations\` | Target file path, creation/modification times, volume serial, MAC address |
| **System State** | **Registry Logs** | `*.LOG1`, `*.LOG2` transaction logs | Dirty hive recovery via RLA replay before static hive parsing |
| **System State** | **Event Logs** | `C:\Windows\System32\winevt\Logs\*.evtx` | Security (4624/4625, 4688), Sysmon (1, 3, 7, 10, 11), PowerShell (4104) |
| **Hardware** | **USB History** | `setupapi.dev.log`, `SYSTEM\USBSTOR`, `SOFTWARE\EMDMgmt` | First/last connection times, device serial numbers, volume labels |
| **Messaging** | **Microsoft Teams** | `IndexedDB` &amp; `LevelDB` stores | Reconstructed chat messages, Base64 Adaptive Cards, calls, meetings, carved media |
| **Browsers** | **Chromium &amp; Firefox** | `History`, `Downloads`, `places.sqlite` | SQLite + WAL recovery, full-text URL search, PRTime timestamp normalization |
| **Network/Cloud**| **Cloud Sync** | OneDrive (`SyncEngineDatabase.db`), Google Drive | Synchronized file paths, cloud sync status, account identities |

<br>

## ▍Field Kit &amp; Arsenal

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

![Windows Forensics](https://img.shields.io/badge/Windows_Forensics-1F6F35?style=flat-square&labelColor=1F6F35)
![Endpoint Triage](https://img.shields.io/badge/Endpoint_Triage-1F6F35?style=flat-square&labelColor=1F6F35)
![Incident Response](https://img.shields.io/badge/Incident_Response-1F6F35?style=flat-square&labelColor=1F6F35)
![Artifact Parser Dev](https://img.shields.io/badge/Artifact_Parser_Dev-1F6F35?style=flat-square&labelColor=1F6F35)
![Threat Hunting](https://img.shields.io/badge/Threat_Hunting-1F6F35?style=flat-square&labelColor=1F6F35)
![Timeline Reconstruction](https://img.shields.io/badge/Timeline_Reconstruction-1F6F35?style=flat-square&labelColor=1F6F35)

</td></tr>
<tr><td><b>Code &amp; Stack</b></td><td>

![Python](https://img.shields.io/badge/Python-161B22?style=flat-square&logo=python&logoColor=3FB950&labelColor=161B22)
![FastAPI](https://img.shields.io/badge/FastAPI-161B22?style=flat-square&logo=fastapi&logoColor=009688&labelColor=161B22)
![TypeScript](https://img.shields.io/badge/TypeScript-161B22?style=flat-square&logo=typescript&logoColor=3178C6&labelColor=161B22)
![React](https://img.shields.io/badge/React_18-161B22?style=flat-square&logo=react&logoColor=61DAFB&labelColor=161B22)
![Tailwind CSS](https://img.shields.io/badge/Tailwind-161B22?style=flat-square&logo=tailwindcss&logoColor=38B2AC&labelColor=161B22)
![eBPF / BCC](https://img.shields.io/badge/eBPF_BCC-161B22?style=flat-square&labelColor=161B22&color=F85149)
![SQLite](https://img.shields.io/badge/SQLite-161B22?style=flat-square&logo=sqlite&logoColor=003B57&labelColor=161B22)
![PowerShell](https://img.shields.io/badge/PowerShell-161B22?style=flat-square&logo=powershell&logoColor=white&labelColor=161B22)
![Bash](https://img.shields.io/badge/Bash-161B22?style=flat-square&logo=gnubash&logoColor=white&labelColor=161B22)

</td></tr>
</table>

<br>

## ▍Investigative Principles &amp; Evidence Handling

In DFIR, the validity of conclusions relies entirely on the integrity of the data and the reproducibility of the extraction process. Every tool and investigation adheres to four fundamental principles:

1. **Read-Only Ingestion:** Evidence is never mounted with write permissions. Forensic disk containers (`.E01`, `.RAW`, `.VHDX`) are mounted through read-only VFS virtual devices with strict write-blocking.
2. **Deterministic Transaction Replay:** Registry hives are never parsed "dirty" without replaying associated `.LOG1` and `.LOG2` transaction logs first, guaranteeing that pending system transactions are properly committed.
3. **Multi-Source Corroboration:** No artifact stands alone. A process launch is verified across Prefetch, Shimcache, Amcache, and Event ID 4688/Sysmon 1 to build unshakeable timelines.
4. **Cryptographic Validation:** SHA-256 cryptographic hashes are computed across original containers, carved assets, and exported reports to guarantee complete chain-of-custody defensibility.

<br>

## ▍Credentials &amp; Certifications

![CEH](https://img.shields.io/badge/CEH-Certified_Ethical_Hacker-BC8CFF?style=for-the-badge&labelColor=0D1117)
![DFIR Analyst](https://img.shields.io/badge/Specialization-Digital_Forensics_%26_Incident_Response-388BFD?style=for-the-badge&labelColor=0D1117)

<br>

---

<p align="center">
  <sub>Open to conversations regarding digital forensics, artifact parser development, and incident response automation.</sub><br><br>
  <a href="https://www.linkedin.com/in/sanjeeth-solleti/"><img src="https://img.shields.io/badge/LinkedIn-0D1117?style=flat-square&labelColor=0D1117&color=0A66C2&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="mailto:vasavasanjeeth@gmail.com"><img src="https://img.shields.io/badge/Email-0D1117?style=flat-square&logo=gmail&logoColor=white&labelColor=0D1117&color=2EA043" alt="Email"></a>
  <a href="https://github.com/sanjeeth-solleti?tab=repositories"><img src="https://img.shields.io/badge/GitHub-0D1117?style=flat-square&logo=github&logoColor=white&labelColor=0D1117&color=8B949E" alt="GitHub"></a>
  <br><br>
  <img src="https://komarev.com/ghpvc/?username=sanjeeth-solleti&label=PROFILE%20VIEWS&color=388BFD&style=flat-square" alt="Profile views">
</p>
