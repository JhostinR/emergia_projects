<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Eliminar Extension</title>
    <link rel="stylesheet" href="styles/index.css">
</head>
<body>
    <div>
        <h1>Descifrador</h1>
        <form action="" method="post" enctype="multipart/form-data">
            <input type="file" name="archivo" id="archivo">
            <input class="submit" type="submit" value="verificar" name="submit">
        </form>
    </div>
    <?php
    if (isset($_POST['submit']))
        // Verificar si se ha seleccionado un archivo
        if (!isset($_FILES['archivo']) || $_FILES['archivo']['error'] == UPLOAD_ERR_NO_FILE) {
            echo "<p>¡Por favor, selecciona un archivo primero!</p>";
        } else {
            // Obtener el nombre del archivo seleccionado
            $nombreArchivo = $_FILES['archivo']['name'];
            $nombreTempArchivo = $_FILES['archivo']['tmp_name'];

        // Ruta donde se encuentra el archivo original
        $directorioOrigen = dirname(realpath($nombreTempArchivo)) . '/';

        // Quitar la extensión .pgp del nombre del archivo
        $nombreSinExtension = substr($nombreArchivo, 0, -4);

        // Ruta donde se guardará el archivo sin la extensión .pgp
        $rutaDestino = $directorioOrigen . $nombreSinExtension;

        // Mover el archivo a la ubicación deseada
        if (file_exists($rutaDestino)) {
            echo "<p>El archivo sin extensión ya existe en la ruta: $rutaDestino</p>";
            // Aquí se pueden agregar otras acciones si el archivo ya existe
        } else {
            // Mover el archivo a la ubicación deseada
            if (move_uploaded_file($nombreTempArchivo, $rutaDestino)) {
                echo "<p>El archivo se ha guardado correctamente en la ruta: $rutaDestino</p>";
            } else {
                echo "<p>Error al guardar el archivo.</p>";
            }
        }
    }
    ?>
</body>
</html>