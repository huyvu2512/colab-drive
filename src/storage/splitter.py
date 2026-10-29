import os
import re
import math
import shutil
from src.core.logger import log
from src.core.utils import format_size

def split_file_into_parts(file_path, dest_parent_dir, split_option):
    if split_option == "Khong cat" or not os.path.isfile(file_path):
        return False, None
        
    parts_match = re.search(r'(\d+)', split_option)
    num_parts = int(parts_match.group(1)) if parts_match else 2
    
    file_sz = os.path.getsize(file_path)
    if file_sz < 1024 * 1024:
        return False, None
        
    parent_dir = os.path.dirname(file_path)
    base_name, _ = os.path.splitext(os.path.basename(file_path))
    clean_base = re.sub(r'[/\\?%*:|"<>]', '_', base_name)
    split_folder_name = f"{clean_base}_parts"
    split_dest_dir = os.path.join(dest_parent_dir, split_folder_name)
    os.makedirs(split_dest_dir, exist_ok=True)
    
    part_bytes = math.ceil(file_sz / num_parts)
    log("SYSTEM", f"Đang chia nhỏ tệp ({format_size(file_sz)}) thành {num_parts} phần vào thư mục: {split_folder_name}...", "INFO")
    archive_temp = os.path.join(parent_dir, f"{clean_base}.7z")
    cmd_split = f'7z a -v{part_bytes}b "{archive_temp}" "{file_path}" -mx0 > /dev/null 2>&1'
    
    if os.system(cmd_split) == 0:
        os.remove(file_path)
        for part in os.listdir(parent_dir):
            if part.startswith(clean_base) and ('.7z.' in part or part.endswith('.7z')):
                shutil.move(os.path.join(parent_dir, part), os.path.join(split_dest_dir, part))
        log("SUCCESS", f"Đã chia thành {num_parts} phần hoàn tất và lưu tại: {split_dest_dir}", "SUCCESS")
        return True, split_folder_name
        
    log("WARN", "Không thể nén chia nhỏ tệp. Sẽ giữ nguyên định dạng gốc.", "WARN")
    return False, None
