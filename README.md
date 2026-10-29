# Colab Drive

Hệ thống tự động hóa tải và đồng bộ tệp tin đa nguồn vào Google Drive trên nền tảng Google Colab.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/huyvu2512/colab-drive/blob/main/colab-drive.ipynb)

## Tổng quan

**Colab Drive** là giải pháp thực thi trên nền tảng Google Colab nhằm tối ưu hóa tốc độ tải xuống và đồng bộ trực tiếp dữ liệu đa phương tiện từ Internet vào Google Drive của người dùng mà không làm tiêu tốn băng thông máy trạm cá nhân.

Dự án được xây dựng với tiêu chí tối giản trong cấu trúc, tự động hóa cao độ trong quá trình truyền tải, hỗ trợ vượt các cơ chế hạn chế mạng và tích hợp hệ thống nhật ký (log) chuyên nghiệp theo phong cách DevOps/CLI.

## Tính năng chính

- **Hỗ trợ đa nguồn toàn diện:** Tương thích với hơn 1.800 nền tảng trực tuyến (YouTube, Facebook, TikTok, Douyin, Bilibili, OK.ru, VK, Vimeo, Twitch,...), các luồng phát trực tiếp HLS (`.m3u8`), DASH (`.mpd`), liên kết tải trực tiếp (`.mp4`, `.mkv`, `.iso`, `.zip`,...) và giao thức chia sẻ tệp BitTorrent/Magnet link.
- **Tự động tăng tốc truyền tải:** Mặc định kích hoạt bộ tăng tốc `aria2c` đa luồng (16 kết nối song song) kết hợp `yt-dlp`. Tự động chuyển đổi cơ chế sang native hoặc tải trực tiếp khi phát hiện máy chủ đích có giới hạn kết nối mà không cần người dùng can thiệp thủ công.
- **Tự động gán đuôi tệp thông minh:** Khi đặt tên tệp tùy biến (ví dụ `name123`), hệ thống tự động nhận diện và gán đúng phần mở rộng gốc của tệp (`.mp4`, `.mpd`, `.mkv`, `.ts`,...) mà người dùng không cần gõ đuôi tệp.
- **Định tuyến máy chủ ủy danh (Proxy):** Hỗ trợ danh sách proxy HTTP/HTTPS/SOCKS5 (có hoặc không có xác thực) giúp vượt qua các rào cản chặn địa lý (Geo-Block) và giới hạn IP.
- **Tùy biến tiêu đề mạng:** Thiết lập `User-Agent` hiện đại và hỗ trợ nhập `Referer`/`Origin` tùy chỉnh để xử lý các liên kết bảo vệ chống tải trái phép (HTTP 403 Forbidden).
- **Cơ chế dự phòng đa tầng (Auto Fallback):** Tự động điều chỉnh linh hoạt giữa các chế độ ghép kênh, format tương thích và tải trực tiếp khi xảy ra lỗi mạng hoặc luồng stream phức tạp.
- **Đồng bộ hóa Google Drive:** Tự động di chuyển dữ liệu vào thư mục chỉ định trên Google Drive, có thuật toán chống ghi đè tệp trùng tên.
- **Hệ thống nhật ký chuẩn mực:** Toàn bộ thông tin thực thi được hiển thị với dấu thời gian Việt Nam (UTC+7, `HH:MM:SS`), mã định danh phân hệ ôm sát gọn gàng và màu sắc ANSI chuyên nghiệp, không sử dụng biểu tượng cảm xúc.

## Hướng dẫn vận hành

### Bước 1: Mở sổ tay trên Google Colab
Nhấn vào liên kết [Mở trên Google Colab](https://colab.research.google.com/github/huyvu2512/colab-drive/blob/main/colab-drive.ipynb) hoặc tải tệp `colab-drive.ipynb` lên Google Colab của bạn.

### Bước 2: Thiết lập môi trường và cài đặt phụ thuộc
Chạy ô **Bước 1** để hệ thống tự động kiểm tra và cài đặt phiên bản mới nhất của `yt-dlp`, `aria2c` và `ffmpeg`.

### Bước 3: Xác thực và kết nối Google Drive
Chạy ô **Bước 2** và cấp quyền kết nối với phân vùng lưu trữ Google Drive cá nhân (`/content/drive/MyDrive/`).

### Bước 4: Tải xuống và đồng bộ dữ liệu
Thiết lập các tham số đầu vào tại biểu mẫu ở **Bước 3**:
- `LINK_CAN_TAI`: Dán 1 hoặc nhiều liên kết cần tải (ngăn cách bằng dấu xuống dòng hoặc dấu phẩy).
- `THU_MUC_DRIVE`: Đường dẫn thư mục lưu trữ đích trên Google Drive (mặc định: `/content/drive/MyDrive/colab-drive`).
- `TEN_FILE_TU_DAT`: Đặt tên tệp tùy biến (ví dụ `name123`, hệ thống sẽ tự động gán đuôi định dạng gốc như `.mp4`, `.mpd`...). Để trống nếu muốn giữ nguyên tên gốc của video/tệp.
- `DANH_SACH_PROXY`: Danh sách địa chỉ proxy (định dạng `IP:PORT:USER:PASS` hoặc `protocol://...`) nếu cần vượt tường lửa/chặn vùng.
- `REFERER_VUOT_CHAN`: Tiêu đề `Referer` nguồn trang web gốc để vượt lỗi chặn tải 403 Forbidden.

Nhấn nút thực thi để tiến trình tự động tải và chuyển giao tệp vào Google Drive.

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
