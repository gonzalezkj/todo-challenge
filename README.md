# INSTRUCCIONES

## Versiones utilizadas para este challenge:

Version de Python 3.9.13    

Version de Django 3.1.4  

## Librerias instaladas:
pip install djangorestframework==3.13.1    

pip install django-rest-auth==0.9.5    

pip install django-allauth==0.51.0  
 
pip install django-filter==22.1  


## Explicación de uso:

Primero es necesario registrarse, para ello se ingresa a la siguiente URL: http://127.0.0.1:8000/rest-auth/registration/
Al registrarse y loguearse será posible visualizar las tareas, publicarlas, modificarlas y eliminarlas.
Si no desea registrarse es posible utilizar el usuario 'Admin' con contraseña 'usuario1'.

Para visualizar todas las tareas creadas: http://127.0.0.1:8000/api/tarea/
Para eliminar o modificar una tarea es necesario identificar el ID y seleccionar el boton DELETE, por ejemplo: http://127.0.0.1:8000/api/tarea/1
Es posible filtrar tanto por ID, por contenido de la tarea y por fecha de creación.
