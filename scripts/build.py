#!/usr/bin/env python3
# Build script for colab-drive.ipynb
# Automatically packages modules into Google Colab notebook format
import json
import os

notebook = {
    'nbformat': 4,
    'nbformat_minor': 0,
    'metadata': {
        'colab': {'provenance': []},
        'kernelspec': {'name': 'python3', 'display_name': 'Python 3'},
        'language_info': {'name': 'python'}
    },
    'cells': []
}

# 1. Header Markdown Cell
header_md = """# Colab Drive
Tự động hóa tải và đồng bộ tệp tin đa nguồn vào Google Drive trên nền tảng Google Colab.

- Hỗ trợ đa nguồn: YouTube, TikTok, Facebook, Google Drive, MEGA, BitTorrent/Magnet, Direct Link...
- Tự động hóa: Hàng chờ tác vụ, chọn chất lượng (4K, 1080p, MP3), chia nhỏ tệp lớn và chống ngắt kết nối.

Quy trình 4 bước:
- Bước 1: Thiết lập môi trường & Chống ngắt kết nối
- Bước 2: Xác thực & Kết nối Google Drive
- Bước 3: Nhập liên kết & Kiểm tra thông số
- Bước 4: Cấu hình lưu trữ & Thực thi tải xuống"""

notebook['cells'].append({
    'cell_type': 'markdown',
    'metadata': {'id': 'header_intro'},
    'source': [line + '\n' for line in header_md.split('\n')]
})

# 2. Step 1: Install dependencies, Deno JS runtime & Anti-disconnect
step1_code = """#@title Bước 1: Thiết lập môi trường và cài đặt các công cụ tải chuyên dụng
#@markdown Cài đặt hệ sinh thái công cụ: yt-dlp, Deno JS runtime, gdown, megatools, aria2c, ffmpeg, p7zip và kích hoạt chống ngắt kết nối.

import os
import sys
from datetime import datetime, timezone, timedelta
from IPython.display import display, Javascript

VN_TZ = timezone(timedelta(hours=7))

def log(tag, msg, level="INFO"):
    colors = {
        "SYSTEM": "\\033[36m",
        "SUCCESS": "\\033[32m",
        "INFO": "\\033[34m",
        "WARN": "\\033[33m",
        "ERROR": "\\033[31m",
        "DRIVE": "\\033[35m",
        "FETCH": "\\033[94m",
        "PROBE": "\\033[95m",
        "QUEUE": "\\033[96m",
        "PROGRESS": "\\033[96m",
        "TRANSFER": "\\033[33m",
        "EXTRACT": "\\033[96m",
        "NOTIFY": "\\033[92m"
    }
    reset = "\\033[0m"
    dim = "\\033[90m"
    ts = datetime.now(VN_TZ).strftime("%H:%M:%S")
    tag_color = colors.get(level, "\\033[37m")
    print(f"{dim}{ts}{reset} {tag_color}[{tag}]{reset} {msg}")

log("SYSTEM", "Bắt đầu khởi tạo môi trường hệ thống...", "SYSTEM")

# Kích hoạt Anti-Disconnect JavaScript Heartbeat
js_heartbeat = '''
function ConnectButton(){
    console.log("Connect pushed"); 
    document.querySelector("#top-toolbar > colab-connect-button").shadowRoot.querySelector("#connect").click() 
}
setInterval(ConnectButton, 60000);
'''
display(Javascript(js_heartbeat))
log("SYSTEM", "Đã kích hoạt cơ chế tự động duy trì kết nối phiên làm việc (Anti-Disconnect).", "SYSTEM")

log("SYSTEM", "Cài đặt và cập nhật các gói Python: yt-dlp, gdown, streamlink...", "INFO")
os.system("pip install --upgrade --no-cache-dir -q yt-dlp gdown streamlink")

log("SYSTEM", "Cài đặt Deno JavaScript Runtime (giải mã chữ ký YouTube n-sig chống 403 Forbidden)...", "INFO")
os.system("curl -fsSL https://deno.land/install.sh | sh > /dev/null 2>&1")
deno_bin = os.path.expanduser("~/.deno/bin")
if os.path.exists(deno_bin) and deno_bin not in os.environ["PATH"]:
    os.environ["PATH"] = f"{deno_bin}:{os.environ['PATH']}"

log("SYSTEM", "Cài đặt các công cụ hệ thống: aria2c, ffmpeg, megatools, p7zip-full, unrar, curl, wget, nodejs...", "INFO")
os.system("apt-get update -y -q && apt-get install -y -q ffmpeg aria2 megatools p7zip-full unrar curl wget nodejs")

log("SUCCESS", "Hệ thống các công cụ tải chuyên dụng và Deno JS runtime đã sẵn sàng.", "SUCCESS")
"""

notebook['cells'].append({
    'cell_type': 'code',
    'metadata': {'id': 'setup_environment', 'cellView': 'form'},
    'source': [line + '\n' for line in step1_code.split('\n')],
    'execution_count': None,
    'outputs': []
})

# 3. Step 2: Mount Google Drive & Buffer Storage Check
step2_code = """#@title Bước 2: Xác thực và kết nối Google Drive
#@markdown Liên kết phân vùng lưu trữ Google Drive và kiểm tra bộ đệm máy ảo xử lý tệp.

import os
import shutil
from datetime import datetime, timezone, timedelta

VN_TZ = timezone(timedelta(hours=7))

def log(tag, msg, level="INFO"):
    colors = {
        "SYSTEM": "\\033[36m",
        "SUCCESS": "\\033[32m",
        "INFO": "\\033[34m",
        "WARN": "\\033[33m",
        "ERROR": "\\033[31m",
        "DRIVE": "\\033[35m",
        "FETCH": "\\033[94m",
        "PROBE": "\\033[95m",
        "QUEUE": "\\033[96m",
        "PROGRESS": "\\033[96m",
        "TRANSFER": "\\033[33m",
        "EXTRACT": "\\033[96m",
        "NOTIFY": "\\033[92m"
    }
    reset = "\\033[0m"
    dim = "\\033[90m"
    ts = datetime.now(VN_TZ).strftime("%H:%M:%S")
    tag_color = colors.get(level, "\\033[37m")
    print(f"{dim}{ts}{reset} {tag_color}[{tag}]{reset} {msg}")

log("DRIVE", "Yêu cầu quyền truy cập phân vùng Google Drive...", "DRIVE")
try:
    from google.colab import drive
    drive.mount('/content/drive')
    if os.path.exists('/content/drive/MyDrive'):
        log("SUCCESS", "Kết nối Google Drive thành công.", "SUCCESS")
        log("DRIVE", "Điểm gắn lưu trữ: /content/drive/MyDrive/", "DRIVE")
        
        total, used, free = shutil.disk_usage('/content')
        total_gb = total / (1024**3)
        used_gb = used / (1024**3)
        free_gb = free / (1024**3)
        log("SYSTEM", f"Bộ đệm máy ảo Colab: Đã dùng {used_gb:.2f} GB / Khả dụng {free_gb:.2f} GB (Tổng: {total_gb:.2f} GB).", "INFO")
        if free_gb < 2.0:
            log("WARN", f"Cảnh báo: Bộ đệm máy ảo Colab còn dưới {free_gb:.2f} GB khả dụng.", "WARN")
    else:
        log("WARN", "Đã gắn kết phân vùng nhưng chưa nhận diện được thư mục MyDrive.", "WARN")
except Exception as e:
    log("ERROR", f"Kết nối Google Drive thất bại: {e}", "ERROR")
"""

