# Casos de Prueba - Eliminar Cuenta de la Plataforma

**Historia de Usuario:** Como usuario registrado, quiero poder eliminar mi cuenta para que mis datos personales sean removidos y deje de tener acceso a la plataforma.

**Fecha de creación:** 22 de julio de 2025

---

## CP001 - Verificar acceso a la opción "Eliminar cuenta"

**Descripción:** Verificar que un usuario autenticado puede acceder a la opción "Eliminar cuenta" desde la configuración del perfil.

**Precondiciones:**
- Usuario registrado y autenticado en la plataforma
- El usuario tiene una cuenta activa

**Pasos a ejecutar:**
1. Iniciar sesión con credenciales válidas
2. Navegar a la sección de "Configuración" o "Perfil"
3. Buscar la opción "Eliminar cuenta"

**Resultado esperado:**
- La opción "Eliminar cuenta" debe estar visible en la sección de configuración
- La opción debe estar claramente identificada pero ubicada de manera que evite clics accidentales

**Criterio de aceptación relacionado:** 1

---

## CP002 - Verificar mensaje de confirmación al eliminar cuenta

**Descripción:** Verificar que al seleccionar "Eliminar cuenta" se muestra un mensaje de confirmación apropiado.

**Precondiciones:**
- Usuario autenticado en la plataforma
- Acceso a la opción "Eliminar cuenta"

**Pasos a ejecutar:**
1. Navegar a la configuración del perfil
2. Hacer clic en la opción "Eliminar cuenta"
3. Observar el mensaje de confirmación mostrado

**Resultado esperado:**
- Se debe mostrar un mensaje de confirmación claro
- El mensaje debe indicar que la acción es irreversible
- Debe incluir información sobre las consecuencias de la eliminación
- Debe presentar opciones para confirmar o cancelar la acción

**Criterio de aceptación relacionado:** 2

---

## CP003 - Confirmar eliminación con verificación de contraseña

**Descripción:** Verificar que el usuario puede confirmar la eliminación proporcionando su contraseña.

**Precondiciones:**
- Usuario autenticado
- Mensaje de confirmación de eliminación visible

**Pasos a ejecutar:**
1. En el diálogo de confirmación, ingresar la contraseña actual del usuario
2. Hacer clic en "Confirmar eliminación"
3. Observar el comportamiento del sistema

**Resultado esperado:**
- El sistema acepta la contraseña válida
- Procede con la eliminación de la cuenta
- Muestra confirmación del proceso

**Criterio de aceptación relacionado:** 2

---

## CP004 - Verificar eliminación efectiva de datos personales

**Descripción:** Verificar que los datos personales del usuario son eliminados completamente del sistema.

**Precondiciones:**
- Cuenta de usuario con datos personales (nombre, email, información de perfil)
- Proceso de eliminación completado

**Pasos a ejecutar:**
1. Completar el proceso de eliminación de cuenta
2. Verificar en la base de datos que los datos personales fueron eliminados
3. Confirmar que no existen registros identificables del usuario

**Resultado esperado:**
- Los datos personales del usuario deben ser eliminados permanentemente
- No debe quedar información identificable en el sistema
- Los datos relacionados deben ser anonimizados según las políticas

**Criterio de aceptación relacionado:** 3

---

## CP005 - Verificar notificación de éxito tras eliminación

**Descripción:** Verificar que el usuario recibe una notificación confirmando la eliminación exitosa.

**Precondiciones:**
- Proceso de eliminación de cuenta completado

**Pasos a ejecutar:**
1. Completar el proceso de eliminación
2. Observar las notificaciones en pantalla
3. Verificar el envío de notificación por email (si aplica)

**Resultado esperado:**
- Se muestra un mensaje visual confirmando la eliminación exitosa
- Se envía un email de confirmación al correo del usuario (si configurado)
- Las notificaciones contienen información clara sobre la acción completada

**Criterio de aceptación relacionado:** 4

---

## CP006 - Verificar acceso denegado tras eliminación

