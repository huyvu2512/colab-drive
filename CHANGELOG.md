# Lịch sử thay đổi

## v2.1.0 — 30/10/2026 01:35

- **[d4cb6ec](https://github.com/huyvu2512/colab-drive/commit/d4cb6ec)** Tinh giản giao diện Bước 4: gỡ bỏ tùy chọn kiểm tra tệp tồn tại và tự động giải nén để tối ưu luồng chạy.
- **[90adadd](https://github.com/huyvu2512/colab-drive/commit/90adadd)** Tái cấu trúc toàn bộ mã nguồn theo mô hình module hóa chuyên nghiệp (`src/`, `scripts/build.py`).

## v2.0.0 — 30/10/2026 01:28

- **[3f0673f](https://github.com/huyvu2512/colab-drive/commit/3f0673f)** Bổ sung bộ chọn chất lượng tải (`CHAT_LUONG_TAI`) đảm bảo khớp chuẩn 100% giữa Bước 3 và Bước 4.
- **[3f0673f](https://github.com/huyvu2512/colab-drive/commit/3f0673f)** Hỗ trợ giới hạn tải Danh sách phát (`GIOI_HAN_PLAYLIST`) cho hơn 1.800 nền tảng trực tuyến.
- **[3f0673f](https://github.com/huyvu2512/colab-drive/commit/3f0673f)** Bổ sung cơ chế timeout 3 phút cho BitTorrent/Magnet, tự động dời tác vụ nghẽn xuống cuối hàng chờ để thử lại sau.
- **[3f0673f](https://github.com/huyvu2512/colab-drive/commit/3f0673f)** Bổ sung tính năng tự động chia nhỏ tệp lớn (`CAT_TEP_DUNG_LUONG_LON`) vào thư mục riêng biệt trên Google Drive.

## v1.1.0 — 30/10/2026 01:14

- **[c2b9b16](https://github.com/huyvu2512/colab-drive/commit/c2b9b16)** Nâng cấp bộ phân tích liên kết `extract_urls` hỗ trợ nhiều ký tự phân tách và quản lý hàng chờ tác vụ (`[QUEUE]`).
- **[d7ab51f](https://github.com/huyvu2512/colab-drive/commit/d7ab51f)** Bổ sung hiển thị chuẩn độ phân giải thân thiện (1080p Full HD, 4K Ultra HD, 2K QHD...) ở Bước 3.
- **[d7ab51f](https://github.com/huyvu2512/colab-drive/commit/d7ab51f)** Khắc phục lỗi đè dòng thanh tiến trình live ETA và loại bỏ cảnh báo trùng lặp từ bộ ghép kênh.
- **[98cb48c](https://github.com/huyvu2512/colab-drive/commit/98cb48c)** Cài đặt Deno JavaScript Runtime giải mã chữ ký YouTube n-sig chống lỗi 403 Forbidden.
- **[9e7d13c](https://github.com/huyvu2512/colab-drive/commit/9e7d13c)** Tích hợp thanh tiến trình thời gian thực (ETA), tốc độ truyền tải MB/s và logger doanh nghiệp chuẩn múi giờ UTC+7.

## v1.0.0 — 29/10/2026 23:50

- **[3f5feba](https://github.com/huyvu2512/colab-drive/commit/3f5feba)** Chuẩn hóa cảnh báo dung lượng bộ đệm máy ảo Colab.
- **[c897f9b](https://github.com/huyvu2512/colab-drive/commit/c897f9b)** Tích hợp đa engine chuyên dụng: Google Drive (gdown), MEGA (megatools), BitTorrent (aria2c), Video streams (yt-dlp).
- **[b7cf5d3](https://github.com/huyvu2512/colab-drive/commit/b7cf5d3)** Chuẩn hóa quy trình 4 bước vận hành và tách biệt khâu tiền kiểm tra siêu dữ liệu ở Bước 3.
- **[93557e9](https://github.com/huyvu2512/colab-drive/commit/93557e9)** Khởi tạo dự án Colab Drive tự động hóa tải và đồng bộ dữ liệu vào Google Drive.
