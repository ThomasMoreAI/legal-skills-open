---
name: arbitration-minhlongs
title: /arbitration — Vietnamese Commercial Arbitration & Dispute Resolution Suite
description: Vietnamese Commercial Arbitration, Out-of-Court Dispute Resolution & New York Convention Suite.
author: minhlongs
author_url: https://github.com/minhlongs/mekong-cli/tree/main/.agents/skills/arbitration
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: vn
practice: arbitration
language: pt
---

# /arbitration — Vietnamese Commercial Arbitration & Dispute Resolution Suite

Quản lý và giải quyết tranh chấp kinh tế, thương mại bằng Trọng tài thương mại theo Luật Trọng tài thương mại 2010, Quy tắc tố tụng VIAC, soạn thảo điều khoản trọng tài mẫu, tính biểu phí trọng tài, ban hành phán quyết chung thẩm và thẩm tra công nhận phán quyết trọng tài nước ngoài theo Công ước New York 1958.

## Căn cứ Pháp lý & Khung Quy chuẩn

1. **Luật Trọng tài thương mại 2010** (Luật số 54/2010/QH12).
2. **Nghị quyết số 01/2014/NQ-HĐTP** của Hội đồng Thẩm phán TANDTC hướng dẫn thi hành một số quy định của Luật Trọng tài thương mại.
3. **Nghị định số 22/2017/NĐ-CP** về hòa giải thương mại (Commercial Mediation).
4. **Bộ luật Tố tụng dân sự 2015** (Phần thứ bảy: Thủ tục công nhận và cho thi hành tại Việt Nam phán quyết của trọng tài nước ngoài).
5. **Công ước New York 1958** về công nhận và cho thi hành phán quyết trọng tài nước ngoài (New York Convention).
6. **Quy tắc tố tụng VIAC** (Trung tâm Trọng tài Quốc tế Việt Nam).

---

## Tính năng Nghiệp vụ Cốt lõi

### 1. Soạn thảo & Thẩm định Điều khoản Trọng tài (Điều 16–19)
- Thẩm định tính hợp lệ của thỏa thuận trọng tài: cơ quan trọng tài (`VIAC`, `SIAC`, `ICC`, `HKIAC`, `AD_HOC`), địa điểm trọng tài (Seat), luật áp dụng và ngôn ngữ tố tụng.
- Đảm bảo số lượng trọng tài viên là số lẻ (1 hoặc 3 trọng tài viên theo Điều 39).
- Tự động sinh điều khoản trọng tài thương mại mẫu hợp chuẩn.

### 2. Thụ lý Khởi kiện & Tính Biểu phí Trọng tài VIAC (Điều 30–34)
- Tiếp nhận đơn khởi kiện, thông tin nguyên đơn, bị đơn, tóm tắt tranh chấp và giá trị tranh chấp (VND).
- Tính biểu phí trọng tài theo thang lũy tiến của VIAC cho Hội đồng 3 trọng tài viên hoặc Trọng tài viên duy nhất (70% mức phí).

### 3. Ban hành Phán quyết Trọng tài & Thẩm tra Điều 68 (Điều 60, 61, 68)
- Ghi nhận phán quyết trọng tài có giá trị chung thẩm và bắt buộc thi hành kể từ ngày ban hành.
- Thẩm tra nguy cơ bị Tòa án hủy phán quyết theo Điều 68: thỏa thuận trọng tài vô hiệu, thành phần HĐTT trái luật, vượt quá thẩm quyền hoặc trái nguyên tắc cơ bản của pháp luật Việt Nam.

### 4. Công nhận & Cho Thi hành Phán quyết Trọng tài Nước ngoài (Điều 451–463 BLTTDS 2015)
- Thẩm tra hồ sơ yêu cầu công nhận phán quyết trọng tài quốc tế tại Việt Nam theo Công ước New York 1958.
- Kiểm tra tính hợp lệ về thời hiệu nộp đơn (03 năm kể từ ngày phán quyết có hiệu lực) và hợp pháp hóa lãnh sự tài liệu, bản dịch công chứng tiếng Việt.

### 5. National Arbitration Telemetry & Status
- Báo cáo tổng thể điều khoản trọng tài, số lượng vụ kiện thụ lý, tổng giá trị tranh chấp, phí trọng tài thu nộp và hồ sơ công nhận quốc tế.

---

## Hướng dẫn Sử dụng CLI (`mekong arbitration`)

```bash
# Xem báo cáo tổng quan telemetry trọng tài thương mại quốc gia
mekong arbitration

# Soạn thảo và thẩm định điều khoản trọng tài mẫu hợp đồng
mekong arbitration clause "Hợp đồng Cung cấp Thiết bị Nhà máy" --inst "VIAC" --seat "Hà Nội" --law "VIETNAMESE_LAW" --lang "VIETNAMESE" --arbitrators 3

# Thụ lý đơn khởi kiện trọng tài và tính phí VIAC
mekong arbitration claim "Công ty Cổ phần Thép Việt" --respondent "Tập đoàn Xây dựng Delta" --subject "Vi phạm nghĩa vụ thanh toán vật liệu" --amount 8500000000 --arbitrators 3

# Ban hành phán quyết trọng tài chung thẩm
mekong arbitration award "ARB-CLM-A1B2C3D4" --president "GS. TS. Lê Hồng Hạnh" --granted-pct 100 --amount 8500000000

# Thẩm tra công nhận phán quyết trọng tài nước ngoài theo Công ước New York
mekong arbitration foreign "SIAC" --country "Singapore" --amount-usd 3200000 --ny-member --consular --years 1.2

# Tra cứu danh mục hồ sơ trọng tài
mekong arbitration list --category ALL --limit 50

# Xem trạng thái hệ thống dạng JSON
mekong arbitration status --json
```

---

## Native MCP Tools

Bộ công cụ MCP trọng tài thương mại quốc gia (FastMCP & JSON-RPC 2.0 stdio):

- `mekong_arbitration_clause`: Soạn thảo và kiểm tra tính hợp lệ của điều khoản trọng tài (Điều 16-19).
- `mekong_arbitration_claim`: Thụ lý đơn khởi kiện trọng tài và tính phí trọng tài VIAC (Điều 30-34).
- `mekong_arbitration_award`: Ban hành phán quyết trọng tài chung thẩm và thẩm tra căn cứ hủy (Điều 60, 61, 68).
- `mekong_arbitration_foreign`: Thẩm tra điều kiện công nhận phán quyết trọng tài nước ngoài theo Công ước New York 1958.
- `mekong_arbitration_list`: Tra cứu danh sách điều khoản, vụ kiện, phán quyết trọng tài và hồ sơ quốc tế.
- `mekong_arbitration_status`: Truy xuất dữ liệu telemetry trọng tài thương mại và giải quyết tranh chấp.
