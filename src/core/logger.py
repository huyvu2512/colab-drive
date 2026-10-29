import sys
from datetime import datetime, timezone, timedelta

VN_TZ = timezone(timedelta(hours=7))

colors = {
    "SYSTEM": "\033[36m",
    "SUCCESS": "\033[32m",
    "INFO": "\033[34m",
    "WARN": "\033[33m",
    "ERROR": "\033[31m",
    "DRIVE": "\033[35m",
    "FETCH": "\033[94m",
    "PROBE": "\033[95m",
    "QUEUE": "\033[96m",
    "PROGRESS": "\033[96m",
    "TRANSFER": "\033[33m",
    "EXTRACT": "\033[96m",
    "SKIP": "\033[93m",
    "NOTIFY": "\033[92m"
}

is_progress_line_active = False

def log(tag, msg, level="INFO"):
    global is_progress_line_active
    reset = "\033[0m"
    dim = "\033[90m"
    ts = datetime.now(VN_TZ).strftime("%H:%M:%S")
    tag_color = colors.get(level, "\033[37m")
    
    if is_progress_line_active:
        sys.stdout.write('\n')
        sys.stdout.flush()
        is_progress_line_active = False
        
    print(f"{dim}{ts}{reset} {tag_color}[{tag}]{reset} {msg}")
