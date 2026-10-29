# Colab Drive

Hệ thống tự động hóa tải và đồng bộ tệp tin đa nguồn vào Google Drive trên nền tảng Google Colab.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/huyvu2512/colab-drive/blob/main/colab-drive.ipynb)

## Tổng quan

**Colab Drive** là giải pháp thực thi trên nền tảng Google Colab tích hợp các công cụ tải xuống hàng đầu thế giới nhằm tối ưu hóa tốc độ và chuyển dữ liệu đa nguồn trực tiếp vào Google Drive cá nhân mà không tiêu tốn băng thông máy trạm.

Hệ thống tự động nhận diện nguồn liên kết (URL Routing) để phân bổ engine tải tối ưu nhất:
- **Google Drive (`drive.google.com`):** Tích hợp `gdown` tải tệp đơn lẻ (vượt qua màn hình xác nhận tệp quá lớn không thể quét virus) hoặc tải toàn bộ thư mục (Folder) từ Drive khác sang Drive của bạn.
- **Nền tảng MEGA (`mega.nz`):** Tích hợp `megatools` tải trực tiếp dữ liệu từ đám mây MEGA.
- **Mạng P2P BitTorrent / Magnet:** Tích hợp `aria2c` đa luồng kết hợp DHT và danh sách OpenTrackers công cộng, kèm cơ chế tự động dời tác vụ nghẽn seeder (timeout 3 phút) xuống cuối hàng chờ.
- **Hơn 1.800 nền tảng mạng xã hội và phát trực tuyến:** Tích hợp `yt-dlp` và Deno JavaScript Runtime (YouTube, TikTok, Facebook, Douyin, Bilibili, VK, OK.ru, Vimeo, Twitch,... và các luồng HLS `.m3u8`, DASH `.mpd`).
- **Liên kết tải trực tiếp (Direct Link):** Tự động phân luồng tải đa kết nối (`-x16 -s16`) cho mọi định dạng tệp (`.zip`, `.rar`, `.7z`, `.iso`, `.exe`, `.mp4`...).

## Tính năng nâng cao

1. **Quản lý hàng chờ thông minh (Task Queue):**
   - Hỗ trợ dán hàng loạt liên kết phân tách bằng dấu phẩy, chấm phẩy, khoảng trắng hoặc xuống dòng.
   - Cơ chế chịu lỗi: Tự động phát hiện tác vụ Torrent không có seeder sau 3 phút để đưa xuống cuối hàng chờ thử lại sau; tự động bỏ qua (Skip) các liên kết bị xóa hoặc lỗi kỹ thuật để tiếp tục chạy các liên kết còn lại trong hàng chờ.

2. **Khớp chuẩn chất lượng 100% giữa Bước 3 và Bước 4:**
   - Hỗ trợ lựa chọn: `Cao nhat (Best - Tu dong)`, `2160p (4K Ultra HD)`, `1440p (2K QHD)`, `1080p (Full HD)`, `720p (HD)`, `480p (SD)` và `Chi am thanh (Audio MP3/M4A)`.
   - Bước 3 chuẩn đoán chính xác định dạng thực tế của nguồn; Bước 4 tải đúng định dạng đó mà không có sự sai lệch.

3. **Hỗ trợ Danh sách phát đa nền tảng (Playlist):**
   - Hỗ trợ tải trọn bộ hoặc giới hạn số tập (ví dụ: `1-10`, `1-5`, `tat_ca`).
   - Tự động tạo thư mục con riêng biệt theo tên Playlist trên Google Drive để gom tệp gọn gàng.

4. **Chia nhỏ tệp lớn (Auto-Split Archive) vào thư mục riêng:**
   - Tự động chia nhỏ tệp vượt ngưỡng (`1GB`, `2GB`, `4GB`) thành các phần nén `.7z` và lưu trữ riêng biệt vào từng thư mục con mang tên tệp, chống lẫn lộn dữ liệu giữa các tác vụ trong hàng chờ.

## Quy trình 4 bước chuẩn hóa