notebook['cells'].append({
    'cell_type': 'code',
    'metadata': {'id': 'mount_drive_storage', 'cellView': 'form'},
    'source': [line + '\n' for line in step2_code.split('\n')],
    'execution_count': None,
    'outputs': []
})

# 4. Step 3: Input URLs & Probe info with friendly resolution, quality selector, playlist and queue
step3_code = """#@title Bước 3: Nhập liên kết và kiểm tra thông tin nguồn
#@markdown Hỗ trợ nhập một hoặc nhiều liên kết (phân tách bằng dấu phẩy, dấu chấm phẩy, khoảng trắng hoặc xuống dòng). Hệ thống sẽ tự động lập hàng chờ (Queue) để kiểm tra và xử lý tuần tự.

LINK_CAN_TAI = "" #@param {type:"string"}
CHAT_LUONG_TAI = "Cao nhat (Tu dong)" #@param ["Cao nhat (Tu dong)", "2160p (4K Ultra HD)", "1440p (2K QHD)", "1080p (Full HD)", "720p (HD)", "480p (SD)", "Chi am thanh (Audio MP3/M4A)"]
GIOI_HAN_PLAYLIST = "" #@param {type:"string"}
DANH_SACH_PROXY = "" #@param {type:"string"}
REFERER_VUOT_CHAN = "" #@param {type:"string"}
NOI_DUNG_COOKIE = "" #@param {type:"string"}

import os
import re
import json
import urllib.request
import urllib.parse
from datetime import datetime, timezone, timedelta
import yt_dlp

VN_TZ = timezone(timedelta(hours=7))

deno_bin = os.path.expanduser("~/.deno/bin")
if os.path.exists(deno_bin) and deno_bin not in os.environ["PATH"]:
    os.environ["PATH"] = f"{deno_bin}:{os.environ['PATH']}"

def log(tag, msg, level="INFO"):
    colors = {
        "SYSTEM": "\\033[36m",
        "SUCCESS": "\\033[32m",
        "INFO": "\\033[34m",
        "WARN": "\\033[33m",
        "ERROR": "\\033[31m",
        "DRIVE": "\\033[35m",
        "FETCH": "\\033[94m",
        "PROBE": "\\033[95m",
        "QUEUE": "\\033[96m",
        "PROGRESS": "\\033[96m",
        "TRANSFER": "\\033[33m",
        "EXTRACT": "\\033[96m",
        "NOTIFY": "\\033[92m"
    }
    reset = "\\033[0m"
    dim = "\\033[90m"
    ts = datetime.now(VN_TZ).strftime("%H:%M:%S")
    tag_color = colors.get(level, "\\033[37m")
    print(f"{dim}{ts}{reset} {tag_color}[{tag}]{reset} {msg}")

def parse_proxies(proxy_raw):
    proxies = []
    if not proxy_raw or not proxy_raw.strip():
        return proxies
    raw_clean = proxy_raw.replace(',', '\\n').replace(';', '\\n').replace('|', '\\n').replace(' ', '\\n')
    for line in raw_clean.split('\\n'):
        line = line.strip()
        if not line:
            continue
        parts = line.split(':')
        if len(parts) == 4:
            ip, port, user, pwd = parts
            proxies.append(f"http://{user}:{pwd}@{ip}:{port}")
        elif len(parts) == 2:
            ip, port = parts
            proxies.append(f"http://{ip}:{port}")
        elif line.startswith(('http://', 'https://', 'socks5://', 'socks4://')):
            proxies.append(line)
    return proxies

def format_size(bytes_val):
    if not bytes_val or bytes_val <= 0:
        return "Không xác định"
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_val < 1024.0:
            return f"{bytes_val:.2f} {unit}"
        bytes_val /= 1024.0
    return f"{bytes_val:.2f} PB"

def format_resolution(width, height, fps=None):
    if not height:
        return "Tự động (Chất lượng cao nhất)"
    try:
        h = int(height)
        w = int(width) if width else 0
        if h >= 4320 or w >= 7680:
            label = "8K Ultra HD (4320p)"
        elif h >= 2160 or w >= 3840:
            label = "4K Ultra HD (2160p)"
        elif h >= 1440 or w >= 2560:
            label = "2K QHD (1440p)"
        elif h >= 1080 or w >= 1920:
            label = "1080p Full HD"
        elif h >= 720 or w >= 1280:
            label = "720p HD"
        elif h >= 480:
            label = "480p SD"
        elif h >= 360:
            label = "360p"
        elif h >= 240:
            label = "240p"
        elif h >= 144:
            label = "144p"
        else:
            label = f"{h}p"
            
        dim_str = f"{w}x{h}" if w > 0 else f"{h}p"
        fps_str = f" @ {fps}fps" if fps and int(fps) > 30 else ""
        return f"{label} ({dim_str}{fps_str})"
    except:
        return f"{height}p"

def extract_urls(raw_text):
    if not raw_text or not raw_text.strip():
        return []
    cleaned = raw_text.replace(',', '\\n').replace(';', '\\n').replace('|', '\\n')
    urls_list = []
    for line in cleaned.split('\\n'):
        line = line.strip()
        if not line:
            continue
        for token in line.split():
            token = token.strip()
            if token:
                urls_list.append(token)
    return urls_list

urls = extract_urls(LINK_CAN_TAI)
if not urls:
    log("ERROR", "Chưa có thông tin liên kết đầu vào.", "ERROR")
    raise ValueError("Vui lòng nhập liên kết hợp lệ tại ô LINK_CAN_TAI.")

proxies = parse_proxies(DANH_SACH_PROXY)
temp_workspace = "/content/temp_download"
os.makedirs(temp_workspace, exist_ok=True)

cookie_file_path = None
if NOI_DUNG_COOKIE.strip():
    cookie_input = NOI_DUNG_COOKIE.strip()
    if os.path.isfile(cookie_input):
        cookie_file_path = cookie_input
        log("SYSTEM", f"Sử dụng tệp Cookie xác thực: {cookie_file_path}", "INFO")
    else:
        cookie_file_path = os.path.join(temp_workspace, "auth_cookies.txt")
        with open(cookie_file_path, "w", encoding="utf-8") as cf:
            cf.write(cookie_input)
        log("SYSTEM", "Đã khởi tạo tệp Cookie xác thực từ dữ liệu đầu vào.", "INFO")

log("QUEUE", f"Đã khởi tạo hàng chờ gồm {len(urls)} tác vụ cần xử lý.", "INFO")
log("SYSTEM", f"Bắt đầu phân tích thông số kỹ thuật cho {len(urls)} liên kết trong hàng chờ...", "SYSTEM")

session_tasks = []

for idx, url in enumerate(urls, start=1):
    log("PROBE", f"[Hàng chờ {idx}/{len(urls)}] Phân tích liên kết: {url}", "PROBE")
    current_proxy = proxies[(idx - 1) % len(proxies)] if proxies else None
    
    is_torrent = url.startswith('magnet:?') or url.lower().endswith('.torrent') or '.torrent?' in url.lower()
    is_gdrive = 'drive.google.com' in url.lower() or 'docs.google.com' in url.lower()
    is_mega = 'mega.nz' in url.lower() or 'mega.co.nz' in url.lower()
    
    task_info = {
        "url": url,
        "type": "standard",
        "proxy": current_proxy,
        "title": "Tệp tin tải xuống",
        "resolution": "Không xác định",
        "filesize_str": "Không xác định",
        "duration_str": "Không xác định",
        "ext": "mp4",
        "format_spec": "bestvideo+bestaudio/best",
        "is_audio_only": False,
        "is_playlist": False,
        "playlist_title": "",
        "playlist_items": GIOI_HAN_PLAYLIST.strip()
    }
    
    if is_gdrive:
        task_info["type"] = "gdrive"
        is_folder = '/folders/' in url.lower()
        task_info["is_folder"] = is_folder
        task_info["resolution"] = "Thư mục Google Drive" if is_folder else "Tệp Google Drive"
        log("INFO", f"Nguồn: Google Drive ({task_info['resolution']})", "INFO")
        log("INFO", f"Công cụ tải tối ưu: gdown (Hỗ trợ vượt xác thực virus & tải trọn thư mục)", "INFO")
        session_tasks.append(task_info)
        continue

    elif is_mega:
        task_info["type"] = "mega"
        task_info["resolution"] = "Dữ liệu đám mây MEGA"
        log("INFO", f"Nguồn: Nền tảng lưu trữ MEGA (mega.nz)", "INFO")
        log("INFO", f"Công cụ tải tối ưu: megatools", "INFO")
        session_tasks.append(task_info)
        continue

    elif is_torrent:
        task_info["type"] = "torrent"
        task_info["title"] = "Gói tệp BitTorrent / Magnet"
        task_info["resolution"] = "Đa luồng P2P"
        log("INFO", f"Nguồn: Giao thức chia sẻ tệp BitTorrent / Magnet Link", "INFO")
        log("INFO", f"Công cụ tải tối ưu: aria2c (Kích hoạt DHT, OpenTrackers & tự động xử lý nghẽn)", "INFO")
        session_tasks.append(task_info)
        continue

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }
    if REFERER_VUOT_CHAN.strip():
        headers['Referer'] = REFERER_VUOT_CHAN.strip()
        headers['Origin'] = urllib.parse.urlsplit(REFERER_VUOT_CHAN.strip()).scheme + "://" + urllib.parse.urlsplit(REFERER_VUOT_CHAN.strip()).netloc
    elif 'seenow' in url.lower() or 'vtv' in url.lower():
        headers['Referer'] = 'https://vtvprime.vn/'
        headers['Origin'] = 'https://vtvprime.vn'

    ydl_inspect_opts = {
        'quiet': True,
        'no_warnings': True,
        'http_headers': headers,
        'remote_components': ['ejs:github'],
        'extract_flat': 'in_playlist',
        'extractor_args': {
            'youtube': {
                'player_client': ['web', 'mweb', 'android']
            }
        }
    }
    if GIOI_HAN_PLAYLIST.strip() and GIOI_HAN_PLAYLIST.strip().lower() not in ('tat_ca', 'all', ''):
        ydl_inspect_opts['playlist_items'] = GIOI_HAN_PLAYLIST.strip()
    if cookie_file_path:
        ydl_inspect_opts['cookiefile'] = cookie_file_path
    if current_proxy:
        ydl_inspect_opts['proxy'] = current_proxy

    try:
        with yt_dlp.YoutubeDL(ydl_inspect_opts) as ydl:
            meta = ydl.extract_info(url, download=False)
            
            # Kiểm tra nếu là Playlist đa nền tảng
            if meta.get('_type') == 'playlist' or 'entries' in meta:
                task_info["type"] = "playlist"
                task_info["is_playlist"] = True
                task_info["playlist_title"] = meta.get('title') or "Danh_sach_phat"
                entries = list(meta.get('entries', []))
                count_entries = len(entries)
                task_info["title"] = f"Danh sách phát: {task_info['playlist_title']}"
                task_info["resolution"] = f"Bộ sưu tập ({count_entries} video/tệp)"
                task_info["filesize_str"] = "Đa luồng dữ liệu"
                task_info["duration_str"] = f"{count_entries} mục"
                
                # Cấu hình chất lượng cho từng phần tử trong playlist
                if CHAT_LUONG_TAI == "Chi am thanh (Audio MP3/M4A)":
                    task_info["format_spec"] = "bestaudio/best"
                    task_info["is_audio_only"] = True
                    task_info["ext"] = "mp3"
                else:
                    task_info["format_spec"] = "bestvideo+bestaudio/best"
                    task_info["ext"] = "mp4"
                
                log("INFO", f"Phát hiện danh sách phát đa video: {task_info['playlist_title']} ({count_entries} mục)", "INFO")
                pl_limit_lbl = GIOI_HAN_PLAYLIST.strip() if GIOI_HAN_PLAYLIST.strip() else "Toàn bộ"
                log("INFO", f"Giới hạn cấu hình: {pl_limit_lbl} | Chất lượng: {CHAT_LUONG_TAI}", "INFO")
                session_tasks.append(task_info)
                continue
                
            title = meta.get('title', 'Không xác định')
            ext = meta.get('ext', 'mp4')
            duration = meta.get('duration_string') or (f"{meta.get('duration')}s" if meta.get('duration') else "Không xác định")
            
            # Quét chính xác độ phân giải thực tế của nguồn
            formats = meta.get('formats', [])
            available_heights = sorted(list(set([f.get('height') for f in formats if f.get('height') and f.get('vcodec') != 'none'])))
            max_available_height = available_heights[-1] if available_heights else (meta.get('height') or 0)
            
            # Ánh xạ theo tùy chọn CHAT_LUONG_TAI đảm bảo khớp 100% giữa Bước 3 và Bước 4
            target_format = "bestvideo+bestaudio/best"
            is_audio = False
            
            if CHAT_LUONG_TAI == "Chi am thanh (Audio MP3/M4A)":
                target_format = "bestaudio/best"
                is_audio = True
                ext = "mp3"
                res_label = "Chỉ âm thanh (Tự động trích xuất MP3 320kbps)"
            elif CHAT_LUONG_TAI == "Cao nhat (Tu dong)":
                target_format = "bestvideo+bestaudio/best"
                res_label = f"{format_resolution(meta.get('width'), max_available_height, meta.get('fps'))} [Tối đa nguồn]"
            else:
                req_h = 2160 if "4K" in CHAT_LUONG_TAI else (1440 if "2K" in CHAT_LUONG_TAI else (1080 if "1080p" in CHAT_LUONG_TAI else (720 if "720p" in CHAT_LUONG_TAI else (480 if "480p" in CHAT_LUONG_TAI else max_available_height))))
                if max_available_height < req_h and max_available_height > 0:
                    target_format = f"bestvideo[height<={max_available_height}]+bestaudio/best[height<={max_available_height}]"
                    res_label = f"{format_resolution(None, max_available_height)} [Nguồn tối đa {max_available_height}p, tự động khớp tối đa]"
                else:
                    target_format = f"bestvideo[height<={req_h}]+bestaudio/best[height<={req_h}]"
                    res_label = f"{format_resolution(None, req_h)} [Khớp chuẩn yêu cầu]"
                
            bytes_sz = meta.get('filesize') or meta.get('filesize_approx')
            size_str = format_size(bytes_sz)
            
            task_info.update({
                "type": "video_stream",
                "title": title,
                "resolution": res_label,
                "filesize_str": size_str,
                "duration_str": duration,
                "ext": ext,
                "format_spec": target_format,
                "is_audio_only": is_audio
            })
            
            log("INFO", f"Tiêu đề: {title}", "INFO")
            log("INFO", f"Chất lượng chuẩn đoán: {res_label} | Thời lượng: {duration}", "INFO")
            log("INFO", f"Dung lượng ước tính: {size_str} | Định dạng đích: {ext}", "INFO")
            
    except Exception as e:
        task_info["type"] = "direct_file"
        try:
            req = urllib.request.Request(url, headers=headers, method='HEAD')
            with urllib.request.urlopen(req, timeout=5) as resp:
                sz = int(resp.headers.get('Content-Length', 0))
                ctype = resp.headers.get('Content-Type', 'Direct link')
                task_info["title"] = os.path.basename(urllib.parse.urlsplit(url).path) or "direct_file"
                task_info["filesize_str"] = format_size(sz)
                task_info["resolution"] = f"Tệp tải trực tiếp ({ctype})"
                log("INFO", f"Tiêu đề: {task_info['title']}", "INFO")
                log("INFO", f"Dung lượng tệp: {task_info['filesize_str']} | Định dạng: {ctype}", "INFO")
        except:
            log("WARN", "Không thể lấy trước siêu dữ liệu. Hệ thống sẽ xử lý bằng bộ tải đa luồng ở Bước 4.", "WARN")

    session_tasks.append(task_info)

cache_path = os.path.join(temp_workspace, "session_tasks.json")
with open(cache_path, "w", encoding="utf-8") as f:
    json.dump({
        "urls": urls,
        "proxies": proxies,
        "referer": REFERER_VUOT_CHAN.strip(),
        "cookie_file": cookie_file_path,
        "chat_luong": CHAT_LUONG_TAI,
        "gioi_han_playlist": GIOI_HAN_PLAYLIST.strip(),
        "tasks": session_tasks
    }, f, ensure_ascii=False, indent=2)

print("\\n" + "="*60)
log("SUCCESS", f"Hoàn tất kiểm tra {len(session_tasks)}/{len(urls)} liên kết trong hàng chờ.", "SUCCESS")
print(f"Danh sách hàng chờ sẵn sàng tải ({len(session_tasks)} tác vụ):")
for i, t in enumerate(session_tasks, start=1):
    t_title = t.get('title', 'Tệp tin')
    t_res = t.get('resolution', 'Không xác định')
    t_sz = t.get('filesize_str', 'Không xác định')
    print(f"  + [{i}/{len(session_tasks)}] {t_title} | {t_res} | {t_sz}")
print("="*60)
"""

