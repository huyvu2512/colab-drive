# Lịch sử thay đổi

## v2.2.4 — 30/10/2026 02:15

- **[3d41c79](https://github.com/huyvu2512/colab-drive/commit/3d41c79f09fd814ecb6aa9dfc4f1c78a3db18f0f)** Bổ sung ảnh xem trước giao diện ssets/preview.png và loại bỏ tệp .gitignore.

## v2.2.3 — 30/10/2026 02:05

- **[c858b2b](https://github.com/huyvu2512/colab-drive/commit/c858b2b7f9759a0973b9d1af8330eb6128351d66)** Tinh giản tiêu đề mô tả chính của dự án thành câu hành động trực diện.

## v2.2.2 — 30/10/2026 01:55

- **[7b576d8](https://github.com/huyvu2512/colab-drive/commit/7b576d85c64c406be08ec8c5e6fa7edce64a6df3)** Thiết lập tài liệu phát triển AGENTS.md bằng tiếng Anh và chuẩn hóa Semantic Versioning.

## v2.2.1 — 30/10/2026 01:45

- **[2969efd](https://github.com/huyvu2512/colab-drive/commit/2969efd94c8d9acf779ab57608818d5de91dafcf)** Tinh chỉnh tên chất lượng 'Cao nhat (Tu dong)' và để trống giới hạn playlist mặc định tải toàn bộ.

## v2.2.0 — 30/10/2026 01:43

- **[9b98b45](https://github.com/huyvu2512/colab-drive/commit/9b98b45bb3523d8951a33f295415a275d0622be8)** Hỗ trợ chia đều tệp thành 2, 4, 6, 8, 10 phần nén `.7z` lưu vào thư mục riêng biệt.
- **[3bfdaf4](https://github.com/huyvu2512/colab-drive/commit/3bfdaf401cdc0c0255cc6e3c0d91b3cba4d1c88c)** Tinh giản phần giới thiệu đầu sổ tay `colab-drive.ipynb` thành phiên bản ngắn gọn, súc tích.
- **[286dbb5](https://github.com/huyvu2512/colab-drive/commit/286dbb581063e194477d7a28e71211fba1518796)** Đồng bộ toàn diện tài liệu README, README_EN và CHANGELOG theo chuẩn mẫu youtube-customizer.

## v2.1.0 — 30/10/2026 01:35

- **[d4cb6ec](https://github.com/huyvu2512/colab-drive/commit/d4cb6ec13160ded48fdcbef7d0faccee5f736e43)** Tinh giản giao diện Bước 4: gỡ bỏ tùy chọn kiểm tra tệp tồn tại và tự động giải nén để tối ưu luồng chạy.
- **[90adadd](https://github.com/huyvu2512/colab-drive/commit/90adadd33d987a6a3e176bad67f3018ee1ae5b3e)** Tái cấu trúc toàn bộ mã nguồn theo mô hình module hóa chuyên nghiệp (`src/`, `scripts/build.py`).

## v2.0.0 — 30/10/2026 01:28

- **[3f0673f](https://github.com/huyvu2512/colab-drive/commit/3f0673fc708261c39f974b0d463fdd20883ad854)** Bổ sung bộ chọn chất lượng tải (`CHAT_LUONG_TAI`) đảm bảo khớp chuẩn 100% giữa Bước 3 và Bước 4.
- **[3f0673f](https://github.com/huyvu2512/colab-drive/commit/3f0673fc708261c39f974b0d463fdd20883ad854)** Hỗ trợ giới hạn tải Danh sách phát (`GIOI_HAN_PLAYLIST`) cho hơn 1.800 nền tảng trực tuyến.
- **[3f0673f](https://github.com/huyvu2512/colab-drive/commit/3f0673fc708261c39f974b0d463fdd20883ad854)** Bổ sung cơ chế timeout 3 phút cho BitTorrent/Magnet, tự động dời tác vụ nghẽn xuống cuối hàng chờ để thử lại sau.
- **[3f0673f](https://github.com/huyvu2512/colab-drive/commit/3f0673fc708261c39f974b0d463fdd20883ad854)** Bổ sung tính năng tự động chia nhỏ tệp lớn (`CAT_TEP_DUNG_LUONG_LON`) vào thư mục riêng biệt trên Google Drive.

## v1.1.0 — 30/10/2026 01:14

- **[c2b9b16](https://github.com/huyvu2512/colab-drive/commit/c2b9b16ad78e3778697867d574174c7d52b135b7)** Nâng cấp bộ phân tích liên kết `extract_urls` hỗ trợ nhiều ký tự phân tách và quản lý hàng chờ tác vụ (`[QUEUE]`).
- **[d7ab51f](https://github.com/huyvu2512/colab-drive/commit/d7ab51f8e95cc489d77470a0b8c9ab51350ed74a)** Bổ sung hiển thị chuẩn độ phân giải thân thiện (1080p Full HD, 4K Ultra HD, 2K QHD...) ở Bước 3.
- **[d7ab51f](https://github.com/huyvu2512/colab-drive/commit/d7ab51f8e95cc489d77470a0b8c9ab51350ed74a)** Khắc phục lỗi đè dòng thanh tiến trình live ETA và loại bỏ cảnh báo trùng lặp từ bộ ghép kênh.
- **[98cb48c](https://github.com/huyvu2512/colab-drive/commit/98cb48c41cff038bb825ead4d88f989ef032437b)** Cài đặt Deno JavaScript Runtime giải mã chữ ký YouTube n-sig chống lỗi 403 Forbidden.
- **[9e7d13c](https://github.com/huyvu2512/colab-drive/commit/9e7d13cdfa37eae0e2fcf7980b5f1ae89367bb6f)** Tích hợp thanh tiến trình thời gian thực (ETA), tốc độ truyền tải MB/s và logger doanh nghiệp chuẩn múi giờ UTC+7.

## v1.0.0 — 30/10/2026 00:50

- **[3f5feba](https://github.com/huyvu2512/colab-drive/commit/3f5febad0be5ba274e249cc31b7b1378624f197c)** Chuẩn hóa cảnh báo dung lượng bộ đệm máy ảo Colab.
- **[c897f9b](https://github.com/huyvu2512/colab-drive/commit/c897f9b0934d1b05e834812e01f1dac29e14104f)** Tích hợp đa engine chuyên dụng: Google Drive (gdown), MEGA (megatools), BitTorrent (aria2c), Video streams (yt-dlp).
- **[b7cf5d3](https://github.com/huyvu2512/colab-drive/commit/b7cf5d3c2c53f9ff9d3b57f73cc6457b209e3884)** Chuẩn hóa quy trình 4 bước vận hành và tách biệt khâu tiền kiểm tra siêu dữ liệu ở Bước 3.
- **[3540629](https://github.com/huyvu2512/colab-drive/commit/354062923ed4777469b260279f8db26e0adea6d2)** Nâng cấp toàn diện: cơ chế chống ngắt kết nối, kiểm tra bộ nhớ đệm Drive, xác thực cookie và thông báo Telegram.
- **[729e693](https://github.com/huyvu2512/colab-drive/commit/729e6934e1edb8c0d5be5d82e09cc427070b7ba4)** Hỗ trợ phân tách proxy linh hoạt (phẩy, khoảng trắng, chấm phẩy, gạch đứng) và xoay tua Round-Robin.
- **[81a07f9](https://github.com/huyvu2512/colab-drive/commit/81a07f9a18b23f8bc054300cdd668e4b6a3e657b)** Tự động hóa tải đa luồng tốc độ cao với cơ chế tự động chuyển đổi luồng dự phòng.
- **[6aa2fff](https://github.com/huyvu2512/colab-drive/commit/6aa2fffa2780afe5574a30320cdfc54b00952fe7)** Chuẩn hóa định dạng thời gian log theo múi giờ Việt Nam (UTC+7) và làm sạch thẻ log hệ thống.
- **[cecad45](https://github.com/huyvu2512/colab-drive/commit/cecad457d48df18a705570cf504068c8b0fddee7)** Cập nhật tiêu đề sổ tay thành Colab Drive.
- **[8bf423b](https://github.com/huyvu2512/colab-drive/commit/8bf423b34137d981fa379319ebd53f144912c1a0)** Đổi tên dự án thành colab-drive, tinh giản quy trình tải và chuẩn hóa nhật ký vận hành.

## v0.1.0 — 12/07/2026 11:50

- **[801a11b](https://github.com/huyvu2512/colab-drive/commit/801a11bdb8bc0c8d8ed719cfc8d848a5d2d02cd7)** Bổ sung hỗ trợ danh sách proxy vượt chặn khu vực địa lý cho các nguồn video.
- **[128eec7](https://github.com/huyvu2512/colab-drive/commit/128eec7ccd639b99d898d1d4cf6fd86c6bd8a557)** Thêm tùy chọn chế độ tải và xử lý lỗi 403 Forbidden bằng Referer Header.
- **[4141e14](https://github.com/huyvu2512/colab-drive/commit/4141e145d16b31e205f25cebcb7f558d17dbb5c9)** Hỗ trợ tải tuần tự nhiều liên kết video chính.
- **[4cc07b4](https://github.com/huyvu2512/colab-drive/commit/4cc07b48e6dd7f93386b3556908e222dacb75e24)** Sửa lỗi định dạng chuỗi gây hiển thị dấu nháy kép trên Colab Form.
- **[ad82a62](https://github.com/huyvu2512/colab-drive/commit/ad82a622b2773b5e28b514fe1992c083a6fe033e)** Hoàn thiện giao diện Form và chuẩn hóa các biến tham số.
- **[7e5e27d](https://github.com/huyvu2512/colab-drive/commit/7e5e27dd525d5086309b50996f6a8a4b5f9d95a3)** Hỗ trợ ô nhập liệu đa dòng cho danh sách liên kết.
- **[0b5bad2](https://github.com/huyvu2512/colab-drive/commit/0b5bad2cfdc49e12988ccd69333d106019cd9dee)** Chuẩn hóa tên biến tiếng Việt không dấu dễ sử dụng.
- **[a635e34](https://github.com/huyvu2512/colab-drive/commit/a635e34acd693cd1e6fb90aba2a06fc8e63b6923)** Đơn giản hóa các bước thao tác và gộp cell thực thi tải xuống.
- **[e342e60](https://github.com/huyvu2512/colab-drive/commit/e342e60da4080f75b92d3e79c1dfb37f8e4a7ad5)** Khởi tạo mã nguồn ban đầu của dự án.
