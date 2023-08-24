const ID_BBDD = '1gCRP2HDD-NXm0rUZNrbegVJSYy7i5x-MJ57wuYhs0yI'


/**
 * Se comprueba si el asesor ya tiene casos asigandos sin revisar
 * Si no, se asigna un caso de la base a nueva a las gestiones
 * Se retorna fila del nuevo caso
 */
const asignarCaso = (user = 'jcgomezb') => {
  let sheetCarga = SpreadsheetApp.openById(ID_BBDD).getSheetByName('DataCarga')
  let dataSheet = SpreadsheetApp.openById(ID_BBDD).getSheetByName('BBDD')
  let dataBase = dataSheet.getDataRange().getValues()
  dataBase.shift()
  dataBase.shift()

  let fila = getSinRevision(user)
  if (fila) {
    return fila
  } else {
    if (sheetCarga.getLastRow() != 1) {
      var lock = LockService.getScriptLock();

      lock.waitLock(10000);
      let nuevo = sheetCarga.getRange(sheetCarga.getLastRow(), 1, 1, sheetCarga.getLastColumn()).getValues()[0]


      if (nuevo) {
        sheetCarga.deleteRow(sheetCarga.getLastRow())
        nuevo.push(user)
        nuevo.push("")
        nuevo.push("Sin revisar")
        nuevo.push("[]")
        nuevo.push("")
        dataSheet.appendRow(nuevo)
        SpreadsheetApp.flush()
        lock.releaseLock();
        return dataSheet.getLastRow()
      }
    } else {
      throw "No hay casos a asignar"
    }
  }
}

/**
 * Se obtienen datos ya cargados en BBDD
 * Se comprueba si el asesor ya tiene casos asigandos sin revisar
 * Se retorna fila
 */
const getSinRevision = (user = 'jcgomezb') => {
  let sheetBase = SpreadsheetApp.openById(ID_BBDD).getSheetByName('BBDD')
  let data = sheetBase.getDataRange().getValues()
  data.shift()
  data.shift()
  var fila = ""
  data.forEach((el, index) => {
    if (el[7] == user && el[9] === "Sin revisar") {
      fila = index + 3
    }
  })
  return fila
}

// Funcion para buscar el id de tarea en la lista de tareas pendientes

const buscarTarea = (id = 'INF_5622843',user='jacanon') => {
  let sheetCarga = SpreadsheetApp.openById(ID_BBDD).getSheetByName('DataCarga')
  let dataSheet = SpreadsheetApp.openById(ID_BBDD).getSheetByName('BBDD')
  let data = sheetCarga.getRange(1, 4, sheetCarga.getLastRow(), 1).getValues()

  let index = data.findIndex((el) => el[0] == id)

  if (index < 0) throw new Error('No se encontró la tarea')


  let nuevo = sheetCarga.getRange(index + 1, 1, 1, sheetCarga.getLastColumn()).getValues()[0]

  var lock = LockService.getScriptLock();

  lock.waitLock(10000);

  sheetCarga.deleteRow(index+1)

  if (nuevo) {
    nuevo.push(user)
    nuevo.push("")
    nuevo.push("Sin revisar")
    nuevo.push("[]")
    nuevo.push("")
   
    dataSheet.appendRow(nuevo)
    SpreadsheetApp.flush()
    let nuevoIndex=dataSheet.getLastRow()
    lock.releaseLock()
    return nuevoIndex
  }

}



/**
 * Se retorna caso de la fila enviada
 */
const getDataById = (fila) => {
  let sheet = SpreadsheetApp.openById(ID_BBDD).getSheetByName('BBDD')
  let data = sheet.getRange(fila, 1, 1, sheet.getLastColumn()).getValues() //sheet.getDataRange().getValues()
  let tipos = sheet.getRange(1, 1, 1, sheet.getLastColumn()).getValues()[0]
  let encabezado = sheet.getRange(2, 1, 1, sheet.getLastColumn()).getValues()[0]
  let objeto = {}
  data.forEach((el, index) => {

    el.forEach((item, i) => {
      if (tipos[i] == 'date') {
        objeto[encabezado[i]] = new Date(item)
      } else {
        if (tipos[i] == 'json') {
          objeto[encabezado[i]] = JSON.parse(item)

        } else {
          objeto[encabezado[i]] = item
        }
      }
    })

  })

  console.log(objeto)

  return JSON.stringify(objeto)
}

const getData = (user, filtros = { ff: "2022-11-23" }) => {

  let sheet = SpreadsheetApp.openById(ID_BBDD).getSheetByName('BBDD')
  let data = sheet.getDataRange().getValues()

  const lista = convertToObject(data, user, filtros)
  return lista
}

