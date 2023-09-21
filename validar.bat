@echo off
setlocal enabledelayedexpansion

set /p "selected_folder_path=Ingrese la ruta de la carpeta seleccionada: "
set /p "output_csv_path=Ingrese la ruta de guardado del archivo CSV: "

(for /r "%selected_folder_path%" %%i in (*) do (
    set "folder=%%~dpi"
    set "folder=!folder:%selected_folder_path%=!"
    echo !folder:~0,-1!;%%~nxi
)) > "%output_csv_path%"

echo Se ha creado el archivo CSV con las carpetas y archivos.

endlocal  