notebook['cells'].append({
    'cell_type': 'code',
    'metadata': {'id': 'inspect_source_urls', 'cellView': 'form'},
    'source': [line + '\n' for line in step3_code.split('\n')],
    'execution_count': None,
    'outputs': []
})

# 5. Step 4: Storage, Queue Execution, Auto-Split, Timeout/Retry and Drive Sync
step4_code = """#@title Bước 4: Cấu hình lưu trữ và tiến hành tải xuống
#@markdown Thiết lập thư mục lưu trữ, đặt tên tệp tùy biến, chia nhỏ tệp lớn và bắt đầu tải xuống theo hàng chờ.

THU_MUC_DRIVE = "/content/drive/MyDrive/colab-drive" #@param {type:"string"}
TEN_FILE_TU_DAT = "" #@param {type:"string"}
CAT_TEP_DUNG_LUONG_LON = "Khong cat" #@param ["Khong cat", "Chia thanh 2 phan", "Chia thanh 4 phan", "Chia thanh 6 phan", "Chia thanh 8 phan", "Chia thanh 10 phan"]
TELEGRAM_BOT_TOKEN = "" #@param {type:"string"}
TELEGRAM_CHAT_ID = "" #@param {type:"string"}

import os
import re
import sys
import json
import time
import shutil
import urllib.request
import urllib.parse
from datetime import datetime, timezone, timedelta
import yt_dlp

VN_TZ = timezone(timedelta(hours=7))

deno_bin = os.path.expanduser("~/.deno/bin")
if os.path.exists(deno_bin) and deno_bin not in os.environ["PATH"]:
    os.environ["PATH"] = f"{deno_bin}:{os.environ['PATH']}"

is_progress_line_active = False

def log(tag, msg, level="INFO"):
    global is_progress_line_active
    colors = {
        "SYSTEM": "\\033[36m",
        "SUCCESS": "\\033[32m",
        "INFO": "\\033[34m",
        "WARN": "\\033[33m",
        "ERROR": "\\033[31m",
        "DRIVE": "\\033[35m",
        "FETCH": "\\033[94m",
        "PROBE": "\\033[95m",
        "QUEUE": "\\033[96m",
        "PROGRESS": "\\033[96m",
        "TRANSFER": "\\033[33m",
        "EXTRACT": "\\033[96m",
        "SKIP": "\\033[93m",
        "NOTIFY": "\\033[92m"
    }
    reset = "\\033[0m"
    dim = "\\033[90m"
    ts = datetime.now(VN_TZ).strftime("%H:%M:%S")
    tag_color = colors.get(level, "\\033[37m")
    
    if is_progress_line_active:
        sys.stdout.write('\\n')
        sys.stdout.flush()
        is_progress_line_active = False
        
    print(f"{dim}{ts}{reset} {tag_color}[{tag}]{reset} {msg}")

def format_size(bytes_val):
    if not bytes_val or bytes_val <= 0:
        return "Không xác định"
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_val < 1024.0:
            return f"{bytes_val:.2f} {unit}"
        bytes_val /= 1024.0
    return f"{bytes_val:.2f} PB"

def format_eta(seconds):
    if seconds is None:
        return "Đang tính..."
    try:
        sec = int(seconds)
        if sec < 0:
            return "Đang hoàn tất..."
        m, s = divmod(sec, 60)
        h, m = divmod(m, 60)
        if h > 0:
            return f"{h:02d}h:{m:02d}m:{s:02d}s"
        return f"{m:02d}m:{s:02d}s"
    except:
        return "Đang tính..."

def send_telegram(token, chat_id, message):
    if not token or not chat_id:
        return
    try:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        payload = json.dumps({"chat_id": chat_id, "text": message}).encode('utf-8')
        req = urllib.request.Request(url, data=payload, headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            if resp.status == 200:
                log("NOTIFY", "Đã gửi thông báo báo cáo tiến trình qua Telegram.", "NOTIFY")
    except Exception as e:
        log("WARN", f"Không thể gửi thông báo Telegram: {e}", "WARN")

def mask_proxy(p_str):
    return re.sub(r'//.*?:.*?@', '//***:***@', p_str)

def get_unique_filename(dest_dir, filename):
    base, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    while os.path.exists(os.path.join(dest_dir, new_filename)):
        new_filename = f"{base}_{counter}{ext}"
        counter += 1
    return new_filename

logged_destinations = set()

class YTDLSystemLogger:
    def debug(self, msg):
        global logged_destinations
        if msg.startswith('[download] Destination:'):
            dest_name = os.path.basename(msg.split(': ')[-1])
            if dest_name not in logged_destinations:
                logged_destinations.add(dest_name)
                log("FETCH", f"Bắt đầu khởi tạo luồng tệp: {dest_name}", "INFO")
        elif 'Merging formats into' in msg:
            merged_name = os.path.basename(msg.split('"')[1]) if '"' in msg else "tệp hoàn chỉnh"
            log("TRANSFER", f"Đang ghép kênh video + âm thanh hoàn chỉnh (FFmpeg): {merged_name}...", "TRANSFER")
            
    def info(self, msg):
        if 'Extracting URL' in msg:
            log("FETCH", "Đang kết nối và phân tích luồng trực tiếp từ máy chủ...", "INFO")
        elif 'Downloading 1 format(s)' in msg:
            fmt = msg.split(': ')[-1] if ': ' in msg else "tối ưu"
            log("FETCH", f"Đã khóa định dạng tải xuống tốt nhất ({fmt}). Bắt đầu truyền tải...", "INFO")
        elif not msg.startswith('[download]') and not msg.startswith('[youtube]'):
            log("INFO", msg, "INFO")
            
    def warning(self, msg):
        ignore_keywords = ['No supported JavaScript runtime', 'Remote components', 'n challenge solving', 'PO Token', 'SABR-only', 'URL']
        if any(w in msg for w in ignore_keywords):
            return
        log("WARN", msg, "WARN")
        
    def error(self, msg):
        if 'Got error: 297 bytes read' not in msg:
            log("ERROR", msg, "ERROR")

last_progress_time = 0

def ytdl_progress_hook(d):
    global last_progress_time, is_progress_line_active
    if d['status'] == 'downloading':
        now = time.time()
        if now - last_progress_time >= 1.0:
            last_progress_time = now
            is_progress_line_active = True
            downloaded = d.get('downloaded_bytes', 0)
            total = d.get('total_bytes') or d.get('total_bytes_estimate', 0)
            speed = d.get('speed') or 0
            eta = d.get('eta')
            
            percent_str = f"{(downloaded / total * 100):.1f}%" if total > 0 else "---%"
            speed_str = f"{(speed / (1024**2)):.2f} MB/s" if speed else "--- MB/s"
            dl_mb = downloaded / (1024**2)
            tot_mb = total / (1024**2) if total > 0 else 0
            size_prog = f"({dl_mb:.1f}/{tot_mb:.1f} MB)" if total > 0 else f"({dl_mb:.1f} MB)"
            eta_str = format_eta(eta)
            
            dim = "\\033[90m"
            cyan = "\\033[96m"
            reset = "\\033[0m"
            ts = datetime.now(VN_TZ).strftime("%H:%M:%S")
            line = f"\\r{dim}{ts}{reset} {cyan}[PROGRESS]{reset} Tiến độ: {percent_str} {size_prog} | Tốc độ: {speed_str} | Còn lại (ETA): {eta_str}"
            sys.stdout.write(line)
            sys.stdout.flush()
    elif d['status'] == 'finished':
        if is_progress_line_active:
            sys.stdout.write('\\n')
            sys.stdout.flush()
            is_progress_line_active = False
        fname = os.path.basename(d.get('filename', 'tệp'))
        log("SUCCESS", f"Đã tải xong luồng dữ liệu của tệp: {fname}", "SUCCESS")

temp_workspace = "/content/temp_download"
cache_path = os.path.join(temp_workspace, "session_tasks.json")

if not os.path.exists(cache_path):
    log("ERROR", "Chưa tìm thấy dữ liệu nguồn. Vui lòng chạy ô Bước 3 trước khi thực thi Bước 4.", "ERROR")
    raise FileNotFoundError("Chưa thực thi Bước 3 để nạp liên kết.")

with open(cache_path, "r", encoding="utf-8") as f:
    session_data = json.load(f)

urls = session_data.get("urls", [])
proxies = session_data.get("proxies", [])
referer = session_data.get("referer", "")
cookie_file_path = session_data.get("cookie_file")
tasks_meta = session_data.get("tasks", [])
gioi_han_playlist = session_data.get("gioi_han_playlist", "")

os.makedirs(THU_MUC_DRIVE, exist_ok=True)

_, _, vm_free = shutil.disk_usage('/content')
free_gb = vm_free / (1024**3)
log("SYSTEM", f"Kiểm tra bộ nhớ: Bộ đệm máy ảo Colab khả dụng {free_gb:.2f} GB.", "INFO")
if free_gb < 2.0:
    log("WARN", f"Cảnh báo: Bộ đệm máy ảo Colab còn dưới {free_gb:.2f} GB khả dụng.", "WARN")

# Khởi tạo hàng chờ tác vụ linh hoạt
task_queue = list(tasks_meta)
total_tasks_initial = len(task_queue)

log("QUEUE", f"Bắt đầu thực thi hàng chờ tải xuống gồm {total_tasks_initial} tác vụ đa nguồn...", "SYSTEM")

success_count = 0
failed_count = 0
saved_files_report = []
processed_index = 0

while task_queue:
    current_meta = task_queue.pop(0)
    processed_index += 1
    
    target_url = current_meta.get("url")
    task_type = current_meta.get("type", "standard")
    title_display = current_meta.get("title", target_url)
    res_display = current_meta.get("resolution", "")
    sz_display = current_meta.get("filesize_str", "")
    format_spec = current_meta.get("format_spec", "bestvideo+bestaudio/best")
    is_audio_only = current_meta.get("is_audio_only", False)
    is_playlist = current_meta.get("is_playlist", False)
    playlist_title = current_meta.get("playlist_title", "Playlist")
    torrent_attempt = current_meta.get("torrent_attempt", 0)
    
    extra_info = f" ({res_display} | {sz_display})" if res_display and res_display != "Không xác định" else ""
    log("FETCH", f"[Hàng chờ {processed_index}/{total_tasks_initial}] Đang tải: {title_display}{extra_info}", "FETCH")
    
    # 1. Cơ chế kiểm tra tệp đã tồn tại trên Drive (Skip Existing)
    if BO_QUA_TEP_DA_CO and not is_playlist and title_display != "Tệp tin tải xuống":
        clean_name = re.sub(r'[/\\\\?%*:|"<>]', '_', title_display)
        match_found = False
        for ex_file in os.listdir(THU_MUC_DRIVE):
            if ex_file.startswith(clean_name[:40]) and os.path.getsize(os.path.join(THU_MUC_DRIVE, ex_file)) > 1024*1024:
                match_found = True
                break
        if match_found:
            log("SKIP", f"Tệp tin đã tồn tại hoàn chỉnh trên Google Drive. Tự động bỏ qua tác vụ.", "SKIP")
            skipped_count += 1
            success_count += 1
            continue

    current_proxy = current_meta.get("proxy")
    if current_proxy:
        log("SYSTEM", f"Định tuyến qua proxy: {mask_proxy(current_proxy)}", "INFO")
        
    sub_task_dir = os.path.join(temp_workspace, f"download_task_{processed_index:03d}")
    os.makedirs(sub_task_dir, exist_ok=True)
    
    download_ok = False
    
    # 2. Xử lý nguồn GOOGLE DRIVE (gdown)
    if task_type == "gdrive" or 'drive.google.com' in target_url.lower():
        is_folder = '/folders/' in target_url.lower() or current_meta.get("is_folder", False)
        log("FETCH", f"Kích hoạt engine gdown cho Google Drive ({'Thư mục' if is_folder else 'Tệp tin'})...", "FETCH")
        if is_folder:
            cmd = f'gdown --folder "{target_url}" -O "{sub_task_dir}" --remaining-ok'
        else:
            cmd = f'gdown "{target_url}" -O "{sub_task_dir}" --fuzzy'
        if current_proxy:
            cmd = f'export http_proxy="{current_proxy}" && export https_proxy="{current_proxy}" && ' + cmd
        ret = os.system(cmd)
        if ret == 0:
            download_ok = True
        else:
            log("WARN", "gdown báo lỗi. Thử nghiệm tải dự phòng bằng aria2c...", "WARN")
            direct_cmd = f'aria2c -x16 -s16 -k1M --file-allocation=none -d "{sub_task_dir}" "{target_url}"'
            if os.system(direct_cmd) == 0:
                download_ok = True
            else:
                log("ERROR", f"Không thể tải tệp từ Google Drive: {target_url}. Tự động bỏ qua.", "ERROR")
                failed_count += 1
                continue

    # 3. Xử lý nguồn MEGA (megatools)
    elif task_type == "mega" or 'mega.nz' in target_url.lower() or 'mega.co.nz' in target_url.lower():
        log("FETCH", "Kích hoạt engine megatools cho nền tảng MEGA...", "FETCH")
        cmd = f'megatools dl "{target_url}" --path "{sub_task_dir}"'
        if os.system(cmd) == 0:
            download_ok = True
        else:
            log("ERROR", f"Không thể tải tệp từ MEGA: {target_url}. Tự động bỏ qua.", "ERROR")
            failed_count += 1
            continue

    # 4. Xử lý nguồn BITTORRENT / MAGNET (aria2c với cơ chế timeout 3 phút và dời hàng chờ)
    elif task_type == "torrent" or target_url.startswith('magnet:?') or target_url.lower().endswith('.torrent'):
        log("FETCH", "Kích hoạt engine aria2c P2P (DHT/Peer/Trackers)...", "FETCH")
        cmd = f'aria2c --enable-dht=true --enable-dht6=true --bt-enable-lpd=true --bt-max-peers=120 --seed-time=0 --bt-stop-timeout=180 --summary-interval=10 --file-allocation=none -d "{sub_task_dir}" "{target_url}"'
        ret_status = os.system(cmd)
        
        has_files = any(os.path.isfile(os.path.join(sub_task_dir, f)) for f in os.listdir(sub_task_dir) if not f.endswith('.aria2'))
        if ret_status == 0 and has_files:
            download_ok = True
        else:
            if torrent_attempt == 0:
                current_meta['torrent_attempt'] = 1
                log("WARN", "Tác vụ Torrent/Magnet không nhận được seeder sau 3 phút. Đẩy xuống cuối hàng chờ để thử lại sau...", "WARN")
                task_queue.append(current_meta)
                shutil.rmtree(sub_task_dir, ignore_errors=True)
                continue
            else:
                log("ERROR", "Tác vụ Torrent/Magnet vẫn không tìm thấy peer/seeder ở lượt thử thứ 2. Tự động bỏ qua (Skip).", "ERROR")
                failed_count += 1
                shutil.rmtree(sub_task_dir, ignore_errors=True)
                continue

    # 5. Xử lý luồng VIDEO / AUDIO / PLAYLIST / DIRECT FILE (yt-dlp)
    else:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
        if referer:
            headers['Referer'] = referer
            headers['Origin'] = urllib.parse.urlsplit(referer).scheme + "://" + urllib.parse.urlsplit(referer).netloc
        elif 'seenow' in target_url.lower() or 'vtv' in target_url.lower():
            headers['Referer'] = 'https://vtvprime.vn/'
            headers['Origin'] = 'https://vtvprime.vn'

        outtmpl_pattern = os.path.join(sub_task_dir, '%(title).200B.%(ext)s')
        if is_playlist:
            outtmpl_pattern = os.path.join(sub_task_dir, '%(playlist_index)s - %(title).200B.%(ext)s')

        ydl_opts = {
            'outtmpl': outtmpl_pattern,
            'format': format_spec,
            'merge_output_format': 'mp4' if not is_audio_only else None,
            'concurrent_fragment_downloads': 4,
            'retries': 5,
            'fragment_retries': 5,
            'quiet': True,
            'no_warnings': True,
            'http_headers': headers,
            'logger': YTDLSystemLogger(),
            'progress_hooks': [ytdl_progress_hook],
            'remote_components': ['ejs:github'],
            'extractor_args': {
                'youtube': {
                    'player_client': ['web', 'mweb', 'android']
                }
            }
        }
        
        if is_audio_only:
            ydl_opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }]
            
        if is_playlist and gioi_han_playlist.strip() and gioi_han_playlist.strip().lower() not in ('tat_ca', 'all', ''):
            ydl_opts['playlist_items'] = gioi_han_playlist.strip()

        if cookie_file_path:
            ydl_opts['cookiefile'] = cookie_file_path
        if current_proxy:
            ydl_opts['proxy'] = current_proxy

        log("FETCH", f"Khởi chạy tải luồng ổn định ({format_spec})...", "INFO")
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([target_url])
            download_ok = True
        except Exception as err:
            log("WARN", f"Định dạng ghép kênh gặp lỗi ({err}). Tự động thử định dạng tương thích...", "WARN")
            ydl_opts['extractor_args']['youtube']['player_client'] = ['android']
            ydl_opts['format'] = 'bestvideo+bestaudio/best' if not is_audio_only else 'bestaudio/best'
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([target_url])
                download_ok = True
            except Exception as err2:
                log("WARN", "Chuyển sang định dạng tương thích đơn luồng 'best'...", "WARN")
                ydl_opts['format'] = 'best'
                try:
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([target_url])
                    download_ok = True
                except Exception as err3:
                    log("ERROR", f"Không thể tải xuống tệp từ nguồn ({err3}). Tự động bỏ qua (Skip).", "ERROR")
                    failed_count += 1
                    shutil.rmtree(sub_task_dir, ignore_errors=True)
                    continue



    # 6. Cơ chế tự động chia nhỏ tệp lớn (Auto-Split) vào thư mục riêng biệt
    if download_ok and CAT_TEP_DUNG_LUONG_LON != "Khong cat":
        vol_size = "2000m" if "2GB" in CAT_TEP_DUNG_LUONG_LON else ("4000m" if "4GB" in CAT_TEP_DUNG_LUONG_LON else "1000m")
        threshold_bytes = 2 * 1024 * 1024 * 1024 if "2GB" in CAT_TEP_DUNG_LUONG_LON else (4 * 1024 * 1024 * 1024 if "4GB" in CAT_TEP_DUNG_LUONG_LON else 1024 * 1024 * 1024)
        
        for item in list(os.listdir(sub_task_dir)):
            item_path = os.path.join(sub_task_dir, item)
            if os.path.isfile(item_path) and os.path.getsize(item_path) >= threshold_bytes:
                base_name, _ = os.path.splitext(item)
                clean_base = re.sub(r'[/\\\\?%*:|"<>]', '_', base_name)
                split_folder_name = f"{clean_base}_parts"
                split_dest_dir = os.path.join(THU_MUC_DRIVE, split_folder_name)
                os.makedirs(split_dest_dir, exist_ok=True)
                
                log("SYSTEM", f"Tệp dung lượng lớn ({format_size(os.path.getsize(item_path))}). Bắt đầu chia nhỏ {CAT_TEP_DUNG_LUONG_LON} vào thư mục riêng: {split_folder_name}...", "INFO")
                archive_temp = os.path.join(sub_task_dir, f"{clean_base}.7z")
                cmd_split = f'7z a -v{vol_size} "{archive_temp}" "{item_path}" > /dev/null 2>&1'
                if os.system(cmd_split) == 0:
                    os.remove(item_path)
                    for split_part in os.listdir(sub_task_dir):
                        if split_part.startswith(clean_base) and ('.7z.' in split_part or split_part.endswith('.7z')):
                            shutil.move(os.path.join(sub_task_dir, split_part), os.path.join(split_dest_dir, split_part))
                    log("SUCCESS", f"Đã chia nhỏ hoàn tất và lưu tại: {split_dest_dir}", "SUCCESS")
                    saved_files_report.append(f"{split_folder_name} (Thư mục chia nhỏ)")
                else:
                    log("WARN", "Không thể nén chia nhỏ tệp. Sẽ giữ nguyên định dạng gốc.", "WARN")

    # 7. Quét tệp tin đầu ra và chuyển giao lên Google Drive
    output_items = []
    for entry in os.listdir(sub_task_dir):
        full_entry = os.path.join(sub_task_dir, entry)
        if not entry.endswith(('.part', '.ytdl', '.aria2')):
            output_items.append(full_entry)

    if download_ok and output_items:
        target_drive_folder = THU_MUC_DRIVE
        if is_playlist:
            clean_pl_title = re.sub(r'[/\\\\?%*:|"<>]', '_', playlist_title)
            target_drive_folder = os.path.join(THU_MUC_DRIVE, clean_pl_title)
            os.makedirs(target_drive_folder, exist_ok=True)
            log("TRANSFER", f"Chuyển giao {len(output_items)} mục của danh sách phát vào thư mục: {target_drive_folder}", "TRANSFER")
        else:
            log("TRANSFER", f"Chuyển giao {len(output_items)} mục dữ liệu vào Google Drive: {target_drive_folder}", "TRANSFER")
        
        custom_raw = TEN_FILE_TU_DAT.strip()
        custom_base, specified_ext = os.path.splitext(custom_raw) if custom_raw else ("", "")
        num_suffix = f"_{processed_index}" if total_tasks_initial > 1 and not is_playlist else ""

        for item_idx, item_path in enumerate(output_items):
            orig_name = os.path.basename(item_path)
            orig_base, orig_ext = os.path.splitext(orig_name)

            if os.path.isdir(item_path):
                dest_name = f"{custom_base}{num_suffix}" if (custom_raw and not is_playlist) else orig_name
                target_dest_path = os.path.join(target_drive_folder, dest_name)
                if os.path.exists(target_dest_path):
                    target_dest_path = os.path.join(target_drive_folder, f"{dest_name}_{item_idx+1}")
                shutil.move(item_path, target_dest_path)
                log("SUCCESS", f"Lưu trữ thành công thư mục: {target_dest_path}", "SUCCESS")
                saved_files_report.append(os.path.basename(target_dest_path) + " (Thư mục)")
            else:
                if custom_raw and not is_playlist:
                    final_ext = specified_ext if specified_ext else orig_ext
                    part_suffix = f"_{item_idx+1}" if len(output_items) > 1 else ""
                    dest_filename = f"{custom_base}{num_suffix}{part_suffix}{final_ext}"
                else:
                    dest_filename = orig_name

                target_fname = get_unique_filename(target_drive_folder, dest_filename)
                dest_path = os.path.join(target_drive_folder, target_fname)
                shutil.move(item_path, dest_path)
                log("SUCCESS", f"Lưu trữ thành công: {dest_path}", "SUCCESS")
                saved_files_report.append(target_fname)
                
        success_count += 1
    elif not download_ok:
        log("ERROR", f"Thất bại khi xử lý tác vụ [{processed_index}/{total_tasks_initial}]", "ERROR")
        failed_count += 1

    shutil.rmtree(sub_task_dir, ignore_errors=True)

try:
    shutil.rmtree(temp_workspace, ignore_errors=True)
except:
    pass

print("\\n" + "="*60)
log("SYSTEM", f"Tổng kết hàng chờ: {success_count} thành công, {failed_count} thất bại.", "SYSTEM")
log("DRIVE", f"Thư mục lưu trữ trên Google Drive: {THU_MUC_DRIVE}", "DRIVE")
print("="*60)

if TELEGRAM_BOT_TOKEN.strip() and TELEGRAM_CHAT_ID.strip():
    ts_now = datetime.now(VN_TZ).strftime("%H:%M:%S - %d/%m/%Y")
    report_lines = [
        "[Colab Drive] Bao cao ket qua hang cho:",
        f"- Thoi gian hoan tat: {ts_now}",
        f"- Tong so tac vu: {total_tasks_initial}",
        f"- Thanh cong: {success_count}",
        f"- That bai: {failed_count}",
        f"- Thu muc luu tru: {THU_MUC_DRIVE}"
    ]
    if saved_files_report:
        report_lines.append(f"- Tep/Thu muc da luu ({len(saved_files_report)}):")
        for fn in saved_files_report[:10]:
            report_lines.append(f"  + {fn}")
        if len(saved_files_report) > 10:
            report_lines.append(f"  ... va {len(saved_files_report) - 10} muc khac")
    
    send_telegram(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, "\\n".join(report_lines))
"""

notebook['cells'].append({
    'cell_type': 'code',
    'metadata': {'id': 'execute_download_and_sync', 'cellView': 'form'},
    'source': [line + '\n' for line in step4_code.split('\n')],
    'execution_count': None,
    'outputs': []
})

target_path = r'C:\Users\Huy Vu\Downloads\colab-drive\colab-drive.ipynb'
with open(target_path, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, ensure_ascii=False, indent=2)

print('Successfully generated polished Colab Drive notebook with all requested features')
