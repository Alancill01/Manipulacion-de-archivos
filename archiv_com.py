import zipfile
def comprimir_archivos(nombre_archivo_zip, archivos_a_comprimir):
    with zipfile.ZipFile(nombre_archivo_zip, 'w') as archivo_zip:
        for archivo in archivos_a_comprimir:
            archivo_zip.write(archivo)
comprimir_archivos('sample.zip', ['sample.xlsx'])