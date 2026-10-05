---
name: notary-minhlongs
title: mekong notary — Autonomous Vietnamese Notary, Legal Practice & Judicial Authentication Suite
description: Vietnamese Notary, Legal Practice & Judicial Authentication Compliance Suite.
author: minhlongs
author_url: https://github.com/minhlongs/mekong-cli/tree/main/.agents/skills/notary
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: vn
practice: general
language: en
---

# mekong notary — Autonomous Vietnamese Notary, Legal Practice & Judicial Authentication Suite

## Căn Cứ Pháp Lý & Chuẩn Mực Nghiệp Vụ
1. **Luật Công chứng 2014 (Luật số 53/2014/QH13) & Luật Công chứng 2024**:
   - Thống nhất quản lý hoạt động công chứng chứng nhận tính xác thực, hợp pháp của hợp đồng, giao dịch dân sự, kinh tế, thương mại.
   - Thẩm quyền quản lý: **Bộ Tư pháp**, Sở Tư pháp các tỉnh/thành phố trực thuộc Trung ương, Hội Công chứng viên.
   - Tổ chức hành nghề công chứng: Phòng công chứng (đơn vị sự nghiệp công lập) và Văn phòng công chứng (thành lập theo mô hình công ty hợp danh có từ 2 công chứng viên hợp danh trở lên).
   - Công chứng viên: Bắt buộc có chứng chỉ hành nghề công chứng, thẻ công chứng viên và tham gia bảo hiểm trách nhiệm nghề nghiệp bắt buộc.
   - Các hợp đồng, giao dịch **bắt buộc phải công chứng** theo luật định:
     * Hợp đồng chuyển nhượng, tặng cho, thế chấp, góp vốn bằng quyền sử dụng đất, quyền sở hữu nhà ở (Luật Đất đai 2024, Luật Nhà ở 2023).
     * Văn bản thỏa thuận phân chia di sản thừa kế, văn bản từ chối nhận di sản thừa kế.
     * Hợp đồng mua bán, tặng cho phương tiện, tài sản có đăng ký quyền sở hữu.
   - Cơ sở dữ liệu công chứng ngăn chặn (Điều 62): Ngăn chặn kịp thời các giao dịch tẩu tán tài sản, tài sản đang thế chấp ngân hàng hoặc bị kê biên thi hành án.
   - Thời hạn lưu trữ hồ sơ: Tối thiểu **20 năm** tại tổ chức hành nghề; bản chính văn bản công chứng phải lưu trữ **vĩnh viễn** (Điều 64).
2. **Luật Luật sư 2006 (Luật số 65/2006/QH11, sửa đổi 2012)**:
   - Tổ chức hành nghề luật sư: Văn phòng luật sư (do 1 luật sư thành lập) hoặc Công ty luật (TNHH, Hợp danh).
   - Điều kiện hành nghề: Chứng chỉ hành nghề luật sư do Bộ Tư pháp cấp, Thẻ luật sư do Liên đoàn Luật sư Việt Nam / Đoàn luật sư cấp tỉnh cấp.
   - Hợp đồng dịch vụ pháp lý: Bắt buộc lập thành văn bản, ghi rõ thù lao và chi phí; tổ chức hành nghề luật sư phải mua bảo hiểm trách nhiệm nghề nghiệp cho luật sư.
   - **Quy tắc đạo đức và điều cấm (Điều 9)**: Nghiêm cấm luật sư cung cấp dịch vụ pháp lý cho các khách hàng có quyền lợi đối lập trong cùng một vụ án, vụ việc (xung đột lợi ích); cấm tiết lộ bí mật thông tin của thân chủ.
3. **Nghị định số 23/2015/NĐ-CP (Cấp bản sao từ sổ gốc, chứng thực bản sao từ bản chính, chứng thực chữ ký)**:
   - Thẩm quyền: UBND cấp xã/phường, Phòng Tư pháp cấp quận/huyện, Cơ quan đại diện Việt Nam ở nước ngoài và Công chứng viên của tổ chức hành nghề công chứng.
   - Các trường hợp **từ chối chứng thực bản sao** (Điều 22): Bản chính bị tẩy xóa, sửa chữa, thêm, bớt nội dung không hợp lệ; bản chính bị hư hỏng, rách nát không xác định được nội dung; bản chính đóng dấu mật hoặc chứa nội dung trái pháp luật, đạo đức xã hội.
