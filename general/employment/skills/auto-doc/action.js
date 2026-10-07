const PizZip = require("pizzip");
const Docxtemplater = require("docxtemplater");
const fs = require("fs");
const path = require("path");

// 1. Nhận toàn bộ 8 thông tin cá nhân từ AI truyền vào
const args = process.argv.slice(2);
const hoTen = args[0] || "..................";
const viTri = args[1] || "..................";
const luong = args[2] || "..................";
const ngaySinh = args[3] || "..../..../......";
const cccd = args[4] || "..................";
const ngayCap = args[5] || "..../..../......";
const noiCap = args[6] || "..................";
const diaChi = args[7] || "....................................";

// =========================================================================
// 2. BỘ LỌC TỰ ĐỘNG PHÂN LOẠI FORM HỢP ĐỒNG THEO PHÒNG BAN
// =========================================================================
let templateName = "template.docx";
const viTriLower = viTri.toLowerCase();

// A. Phòng Kinh doanh (Sales)
if (viTriLower.includes("sale") || viTriLower.includes("kinh doanh") || viTriLower.includes("bán hàng")) {
    templateName = "form_sales.docx";
    console.log("[Hệ thống] Nhận diện bộ phận KINH DOANH. Dùng form: form_sales.docx");
} 
// B. Phòng Kỹ thuật / IT
else if (viTriLower.includes("kỹ thuật") || viTriLower.includes("it") || viTriLower.includes("lập trình") || viTriLower.includes("tech")) {
    templateName = "form_kythuat.docx";
    console.log("[Hệ thống] Nhận diện bộ phận KỸ THUẬT. Dùng form: form_kythuat.docx");
} 
// C. Phòng Kế toán / Tài chính
else if (viTriLower.includes("kế toán") || viTriLower.includes("tài chính") || viTriLower.includes("thu ngân")) {
    templateName = "form_ketoan.docx";
    console.log("[Hệ thống] Nhận diện bộ phận KẾ TOÁN. Dùng form: form_ketoan.docx");
} 
// D. Phòng Hành chính / Nhân sự
else if (viTriLower.includes("hành chính") || viTriLower.includes("nhân sự") || viTriLower.includes("hr")) {
    templateName = "form_hanhchinh.docx";
    console.log("[Hệ thống] Nhận diện bộ phận HÀNH CHÍNH - NHÂN SỰ. Dùng form: form_hanhchinh.docx");
} 
// E. Các vị trí khác chưa có form riêng
else {
    console.log(`[Hệ thống] Không khớp bộ phận đặc thù. Dùng form tiêu chuẩn (template.docx) cho vị trí: ${viTri}`);
}

const templatePath = path.join(__dirname, templateName);
const safeName = hoTen.normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/\s+/g, "_");
const outputPath = path.join("D:", "openclaw", `Hop_Dong_${safeName}.docx`);

try {
    // Kiểm tra xem sếp đã tạo đủ file Word trong thư mục chưa
    if (!fs.existsSync(templatePath)) {
        console.log(`[Lỗi] Chưa có file mẫu: ${templateName}. Sếp hãy copy file template.docx ra và đổi tên thành ${templateName} nhé!`);
        process.exit(1);
    }

    const content = fs.readFileSync(templatePath, "binary");
    const zip = new PizZip(content);
    const doc = new Docxtemplater(zip, { paragraphLoop: true, linebreaks: true });

    const today = new Date();
    const ngayTao = `${today.getDate()}/${today.getMonth() + 1}/${today.getFullYear()}`;

    // 3. Đổ full 8 thông tin vào mẫu Word
    doc.render({
        hoTen: hoTen,
        viTri: viTri,
        luong: luong,
        ngayTao: ngayTao,
        ngaySinh: ngaySinh,
        cccd: cccd,
        ngayCap: ngayCap,
        noiCap: noiCap,
        diaChi: diaChi
    });

    const buf = doc.getZip().generate({ type: "nodebuffer" });
    fs.writeFileSync(outputPath, buf);

    console.log(`THÀNH CÔNG! Đã tạo hợp đồng cho ${hoTen} tại: ${outputPath}`);
} catch (error) {
    console.log(`[Lỗi] Không thể tạo hợp đồng: ${error.message}`);
}
