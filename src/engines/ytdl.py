import os
import sys
import time
from src.core.logger import log, VN_TZ
from src.core.utils import format_eta

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
    global last_progress_time
    import src.core.logger as core_logger
    if d['status'] == 'downloading':
        now = time.time()
        if now - last_progress_time >= 1.0:
            last_progress_time = now
            core_logger.is_progress_line_active = True
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
            
            dim = "\033[90m"
            cyan = "\033[96m"
            reset = "\033[0m"
            from datetime import datetime
            ts = datetime.now(VN_TZ).strftime("%H:%M:%S")
            line = f"\r{dim}{ts}{reset} {cyan}[PROGRESS]{reset} Tiến độ: {percent_str} {size_prog} | Tốc độ: {speed_str} | Còn lại (ETA): {eta_str}"
            sys.stdout.write(line)
            sys.stdout.flush()
    elif d['status'] == 'finished':
        if core_logger.is_progress_line_active:
            sys.stdout.write('\n')
            sys.stdout.flush()
            core_logger.is_progress_line_active = False
        fname = os.path.basename(d.get('filename', 'tệp'))
        log("SUCCESS", f"Đã tải xong luồng dữ liệu của tệp: {fname}", "SUCCESS")
