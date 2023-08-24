const tiposLogs = {
  inicio: 'Nuevo email',  
  seguimiento: 'Seguimiento'  
}

function doGet(e) {

  let template = HtmlService.createTemplateFromFile("index")
  return template.evaluate().setTitle("Adamo Gestion BO")
    //.setSandboxMode(HtmlService.SandboxMode.IFRAME).setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);

}


function include(fileName) {
  return HtmlService.createHtmlOutputFromFile(fileName).getContent()
}

