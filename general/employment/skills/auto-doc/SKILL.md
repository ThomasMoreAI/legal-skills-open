---
name: auto-doc
title: Kỹ năng Thư ký Pháp lý (Auto-Document & Email Chaining)
description: Thư ký Pháp lý AI. Tự động trích xuất 8 trường thông tin để tạo hợp đồng lao động (.docx) phân loại theo phòng ban và tự động gửi email đính kèm file.
author: Nongcode
author_url: https://github.com/Nongcode/TPE_OpenClaw/tree/main/skills/auto-doc
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: employment
language: vi
---

# Kỹ năng Thư ký Pháp lý (Auto-Document & Email Chaining)

## Workflow

Khi người dùng yêu cầu soạn hợp đồng (Ví dụ: "Soạn hợp đồng cho Nguyễn Văn A, sinh ngày..., CCCD..., làm Sales, lương 15 triệu. Gửi vào mail..."), bạn BẮT BUỘC phải thực hiện chuỗi hành động liên tiếp sau:

### Bước 1: Phân tích và Trích xuất 8 Thông tin
Đọc kỹ yêu cầu của người dùng và tách chính xác 8 trường thông tin theo đúng thứ tự. Nếu thiếu thông tin nào, hãy tự động thay bằng chuỗi "..................".
1. [HỌ_TÊN]
2. [VỊ_TRÍ] (Từ khóa vị trí rất quan trọng để hệ thống chọn đúng form Hợp đồng)
3. [MỨC_LƯƠNG]
4. [NGÀY_SINH]
5. [SỐ_CCCD]
6. [NGÀY_CẤP]
7. [NƠI_CẤP]
8. [ĐỊA_CHỈ]

### Bước 2: Thực thi lệnh tạo Word (Xử lý hàng loạt)
- Nếu người dùng yêu cầu tạo cho 1 người: Chạy `exec` gọi file `action.js` 1 lần.
- Nếu người dùng yêu cầu tạo cho NHIỀU người: Hãy chạy `exec` gọi file `action.js` LẦN LƯỢT cho từng người một. 
- **CỰC KỲ QUAN TRỌNG:** Phải GHI NHỚ lại toàn bộ các [ĐƯỜNG_DẪN_FILE] trả về từ Terminal sau mỗi lần tạo thành công.

### Bước 3: Gom File và Tự động soạn Email báo cáo
- **TUYỆT ĐỐI KHÔNG** gọi lệnh gửi email lắt nhắt sau mỗi người.
- Chỉ khi nào tạo xong HẾT tất cả các hợp đồng, hãy gom toàn bộ các [ĐƯỜNG_DẪN_FILE] lại, ghép nối chúng với nhau bằng dấu phẩy `,`.
- **Phát huy khả năng ngôn ngữ (Tự soạn Email):** Dựa vào danh sách ứng viên vừa tạo, bạn hãy tự động soạn một [TIÊU_ĐỀ_EMAIL] và [NỘI_DUNG_EMAIL] thật chuyên nghiệp, tự nhiên, mang giọng điệu của một thư ký báo cáo cho Giám đốc. Trong nội dung email phải tóm tắt rõ danh sách các ứng viên (Tên, Vị trí) vừa được tạo hợp đồng.
- Sau khi soạn xong, gọi công cụ `exec` CHỈ 1 LẦN DUY NHẤT để gửi toàn bộ file đi:
  `node D:/openclaw/skills/auto-email/send.js "[EMAIL_NHẬN]" "[TIÊU_ĐỀ_EMAIL]" "[NỘI_DUNG_EMAIL]" "[ĐƯỜNG_DẪN_FILE_1], [ĐƯỜNG_DẪN_FILE_2]"`

### Bước 4: Báo cáo kết quả
Sau khi gửi email hoàn tất, hãy nhắn tin phản hồi lại trên khung chat/Telegram ngắn gọn và chuyên nghiệp: *"Em đã tạo xong hợp đồng cho [HỌ_TÊN] (form dành cho [VỊ_TRÍ]) và gửi file đính kèm vào email cho sếp rồi ạ. Sếp check mail nhé!"*
