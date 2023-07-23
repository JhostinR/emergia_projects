<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles/styles.css">
    <title>Verificar Archivo</title>
    <link rel="stylesheet" href="styles/styles.css">
</head>
<body>
    <h1>AÑADE TU ARCHIVO</h1>
    <form action="" method="post" enctype="multipart/form-data">
        <!-- Botón para seleccionar el archivo -->
        <input type="file" name="archivo" id="archivo">
        <input class="submit" type="submit" value="Subir archivo" name="submit">
    </form>

    <?php
    if (isset($_POST['submit'])) {
        // Obtener el nombre del archivo seleccionado
        $nombreArchivo = $_FILES['archivo']['name'];
        $nombreTempArchivo = $_FILES['archivo']['tmp_name'];

        // Ruta donde se guardará el archivo (directorio absoluto)
        $directorioDestino = __DIR__ . '/';

        // Mover el archivo a la ubicación deseada (no necesario para este caso)
        // move_uploaded_file($nombreTempArchivo, $directorioDestino . $nombreArchivo);

        // Quitar la extensión .pgp del nombre del archivo
        $nombreCortado = substr($nombreArchivo, 0, -4);

        // Renombrar el archivo sin la extensión .pgp
        $nuevoNombreArchivo = $directorioDestino . $nombreCortado;

        if (rename($nombreTempArchivo, $nuevoNombreArchivo)) {
            echo "<p>El archivo se ha subido y renombrado correctamente.</p>";

            // Verificar si el archivo cortado existe en la misma ruta
            if (file_exists($nuevoNombreArchivo)) {
                echo "<p>El archivo sin extensión .pgp existe en la misma ruta.</p>";
            } else {
                echo "<p>El archivo sin extensión .pgp no existe en la misma ruta.</p>";
            }
        } else {
            echo "<p>Error al subir y renombrar el archivo.</p>";
        }
    }
    ?>
</body>
</html>