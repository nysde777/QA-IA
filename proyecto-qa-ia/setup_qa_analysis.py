#!/usr/bin/env python3
"""
Script simplificado para análisis de logs de Cypress con GPT
Ejecuta directamente el análisis de logs existentes
"""

import os
import sys
import subprocess
import glob
from pathlib import Path

def setup_directories():
    """Crear directorios necesarios"""
    print("� Verificando directorios...")
    
    directories = ["logs", "analysis"]
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"  ✓ {directory}/")
    
    print("✅ Directorios listos")

def check_logs_exist():
    """Verificar que existan logs de Cypress"""
    log_files = glob.glob("logs/test-results-*.json")
    if not log_files:
        print("⚠️  No se encontraron logs de Cypress")
        print("\n📝 Para generar logs:")
        print("   1. Ejecuta: npx cypress run")
        print("   2. Los logs se guardarán automáticamente en logs/")
        return False
    
    print(f"✅ Encontrados {len(log_files)} archivos de logs")
    return True

def check_openai_key():
    """Verificar que la API key de OpenAI esté configurada"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("⚠️  OPENAI_API_KEY no está configurada")
        print("\n📝 Configura tu API key:")
        print("   $env:OPENAI_API_KEY = 'tu_api_key_aqui'")
        return False
    
    print(f"✅ API key configurada (***{api_key[-4:]})")
    return True

def install_requirements():
    """Instalar dependencias necesarias"""
    print("📦 Verificando dependencias...")
    try:
        import openai
        print("✅ OpenAI library disponible")
        return True
    except ImportError:
        print("� Instalando dependencias...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "openai>=1.0.0"])
            print("✅ Dependencias instaladas")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Error instalando dependencias: {e}")
            return False

def run_log_analysis():
    """Ejecutar análisis de logs con GPT"""
    print("🤖 Analizando logs con GPT...")
    try:
        subprocess.check_call([sys.executable, "cypress_log_analyzer.py"])
        print("✅ Análisis completado")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error en análisis: {e}")
        return False

def main():
    """Función principal simplificada"""
    print("🚀 ANÁLISIS QA + IA - PROCESADOR DE LOGS")
    print("=" * 40)
    
    # 1. Verificar directorios
    setup_directories()
    
    # 2. Verificar dependencias
    if not install_requirements():
        print("❌ No se pudieron instalar las dependencias")
        return
    
    # 3. Verificar API key
    if not check_openai_key():
        print("❌ Configura tu API key primero")
        return
    
    # 4. Verificar logs
    if not check_logs_exist():
        print("❌ Ejecuta Cypress primero para generar logs")
        print("💡 Comando: npx cypress run")
        return
    
    print("\n🎯 TODO LISTO - INICIANDO ANÁLISIS")
    print("=" * 40)
    
    # 5. Ejecutar análisis
    if run_log_analysis():
        print("\n✨ ¡ANÁLISIS COMPLETADO!")
        print("📊 Revisa los resultados en: analysis/")
        
        # Mostrar archivos generados
        analysis_files = glob.glob("analysis/gpt_analysis_*.json")
        if analysis_files:
            latest_file = max(analysis_files, key=os.path.getmtime)
            print(f"📄 Último análisis: {latest_file}")
    else:
        print("❌ Error en el análisis")

if __name__ == "__main__":
    main()
