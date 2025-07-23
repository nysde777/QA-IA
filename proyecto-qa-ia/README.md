# QA + IA: Análisis Inteligente de Pruebas Automatizadas

Sistema simplificado para analizar logs de Cypress usando GPT-4 y obtener insights predictivos y priorización por riesgo.

## 🚀 Inicio Rápido (3 pasos)

### 1. Configurar API Key de OpenAI
```powershell
$env:OPENAI_API_KEY = "tu_api_key_aqui"
```

### 2. Ejecutar tests de Cypress (genera logs automáticamente)
```bash
npx cypress run
```

### 3. Analizar logs con GPT
```bash
python setup_qa_analysis.py
```

¡Eso es todo! El script analizará automáticamente todos los logs y generará reportes inteligentes.

## 📁 Estructura del Proyecto

```
proyecto-qa-ia/
├── cypress/
│   ├── e2e/
│   │   └── saucedemo-complete-flow.cy.js  # Tests automatizados
│   └── support/
├── logs/                                  # Logs de ejecución (se crean automáticamente)
│   └── test-results-*.json
├── analysis/                              # Análisis de GPT (se crean automáticamente)
│   └── gpt_analysis_*.json
├── cypress.config.js                      # Configuración con logging
├── cypress_log_analyzer.py               # Analizador principal
└── setup_qa_analysis.py                  # Script simplificado (¡SOLO EJECUTA ESTE!)
```

## 🔧 Flujo de Trabajo

### Paso 1: Generar logs
```bash
npx cypress run
```
Esto ejecuta los tests y genera automáticamente logs en `logs/`

### Paso 2: Analizar con IA
```bash
python setup_qa_analysis.py
```
Esto procesa los logs y genera análisis inteligente en `analysis/`

## 🛠️ Troubleshooting

### ❌ Error: OPENAI_API_KEY not configured
```powershell
$env:OPENAI_API_KEY = "tu_api_key_aqui"
```

### ❌ Error: No log files found
```bash
# Ejecutar tests primero para generar logs
npx cypress run
```

### ❌ Error: OpenAI library not found
El script instalará automáticamente las dependencias necesarias.

## ✨ ¿Qué hace el análisis?

El sistema GPT-4 analiza tus logs y genera:

- 🎯 **Priorización por riesgo**: Qué tests fallan más y son críticos
- 🔮 **Análisis predictivo**: Dónde pueden ocurrir fallas futuras  
- 🤖 **Nuevas pruebas**: Suggestions de tests adicionales automatizados
- � **Optimizaciones**: Cómo mejorar tu suite de pruebas

## 📋 Tests Incluidos

1. **Login Test**: Autenticación con credenciales válidas
2. **Add to Cart**: Agregar producto al carrito
3. **Checkout Process**: Proceso completo de compra
4. **Form Validation**: Validación de formularios
5. **E2E Flow**: Flujo completo de principio a fin