**Descripción:** Verificar que no es posible iniciar sesión con credenciales de una cuenta eliminada.

**Precondiciones:**
- Cuenta de usuario previamente eliminada
- Credenciales de la cuenta eliminada

**Pasos a ejecutar:**
1. Intentar iniciar sesión con el email/usuario de la cuenta eliminada
2. Ingresar la contraseña que tenía la cuenta
3. Hacer clic en "Iniciar sesión"

**Resultado esperado:**
- El sistema debe denegar el acceso
- Se debe mostrar un mensaje indicando que la cuenta no existe
- No se debe permitir el acceso a la plataforma

**Criterio de aceptación relacionado:** 5

---

## CP007 - Verificar mensaje específico para cuenta inexistente

**Descripción:** Verificar que se muestra un mensaje apropiado al intentar acceder con credenciales de cuenta eliminada.

**Precondiciones:**
- Cuenta eliminada previamente
- Pantalla de inicio de sesión

**Pasos a ejecutar:**
1. Intentar iniciar sesión con credenciales de cuenta eliminada
2. Observar el mensaje de error mostrado

**Resultado esperado:**
- El mensaje debe indicar claramente que la cuenta no existe
- No debe revelar información sensible sobre la eliminación
- Debe ser un mensaje user-friendly pero seguro

**Criterio de aceptación relacionado:** 5

---

## CP008 - Verificar que solo el usuario autenticado puede eliminar su cuenta

**Descripción:** Verificar que solo el propietario de la cuenta puede eliminarla.

**Precondiciones:**
- Usuario A autenticado
- Existencia de Usuario B con cuenta diferente

**Pasos a ejecutar:**
1. Iniciar sesión como Usuario A
2. Intentar acceder a funciones de eliminación de cuenta de Usuario B
3. Verificar restricciones de seguridad

**Resultado esperado:**
- El Usuario A solo puede eliminar su propia cuenta
- No tiene acceso a funciones de eliminación de otras cuentas
- El sistema mantiene la segregación de permisos

**Criterio de aceptación relacionado:** 6

---

## CP009 - Verificar que no se permite eliminación sin autenticación

**Descripción:** Verificar que no es posible eliminar cuentas sin estar autenticado.

**Precondiciones:**
- Usuario no autenticado (sesión cerrada)

**Pasos a ejecutar:**
1. Acceder a la plataforma sin iniciar sesión
2. Intentar navegar directamente a URLs de eliminación de cuenta
3. Verificar las restricciones de acceso

**Resultado esperado:**
- No se debe permitir acceso a funciones de eliminación sin autenticación
- El sistema debe redirigir a la página de inicio de sesión
- Se deben aplicar controles de seguridad apropiados

**Criterio de aceptación relacionado:** 6

---

## CP010 - Verificar período de recuperación (7 días)

**Descripción:** Verificar que existe un período de gracia de 7 días para recuperar la cuenta eliminada.

**Precondiciones:**
- Función de período de recuperación habilitada
- Cuenta recién eliminada

**Pasos a ejecutar:**
1. Eliminar una cuenta de usuario
2. Verificar que se active el período de recuperación de 7 días
3. Confirmar que la cuenta está en estado "pendiente de eliminación"

**Resultado esperado:**
- La cuenta debe quedar en estado "pendiente de eliminación" por 7 días
- Los datos no deben ser eliminados inmediatamente
- Debe existir posibilidad de recuperación durante este período

**Criterio de aceptación relacionado:** 7

---

## CP011 - Verificar cancelación de eliminación durante período de recuperación

**Descripción:** Verificar que el usuario puede cancelar la eliminación durante el período de gracia.

**Precondiciones:**
- Cuenta en período de recuperación (menos de 7 días desde eliminación)
- Enlace de recuperación válido

**Pasos a ejecutar:**
1. Acceder al enlace de recuperación enviado por email
2. Confirmar la cancelación de eliminación
3. Verificar que la cuenta se restaura completamente

