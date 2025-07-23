import re
import os

def anonimizar_texto(texto: str) -> str:
    """
    Reemplaza datos sensibles en el texto por etiquetas genéricas para proteger la privacidad.
    
    Datos que anonimiza:
    - Emails
    - URLs
    - Nombres propios (simple detección con mayúsculas y contexto)
    - Nombres de usuario (ej. usuario123)
    - Números de teléfono o identificadores numéricos
    """
    
    # Reemplazar emails
    texto = re.sub(r'\b[\w.-]+@[\w.-]+\.\w{2,}\b', '[EMAIL]', texto)
    
    # Reemplazar URLs (http, https, www)
    texto = re.sub(r'\bhttps?://[^\s]+', '[URL]', texto)
    texto = re.sub(r'\bwww\.[^\s]+', '[URL]', texto)
    
    # Reemplazar nombres de usuario (palabras con combinación de letras y números, ejemplo: usuario123, user_01)
    texto = re.sub(r'\b[a-zA-Z0-9_]{3,15}\b', lambda m: '[USUARIO]' if re.search(r'\d', m.group()) else m.group(), texto)
    
    # Reemplazar números de teléfono o IDs (secuencias numéricas de 5 o más dígitos)
    texto = re.sub(r'\b\d{5,}\b', '[ID_NUM]', texto)
    
    # Reemplazar nombres propios simples (palabras que empiezan con mayúscula y no están al inicio de oración)
    # Esto es una heurística simple y puede necesitar ajustes según el contexto
    def reemplazar_nombre(match):
        palabra = match.group()
        # Excluir palabras comunes con mayúscula inicial que no sean nombres propios
        no_nombres = {'El', 'La', 'Como', 'En', 'De', 'Para', 'Los', 'Las', 'Y', 'O', 'Si', 'Al', 
                     'Con', 'Por', 'Sin', 'Tras', 'Historia', 'Usuario', 'Descripción', 'Criterios',
                     'Acceso', 'Confirmación', 'Eliminación', 'Notificación', 'Seguridad', 'Recuperación',
                     'Eliminar', 'Datos', 'Cuenta', 'Sistema', 'Mensaje', 'Email', 'Correo', 'Período',
                     'Durante', 'Desde', 'Antes', 'Después', 'Entonces', 'También', 'Solo', 'Ejemplo',
                     'Período', 'Días', 'Enlace', 'Enviado', 'Política', 'Privacidad', 'Regulaciones',
                     'Aplicables', 'Visual', 'Exitosamente', 'Nuevamente', 'Credenciales', 'Indica',
                     'Existe', 'Autenticado', 'Autenticación', 'Autorización', 'Previa', 'Aplica',
                     'Ofrecer', 'Corto', 'Definitiva', 'Este', 'Puede', 'Cancelar'}
        if palabra in no_nombres:
            return palabra
        else:
            return '[NOMBRE]'
    
    texto = re.sub(r'\b[A-Z][a-z]{2,}\b', reemplazar_nombre, texto)
    
    return texto

def generar_historia_anonima(archivo_entrada: str, archivo_salida: str = None):
    """
    Lee un archivo de historia de usuario y genera una versión anonimizada.
    
    Args:
        archivo_entrada (str): Ruta del archivo original de historia de usuario
        archivo_salida (str): Ruta del archivo de salida (opcional)
    """
    
    # Definir archivo de salida si no se proporciona
    if archivo_salida is None:
        directorio = os.path.dirname(archivo_entrada)
        nombre_base = os.path.splitext(os.path.basename(archivo_entrada))[0]
        archivo_salida = os.path.join(directorio, f"{nombre_base}-anonima.md")
    
    try:
        # Leer el archivo original
        with open(archivo_entrada, 'r', encoding='utf-8') as archivo:
            contenido_original = archivo.read()
        
        print(f"✅ Archivo leído: {archivo_entrada}")
        print(f"📄 Tamaño original: {len(contenido_original)} caracteres")
        
        # Anonimizar el contenido
        contenido_anonimizado = anonimizar_texto(contenido_original)
        
        # Agregar encabezado de anonimización
        encabezado_anonimo = """<!-- DOCUMENTO ANONIMIZADO -->
<!-- Este documento ha sido procesado para eliminar información sensible -->
<!-- Fecha de anonimización: 22 de julio de 2025 -->

"""
        
        contenido_final = encabezado_anonimo + contenido_anonimizado
        
        # Guardar el archivo anonimizado
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            archivo.write(contenido_final)
        
        print(f"✅ Archivo anonimizado generado: {archivo_salida}")
        print(f"📄 Tamaño anonimizado: {len(contenido_final)} caracteres")
        
        # Mostrar un resumen de los cambios
        mostrar_resumen_cambios(contenido_original, contenido_anonimizado)
        
        return archivo_salida
        
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo {archivo_entrada}")
        return None
    except Exception as e:
        print(f"❌ Error inesperado: {str(e)}")
        return None

