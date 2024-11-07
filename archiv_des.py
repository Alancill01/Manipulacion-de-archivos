import zipfile
def extraer_archivos(nombre_archivo_zip, directorio_destino):
    with zipfile.ZipFile(nombre_archivo_zip, 'r') as archivo_zip:
        archivo_zip.extractall(directorio_destino)
extraer_archivos('sample.zip', 'sample2')
