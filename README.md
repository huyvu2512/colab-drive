<div align="center">

# Colab Drive

**Hệ thống tự động hóa tải và đồng bộ tệp tin đa nguồn vào Google Drive trên nền tảng Google Colab**

[Tiếng Việt](README.md) · [English](README_EN.md)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/huyvu2512/colab-drive/blob/main/colab-drive.ipynb)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB)](https://www.python.org/)
[![Deno](https://img.shields.io/badge/Deno-JS%20Runtime-black)](https://deno.land/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![yt-dlp](https://img.shields.io/badge/Engine-yt--dlp-red)](https://github.com/yt-dlp/yt-dlp)
[![aria2](https://img.shields.io/badge/Engine-aria2-blue)](https://github.com/aria2/aria2)

[![Stars](https://img.shields.io/github/stars/huyvu2512/colab-drive?style=flat-square&label=Stars&color=FFCC00)](https://github.com/huyvu2512/colab-drive/stargazers)
[![Forks](https://img.shields.io/github/forks/huyvu2512/colab-drive?style=flat-square&label=Forks&color=6e7681)](https://github.com/huyvu2512/colab-drive/forks)
[![Issues](https://img.shields.io/github/issues/huyvu2512/colab-drive?style=flat-square&label=Issues&color=f85149)](https://github.com/huyvu2512/colab-drive/issues)
[![Last Commit](https://img.shields.io/github/last-commit/huyvu2512/colab-drive?style=flat-square&label=Last%20Commit&color=3fb950)](https://github.com/huyvu2512/colab-drive/commits/main)

[Mở Sổ Tay Colab](https://colab.research.google.com/github/huyvu2512/colab-drive/blob/main/colab-drive.ipynb) · [Lịch sử thay đổi](CHANGELOG.md) · [Báo Lỗi](https://github.com/huyvu2512/colab-drive/issues) · [Yêu Cầu Tính Năng](https://github.com/huyvu2512/colab-drive/issues)

</div>

---

## Giới thiệu
**Colab Drive** là giải pháp tự động hóa thực thi trên nền tảng Google Colab, được thiết kế nhằm tối ưu hóa tốc độ tải và chuyển giao dữ liệu từ đa dạng các nguồn lưu trữ trên Internet trực tiếp vào Google Drive cá nhân mà không tiêu tốn băng thông hay dung lượng máy trạm. Sản phẩm được phát triển bởi Huy Vũ (@huyvu2512) với mục tiêu nghiên cứu chuyên sâu về tối ưu luồng truyền tải dữ liệu, quản lý hàng chờ chịu lỗi và tích hợp hệ sinh thái công cụ mã nguồn mở cao cấp.

Phiên bản **v2.2.0** hỗ trợ chia đều tệp thành 2, 4, 6, 8 hoặc 10 phần tiện dụng và lưu trữ vào thư mục riêng biệt. Xem [CHANGELOG.md](CHANGELOG.md) để biết chi tiết.

---

## Tính năng chính
- **Đa công cụ chuyên dụng** - Phân phối chính xác engine tối ưu: `gdown` cho Google Drive, `megatools` cho MEGA, `aria2c` cho Direct Link & BitTorrent, `yt-dlp` cho luồng stream video/âm thanh.
- **Giải mã chữ ký Deno JS Runtime** - Tự động tích hợp Deno và EJS challenge solver, giải quyết triệt để lỗi YouTube cipher / n-sig 403 Forbidden trên địa chỉ IP máy chủ đám mây.
- **Quản lý hàng chờ tác vụ (Task Queue)** - Tự động bóc tách danh sách hàng loạt link phân tách bằng dấu phẩy, chấm phẩy, khoảng trắng hoặc xuống dòng; thực thi tuần tự và dọn dẹp bộ đệm sau từng tác vụ.
- **Cơ chế chịu lỗi và dời hàng chờ Torrent** - Tự động theo dõi tiến trình tải BitTorrent/Magnet, nếu sau 3 phút không bắt được seeder (tốc độ 0 KB/s), hệ thống tự dời tác vụ xuống cuối hàng chờ để ưu tiên các link khác trước; tự động bỏ qua (Skip) các link chết mà không làm ngắt quãng phiên làm việc.
- **Khớp chuẩn chất lượng 100% giữa Bước 3 và Bước 4** - Hỗ trợ chọn độ phân giải: Tự động cao nhất, 4K, 2K, 1080p, 720p, 480p hoặc Chỉ âm thanh (Audio MP3 320kbps). Bước 3 đối soát thực tế luồng video nguồn và khóa cấu hình truyền sang Bước 4 tải chính xác, không sai lệch.
- **Hỗ trợ Danh sách phát đa nền tảng (Playlist)** - Hỗ trợ giới hạn tập tải (`1-10`, `1-5`, `tat_ca`) cho hơn 1.800 trang web, tự động tạo thư mục riêng theo tên Playlist trên Google Drive.
- **Chia nhỏ tệp linh hoạt theo số phần** - Cho phép chọn chia đều tệp thành `2`, `4`, `6`, `8` hoặc `10` phần nén `.7z` và lưu trữ riêng biệt vào từng thư mục con mang tên tệp, chống lẫn lộn dữ liệu giữa các tác vụ.
- **Thanh tiến trình thời gian thực (Live ETA)** - Báo cáo tiến độ phần trăm, dung lượng đã tải, tốc độ truyền tải thực tế (MB/s) và ước tính thời gian còn lại (ETA) cập nhật mượt mà mỗi giây.
- **Báo cáo thông báo Telegram Bot** - Tự động gửi tin nhắn tổng kết chi tiết về danh sách tệp đã lưu, số lượng thành công/thất bại và đường dẫn thư mục lưu trữ.

---

## Công nghệ
| Thành phần | Công nghệ |
| :--- | :--- |
| Nền tảng thực thi | Google Colab (Linux Ubuntu VM Environment) |
| Ngôn ngữ & Lõi | Python 3.10+, Bash Shell Scripting |
| Động cơ tải Video/Audio | yt-dlp, FFmpeg |
| Động cơ giải mã chữ ký | Deno JavaScript Runtime, EJS Challenge Solver |
| Động cơ P2P & Direct Link | aria2c (Kích hoạt DHT, OpenTrackers, 16 luồng song song) |
| Động cơ Google Drive | gdown (Hỗ trợ vượt xác nhận quét virus và tải trọn thư mục) |
| Động cơ Đám mây MEGA | megatools |
| Công cụ nén & chia nhỏ tệp | p7zip-full (7z), unrar |
| Đóng gói & Xây dựng | scripts/build.py (Tự động biên dịch `src/` thành `colab-drive.ipynb`) |

---

## Cấu trúc mã nguồn
Toàn bộ mã nguồn dự án được tổ chức theo từng phân hệ chức năng độc lập:

```text
colab-drive/
├── scripts/
│   └── build.py              # Script tự động biên dịch và đóng gói src/ thành colab-drive.ipynb
├── src/
│   ├── core/
│   │   ├── logger.py         # Hệ thống log màu, múi giờ UTC+7 và chống đè dòng tiến trình
│   │   ├── utils.py          # Format dung lượng, ETA, chuẩn độ phân giải, kiểm tra tên tệp
│   │   └── anti_disconnect.py# JavaScript Heartbeat giữ kết nối máy ảo Colab
│   ├── engines/
│   │   ├── ytdl.py           # yt-dlp engine, bộ lọc cảnh báo rác, ghép kênh và progress hook
│   │   ├── aria2.py          # aria2c engine (Direct Link đa luồng & BitTorrent/Magnet timeout 3 phút)
│   │   ├── gdown.py          # gdown engine tải tệp và thư mục Google Drive
│   │   └── mega.py           # megatools engine tải từ đám mây MEGA
│   ├── queue/
│   │   └── parser.py         # Bóc tách URL hàng loạt (phẩy, chấm phẩy, khoảng trắng, xuống dòng)
│   ├── storage/
│   │   ├── drive_sync.py     # Chuyển giao dữ liệu vào Drive và đặt tên thông minh theo hàng chờ
│   │   └── splitter.py       # Tự động chia nhỏ tệp (2, 4, 6, 8, 10 phần) vào thư mục riêng
│   └── notifications/
│       └── telegram.py       # Gửi báo cáo tiến trình và kết quả qua Telegram Bot
├── CHANGELOG.md              # Lịch sử các phiên bản nâng cấp
├── README.md                 # Tài liệu hướng dẫn sử dụng (Tiếng Việt)
├── README_EN.md              # Tài liệu hướng dẫn sử dụng (English)
├── colab-drive.ipynb         # Sổ tay Colab hoàn chỉnh được build sẵn để chạy ngay
└── LICENSE                   # Giấy phép mã nguồn mở MIT
```

- Biên dịch lại sổ tay từ mã nguồn: `python scripts/build.py`

---

## Quy trình 4 bước vận hành

### Bước 1: Thiết lập môi trường và cài đặt các công cụ tải chuyên dụng
- Kích hoạt cơ chế tự động duy trì kết nối phiên làm việc (Anti-Disconnect).
- Cài đặt hệ sinh thái công cụ: `yt-dlp`, Deno JS runtime, `gdown`, `megatools`, `aria2c`, `ffmpeg`, `p7zip-full`, `unrar`.

### Bước 2: Xác thực và kết nối Google Drive
- Gắn kết phân vùng lưu trữ Google Drive cá nhân (`/content/drive/MyDrive/`).
- Kiểm tra dung lượng đã dùng và dung lượng khả dụng trên bộ đệm máy ảo Colab.

### Bước 3: Nhập liên kết và kiểm tra thông tin nguồn (Pre-Inspection)
- Nhập một hoặc nhiều liên kết tại ô `LINK_CAN_TAI`.
- Chọn chất lượng tải mong muốn (`CHAT_LUONG_TAI`), giới hạn playlist nếu có (`GIOI_HAN_PLAYLIST`), proxy, referer, cookies.
- Hệ thống lập hàng chờ, quét siêu dữ liệu thực tế và in bảng tổng hợp thông số tệp sẵn sàng tải.

### Bước 4: Cấu hình lưu trữ và tiến hành tải xuống
- Thiết lập thư mục lưu trên Drive (`THU_MUC_DRIVE`), đặt tên tùy biến (`TEN_FILE_TU_DAT`), chọn chia tệp thành 2, 4, 6, 8 hoặc 10 phần (`CAT_TEP_DUNG_LUONG_LON`), cấu hình Telegram bot.
- Bắt đầu tiến trình tải xuống tuần tự, tự động chuyển giao vào Drive và dọn dẹp bộ đệm sau từng tác vụ.

---

## Tham số cấu hình

| Tham số | Vị trí | Kiểu | Ý nghĩa |
| :--- | :--- | :--- | :--- |
| `LINK_CAN_TAI` | Bước 3 | Chuỗi | Dán 1 hoặc nhiều liên kết (phân tách bằng phẩy, chấm phẩy, khoảng trắng hoặc xuống dòng). |
| `CHAT_LUONG_TAI` | Bước 3 | Lựa chọn | Chọn chất lượng tải (Tự động cao nhất, 4K, 2K, 1080p, 720p, 480p, hoặc Chỉ âm thanh MP3). |
| `GIOI_HAN_PLAYLIST` | Bước 3 | Chuỗi | Giới hạn số lượng video tải từ Playlist (mặc định: `tat_ca`, hoặc `1-10`, `1-5`...). |
| `DANH_SACH_PROXY` | Bước 3 | Chuỗi | Danh sách proxy hỗ trợ xoay tua Round-Robin. |
| `REFERER_VUOT_CHAN` | Bước 3 | Chuỗi | Nguồn trang web gốc để vượt lỗi chặn tải 403 Forbidden. |
| `NOI_DUNG_COOKIE` | Bước 3 | Chuỗi | Dán chuỗi cookies hoặc đường dẫn tệp `cookies.txt` để mở khóa tải 4K/VIP. |
| `THU_MUC_DRIVE` | Bước 4 | Chuỗi | Thư mục đích lưu trữ trên Google Drive (mặc định: `/content/drive/MyDrive/colab-drive`). |
| `TEN_FILE_TU_DAT` | Bước 4 | Chuỗi | Đặt tên tệp tùy ý (hệ thống tự động gán đuôi và đánh số thứ tự theo hàng chờ). |
| `CAT_TEP_DUNG_LUONG_LON` | Bước 4 | Lựa chọn | Tùy chọn chia đều tệp thành 2, 4, 6, 8 hoặc 10 phần (Khong cat, Chia thanh 2 phan...). |
| `TELEGRAM_BOT_TOKEN` | Bước 4 | Chuỗi | Mã token bot Telegram nhận thông báo báo cáo kết quả. |
| `TELEGRAM_CHAT_ID` | Bước 4 | Chuỗi | Mã ID chat Telegram nhận tin nhắn. |

---

## Giấy phép
Dự án được phân phối theo giấy phép mã nguồn mở MIT. Chi tiết vui lòng xem tệp [LICENSE](LICENSE).
