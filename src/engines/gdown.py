import os
from src.core.logger import log

def download_gdrive(target_url, download_dir, is_folder=False, proxy=None):
    log("FETCH", f"Kích hoạt engine gdown cho Google Drive ({'Thư mục' if is_folder else 'Tệp tin'})...", "FETCH")
    if is_folder:
        cmd = f'gdown --folder "{target_url}" -O "{download_dir}" --remaining-ok'
    else:
        cmd = f'gdown "{target_url}" -O "{download_dir}" --fuzzy'
        
    if proxy:
        cmd = f'export http_proxy="{proxy}" && export https_proxy="{proxy}" && ' + cmd
        
    return os.system(cmd)
