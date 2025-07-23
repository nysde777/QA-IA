
### Caso de Prueba 1: Inicio de sesión exitoso
- **Descripción**: Verificar que el usuario pueda iniciar sesión con credenciales válidas.
- **Precondiciones**: La página de inicio de sesión de https://www.saucedemo.com/ está accesible.
- **Datos de entrada**: 
  - Usuario: `standard_user`
  - Contraseña: `secret_sauce`
- **Pasos**:
  1. Navegar a la URL https://www.saucedemo.com/.
  2. Ingresar `standard_user` en el campo de usuario.
  3. Ingresar `secret_sauce` en el campo de contraseña.
  4. Hacer clic en el botón "Login".
- **Resultado esperado**: El usuario es redirigido a la página principal de la aplicación y ve el mensaje de bienvenida.

### Caso de Prueba 2: Inicio de sesión con usuario incorrecto
- **Descripción**: Verificar que el sistema no permita el inicio de sesión con un usuario incorrecto.
- **Precondiciones**: La página de inicio de sesión de https://www.saucedemo.com/ está accesible.
- **Datos de entrada**: 
  - Usuario: `wrong_user`
  - Contraseña: `secret_sauce`
- **Pasos**:
  1. Navegar a la URL https://www.saucedemo.com/.
  2. Ingresar `wrong_user` en el campo de usuario.
  3. Ingresar `secret_sauce` en el campo de contraseña.
  4. Hacer clic en el botón "Login".
- **Resultado esperado**: Se muestra un mensaje de error indicando que las credenciales son incorrectas.

### Caso de Prueba 3: Inicio de sesión con contraseña incorrecta
- **Descripción**: Verificar que el sistema no permita el inicio de sesión con una contraseña incorrecta.
- **Precondiciones**: La página de inicio de sesión de https://www.saucedemo.com/ está accesible.
- **Datos de entrada**: 
  - Usuario: `standard_user`
  - Contraseña: `wrong_password`
- **Pasos**:
  1. Navegar a la URL https://www.saucedemo.com/.
  2. Ingresar `standard_user` en el campo de usuario.
  3. Ingresar `wrong_password` en el campo de contraseña.
  4. Hacer clic en el botón "Login".
- **Resultado esperado**: Se muestra un mensaje de error indicando que las credenciales son incorrectas.

### Caso de Prueba 4: Campos de entrada vacíos
- **Descripción**: Verificar que el sistema no permita el inicio de sesión si los campos de usuario y contraseña están vacíos.
- **Precondiciones**: La página de inicio de sesión de https://www.saucedemo.com/ está accesible.
- **Pasos**:
  1. Navegar a la URL https://www.saucedemo.com/.
  2. Dejar el campo de usuario vacío.
  3. Dejar el campo de contraseña vacío.
  4. Hacer clic en el botón "Login".
- **Resultado esperado**: Se muestra un mensaje de error indicando que ambos campos son requeridos.

### Caso de Prueba 5: Mostrar los caracteres de la contraseña
- **Descripción**: Verificar que el usuario pueda ver u ocultar la contraseña al hacer clic en el icono de visibilidad.
- **Precondiciones**: La página de inicio de sesión de https://www.saucedemo.com/ está accesible.
- **Datos de entrada**: 
  - Usuario: `standard_user`
  - Contraseña: `secret_sauce`
- **Pasos**:
  1. Navegar a la URL https://www.saucedemo.com/.
  2. Ingresar `standard_user` en el campo de usuario.
  3. Ingresar `secret_sauce` en el campo de contraseña.
  4. Hacer clic en el icono de visibilidad de la contraseña.
- **Resultado esperado**: Los caracteres de la contraseña se muestran como texto plano.

### Caso de Prueba 6: Mantenimiento de sesión
- **Descripción**: Comprobar que el usuario permanezca conectado después de iniciar sesión correctamente.
- **Precondiciones**: El usuario ha iniciado sesión correctamente.
- **Pasos**:
  1. Navegar a la URL https://www.saucedemo.com/.
  2. Iniciar sesión con `standard_user` y `secret_sauce`.
  3. Navegar a otra página dentro de la aplicación (por ejemplo, la página de productos).
  4. Regresar a la página de inicio.
- **Resultado esperado**: El usuario sigue conectado sin necesidad de volver a iniciar sesión.

### Caso de Prueba 7: Mensaje de error genérico
- **Descripción**: Verificar que el sistema muestre un mensaje de error genérico si se produce un error inesperado al iniciar sesión.
- **Precondiciones**: La página de inicio de sesión de https://www.saucedemo.com/ está accesible.
- **Datos de entrada**: 
  - Usuario: `standard_user`
  - Contraseña: `secret_sauce` (con un error forzado en el backend)
- **Pasos**:
  1. Navegar a la URL https://www.saucedemo.com/.
  2. Ingresar `standard_user` en el campo de usuario.
  3. Ingresar `secret_sauce` en el campo de contraseña.
  4. Forzar una condición de error en el backend.
  5. Hacer clic en el botón "Login".
- **Resultado esperado**: Se muestra un mensaje de error genérico "Ha ocurrido un error, por favor intenta de nuevo más tarde."

