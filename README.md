# Proyecto

Este proyecto es un ejemplo de aplicación Django que descarga imágenes de una API y las almacena localmente. También incluye tests unitarios para verificar la funcionalidad del proyecto. Se decidió usar este framework ya que ofrece una estructura organizada desde su inicialización, además de un ORM que permite la facil gestión de una base de datos sqlite.

# Pasos para ejecución del proyecto
1. **Clonar el Repositorio**
  git clone https://github.com/sebastianfon945/MO_project.git

3. **Se recomienda crear y Activar el Entorno Virtual**
  python -m venv venv
  source venv/bin/activate  # En Windows: venv\Scripts\activate
4. **Instalar las Dependencias**
  pip install -r requirements.txt

5. **Aplicar Migraciones**
  python manage.py makemigrations
  python manage.py migrate

6. **Ejecutar Tests**
   Se definieron los siguientes test unitarios para las diferentes funciones que ejecutar alguna tarea específica para la descarga de imagenes del API 'https://dog.ceo/api/breeds/image/random'
   - test_add_image:
     
      Descripción: Esta función de prueba verifica que un objeto Image se puede agregar correctamente a la base de datos.
      Responsabilidades:
     
      Crear una instancia de un objeto Image con datos de prueba.
      Guardar la instancia en la base de datos.
      Verificar que la instancia se ha guardado correctamente y que los datos almacenados coinciden con los datos de prueba.
     
   - test_download_image
     Descripción: Esta función de prueba verifica que la función download_image descarga correctamente una imagen desde una URL y la guarda en el sistema de archivos.

    Responsabilidades:
    Simular una URL de imagen y datos de imagen.
    Llamar a la función download_image con los datos de imagen simulados y el nombre del archivo.
    Verificar que el archivo se ha descargado y guardado correctamente en el sistema de archivos.

   - test_download_image_thread
  
     Descripción: Esta función de prueba verifica que la función download_image_thread descarga múltiples imágenes concurrentemente usando multithreading.

    Responsabilidades:
    
    Simular una URL de API que devuelve datos de imágenes.
    Llamar a la función download_image_thread con la URL de la API, la ruta de almacenamiento y el número de descargas.
    Verificar que el número correcto de imágenes se ha descargado y guardado en el sistema de archivos.

   - test_start_download
  
     Descripción: Esta función de prueba verifica que la vista start_download funciona correctamente, incluyendo la descarga de imágenes y la generación de la respuesta adecuada.

    Responsabilidades:
    
    Simular una solicitud GET a la vista start_download.
    Mockear la función download_image_thread para controlar su comportamiento durante la prueba.
    Verificar que la vista devuelve una respuesta JSON con la lista de imágenes descargadas y el tiempo de ejecución.

   -Ejecución de tests: 
   La ejecución de los test o alguno en específico se puede hacer con el comando: pytest get_images/tests.py -x -k test_get_image_url