const convertToObject = (data, user, filtros) => {
  let perfil = usrProff(user)

  let list_data = []
  let tipos = data.shift()
  let encabezado = data.shift()
  data.forEach((el, index) => {
    console.log(new Date(`${filtros.ff} `))
    console.log(new Date(el[0]))
    if (((el[7] == user) || (perfil == 'Supervisor')) && (((new Date(el[0]).getTime() >= new Date(`${filtros.ff} `).getTime() && new Date(el[0]).getTime() <= new Date(`${filtros.ff} 23:59:59`).getTime()) || filtros.ff === '') && ((el[3] == filtros.id) || (filtros.id == '')) && ((el[5] == filtros.error) || (filtros.error == 'Todo')) && ((el[9] == filtros.estado) || (filtros.estado == 'Todo')))) {
      objeto = {}
      objeto['fila'] = index + 3
      el.forEach((item, i) => {

        if (tipos[i] == 'fecha') {
          objeto[encabezado[i]] = item ? new Date(item) : ""
        } else {
          if (tipos[i] == 'json') {
            objeto[encabezado[i]] = JSON.parse(item)

          } else {
            objeto[encabezado[i]] = item
          }
        }
      })
      list_data.push(objeto)
    }
  })
  return JSON.stringify(list_data)
}


const updateStateI = (fila, data, inicial) => {
  let sheet = SpreadsheetApp.openById(ID_BBDD).getSheetByName('BBDD')
  let datax = sheet.getRange(fila, 1, 1, sheet.getLastColumn()).getValues()[0] //sheet.getDataRange().getValues()
  let fechaActual = new Date()
  obj = { 'fecha': fechaActual, 'usr': data.usuario, 'errI': datax[8] ? datax[8] : datax[5], 'errF': data.error, 'obs': data.observacion }
  let dataobs = JSON.parse(datax[10])
  dataobs.push(obj)

  datax[8] = data.error
  datax[9] = data.estado
  datax[10] = JSON.stringify(dataobs)
  datax[11] = inicial ? data.opc : datax[11]
  datax[12] = inicial ? data.donante : datax[12]
  datax[13] = inicial ? data.linea : datax[13]
  datax[14] = inicial ? data.usecreador : datax[14]
  datax[15] = inicial ? data.motivoFinal : datax[15]
  datax[16] = inicial ? data.erroresOSS : datax[16]
  datax[17] = inicial ? data.casoEscalado : datax[17]
  datax[18] = inicial ? data.billing_Id : datax[18]
  datax[19] = fechaActual.toLocaleString('en-US')

  sheet.getRange(fila, 1, 1, datax.length).setValues([datax])
}


const contarFaltantes = () => {
  let sheet = SpreadsheetApp.openById(ID_BBDD).getSheetByName('DataCarga')
  let data = sheet.getDataRange().getValues()
  data.shift()
  data.shift()

  let sheetx = SpreadsheetApp.openById(ID_BBDD).getSheetByName('BBDD')
  let datax = sheetx.getDataRange().getValues()

  let dxt = datax.filter((el, i) =>
    el[9] == 'Sin revisar'
  )
  return data.length + dxt.length
}



function subirCasos() {
  let lock = LockService.getScriptLock()
  lock.tryLock(10000)
  if (lock.hasLock()) {
    return subirCasos_()
  } else {
    throw ("Tiempo de espera agotado")
  }
}

function subirCasos_() {
  let cargue = SpreadsheetApp.openById("1IVpGKIHtnLnL4D-VKSFSGIoZmeiId4BVz3j6TlBplLQ").getSheetByName("cargue")
  let nuevos = cargue.getDataRange().getValues()
  let bbdd = SpreadsheetApp.openById(ID_BBDD).getSheetByName("DataCarga")
  let ordenes = bbdd.getDataRange().getValues()
  let casos = []
  nuevos.shift()


  if (nuevos.length < 1) {
    throw ("El archivo de carga de òrdenes está vacio.")
  } else {
    if (nuevos[0].length !== 8) {
      throw ("El formato del archivo de carga de órdenes es incorrecto, reviselo e intente de nuevo.")
    }
  }

  nuevos.forEach((el) => {
    let x = ordenes.filter((item) => el[3] === item[3] && el[7] === item[6])
    if (x.length <= 0) {
      el.splice(6, 1)
      casos.push(el)
    }
  })

  cargue.clear()
  if (casos.length > 0) {
    bbdd.getRange(bbdd.getLastRow() + 1, 1, casos.length, casos[0].length).setValues(casos)
    return 'Se cargaron: ' + casos.length + ' casos'
  } else {
    throw ("No hay casos nuevos por subir")
  }
}

function usrProff(usr) {
  let bbdd = SpreadsheetApp.openById(ID_BBDD).getSheetByName("USERS")
  let users = bbdd.getDataRange().getValues()

  let user = users.filter((el) => el[0] === usr)[0]
  console.log(user, usr)
  return user[1]
}



