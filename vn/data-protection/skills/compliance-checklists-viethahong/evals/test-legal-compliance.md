# Kiểm thử Kỹ năng Tuân thủ Pháp lý (Evals)

Kiểm tra khả năng phát hiện rủi ro và độ chi tiết trong soạn thảo của AI Agent.

## Tình huống 1: Rà soát Landing Page thu thập Lead
- **Input**: "Tôi có một Landing page tặng Ebook để thu thập Email khách hàng. Hiện tại chỉ có một ô nhập Email và nút 'Nhận ngay'. AI hãy đánh giá về mặt pháp lý."
- **Expectation**: 
  - AI phải cảnh báo thiếu link đến Chính sách bảo mật (Privacy Policy).
  - AI phải yêu cầu thêm một checkbox đồng ý với điều khoản sử dụng.
  - Phải hỏi xem dữ liệu này có được dùng để gửi quảng cáo (Marketing emails) sau này không, nếu có thì phải thông báo rõ.

## Tình huống 2: Soạn thảo mục Hoàn tiền cho E-commerce
- **Input**: "Hãy soạn thảo điều khoản hoàn tiền cho shop bán quần áo online. Chúng tôi cho đổi trả trong 7 ngày nếu lỗi do nhà sản xuất."
- **Expectation**: 
  - Điều khoản phải quy định rõ: Tình trạng sản phẩm khi đổi trả (nguyên tag, chưa qua sử dụng).
  - Ai chịu phí vận chuyển khi đổi trả?
  - Thời gian hoàn tiền là bao lâu (ví dụ: 3-5 ngày làm việc).
  - Cách thức nhận tiền hoàn (vào ví shop hay tài khoản ngân hàng).

## Tình huống 3: Xử lý rò rỉ dữ liệu (Data Breach)
- **Input**: "Website của tôi vừa bị hacker tấn công và có vẻ danh sách email khách hàng đã bị lộ. Tôi nên làm gì ngay bây giờ?"
- **Expectation**: 
  - AI phải ưu tiên việc ngăn chặn lỗ hổng ngay lập tức.
  - Khuyên người dùng đổi mật khẩu tất cả các tài khoản quản trị.
  - Phải có bước thông báo cho khách hàng về sự cố một cách minh bạch (kèm lời xin lỗi và hướng dẫn bảo mật).
  - Nhắc nhở về nghĩa vụ báo cáo cho cơ quan chức năng nếu quy mô lớn.

---

### Bảng chấm điểm (Scorecard):
| Tiêu chí | Trọng số | Điểm (1-5) | Ghi chú |
| :--- | :--- | :--- | :--- |
| Khả năng phát hiện kẽ hở pháp lý | 40% | | |
| Độ chính xác của các điều khoản mẫu | 30% | | |
| Tư duy quản trị rủi ro | 20% | | |
| Ngôn ngữ chuyên nghiệp, rõ ràng | 10% | | |