def mostrar_resumen_cambios(original: str, anonimizado: str):
    """
    Muestra un resumen de los tipos de datos que fueron anonimizados.
    """
    print("\n📊 RESUMEN DE ANONIMIZACIÓN:")
    print("=" * 50)
    
    # Contar diferentes tipos de reemplazos
    emails = len(re.findall(r'\[EMAIL\]', anonimizado))
    urls = len(re.findall(r'\[URL\]', anonimizado))
    usuarios = len(re.findall(r'\[USUARIO\]', anonimizado))
    ids_numericos = len(re.findall(r'\[ID_NUM\]', anonimizado))
    nombres = len(re.findall(r'\[NOMBRE\]', anonimizado))
    
    if emails > 0:
        print(f"📧 Emails anonimizados: {emails}")
    if urls > 0:
        print(f"🌐 URLs anonimizadas: {urls}")
    if usuarios > 0:
        print(f"👤 Usuarios anonimizados: {usuarios}")
    if ids_numericos > 0:
        print(f"🔢 IDs numéricos anonimizados: {ids_numericos}")
    if nombres > 0:
        print(f"👨‍💼 Nombres anonimizados: {nombres}")
    
    total_reemplazos = emails + urls + usuarios + ids_numericos + nombres
    
    if total_reemplazos == 0:
        print("ℹ️ No se encontraron datos sensibles para anonimizar")
    else:
        print(f"✅ Total de elementos anonimizados: {total_reemplazos}")

def main():
    """
    Función principal que ejecuta el proceso de anonimización.
    """
    print("🔒 GENERADOR DE HISTORIA DE USUARIO ANONIMIZADA")
    print("=" * 55)
    
    # Ruta del archivo de historia de usuario
    archivo_historia = r"d:\UDEMY\QA+IA\ARCHIVOS\Modulo6\historia-usuario.md"
    
    # Verificar que el archivo existe
    if not os.path.exists(archivo_historia):
        print(f"❌ Error: No se encontró el archivo {archivo_historia}")
        return
    
    print(f"📖 Procesando: {os.path.basename(archivo_historia)}")
    
    # Generar la versión anonimizada
    archivo_generado = generar_historia_anonima(archivo_historia)
    
    if archivo_generado:
        print(f"\n🎉 ¡Proceso completado exitosamente!")
        print(f"📁 Archivo anonimizado disponible en:")
        print(f"   {archivo_generado}")
        
        # Preguntar si mostrar vista previa
        print(f"\n📋 Vista previa del contenido anonimizado:")
        print("-" * 50)
        
        try:
            with open(archivo_generado, 'r', encoding='utf-8') as archivo:
                lineas = archivo.readlines()
                # Mostrar las primeras 15 líneas
                for i, linea in enumerate(lineas[:15]):
                    print(f"{i+1:2d}: {linea.rstrip()}")
                
                if len(lineas) > 15:
                    print(f"... ({len(lineas) - 15} líneas adicionales)")
                    
        except Exception as e:
            print(f"❌ Error al mostrar vista previa: {str(e)}")
    
    else:
        print(f"\n❌ No se pudo generar el archivo anonimizado")

if __name__ == "__main__":
    main()
