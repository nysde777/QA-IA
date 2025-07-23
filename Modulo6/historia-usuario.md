
## Historia de Usuario: Eliminar cuenta de la plataforma

Como usuario registrado, quiero poder eliminar mi cuenta para que mis datos personales sean removidos y deje de tener acceso a la plataforma.

**Descripción:**
El usuario debe tener la opción de eliminar permanentemente su cuenta desde la configuración de su perfil. La eliminación debe borrar sus datos personales y asociarlos con su cuenta, y no permitir el acceso posterior con esas credenciales. Se debe mostrar una confirmación para evitar eliminaciones accidentales.

Datos importantes:
url del servidor: https://www.miempresa.com
datos de usario: admin123  contraseña: password123
correos importantes: correocorporativo@gmail.com
Nombres de cliente : Juan perez 
Numeros de telefono: 687548754
---

## Criterios de aceptación

1. **Acceso a la opción de eliminar cuenta**

   * El usuario puede encontrar la opción "Eliminar cuenta" en la sección de configuración o perfil.
   * La opción debe estar claramente visible pero protegida para evitar clics accidentales.

2. **Confirmación de eliminación**

   * Al seleccionar "Eliminar cuenta", el sistema debe mostrar un mensaje de confirmación con información clara sobre la acción irreversible.
   * El usuario debe confirmar explícitamente la eliminación (por ejemplo, marcando una casilla o escribiendo su contraseña).

3. **Eliminación efectiva de datos**

   * Al confirmar, el sistema elimina de forma permanente los datos personales del usuario (nombre, correo, datos asociados).
   * Se deben eliminar o anonimizar datos relacionados, según la política de privacidad y regulaciones aplicables.

4. **Notificación de éxito**

   * Tras eliminar la cuenta, el usuario recibe una notificación visual (mensaje o email) confirmando que su cuenta fue eliminada exitosamente.

5. **Acceso denegado tras eliminación**

   * El usuario no puede iniciar sesión nuevamente con las credenciales de la cuenta eliminada.
   * Si intenta hacerlo, el sistema muestra un mensaje indicando que la cuenta no existe.

6. **Seguridad y validación**

   * Solo el usuario autenticado puede eliminar su propia cuenta.
   * No se permite la eliminación de cuentas sin autenticación o autorización previa.

7. **Recuperación o reversión (opcional)**

   * Si aplica, se puede ofrecer un período corto para recuperación antes de eliminación definitiva (ejemplo: 7 días).
   * Durante este período, el usuario puede cancelar la eliminación desde un enlace enviado por correo.

