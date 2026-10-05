---
name: privacy-minhlongs
title: 🛡️ Privacy — Vietnamese Personal Data Protection Decree (PDPD Nghị định 13/2023/NĐ-CP)
description: Vietnamese Personal Data Protection Decree (PDPD Decree 13/2023/ND-CP), DPIA Form 04, cross-border data transfer, and 72-hour breach response.
author: minhlongs
author_url: https://github.com/minhlongs/mekong-cli/tree/main/.agents/skills/privacy
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: vn
practice: data-protection
language: en
---

# 🛡️ Privacy — Vietnamese Personal Data Protection Decree (PDPD Nghị định 13/2023/NĐ-CP)

Autonomous enterprise compliance engine implementing statutory personal data protection, Data Protection Impact Assessment (DPIA Mẫu số 04 gửi A05 - Bộ Công an), cross-border data transfer assessments (Điều 25), and 72-hour data breach reporting (Điều 26) under Vietnamese law.

---

## ⚖️ Căn cứ Pháp lý & Khung Tiêu chuẩn

1. **Nghị định 13/2023/NĐ-CP (PDPD)**:
   - **Phân loại dữ liệu cá nhân (Điều 2)**:
     - *Dữ liệu cá nhân cơ bản*: Họ tên, ngày sinh, giới tính, nơi cư trú, số điện thoại, CMND/CCCD, email, v.v.
     - *Dữ liệu cá nhân nhạy cảm*: Tài khoản ngân hàng, sinh trắc học, vị trí địa lý, tình trạng sức khỏe/hồ sơ bệnh án, quan điểm chính trị/tôn giáo.
   - **11 Quyền của chủ thể dữ liệu (Điều 9)**: Quyền được biết, đồng ý, truy cập, rút lại sự đồng ý, xóa dữ liệu, hạn chế xử lý, cung cấp dữ liệu, phản đối xử lý, khiếu nại, đòi bồi thường, tự bảo vệ.
   - **Đánh giá tác động xử lý dữ liệu cá nhân - DPIA (Điều 24)**: Lập hồ sơ theo Mẫu số 04 gửi Cục A05 - Bộ Công an trong thời hạn 60 ngày.
   - **Chuyển dữ liệu cá nhân ra nước ngoài (Điều 25)**: Thẩm định TIA, ký cam kết bảo vệ dữ liệu (SCC), lập hồ sơ gửi A05.
   - **Thông báo sự cố vi phạm trong vòng 72 giờ (Điều 26)**: Nghĩa vụ bắt buộc thông báo Cục A05 khi xảy ra rò rỉ hoặc mất mát dữ liệu.
   - **Bổ nhiệm DPO / Bộ phận bảo vệ dữ liệu (Điều 28)**: Bắt buộc đối với doanh nghiệp xử lý dữ liệu cá nhân nhạy cảm.
2. **Luật An toàn thông tin mạng 2015 & Luật An ninh mạng 2018**.

---

## 💻 CLI Commands

### 1. Bảng điều khiển tổng quan
```bash
mekong privacy
mekong privacy --json
```

### 2. Đánh giá mức độ tuân thủ doanh nghiệp (Compliance Audit)
```bash
mekong privacy audit "Tập đoàn VNG" --role CONTROLLER_AND_PROCESSOR --sensitive --dpo --cross-border
mekong privacy audit "StartUp Fintech" --role CONTROLLER --sensitive --no-dpo --json
```

### 3. Lập hồ sơ Đánh giá tác động xử lý dữ liệu (DPIA Mẫu 04)
```bash
mekong privacy dpia "Khai phá Dữ liệu Khách hàng" "Cá nhân hóa dịch vụ bán lẻ" "FULL_NAME,PHONE_NUMBER,EMAIL,LOCATION_TRACKING" --basis CONSENT --security "AES-256, RBAC"
mekong privacy dpia "Chấm công Sinh trắc học" "Xác thực danh tính nhân sự" "FULL_NAME,BIOMETRICS,ID_CARD_NUMBER" --json
```

### 4. Thẩm định chuyển dữ liệu cá nhân ra nước ngoài (Điều 25)
```bash
mekong privacy transfer "Đồng bộ CRM Global" "Salesforce Inc" "Singapore" "FULL_NAME,EMAIL,PHONE_NUMBER" --count 50000 --scc
mekong privacy transfer "Lưu trữ Đám mây AWS" "Amazon Web Services" "USA" "FULL_NAME,DOB,BANKING_FINANCIAL" --count 100000 --json
```

### 5. Ghi nhận & kích hoạt ứng phó sự cố rò rỉ dữ liệu 72h (Điều 26)
```bash
mekong privacy breach "Rò rỉ API cổng thanh toán" CRITICAL 15000 "DATA_EXFILTRATION" --hours 3.5
mekong privacy breach "Mất mã khóa Token" HIGH 2500 "UNAUTHORIZED_ACCESS" --json
```

### 6. Tiếp nhận & xử lý yêu cầu quyền chủ thể dữ liệu (DSAR)
```bash
mekong privacy dsar RIGHT_TO_ACCESS "CCCD-079090012345" --details "Yêu cầu trích xuất toàn bộ lịch sử giao dịch cá nhân"
mekong privacy dsar RIGHT_TO_DELETE "USER-889911" --details "Yêu cầu xóa tài khoản và dữ liệu cá nhân theo Điều 9.5" --json
```

### 7. Danh mục & Chỉ số điều hành
```bash
mekong privacy list --type dpia --limit 20
mekong privacy list --type transfer --json
mekong privacy list --type breach
mekong privacy list --type dsar
mekong privacy status --json
```

---

## 🔌 Dual MCP Tools

- `mekong_privacy_audit`: Conduct enterprise PDPD statutory compliance audit.
- `mekong_privacy_dpia`: Create Article 24 DPIA assessment dossier (Form 04 for A05 filing).
- `mekong_privacy_transfer`: Evaluate Article 25 cross-border data transfer compliance and SCC agreement.
- `mekong_privacy_breach`: Report data breach incident and enforce 72-hour statutory notification timeline.
- `mekong_privacy_dsar`: Process Article 9 Data Subject Access Request.
- `mekong_privacy_list`: Query registered DPIA dossiers, overseas transfers, incidents, or DSAR requests.
- `mekong_privacy_status`: Retrieve aggregated PDPD compliance metrics and telemetry.
