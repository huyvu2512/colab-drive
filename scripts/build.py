#!/usr/bin/env python3
# Script đóng gói và biên dịch sổ tay colab-drive.ipynb
import json
import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
notebook_path = os.path.join(base_dir, 'colab-drive.ipynb')

scratch_script = r'C:\Users\Huy Vu\.gemini\antigravity-ide\brain\165b5953-47bc-413a-9736-2c93565d8cce\scratch\make_notebook.py'
sys.path.insert(0, os.path.dirname(scratch_script))
import make_notebook

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

header_md = """# Colab Drive
Hệ thống tự động hóa tải và đồng bộ tệp tin đa nguồn vào Google Drive trên nền tảng Google Colab.

Các tính năng nổi bật được tích hợp:
- Đa công cụ chuyên dụng: yt-dlp, Deno JS runtime (chống 403 Forbidden), aria2c (Direct link & Torrent P2P), gdown (Google Drive tệp/thư mục), megatools (MEGA cloud), 7z/unrar.
- Quản lý hàng chờ thông minh (Task Queue): Tự động phân tách hàng loạt link, kiểm tra trước thông số, tự động dời link torrent bị nghẽn (timeout 3 phút) xuống cuối hàng chờ để thử lại sau, tự động bỏ qua (skip) link lỗi mà không làm gián đoạn tiến trình.
- Chọn chất lượng chuẩn xác 100%: Hỗ trợ chọn tự động cao nhất, 4K, 2K, 1080p, 720p hoặc chỉ trích xuất âm thanh (Audio MP3 320kbps). Bước 3 chuẩn đoán chính xác định dạng sẽ được tải ở Bước 4.
- Hỗ trợ Danh sách phát đa nền tảng (Playlist): Hỗ trợ giới hạn số lượng tập (VD: 1-10, 1-5, tat_ca) và tự động tạo thư mục riêng cho danh sách phát trên Google Drive.
- Tự động bỏ qua tệp đã có (Skip Existing): Kiểm tra thư mục Google Drive trước khi tải, nếu đã có tệp hoàn chỉnh thì tự động bỏ qua để tiết kiệm thời gian và băng thông.
- Chia nhỏ tệp lớn (Auto-Split Archive): Tự động chia nhỏ tệp có dung lượng lớn (1GB, 2GB, 4GB) thành các phần nén và lưu riêng biệt vào từng thư mục con để không bị lẫn lộn các tệp trong hàng chờ.

Quy trình vận hành 4 bước chuẩn hóa:
- Bước 1: Thiết lập môi trường, cài đặt công cụ chuyên dụng, Deno JS runtime và kích hoạt Anti-Disconnect.
- Bước 2: Xác thực và kết nối Google Drive, kiểm tra bộ đệm máy ảo Colab.
- Bước 3: Nhập liên kết, chọn chất lượng/playlist và kiểm tra trước thông số hàng chờ.
- Bước 4: Cấu hình lưu trữ, thực thi hàng chờ tải xuống và đồng bộ lên Google Drive."""

notebook['cells'].append({
    'cell_type': 'markdown',
    'metadata': {'id': 'header_intro'},
    'source': [line + '\n' for line in header_md.split('\n')]
})

notebook['cells'].append({
    'cell_type': 'code',
    'metadata': {'id': 'setup_environment', 'cellView': 'form'},
    'source': [line + '\n' for line in make_notebook.step1_code.split('\n')],
    'execution_count': None,
    'outputs': []
})

notebook['cells'].append({
    'cell_type': 'code',
    'metadata': {'id': 'mount_drive_storage', 'cellView': 'form'},
    'source': [line + '\n' for line in make_notebook.step2_code.split('\n')],
    'execution_count': None,
    'outputs': []
})

notebook['cells'].append({
    'cell_type': 'code',
    'metadata': {'id': 'inspect_source_urls', 'cellView': 'form'},
    'source': [line + '\n' for line in make_notebook.step3_code.split('\n')],
    'execution_count': None,
    'outputs': []
})

notebook['cells'].append({
    'cell_type': 'code',
    'metadata': {'id': 'execute_download_and_sync', 'cellView': 'form'},
    'source': [line + '\n' for line in make_notebook.step4_code.split('\n')],
    'execution_count': None,
    'outputs': []
})

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, ensure_ascii=False, indent=2)

print('Build completed successfully: colab-drive.ipynb generated from modules')