1. **Bước 1: Thiết lập môi trường và cài đặt các công cụ tải chuyên dụng**
   - Kích hoạt cơ chế chống ngắt kết nối (Anti-Disconnect).
   - Cài đặt hệ sinh thái: `yt-dlp`, Deno JS runtime, `gdown`, `aria2c`, `megatools`, `ffmpeg`, `p7zip-full`, `unrar`.

2. **Bước 2: Xác thực và kết nối Google Drive**
   - Kết nối phân vùng lưu trữ Google Drive cá nhân (`/content/drive/MyDrive/`).
   - Kiểm tra bộ đệm máy ảo Colab.

3. **Bước 3: Nhập liên kết và kiểm tra thông tin nguồn (Pre-Inspection)**
   - Nhập liên kết, tùy chọn chất lượng tải, giới hạn playlist, proxy, referer, cookies.
   - Quét trước siêu dữ liệu, đối soát độ phân giải khả dụng và in bảng tổng kết hàng chờ sẵn sàng tải.

4. **Bước 4: Cấu hình lưu trữ và tiến hành tải xuống**
   - Thiết lập thư mục Drive, đặt tên tùy biến, tùy chọn chia nhỏ tệp lớn.
   - Thực thi hàng chờ tải xuống tuần tự và chuyển giao an toàn vào Google Drive.

## Tham số cấu hình

| Tham số | Vị trí | Ý nghĩa |
|---|---|---|
| `LINK_CAN_TAI` | Bước 3 | Dán 1 hoặc nhiều liên kết (phân cách bằng phẩy, chấm phẩy, khoảng trắng hoặc xuống dòng). |
| `CHAT_LUONG_TAI` | Bước 3 | Chọn chất lượng tải (Tự động cao nhất, 4K, 2K, 1080p, 720p, 480p, hoặc chỉ âm thanh MP3). |
| `GIOI_HAN_PLAYLIST` | Bước 3 | Giới hạn số lượng video tải từ Playlist (mặc định: `tat_ca`, hoặc `1-10`, `1-5`...). |
| `DANH_SACH_PROXY` | Bước 3 | Danh sách proxy hỗ trợ xoay tua Round-Robin. |
| `REFERER_VUOT_CHAN` | Bước 3 | Nguồn trang web gốc để vượt lỗi chặn tải 403 Forbidden. |
| `NOI_DUNG_COOKIE` | Bước 3 | Dán chuỗi cookies hoặc đường dẫn tệp `cookies.txt` để mở khóa tải 4K/VIP. |
| `THU_MUC_DRIVE` | Bước 4 | Thư mục đích lưu trữ trên Google Drive (mặc định: `/content/drive/MyDrive/colab-drive`). |
| `TEN_FILE_TU_DAT` | Bước 4 | Đặt tên tệp tùy ý (hệ thống tự động gán đuôi và đánh số thứ tự theo hàng chờ). |
| `CAT_TEP_DUNG_LUONG_LON` | Bước 4 | Tự động chia nhỏ tệp lớn (1GB, 2GB, 4GB) và lưu vào thư mục riêng. |
| `TELEGRAM_BOT_TOKEN` | Bước 4 | Mã token bot Telegram nhận thông báo báo cáo kết quả. |
| `TELEGRAM_CHAT_ID` | Bước 4 | Mã ID chat Telegram nhận tin nhắn. |

## Cấu trúc thư mục

```text
colab-drive/
├── scripts/
│   └── build.py         # Script tự động biên dịch và đóng gói src/ thành colab-drive.ipynb
├── src/                 # Toàn bộ mã nguồn module hóa (core, engines, queue, storage, notifications)
├── colab-drive.ipynb    # Sổ tay Jupyter chính thực thi trên Google Colab
├── README.md            # Tài liệu hướng dẫn sử dụng và thông số kỹ thuật
├── CHANGELOG.md         # Nhật ký các phiên bản nâng cấp
├── LICENSE              # Giấy phép phần mềm mã nguồn mở MIT
└── .gitignore           # Danh mục loại trừ tệp tin hệ thống
```

## Giấy phép

Dự án được phân phối theo giấy phép mã nguồn mở MIT. Chi tiết vui lòng xem tệp [LICENSE](LICENSE).