4. **Nghị định số 82/2020/NĐ-CP**:
   - Xử phạt vi phạm hành chính trong lĩnh vực bổ trợ tư pháp, hành nghề luật sư, công chứng, chứng thực.
5. **Lưu trữ SQLite WAL**: Bảng `notarial_contracts`, `blocked_assets`, `legal_practice_agreements`, `document_authentications` tại `.mekong/notary.db`.

---

## CLI Invocations

```bash
# Báo cáo tổng quan hoạt động công chứng, luật sư và chứng thực tư pháp
mekong notary

# Thực hiện công chứng hợp đồng, tra cứu cơ sở dữ liệu ngăn chặn và tính phí công chứng
mekong notary contract "Chuyển nhượng QSDĐ Thảo Điền" --office "VPCC Sài Gòn" --notary "Nguyễn Văn Bình" --party-a "Trần Minh Tuấn" --party-b "Lê Hoàng Oanh" --type REAL_ESTATE_TRANSFER --value 8500000000 --asset-id "GCN-QSDD-HCM-2026-001"

# Cập nhật cơ sở dữ liệu ngăn chặn giao dịch công chứng (kê biên, thế chấp, phong tỏa)
mekong notary block "GCN-QSDD-HCM-2026-999" --desc "Biệt thự KDC Him Lam, Q7" --reason "Kê biên bảo đảm thi hành án hình sự" --authority "Cục Thi hành án Dân sự TP.HCM"

# Giải tỏa ngăn chặn tài sản trong cơ sở dữ liệu công chứng
mekong notary block "GCN-QSDD-HCM-2026-999" --unblock

# Thẩm định hợp đồng dịch vụ pháp lý và đạo đức nghề nghiệp luật sư (Luật Luật sư)
mekong notary lawyer "Công ty Luật Mekong & Cộng sự" --attorney "LS. Phạm Quốc Toàn" --card "LS-HN-2024-8899" --client "Tập đoàn Alpha" --matter "Tranh chấp M&A cổ phần" --fee 120000000 --no-conflict --insurance

# Chứng thực bản sao từ bản chính hoặc chứng thực chữ ký (Nghị định 23/2015/NĐ-CP)
mekong notary auth "Hộ chiếu & Căn cước công dân" --type COPY_AUTHENTICATION --body "UBND Phường Bến Nghé, Quận 1" --copies 5 --valid

# Tra cứu danh mục hồ sơ công chứng, tài sản bị chặn, hợp đồng luật sư và chứng thực
mekong notary list contracts
mekong notary list blocked
mekong notary list agreements
mekong notary list authentications

# Giám sát trạng thái và xuất JSON headless
mekong notary status --json
```

---

## MCP Tools Integration
- `mekong_notary_contract`: Công chứng hợp đồng, kiểm tra tài sản ngăn chặn và tính biểu phí công chứng theo Thông tư 257/2016/TT-BTC.
- `mekong_notary_block`: Thêm hoặc giải tỏa tài sản trong Cơ sở dữ liệu ngăn chặn công chứng theo Điều 62 Luật Công chứng.
- `mekong_notary_lawyer`: Thẩm định hợp đồng dịch vụ pháp lý, kiểm tra xung đột lợi ích và bảo hiểm nghề nghiệp theo Luật Luật sư.
- `mekong_notary_auth`: Chứng thực bản sao từ bản chính hoặc chứng thực chữ ký cá nhân theo Nghị định 23/2015/NĐ-CP.
- `mekong_notary_list`: Tra cứu danh mục hợp đồng công chứng, tài sản ngăn chặn, hợp đồng luật sư và chứng thực tư pháp.
- `mekong_notary_status`: Báo cáo chỉ số telemetry tổng hợp hệ thống công chứng và bổ trợ tư pháp.
