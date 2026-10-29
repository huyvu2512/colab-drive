import re
import os

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

def parse_proxies(proxy_raw):
    proxies = []
    if not proxy_raw or not proxy_raw.strip():
        return proxies
    raw_clean = proxy_raw.replace(',', '\n').replace(';', '\n').replace('|', '\n').replace(' ', '\n')
    for line in raw_clean.split('\n'):
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
