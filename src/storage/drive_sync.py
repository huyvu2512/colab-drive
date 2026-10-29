import os
import re
import shutil
from src.core.logger import log
from src.core.utils import get_unique_filename

def sync_to_drive(source_dir, drive_dir, custom_name="", is_playlist=False, playlist_title=""):
    os.makedirs(drive_dir, exist_ok=True)
    target_folder = drive_dir
    
    if is_playlist:
        clean_pl_title = re.sub(r'[/\\?%*:|"<>]', '_', playlist_title)
        target_folder = os.path.join(drive_dir, clean_pl_title)
        os.makedirs(target_folder, exist_ok=True)
        
    output_items = [
        os.path.join(source_dir, e) for e in os.listdir(source_dir)
        if not e.endswith(('.part', '.ytdl', '.aria2'))
    ]
    
    saved_reports = []
    custom_raw = custom_name.strip()
    custom_base, specified_ext = os.path.splitext(custom_raw) if custom_raw else ("", "")
    
    for idx, item_path in enumerate(output_items):
        orig_name = os.path.basename(item_path)
        orig_base, orig_ext = os.path.splitext(orig_name)
        
        if os.path.isdir(item_path):
            dest_name = custom_base if (custom_raw and not is_playlist) else orig_name
            target_dest = os.path.join(target_folder, dest_name)
            if os.path.exists(target_dest):
                target_dest = os.path.join(target_folder, f"{dest_name}_{idx+1}")
            shutil.move(item_path, target_dest)
            log("SUCCESS", f"Lưu trữ thành công thư mục: {target_dest}", "SUCCESS")
            saved_reports.append(os.path.basename(target_dest) + " (Thư mục)")
        else:
            if custom_raw and not is_playlist:
                final_ext = specified_ext if specified_ext else orig_ext
                dest_filename = f"{custom_base}_{idx+1}{final_ext}" if len(output_items) > 1 else f"{custom_base}{final_ext}"
            else:
                dest_filename = orig_name
                
            unique_fname = get_unique_filename(target_folder, dest_filename)
            dest_path = os.path.join(target_folder, unique_fname)
            shutil.move(item_path, dest_path)
            log("SUCCESS", f"Lưu trữ thành công: {dest_path}", "SUCCESS")
            saved_reports.append(unique_fname)
            
    return saved_reports
