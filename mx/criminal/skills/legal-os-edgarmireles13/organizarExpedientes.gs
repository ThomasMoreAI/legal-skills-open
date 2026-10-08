/**
 * ORGANIZADOR DE EXPEDIENTES JURÍDICOS — Edgar Jair Mireles González
 * ─────────────────────────────────────────────────────────────────────
 * INSTRUCCIONES:
 *  1. Abre Google Drive → En el menú superior ve a "Nuevo" → "Más" → "Google Apps Script"
 *     (también puedes ir directo a: https://script.google.com)
 *  2. Borra todo el contenido que aparece por defecto.
 *  3. Pega TODO este código.
 *  4. Haz clic en el ícono de guardar (💾) o presiona Ctrl+S.
 *  5. Haz clic en "Ejecutar" (▶) con la función "organizarExpedientes" seleccionada.
 *  6. La primera vez te pedirá autorización — acéptala.
 *  7. Revisa el registro de ejecución (Ver → Registros) para ver el resultado.
 * ─────────────────────────────────────────────────────────────────────
 */

function organizarExpedientes() {
  // IDs de las carpetas ya creadas en tu Drive (revisa/ajusta los IDs si hace falta)
  var CARPETAS = {
    "AMPARO INDIRECTO":         "1PW_eYf1_tNCDPBIfNYAnYvmf3koVgoJd",
    "AMPARO DIRECTO":           "1z1zAkqv5wysqeW_Jqf_WygebPjeBnJKn",
    "PENAL":                    "16EhvT0o2MaSpUmOKPrDLIoBrFTTgCEkv",
    "FISCALIA":                 "1PHVEZO7IICZAqr1UeHW4FRzk3H3rkp0w",
    "FAMILIAR ORAL":            "12N72DFjmCNOujjPBrPNI2J3hquXT-buw",
    "FAMILIAR":                 "1m8TO8yc3VadA3ZGEgPoxRxDot4XFJSdH",
    "ADMINISTRATIVO":           "1Ir-0QWD9WuddLe9386YQfkJgpgQvzyqU",
    "CONTRATOS Y HONORARIOS":   "1DVAXS-79CRkwqKcHlQrwSsfZF3SHjL9S",
    "OTROS":                    "1LU_uAD4oSRIEp0CAUH-SQLmqSWfzD8du"
  };

  // Mapa de archivos: [fileId, carpeta destino]
  var ARCHIVOS = [
    // AMPARO INDIRECTO (16 archivos — caso Chuy 215/2026-VII)
    ["1iyiifNuoNhAIRl_ziOqR9AUls3j7JbLU", "AMPARO INDIRECTO"],  // PREVENCION.docx
    ["1E3PHkRskHQs67JCv7Vb_y3Xnwwk8unha", "AMPARO INDIRECTO"],  // PREVENCION (1).docx
    ["1xMkafNMjkwguqzl7XjDcLRuCuZb4IE19", "AMPARO INDIRECTO"],  // Demanda de Amparo Indirecto Penal (Chuy)
    ["11UEEyhKlaEaVcWNfpkkoi2ggmxSwesuL", "AMPARO INDIRECTO"],  // RecursoDeQueja de CHUY.docx
    ["1LIBfQqLyZMTfLrBxCv4d4xKiqLFODhfU", "AMPARO INDIRECTO"],  // Notificación amparo Chuy 0004_Copy.pdf
    ["1eMsmrHnskEIbfL3lhYsCvrPG0papJf_Y", "AMPARO INDIRECTO"],  // Notificacion amparo Chuy 0002_Copy.pdf
    ["1_L9Sr8RLb3nzyaoRZog82Zhq7ztYvap9", "AMPARO INDIRECTO"],  // Documento (6).docx
    ["1o8l_qHIGExIgjYJdx4uq6t1Dxx3SRzio", "AMPARO INDIRECTO"],  // RecursoDeQueja_215-2026_v2.docx
    ["1CGExa1EE6pPtJbwqL9sspS37c7lsvd_O", "AMPARO INDIRECTO"],  // Notificación amparo Chuy 0004.pdf
    ["1tRnkFIPWOToLBUUziDwUllXa9AGWbz-a", "AMPARO INDIRECTO"],  // Notificacion amparo Chuy 0002.pdf
    ["1mZ349oMB6d4oQmLGK15Um2_k_ksMJqX9", "AMPARO INDIRECTO"],  // CONTESTA PREVENCION DE AMPARO DE JESUS.pdf
    ["1ka4iBc5WcDh7osY5VTVD-JF6nwNXmJhG", "AMPARO INDIRECTO"],  // CONTESTA PREVENCION DE AMPARO DE JESUS.doc
    ["1dwNSJ-bHBFJZXgFarOAsUzVcxVzALeYZ", "AMPARO INDIRECTO"],  // CONTESTA PREVENCION 30 03 26.pdf
    ["114H9cB2Hsi2wSmVQZrPRqhGOjhFa-KP-", "AMPARO INDIRECTO"],  // CONTESTA PREVENCION 30 03 25.pdf
    ["1-ci7kwHYH59MPro258DA8SywaoQMlWih", "AMPARO INDIRECTO"],  // CONTESTA PREVENCION 30 03 25.docx
    ["1Eo3DAvKkPDHQR1Yxb4vfRMXWa2Zzk12_", "AMPARO INDIRECTO"],  // Guardado Autorrecuperación.docx

    // AMPARO DIRECTO (2 archivos)
    ["1NT0CGCm2oDO_EFZz0iHoWIFqjerrBWaj", "AMPARO DIRECTO"],
    ["1CnQueWpmdM2njbqwWXVr8tq9Z4sN31Cx", "AMPARO DIRECTO"],

    // PENAL (9 archivos)
    ["1FCgoMm7wk2ihuNCNr_CyDorwoYRr-mWj", "PENAL"],
    ["1z3KAORELuaPQoNalFjtFk1HAFN9NlSU2", "PENAL"],
    ["1_H-P8i11FZfplqmGGzJyEGj3QLAevlV2", "PENAL"],
    ["1R8bE8e3ECFZc7aZN7VCVb8l5BBNmlEFY", "PENAL"],
    ["1O4OS3N3mf7TlpX-fWWZ_fjVW09CH0tV7", "PENAL"],
    ["1Z-fa_TTQJqyoptaVBicym1NSDsbA46p4", "PENAL"],
    ["19BfVIYOqBYzqZJibXwJMV3QXeDCO5ADn", "PENAL"],
    ["1M5h-ykEioNww9DF0VI9lnQkNFXc2ySNO", "PENAL"],
    ["1e4LAcr48dhbKmfHQVxlaqAWjN0vv7khz", "PENAL"],

    // FISCALIA (2 archivos)
    ["1Yie7VXCXzx8RT80LSo2PGFg0hvbiXdRb", "FISCALIA"],
    ["1H0otTbO5svGyUwdJBbH6mspdbgdy9L4e", "FISCALIA"],

    // FAMILIAR ORAL (4 archivos)
    ["11oL1RxuXfoXY4lC7pwBUPiQPAduN_s7y", "FAMILIAR ORAL"],
    ["169VUCsDlz5vkrGC4FYq19JdPffKAH1i1", "FAMILIAR ORAL"],
    ["1EyKqpko-EkSvd9RvbDB9qoRdApqzId_G", "FAMILIAR ORAL"],
    ["1ObZ9OgoAiCPxUXCE3R3mJ2fCBzo4xZjh", "FAMILIAR ORAL"],

    // FAMILIAR (2 archivos)
    ["13NwSKJ0Onzs30GVMnjA1NPonPUq2o3xg", "FAMILIAR"],
    ["1LP3UKcjtmYFTu2LU3ATxrZDjsWIHi4ea", "FAMILIAR"],

    // ADMINISTRATIVO (6 archivos)
    ["1JKLcHtfifsFrN1fNFVSpbu5INAwLWNzX", "ADMINISTRATIVO"],
    ["1HOV8c2rIU0MA01KpDqolTK0gKeFI8eMI", "ADMINISTRATIVO"],
    ["13E70Aw62HfDYYE8gI_x78dvtV4EOPX88", "ADMINISTRATIVO"],
    ["1nSu7P_ltojY07yzGRDs_UqlJCt", "ADMINISTRATIVO"],
    ["1df0870zd07T_oUrbDr0Hw6Lnz_UqlJCt", "ADMINISTRATIVO"],
    ["1o04QQF5s17nL-BfEBhLOsid6uq30LPZA", "ADMINISTRATIVO"],

    // CONTRATOS Y HONORARIOS (1 archivo)
    ["1Y2oXs_fiuoE9IQNAetfTMwHgw2k8JPZl", "CONTRATOS Y HONORARIOS"],

    // OTROS (7 archivos)
    ["1TaVk1-C--GlWbZjjXr5kumNVCFiNKSmY", "OTROS"],
    ["1NXEuDXWy6yyx_4Ye2WyC7m_XIvsJiiu", "OTROS"],
    ["1QWMwHXu_Xywan-e6iF4157pXx4ddvOWR", "OTROS"],
    ["1XoKDG8BlKE2jPVHm95jFvuYSZAT0vcHK", "OTROS"],
    ["1sxtYCB0S-TMX8ECvT2WnyM3ePfsb2e-0", "OTROS"],
    ["1rwihdaoaFl4NcjEKJF_urLSxCbzA1jV5", "OTROS"],
    ["1SjnFV9nnVGi4Ex8y6iFVAENBhYoF2Km-", "OTROS"]
  ];

  // Ejecución
  var movidos = 0;
  var errores = 0;
  var log = [];

  for (var i = 0; i < ARCHIVOS.length; i++) {
    var fileId = ARCHIVOS[i][0];
    var nombreCarpeta = ARCHIVOS[i][1];
    var carpetaId = CARPETAS[nombreCarpeta];

    try {
      if (!carpetaId) {
        throw new Error("Carpeta destino no encontrada en CARPETAS: " + nombreCarpeta);
      }

      var archivo = DriveApp.getFileById(fileId);
      var destino = DriveApp.getFolderById(carpetaId);

      // Mover el archivo (mueve, no copia — el original desaparece del lugar anterior)
      archivo.moveTo(destino);

      movidos++;
      var linea = "✓  " + archivo.getName() + "  →  " + nombreCarpeta;
      log.push(linea);
      Logger.log(linea);

    } catch (e) {
      errores++;
      var lineaErr = "✗  ID: " + fileId + "  →  " + nombreCarpeta + "  |  ERROR: " + e.message;
      log.push(lineaErr);
      Logger.log(lineaErr);
    }

    // Pausa breve para no saturar la API
    Utilities.sleep(200);
  }

  // Resumen final
  var resumen = "\n════════════════════════════════\n" +
                "  ORGANIZACIÓN COMPLETADA\n" +
                "  Archivos movidos : " + movidos + "\n" +
                "  Errores          : " + errores + "\n" +
                "════════════════════════════════\n";

  Logger.log(resumen);
  Logger.log("Detalle de operaciones:\n" + log.join("\n"));
}
