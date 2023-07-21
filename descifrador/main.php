<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles/index.css">
    <title>Verificar Archivo</title>
</head>
<body>
    <h1>Añade tu archivo</h1>
    <form class="submit" action="" method="post" enctype="multipart/form-data">
        <input class="file" type="file" name="archivo" id="archivo" value="Seleccionar Archivo">
        <input class="submit" type="submit" name="submit" value="Subir Archivo">
    </form>

    <?php
    function verificarArchivoSinExtension($ruta, $nombreArchivo)
    {
        $nombreCortado = substr($nombreArchivo, 0, -4);
        $archivoSinExtension = $ruta . DIRECTORY_SEPARATOR . $nombreCortado;
        return file_exists($archivoSinExtension);
    }

    if (isset($_FILES['archivo'])) {
        $nombreArchivo = $_FILES['archivo']['name'];
        $rutaArchivo = $_FILES['archivo']['tmp_name'];

        // Carpeta donde se guardarán los archivos
        $carpetaDestino = 'ruta/donde/guardar';

        // Movemos el archivo subido a la carpeta destino
        move_uploaded_file($rutaArchivo, $carpetaDestino . DIRECTORY_SEPARATOR . $nombreArchivo);

        // Mostramos la ruta del archivo seleccionado
        echo '<p>Ruta del archivo seleccionado: ' . $carpetaDestino . DIRECTORY_SEPARATOR . $nombreArchivo . '</p>';

        // Verificamos si existe el archivo sin extensión
        $resultado = verificarArchivoSinExtension($carpetaDestino, $nombreArchivo);

        if ($resultado) {
            echo '<p>El archivo sin extensión existe en la misma ruta.</p>';
        } else {
            echo '<p>El archivo sin extensión NO existe en la misma ruta.</p>';
        }
    }
    ?>

    <!-- <form class="carpeta" action="ruta/carpeta/archivos/windows" method="post">
        <input type="submit" name="carpeta_windows" value="Ir a la carpeta de archivos de Windows">
    </form> -->
</body>
</html>