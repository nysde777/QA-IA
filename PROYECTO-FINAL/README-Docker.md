# Jenkins + Cypress Docker Setup

Este setup permite ejecutar pruebas de Cypress automatizadas usando Jenkins en un contenedor Docker.

## Archivos incluidos:

- `Dockerfile`: Imagen personalizada con Jenkins y dependencias de Cypress
- `docker-compose.yml`: Configuración para levantar el servicio
- `plugins.txt`: Lista de plugins de Jenkins necesarios
- `Jenkinsfile`: Pipeline para ejecutar las pruebas automáticamente

## Instrucciones de uso:

### 1. Construir y ejecutar el contenedor:

```bash
# Construir la imagen
docker-compose build

# Ejecutar el contenedor
docker-compose up -d
```

### 2. Acceder a Jenkins:

- Abrir navegador en: http://localhost:8080
- La primera vez necesitarás la contraseña inicial:

```bash
# Obtener la contraseña inicial de Jenkins
docker exec jenkins-cypress-container cat /var/jenkins_home/secrets/initialAdminPassword
```

### 3. Configurar Jenkins:

1. Instalar plugins sugeridos
2. Crear usuario administrador
3. Ir a "Manage Jenkins" > "Global Tool Configuration"
4. Configurar Node.js:
   - Nombre: `NodeJS`
   - Instalar automáticamente: Sí
   - Versión: NodeJS 18.x

### 4. Crear un Job de Pipeline:

1. Nueva tarea > Pipeline
2. En "Pipeline", seleccionar "Pipeline script from SCM" o copiar el contenido del `Jenkinsfile`
3. Guardar y ejecutar

### 5. Comandos útiles:

```bash
# Ver logs del contenedor
docker-compose logs -f

# Entrar al contenedor
docker exec -it jenkins-cypress-container bash

# Parar el contenedor
docker-compose down

# Limpiar todo (incluyendo volúmenes)
docker-compose down -v
```

## Características:

- ✅ Jenkins LTS con Node.js 18
- ✅ Todas las dependencias de Cypress instaladas
- ✅ Pipeline automatizado
- ✅ Captura de screenshots y videos
- ✅ Reportes HTML
- ✅ Persistencia de datos de Jenkins
- ✅ Cache de Cypress optimizado

## Estructura del Pipeline:

1. **Checkout**: Obtiene el código fuente
2. **Install Dependencies**: Instala dependencias npm
3. **Verify Cypress**: Verifica la instalación de Cypress
4. **Run Tests**: Ejecuta las pruebas en modo headless
5. **Post**: Archiva resultados y genera reportes
