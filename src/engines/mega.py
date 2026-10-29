import os
from src.core.logger import log

def download_mega(target_url, download_dir):
    log("FETCH", "Kích hoạt engine megatools cho nền tảng MEGA...", "FETCH")
    cmd = f'megatools dl "{target_url}" --path "{download_dir}"'
    return os.system(cmd)