**Resultado esperado:**
- La cuenta debe ser restaurada a su estado original
- Todos los datos deben estar disponibles nuevamente
- El usuario debe poder iniciar sesión normalmente

**Criterio de aceptación relacionado:** 7

---

## CP012 - Verificar eliminación definitiva después de 7 días

**Descripción:** Verificar que la cuenta se elimina definitivamente después del período de gracia.

**Precondiciones:**
- Cuenta en período de recuperación
- Han transcurrido más de 7 días desde la eliminación inicial

**Pasos a ejecutar:**
1. Esperar que transcurra el período de 7 días
2. Verificar que los datos son eliminados permanentemente
3. Confirmar que no es posible la recuperación

**Resultado esperado:**
- Los datos deben ser eliminados permanentemente después de 7 días
- No debe ser posible recuperar la cuenta
- Todos los enlaces de recuperación deben quedar inválidos

**Criterio de aceptación relacionado:** 7

---

## CP013 - Verificar rechazo de confirmación con contraseña incorrecta

**Descripción:** Verificar que no se puede eliminar la cuenta con una contraseña incorrecta.

**Precondiciones:**
- Usuario autenticado
- Diálogo de confirmación de eliminación visible

**Pasos a ejecutar:**
1. En el diálogo de confirmación, ingresar una contraseña incorrecta
2. Intentar confirmar la eliminación
3. Observar el comportamiento del sistema

**Resultado esperado:**
- El sistema debe rechazar la contraseña incorrecta
- Se debe mostrar un mensaje de error apropiado
- La cuenta no debe ser eliminada
- Debe permanecer en el diálogo de confirmación

**Criterio de aceptación relacionado:** 2, 6

---

## CP014 - Verificar cancelación del proceso de eliminación

**Descripción:** Verificar que el usuario puede cancelar el proceso de eliminación antes de confirmarlo.

**Precondiciones:**
- Usuario autenticado
- Diálogo de confirmación de eliminación visible

**Pasos a ejecutar:**
1. Acceder al diálogo de eliminación de cuenta
2. Hacer clic en "Cancelar" o botón equivalente
3. Verificar que regresa a la configuración sin eliminar la cuenta

**Resultado esperado:**
- El proceso de eliminación debe cancelarse
- La cuenta debe permanecer activa
- El usuario debe regresar a la configuración del perfil
- No debe haber cambios en los datos de la cuenta

**Criterio de aceptación relacionado:** 2

---

## Matriz de Trazabilidad

| Caso de Prueba | Criterio de Aceptación | Prioridad | Estado |
|-----------------|------------------------|-----------|---------|
| CP001 | 1 | Alta | Pendiente |
| CP002 | 2 | Alta | Pendiente |
| CP003 | 2 | Alta | Pendiente |
| CP004 | 3 | Crítica | Pendiente |
| CP005 | 4 | Media | Pendiente |
| CP006 | 5 | Alta | Pendiente |
| CP007 | 5 | Alta | Pendiente |
| CP008 | 6 | Crítica | Pendiente |
| CP009 | 6 | Crítica | Pendiente |
| CP010 | 7 | Media | Pendiente |
| CP011 | 7 | Media | Pendiente |
| CP012 | 7 | Media | Pendiente |
| CP013 | 2, 6 | Alta | Pendiente |
| CP014 | 2 | Media | Pendiente |

---

## Notas Adicionales

- **Prioridad Crítica:** Casos relacionados con seguridad y protección de datos
- **Prioridad Alta:** Casos de funcionalidad principal
- **Prioridad Media:** Casos de funcionalidad opcional o complementaria

**Ambiente de pruebas sugerido:**
- Entorno de testing con base de datos aislada
- Configuración de emails para verificar notificaciones
- Permisos de administrador para verificar eliminación de datos

**Datos de prueba requeridos:**
- Múltiples cuentas de usuario de prueba
- Configuración de servidor de correo para testing
- Acceso a base de datos para verificación de eliminación
