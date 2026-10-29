# Nhật ký thay đổi (Changelog)

Tất cả các thay đổi và cập nhật quan trọng của dự án **Colab Drive** được ghi nhận tại đây.

---

## [2.1.0] - 2026-10-30
### Đã thay đổi (Changed)
- **Tinh giản giao diện Bước 4:** Loại bỏ 2 tùy chọn `BO_QUA_TEP_DA_CO` và `TU_DONG_GIAI_NEN` để quy trình gọn gàng, giảm thiểu tham số không cần thiết.
- Tự động hóa tải toàn diện theo hàng chờ, chia nhỏ tệp lớn và đẩy thẳng vào Google Drive.

---

## [2.0.0] - 2026-10-30
### Đã thêm (Added)
- **Cấu trúc module hóa chuyên nghiệp (`src/`):** Tách mã nguồn thành các module độc lập (`src/core`, `src/engines`, `src/queue`, `src/storage`, `src/notifications`).
- **Script Build tự động (`scripts/build.py`):** Tự động đóng gói toàn bộ mã nguồn module hóa vào sổ tay `colab-drive.ipynb`.
- **Bộ chọn chất lượng tải (`CHAT_LUONG_TAI`):** Hỗ trợ chọn tự động cao nhất, 4K, 2K, 1080p, 720p, 480p và chế độ Chỉ âm thanh (Audio MP3 320kbps).
- **Khớp chuẩn 100%:** Bước 3 chuẩn đoán định dạng nào thì Bước 4 tải chính xác định dạng đó.
- **Giới hạn Danh sách phát (`GIOI_HAN_PLAYLIST`):** Hỗ trợ chọn lọc số tập tải (1-10, 1-5, tat_ca) cho hơn 1.800 trang web, tự động tạo thư mục riêng cho Playlist trên Google Drive.
- **Cơ chế dời hàng chờ Torrent:** Tự động phát hiện sau 3 phút không có seeder/peer và chuyển tác vụ xuống cuối hàng chờ; tự động bỏ qua nếu link bị lỗi.
- **Chia nhỏ tệp lớn vào thư mục riêng (`CAT_TEP_DUNG_LUONG_LON`):** Chia nhỏ tệp (1GB, 2GB, 4GB) và lưu riêng biệt vào từng thư mục con mang tên tệp.

---

## [1.1.0] - 2026-10-30
### Đã thêm (Added)
- Nhận diện độ phân giải thân thiện (1080p Full HD, 4K Ultra HD, 2K QHD...).
- Quản lý hàng chờ (Task Queue) hỗ trợ dán hàng loạt link cách nhau bằng phẩy, chấm phẩy, khoảng trắng hoặc xuống dòng.
- Bộ lọc ngăn chặn đè dòng tiến trình (Clean Live Progress Bar with ETA).
- Tích hợp Deno JavaScript Runtime giải mã chữ ký YouTube n-sig chống lỗi 403 Forbidden.

---

## [1.0.0] - 2026-10-29
### Đã thêm (Added)
- Phát hành phiên bản đầu tiên của Colab Drive.
- Hỗ trợ đa nguồn tải: Google Drive (gdown), MEGA (megatools), BitTorrent (aria2c), Video streams (yt-dlp).
- Đồng bộ trực tiếp dữ liệu vào Google Drive cá nhân.
- Thông báo tiến trình và kết quả qua Telegram Bot.
