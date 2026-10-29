import os
from src.core.logger import log

ARCHIVE_EXTENSIONS = ('.zip', '.rar', '.7z', '.tar', '.gz', '.tar.gz', '.tgz', '.bz2')

def extract_archives_in_dir(target_dir):
    for root, dirs, files in os.walk(target_dir):
        for f in files:
            f_path = os.path.join(root, f)
            lower_f = f.lower()
            if lower_f.endswith(ARCHIVE_EXTENSIONS):
                folder_name = os.path.splitext(f)[0]
                if folder_name.lower().endswith('.tar'):
                    folder_name = os.path.splitext(folder_name)[0]
                extract_dest = os.path.join(target_dir, f"extracted_{folder_name}")
                os.makedirs(extract_dest, exist_ok=True)
                log("EXTRACT", f"Đang tiến hành giải nén tệp lưu trữ: {f}...", "EXTRACT")
                cmd_extract = f'7z x -y "{f_path}" -o"{extract_dest}" > /dev/null 2>&1'
                status_ext = os.system(cmd_extract)
                if status_ext == 0:
                    log("SUCCESS", f"Giải nén thành công tệp: {f}", "SUCCESS")
                    try:
                        os.remove(f_path)
                    except:
                        pass
                else:
                    log("WARN", f"Không thể giải nén tự động tệp: {f}", "WARN")
