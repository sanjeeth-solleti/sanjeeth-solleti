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
  <img src="assets/intro.svg" alt="The DFIR Lab — Open source tools engineered for the gaps where standard forensic suites stop short." width="100%">
</p>

<br>

## Executive Profile

Digital Forensics &amp; Incident Response (**DFIR**) Analyst at **Tata Consultancy Services (TCS)**, specializing in enterprise Windows endpoint forensics, deep triage, cloud collaboration evidence, and end-to-end attack timeline reconstruction.

Forensic investigations routinely encounter critical failure points where standard commercial suites slow down or stop short—unflushed registry transactions locked in volatile `.LOG` files, high-volume event streams exceeding millions of rows, or undocumented IndexedDB and LevelDB messaging stores. My focus centers on building forensically sound, deterministic engines that ingest raw disk containers, replay transactions, and correlate cross-source telemetry into unshakeable, defensible chronologies.

<br>

## Featured DFIR Tooling & Platforms

<a href="https://github.com/sanjeeth-solleti/WFT">
  <img src="assets/card-wft.svg" alt="WFT — Windows Forensic Examination Platform" width="100%">
</a>

<p align="center">
  <a href="https://github.com/sanjeeth-solleti/WFT"><img src="https://img.shields.io/github/stars/sanjeeth-solleti/WFT?style=flat-square&label=stars&labelColor=0D1117&color=38BDF8" alt="WFT stars"></a>
  <a href="https://github.com/sanjeeth-solleti/WFT/network/members"><img src="https://img.shields.io/github/forks/sanjeeth-solleti/WFT?style=flat-square&label=forks&labelColor=0D1117&color=38BDF8" alt="WFT forks"></a>
  <a href="https://github.com/sanjeeth-solleti/WFT/issues"><img src="https://img.shields.io/github/issues/sanjeeth-solleti/WFT?style=flat-square&label=issues&labelColor=0D1117&color=38BDF8" alt="WFT issues"></a>
  <a href="https://github.com/sanjeeth-solleti/WFT/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-0284C7?style=flat-square&labelColor=0D1117" alt="WFT License"></a>
</p>

### 1. [WFT — Windows Forensic Examination Platform](https://github.com/sanjeeth-solleti/WFT)

An enterprise-grade Windows Digital Forensics and Incident Response workstation engineered for comprehensive investigation (**Process + Examine**). WFT bridges the gap between raw disk intake and analytical timelines by uniting virtual file system disk mounting, automated dirty registry transaction log replay, external CLI toolchain orchestration, custom non-EZ parsers, Rust-compiled YARA-X scanning, and RapidOCR into an unified analytics workstation.

- **Zero-Copy DuckDB Columnar Core:** In-process columnar analytical database delivering sub-millisecond queries, live multi-timestamp super-timelines unpivoted across all forensic artifacts, and zero-latency filtering across 500,000+ records.
- **Native Evidence Intake &amp; VFS:** Direct read-only mounting and forensic extraction from `.E01`, `.Ex01`, `.VHDX`, `.VHD`, `.VMDK`, `.RAW`, `.DD`, and `.ISO` disk containers via native `dissect.target` VFS, as well as live triage directories.
- **Automated Registry Integrity:** Mandatory automated dirty registry transaction log replay (`.LOG1` / `.LOG2` via RLA) before hive parsing, ensuring no unflushed forensic transactions are lost.
- **Full Eric Zimmerman Toolchain Orchestration:** Seamless batch processing with PECmd (Prefetch), MFTECmd ($MFT, $J, $LogFile), EvtxECmd (Event Logs), RECmd (Batch Registry), LECmd (LNK Shortcuts), JLECmd (Jump Lists), AmcacheParser, AppCompatCacheParser (Shimcache), SBECmd (ShellBags), SrumECmd (SRUM metrics), WxTCmd (ActivitiesCache), and SQLECmd.
- **Non-EZ Native Forensic Parsers:**
  - *Browsers:* Chromium (Chrome, Edge, Brave) and Firefox databases with full WAL recovery for History, Downloads, and Login Data.
  - *Collaboration:* Microsoft Teams, Discord, and Slack IndexedDB / LevelDB message parsing.
  - *Cloud Sync:* OneDrive (`SyncEngineDatabase.db`) and Google Drive synced metadata.
  - *USB Device Correlator:* Multi-hive correlation cross-referencing `setupapi.dev.log` with `SYSTEM` (`USBSTOR`, `MountedDevices`) and `SOFTWARE` (`EMDMgmt`) to reconstruct end-to-end device connection histories.
  - *Document &amp; MOTW Parser:* Metadata extraction with Mark-of-the-Web (`Zone.Identifier`) zone parsing.
