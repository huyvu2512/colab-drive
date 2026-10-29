import os
import re
import shutil
from src.core.logger import log
from src.core.utils import format_size

def split_large_file(file_path, dest_parent_dir, split_mode):
    if split_mode == "Khong cat" or not os.path.isfile(file_path):
        return False, None
        
    vol_size = "2000m" if "2GB" in split_mode else ("4000m" if "4GB" in split_mode else "1000m")
    threshold_bytes = 2 * 1024 * 1024 * 1024 if "2GB" in split_mode else (4 * 1024 * 1024 * 1024 if "4GB" in split_mode else 1024 * 1024 * 1024)
    
    file_sz = os.path.getsize(file_path)
    if file_sz < threshold_bytes:
        return False, None
        
    parent_dir = os.path.dirname(file_path)
    base_name, _ = os.path.splitext(os.path.basename(file_path))
    clean_base = re.sub(r'[/\\?%*:|"<>]', '_', base_name)
    split_folder_name = f"{clean_base}_parts"
    split_dest_dir = os.path.join(dest_parent_dir, split_folder_name)
    os.makedirs(split_dest_dir, exist_ok=True)
    
    log("SYSTEM", f"Tệp dung lượng lớn ({format_size(file_sz)}). Bắt đầu chia nhỏ {split_mode} vào thư mục riêng: {split_folder_name}...", "INFO")
    archive_temp = os.path.join(parent_dir, f"{clean_base}.7z")
    cmd_split = f'7z a -v{vol_size} "{archive_temp}" "{file_path}" > /dev/null 2>&1'
    
    if os.system(cmd_split) == 0:
        os.remove(file_path)
        for part in os.listdir(parent_dir):
            if part.startswith(clean_base) and ('.7z.' in part or part.endswith('.7z')):
                shutil.move(os.path.join(parent_dir, part), os.path.join(split_dest_dir, part))
        log("SUCCESS", f"Đã chia nhỏ hoàn tất và lưu tại: {split_dest_dir}", "SUCCESS")
        return True, split_folder_name
        
    log("WARN", "Không thể nén chia nhỏ tệp. Sẽ giữ nguyên định dạng gốc.", "WARN")
    return False, None
