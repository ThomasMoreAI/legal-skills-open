import type { Metadata } from "next";
import { Noto_Sans_Thai, IBM_Plex_Sans_Thai, IBM_Plex_Serif } from "next/font/google";
import "./globals.css";
import { Toaster } from "@/components/ui/toaster";

const ibmPlexSans = IBM_Plex_Sans_Thai({
  variable: "--font-ibm-plex-sans",
  subsets: ["thai", "latin"],
  weight: ["300", "400", "500", "600", "700"],
  display: "swap",
});

const ibmPlexSerif = IBM_Plex_Serif({
  variable: "--font-ibm-plex-serif",
  subsets: ["thai", "latin"],
  weight: ["400", "500", "600", "700"],
  display: "swap",
});

const notoSans = Noto_Sans_Thai({
  variable: "--font-noto-sans-thai",
  subsets: ["thai", "latin"],
  weight: ["400", "500", "600", "700"],
  display: "swap",
});

export const metadata: Metadata = {
  title: "ปัญญา AI | Panya-AI — ที่ปรึกษากฎหมายไทยฝั่งนายจ้าง",
  description: "ฐานข้อมูลกฎหมายไทย — กฎหมายแรงงาน ป.พ.พ. ป.อ. และคำพิพากษาศาลฎีกา พร้อม AI ถามตอบพร้อมอ้างอิงมาตรา",
  keywords: ["กฎหมายไทย", "กฎหมายแรงงาน", "คำพิพากษาศาลฎีกา", "Panya-AI", "Legal AI Thailand"],
  authors: [{ name: "Panya-AI" }],
  icons: { icon: "/panya-logo.png" },
  openGraph: {
    title: "Panya-AI — ที่ปรึกษากฎหมายไทยฝั่งนายจ้าง",
    description: "78 กฎหมาย · 8,507 มาตรา · 514 ฎีกา · 615 อนุบัญญัติ · 63 เทมเพลต",
    type: "website",
    locale: "th_TH",
  },
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="th" suppressHydrationWarning>
      <body className={`${ibmPlexSans.variable} ${ibmPlexSerif.variable} ${notoSans.variable} antialiased bg-background text-foreground`}>
        {children}
        <Toaster />
      </body>
    </html>
  );
}
