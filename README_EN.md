<div align="center">

# Colab Drive

**Automated Multi-Source Downloader & Direct Google Drive Synchronizer on Google Colab**

[Tiếng Việt](README.md) · [English](README_EN.md)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/huyvu2512/colab-drive/blob/main/colab-drive.ipynb)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB)](https://www.python.org/)
[![Deno](https://img.shields.io/badge/Deno-JS%20Runtime-black)](https://deno.land/)
[![Version](https://img.shields.io/badge/Version-v2.2.2-red)](CHANGELOG.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![yt-dlp](https://img.shields.io/badge/Engine-yt--dlp-red)](https://github.com/yt-dlp/yt-dlp)
[![aria2](https://img.shields.io/badge/Engine-aria2-blue)](https://github.com/aria2/aria2)

[![Stars](https://img.shields.io/github/stars/huyvu2512/colab-drive?style=flat-square&label=Stars&color=FFCC00)](https://github.com/huyvu2512/colab-drive/stargazers)
[![Forks](https://img.shields.io/github/forks/huyvu2512/colab-drive?style=flat-square&label=Forks&color=6e7681)](https://github.com/huyvu2512/colab-drive/forks)
[![Issues](https://img.shields.io/github/issues/huyvu2512/colab-drive?style=flat-square&label=Issues&color=f85149)](https://github.com/huyvu2512/colab-drive/issues)
[![Last Commit](https://img.shields.io/github/last-commit/huyvu2512/colab-drive?style=flat-square&label=Last%20Commit&color=3fb950)](https://github.com/huyvu2512/colab-drive/commits/main)

[Open Colab Notebook](https://colab.research.google.com/github/huyvu2512/colab-drive/blob/main/colab-drive.ipynb) · [Changelog](CHANGELOG.md) · [Report Bug](https://github.com/huyvu2512/colab-drive/issues) · [Request Feature](https://github.com/huyvu2512/colab-drive/issues)

</div>

---

## Introduction
**Colab Drive** is an automated cloud download solution running on Google Colab, engineered to maximize transfer speeds from diverse Internet sources directly into your personal Google Drive without consuming local machine bandwidth or storage. Designed and developed by Huy Vu (@huyvu2512) with a focus on stream optimization, resilient task queue management, and deep integration of premium open-source download engines.

Version **v2.2.0** supports flexible splitting of files into 2, 4, 6, 8, or 10 equal parts stored in dedicated folders. See [CHANGELOG.md](CHANGELOG.md) for full details.

---

## Key Features
- **Multi-Engine Dispatcher** - Dynamically routes downloads to the optimal tool: `gdown` for Google Drive, `megatools` for MEGA, `aria2c` for Direct Links & BitTorrent, and `yt-dlp` for video/audio streams.
- **Deno JS Signature Decryption** - Pre-installed Deno runtime and remote EJS challenge solver to bypass YouTube cipher/n-sig 403 Forbidden errors on datacenter IP addresses.
- **Smart Task Queue** - Accepts batch links separated by commas, semicolons, whitespace, or newlines; executes sequentially and cleans up buffer storage after each task.
- **Fault-Tolerant Torrent Rescheduling** - Monitors BitTorrent/Magnet progress; if no seeders are connected within 3 minutes (0 KB/s), the task is pushed to the back of the queue; dead links are automatically skipped without breaking execution.
- **100% Quality Alignment between Step 3 & Step 4** - Choose Best, 4K, 2K, 1080p, 720p, 480p, or Audio Only (MP3 320kbps). Step 3 probes actual available streams and locks the configuration for Step 4.
- **Cross-Platform Playlist Limiter** - Supports item range filtering (`1-10`, `1-5`, `all`) across 1,800+ websites and automatically creates dedicated playlist folders on Google Drive.
- **Flexible Equal-Parts Splitting** - Option to split files into 2, 4, 6, 8, or 10 equal `.7z` volumes and store each within its own subfolder.
- **Real-Time Live Progress & ETA** - Real-time progress bar displaying percentage, transferred size, speed (MB/s), and estimated remaining time (ETA).
- **Telegram Bot Notifications** - Automatically dispatches execution summaries detailing saved files, success/failure counts, and Google Drive destination paths.

---

## Technology Stack
| Component | Technology |
| :--- | :--- |
| Execution Environment | Google Colab (Linux Ubuntu VM Environment) |
| Core Language | Python 3.10+, Bash Shell Scripting |
| Video/Audio Engine | yt-dlp, FFmpeg |
| JS Challenge Solver | Deno JavaScript Runtime, EJS Solver |
| P2P & Direct Link Engine | aria2c (DHT, OpenTrackers, 16 concurrent connections) |
| Google Drive Engine | gdown (Bypasses virus scan warnings and downloads full folders) |
| MEGA Cloud Engine | megatools |
| Archive & Splitting Engine | p7zip-full (7z), unrar |
| Build System | scripts/build.py (Compiles `src/` modules into `colab-drive.ipynb`) |

---

## Repository Structure

```text
colab-drive/
├── scripts/
│   └── build.py              # Compiles and bundles src/ into colab-drive.ipynb
├── src/
│   ├── core/
│   │   ├── logger.py         # Tagged color logger, UTC+7 timezone and progress protection
│   │   ├── utils.py          # Formatters for size, ETA, resolution, and sanitized filenames
│   │   └── anti_disconnect.py# JavaScript heartbeat keeping Colab sessions alive
│   ├── engines/
│   │   ├── ytdl.py           # yt-dlp wrapper, log filters, stream merging, and progress hooks
│   │   ├── aria2.py          # aria2c wrapper (Multi-thread direct links & 3-minute torrent timeout)
│   │   ├── gdown.py          # gdown wrapper for Google Drive files and folders
│   │   └── mega.py           # megatools wrapper for MEGA cloud storage
│   ├── queue/
│   │   └── parser.py         # Multi-delimiter URL extractor
│   ├── storage/
│   │   ├── drive_sync.py     # Drive transfer and smart file naming
│   │   └── splitter.py       # Auto-split engine (2, 4, 6, 8, 10 parts) into dedicated folders
│   └── notifications/
│       └── telegram.py       # Telegram Bot reporting module
├── CHANGELOG.md              # Version history
├── README.md                 # Documentation in Vietnamese
├── README_EN.md              # Documentation in English
├── colab-drive.ipynb         # Ready-to-run Jupyter Notebook for Google Colab
└── LICENSE                   # MIT Open Source License
```

- Rebuild notebook from source: `python scripts/build.py`

---

## 4-Step Operational Workflow

### Step 1: Initialize Environment & Install Engines
- Activates the Anti-Disconnect heartbeat.
- Installs `yt-dlp`, Deno JS runtime, `gdown`, `megatools`, `aria2c`, `ffmpeg`, `p7zip-full`, and `unrar`.

### Step 2: Authenticate & Mount Google Drive
- Mounts personal Google Drive storage (`/content/drive/MyDrive/`).
- Checks Colab VM buffer storage availability.

### Step 3: Enter Links & Pre-Inspect Metadata
- Input single or multiple URLs into `LINK_CAN_TAI`.
- Select quality (`CHAT_LUONG_TAI`), playlist limits (`GIOI_HAN_PLAYLIST`), proxy, referer, and cookies.
- System probes technical specs, validates actual resolutions, and prints a summary queue table.

### Step 4: Configure Storage & Execute Download
- Set destination directory (`THU_MUC_DRIVE`), custom naming (`TEN_FILE_TU_DAT`), choose splitting into 2, 4, 6, 8, or 10 parts (`CAT_TEP_DUNG_LUONG_LON`), and Telegram Bot credentials.
- Executes queue sequentially, transfers data into Google Drive, and cleans up local cache.

---

## Configuration Parameters

| Parameter | Step | Type | Description |
| :--- | :--- | :--- | :--- |
| `LINK_CAN_TAI` | Step 3 | String | Paste single or multiple URLs (separated by comma, semicolon, space, or newline). |
| `CHAT_LUONG_TAI` | Step 3 | Select | Target quality (Best, 4K, 2K, 1080p, 720p, 480p, or Audio Only MP3). |
| `GIOI_HAN_PLAYLIST` | Step 3 | String | Playlist items limit (default: `tat_ca` for all, or `1-10`, `1-5`...). |
| `DANH_SACH_PROXY` | Step 3 | String | List of proxies for Round-Robin rotation. |
| `REFERER_VUOT_CHAN` | Step 3 | String | Custom Referer to bypass 403 Forbidden errors. |
| `NOI_DUNG_COOKIE` | Step 3 | String | Cookies string or path to `cookies.txt` for 4K/VIP authorization. |
| `THU_MUC_DRIVE` | Step 4 | String | Google Drive destination folder (default: `/content/drive/MyDrive/colab-drive`). |
| `TEN_FILE_TU_DAT` | Step 4 | String | Custom file name (automatically appends correct extension and queue indices). |
| `CAT_TEP_DUNG_LUONG_LON` | Step 4 | Select | Option to split files into 2, 4, 6, 8, or 10 equal parts (Khong cat, Chia thanh 2 phan...). |
| `TELEGRAM_BOT_TOKEN` | Step 4 | String | Telegram Bot token for notifications. |
| `TELEGRAM_CHAT_ID` | Step 4 | String | Telegram Chat ID for notifications. |

---

## License
Distributed under the MIT Open Source License. See [LICENSE](LICENSE) for details.
