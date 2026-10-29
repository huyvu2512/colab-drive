# Colab Drive

Hệ thống tự động hóa tải và đồng bộ tệp tin đa nguồn vào Google Drive trên nền tảng Google Colab.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/huyvu2512/colab-drive/blob/main/colab-drive.ipynb)

## Tổng quan

**Colab Drive** là giải pháp thực thi trên nền tảng Google Colab tích hợp các công cụ tải xuống hàng đầu thế giới nhằm tối ưu hóa tốc độ và chuyển dữ liệu đa nguồn trực tiếp vào Google Drive cá nhân mà không tiêu tốn băng thông máy trạm.

Hệ thống tự động nhận diện nguồn liên kết (URL Routing) để phân bổ engine tải tối ưu nhất:
- **Google Drive (`drive.google.com`):** Tích hợp `gdown` tải tệp đơn lẻ (vượt qua màn hình xác nhận tệp quá lớn không thể quét virus) hoặc tải toàn bộ thư mục (Folder) từ Drive khác sang Drive của bạn.
- **Nền tảng MEGA (`mega.nz`):** Tích hợp `megatools` tải trực tiếp dữ liệu từ đám mây MEGA.
- **Mạng P2P BitTorrent / Magnet:** Tích hợp `aria2c` đa luồng kết hợp DHT và danh sách OpenTrackers công cộng.
- **Hơn 1.800 nền tảng mạng xã hội và phát trực tuyến:** Tích hợp `yt-dlp` kết hợp `aria2c` (YouTube, TikTok, Facebook, Douyin, Bilibili, VK, OK.ru, Vimeo, Twitch,... và các luồng HLS `.m3u8`, DASH `.mpd`).
- **Liên kết tải trực tiếp (Direct Link):** Tự động phân luồng tải đa kết nối (`-x16 -s16`) cho mọi định dạng tệp (`.zip`, `.rar`, `.7z`, `.iso`, `.exe`, `.mp4`...).

## Quy trình 4 bước chuẩn hóa

1. **Bước 1: Thiết lập môi trường và cài đặt các công cụ tải chuyên dụng**
   - Tự động kích hoạt cơ chế chống ngắt kết nối (Anti-Disconnect).
   - Cài đặt hệ sinh thái: `yt-dlp`, `gdown`, `aria2c`, `megatools`, `ffmpeg`, `p7zip-full`, `unrar`.

2. **Bước 2: Xác thực và kết nối Google Drive**
   - Kết nối phân vùng lưu trữ Google Drive cá nhân (`/content/drive/MyDrive/`).
   - Kiểm tra dung lượng đã dùng và dung lượng khả dụng trên Drive.

3. **Bước 3: Nhập liên kết và kiểm tra thông tin nguồn (Pre-Inspection)**
   - Nhập liên kết, proxy, referer, cookies nếu có.
   - Hệ thống quét trước và báo cáo chi tiết thông số: Tiêu đề tệp/video, độ phân giải tối ưu (4K, 1080p60...), dung lượng ước tính và thời lượng phát trước khi tải.

4. **Bước 4: Cấu hình lưu trữ và tiến hành tải xuống**
   - Tự đặt tên tệp (`TEN_FILE_TU_DAT` - tự động nhận diện và gán đúng đuôi gốc).
   - Tùy chọn tự động giải nén file `.zip`, `.rar`, `.7z` (`TU_DONG_GIAI_NEN`).
   - Tùy chọn nhận tin nhắn báo cáo qua Telegram Bot (`TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`).
   - Bắt đầu tiến trình tải đa nguồn và đồng bộ trực tiếp vào Google Drive.

## Tham số cấu hình

| Tham số | Ý nghĩa |
|---|---|
| `LINK_CAN_TAI` | Dán 1 hoặc nhiều liên kết cần tải (phân cách bằng dấu xuống dòng hoặc dấu phẩy). |
| `DANH_SACH_PROXY` | Danh sách proxy hỗ trợ xoay tua Round-Robin (phân cách bằng phẩy, chấm phẩy, khoảng trắng hoặc xuống dòng). |
| `REFERER_VUOT_CHAN` | Nguồn trang web gốc để vượt lỗi chặn tải 403 Forbidden. |
| `NOI_DUNG_COOKIE` | Dán chuỗi cookies hoặc đường dẫn tệp `cookies.txt` để mở khóa tải 4K/VIP. |
| `THU_MUC_DRIVE` | Thư mục đích lưu trữ trên Google Drive (mặc định: `/content/drive/MyDrive/colab-drive`). |
| `TEN_FILE_TU_DAT` | Đặt tên tệp tùy ý (hệ thống tự động gán đuôi định dạng gốc). Để trống sẽ lấy tên nguồn. |
| `TU_DONG_GIAI_NEN` | Tự động giải nén các tệp nén đa định dạng trên đám mây trước khi chuyển vào Drive. |
| `TELEGRAM_BOT_TOKEN` | Mã token bot Telegram nhận thông báo báo cáo kết quả. |
| `TELEGRAM_CHAT_ID` | Mã ID chat Telegram nhận tin nhắn. |

## Cấu trúc thư mục

```text
colab-drive/
├── colab-drive.ipynb    # Sổ tay Jupyter chính thực thi trên Google Colab
├── README.md            # Tài liệu hướng dẫn sử dụng và thông số kỹ thuật
├── LICENSE              # Giấy phép phần mềm mã nguồn mở MIT
└── .gitignore           # Danh mục loại trừ tệp tin hệ thống
```

## Giấy phép

Dự án được phân phối theo giấy phép mã nguồn mở MIT. Chi tiết vui lòng xem tệp [LICENSE](LICENSE).
