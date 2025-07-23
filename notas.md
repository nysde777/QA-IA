
Fase 1 – Inicializar proyecto Cypress
Fase 2 – Escribir los primeros tests (Login)
Fase 3 – Generar logs y análisis IA
    3.1 Registrar resultados en JSON
    3.2 Procesar logs (Python)
    3.3 Priorización por riesgo & generación automática de tests (GPT‑4o)
    3.4 Datos sintéticos avanzados (Faker)
Fase 4 – Análisis predictivo con ML ligero
Fase 5 – Dockerizar todo (imagen reproducible)
Fase 6 – Pipeline Jenkins (CI/CD clásico)

------------------------------------------------
Modulo 6 
---------------------------------------------------
reporte_original = """
El cliente Juan Pérez con email juan.perez@example.com reporta que la app falla al intentar subir una foto.
"""

# Reemplazamos datos personales por etiquetas
reporte_anonimizado = reporte_original.replace("Juan Pérez", "[NOMBRE_CLIENTE]").replace("juan.perez@example.com", "[EMAIL_CLIENTE]")

# Ahora este texto anonimizado es seguro para enviarlo a la API de GPT
print(reporte_anonimizado)

--------------------------------------------------
# La IA genera estos casos para validar un formulario de registro:

casos_generados = [
    {"edad": 25, "acción": "registrar usuario"},
    {"edad": 28, "acción": "registrar usuario"},
]

# Notamos que no hay casos para edades menores o mayores, por lo que agregamos manualmente
casos_equilibrados = casos_generados + [
    {"edad": 14, "acción": "registro rechazado - menor de edad"},
    {"edad": 70, "acción": "registro aceptado - adulto mayor"},
]

print(casos_equilibrados)
-------------------------------------------------
Ejemplo
Historia de Usuario -> IA Casos de prueba 10 -> Script de los 10 casos de prueba 8 cumpliendo con la US -> Revision Manual -> Verificar que los casos de prueba cubren todos los criterios de acetpaccion. 

------------------------------------------------
# Combinar IA con el juicio humano para mejores resultados
casos_ia = [
    {"input": "admin", "expected_output": "Acceso total"},
    {"input": "guest", "expected_output": "Acceso limitado"},
    {"input": "", "expected_output": "Error: campo vacío"},
    {"input": "user!", "expected_output": "Error: caracteres inválidos"},
    {"input": "usuario", "expected_output": "Acceso concedido"},
]

# Un tester elige y mejora casos
casos_seleccionados = [casos_ia[0], casos_ia[2]]
casos_seleccionados.append({"input": "user123", "expected_output": "Acceso concedido"})
print(casos_seleccionados)
----------------------------------------------------

# Pregunta: ¿La pantalla principal es fácil de usar y clara para usuarios nuevos?  
# Respuesta: Requiere evaluación con usuarios reales y observación directa.
----------------------------------------------------
Respuesta de GPT -> Antes de utilizarla -> Validamos que es un JSON Correcto -> La usamos en nuestra aplicacion

---------------------
Input Correo: Dame una receta de cocina -> Numero de tokens Costo +++
--------------------- 
Esta es la receta de cocina 