- **Threat Hunting &amp; Inspection:** Rust-based compiled YARA-X rule engine scanning for webshells, beacons, and LOLBins, accompanied by RapidOCR text extraction from carved screenshots, receipts, and images.
- **Examiner UI:** Virtualized AG Grid with dynamic bookmarks, FTK Imager-style NTFS directory browser, interactive Cytoscape network entity graph linking IPs, binaries, and accounts, plus an integrated 16-byte dual Hex/ASCII inspector.

<br><br>

<a href="https://github.com/sanjeeth-solleti/MSTeams_Parser">
  <img src="assets/card-msteams.svg" alt="MSTeams_Parser — Microsoft Teams Forensic Suite" width="100%">
</a>

<p align="center">
  <a href="https://github.com/sanjeeth-solleti/MSTeams_Parser"><img src="https://img.shields.io/github/stars/sanjeeth-solleti/MSTeams_Parser?style=flat-square&label=stars&labelColor=0D1117&color=C084FC" alt="MSTeams_Parser stars"></a>
  <a href="https://github.com/sanjeeth-solleti/MSTeams_Parser/network/members"><img src="https://img.shields.io/github/forks/sanjeeth-solleti/MSTeams_Parser?style=flat-square&label=forks&labelColor=0D1117&color=C084FC" alt="MSTeams_Parser forks"></a>
  <a href="https://github.com/sanjeeth-solleti/MSTeams_Parser/issues"><img src="https://img.shields.io/github/issues/sanjeeth-solleti/MSTeams_Parser?style=flat-square&label=issues&labelColor=0D1117&color=C084FC" alt="MSTeams_Parser issues"></a>
  <a href="https://github.com/sanjeeth-solleti/MSTeams_Parser/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-7C3AED?style=flat-square&labelColor=0D1117" alt="MSTeams_Parser License"></a>
</p>

### 2. [MSTeams_Parser — Microsoft Teams DFIR Forensic Suite](https://github.com/sanjeeth-solleti/MSTeams_Parser)

A standalone DFIR suite engineered for parsing, reconstructing, and analyzing Microsoft Teams communication artifacts from raw forensic disk images and live triage extractions.

- **Air-Gapped Forensic Safety:** Embedded server binds strictly to `127.0.0.1`. Absolutely no data leaves the workstation, upholding forensic confidentiality.
- **Multi-Source Ingestion Pipeline:** Ingests New Teams (`%LOCALAPPDATA%\Packages\MSTeams_8wekyb3d8bbwe\...\IndexedDB`) and Classic Teams (`%APPDATA%\Microsoft\Teams\IndexedDB`), raw LevelDB files with `dfindexeddb` &amp; `cramjam`, pre-parsed UTF-16 JSON dumps, and candidate CSV logs.
- **Message Normalization &amp; Event Parsing:** Unpacks raw XML/JSON markup into intelligible timelines: Base64 JSON Adaptive Cards, call started/ended events with participant lists and durations, meeting policy updates, member role changes, and file shares.
- **Identity &amp; Contact Resolution:** Resolves internal GUIDs (`8:orgid:<guid>`) to real employee names, emails, job roles, and corporate directory records.
- **Carving &amp; Telemetry Suppression:** Carves cached images and attachments, identifying file headers via magic bytes while automatically filtering UI telemetry, emojis, and noise (&lt; 3.5 KB).
- **Examiner Reporting:** Standalone HTML chat viewer, Excel-ready CSV summaries (UTF-8 BOM), ZIP media bundle, audit log, and dual UTC/IST timestamps.

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
