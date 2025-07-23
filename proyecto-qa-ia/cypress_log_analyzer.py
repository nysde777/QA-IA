import json
import os
import glob
from datetime import datetime
from typing import List, Dict, Any
import openai
from pathlib import Path

class CypressLogAnalyzer:
    def __init__(self, api_key: str):
        """
        Inicializar el analizador de logs de Cypress
        
        Args:
            api_key (str): API key de OpenAI
        """
        self.client = openai.OpenAI(api_key=api_key)
        self.logs_dir = Path("logs")
        self.analysis_dir = Path("analysis")
        self.analysis_dir.mkdir(exist_ok=True)
    
    def load_latest_logs(self) -> List[Dict[str, Any]]:
        """
        Cargar los logs más recientes de Cypress
        
        Returns:
            List[Dict]: Lista de logs de pruebas
        """
        log_files = glob.glob(str(self.logs_dir / "test-results-*.json"))
        if not log_files:
            raise FileNotFoundError("No se encontraron archivos de logs de Cypress")
        
        # Ordenar por fecha de modificación (más reciente primero)
        log_files.sort(key=os.path.getmtime, reverse=True)
        
        logs = []
        # Cargar los últimos 5 archivos de logs para análisis
        for log_file in log_files[:5]:
            with open(log_file, 'r', encoding='utf-8') as f:
                logs.append(json.load(f))
        
        return logs
    
    def analyze_risk_prioritization(self, logs: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Analizar logs y generar priorización por riesgo usando GPT
        
        Args:
            logs (List[Dict]): Logs de pruebas de Cypress
            
        Returns:
            Dict: Análisis de priorización por riesgo
        """
        # Preparar datos para el análisis
        summary_data = self._prepare_summary_data(logs)
        
        prompt = f"""
        Como experto en QA y análisis de riesgos, analiza los siguientes resultados de pruebas automatizadas en Cypress:

        DATOS DE PRUEBAS:
        {json.dumps(summary_data, indent=2)}

        INSTRUCCIONES:
        1. Identifica patrones de fallas recurrentes
        2. Calcula el riesgo basado en:
           - Frecuencia de fallas
           - Criticidad del flujo de negocio
           - Tiempo de duración de las pruebas
           - Tendencias de estabilidad

        3. Genera una lista priorizada de pruebas que requieren atención inmediata

        FORMATO DE RESPUESTA (JSON):
        {{
            "risk_analysis": {{
                "high_risk_tests": [
                    {{
                        "test_name": "nombre del test",
                        "risk_score": 9.5,
                        "risk_factors": ["factor1", "factor2"],
                        "recommended_actions": ["acción1", "acción2"]
                    }}
                ],
                "medium_risk_tests": [...],
                "trends": {{
                    "failure_patterns": "descripción de patrones",
                    "stability_trend": "mejorando/empeorando/estable"
                }},
                "recommendations": [
                    "recomendación específica 1",
                    "recomendación específica 2"
                ]
            }}
        }}
        """
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini-2024-07-18",
                messages=[
                    {"role": "system", "content": "Eres un experto en QA automation y análisis de riesgos. Responde siempre en formato JSON válido."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3
            )
            
            analysis = json.loads(response.choices[0].message.content)
            return analysis
            
        except Exception as e:
            print(f"Error en análisis de riesgos: {e}")
            return {"error": str(e)}
    
    def generate_predictive_analysis(self, logs: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Generar análisis predictivo usando GPT
        
        Args:
            logs (List[Dict]): Logs de pruebas de Cypress
            
        Returns:
            Dict: Análisis predictivo
        """
        summary_data = self._prepare_summary_data(logs)
        
        prompt = f"""
        Como experto en QA predictivo y machine learning, analiza los siguientes datos históricos de pruebas:

        DATOS HISTÓRICOS:
        {json.dumps(summary_data, indent=2)}

        INSTRUCCIONES:
        1. Identifica tendencias en los datos
        2. Predice posibles fallas futuras
        3. Recomienda nuevas pruebas automatizadas
        4. Sugiere optimizaciones en la suite de pruebas

        FORMATO DE RESPUESTA (JSON):
        {{
            "predictive_analysis": {{
                "future_risk_areas": [
                    {{
                        "area": "nombre del área",
                        "risk_probability": 0.85,
                        "impact": "alto/medio/bajo",
                        "suggested_tests": [
                            "test automatizado sugerido 1",
                            "test automatizado sugerido 2"
                        ]
                    }}
                ],
                "performance_predictions": {{
                    "expected_failure_rate": "porcentaje estimado",
                    "test_duration_trend": "aumentando/disminuyendo/estable",
                    "stability_forecast": "descripción de estabilidad futura"
                }},
                "automated_test_suggestions": [
                    {{
                        "test_type": "tipo de prueba",
                        "priority": "alta/media/baja",
                        "test_scenario": "descripción del escenario",
                        "expected_value": "valor esperado de la prueba"
                    }}
                ],
                "optimization_recommendations": [
                    "recomendación de optimización 1",
                    "recomendación de optimización 2"
                ]
            }}
        }}
        """
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Eres un experto en análisis predictivo para QA automation. Responde siempre en formato JSON válido."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.4
            )
            
            analysis = json.loads(response.choices[0].message.content)
            return analysis
            
        except Exception as e:
            print(f"Error en análisis predictivo: {e}")
            return {"error": str(e)}
    
    def _prepare_summary_data(self, logs: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Preparar datos resumidos para análisis
        
        Args:
            logs (List[Dict]): Logs de pruebas
            
        Returns:
            Dict: Datos resumidos
        """
        summary = {
            "total_executions": len(logs),
            "test_results": [],
            "failure_patterns": {},
            "performance_metrics": []
        }
        
        for log in logs:
            execution = {
                "timestamp": log["timestamp"],
                "total_tests": log["totalTests"],
                "passed": log["totalPassed"],
                "failed": log["totalFailed"],
                "duration": log["totalDuration"],
                "success_rate": log["totalPassed"] / log["totalTests"] if log["totalTests"] > 0 else 0
            }
            
            # Agregar detalles de tests fallidos
            failed_tests = []
            for run in log["runs"]:
                for test in run["tests"]:
                    if test["state"] == "failed":
                        failed_tests.append({
                            "name": test["title"],
                            "spec": run["spec"],
                            "error": test["error"]["message"] if test["error"] else "Unknown error",
                            "duration": test["duration"]
                        })
            
            execution["failed_tests"] = failed_tests
            summary["test_results"].append(execution)
            
            # Contar patrones de fallas
            for failed_test in failed_tests:
                test_name = failed_test["name"]
                if test_name not in summary["failure_patterns"]:
                    summary["failure_patterns"][test_name] = 0
                summary["failure_patterns"][test_name] += 1
        
        return summary
    
    def run_complete_analysis(self) -> Dict[str, Any]:
        """
        Ejecutar análisis completo de logs
        
        Returns:
            Dict: Análisis completo
        """
        print("🔍 Cargando logs de Cypress...")
        logs = self.load_latest_logs()
        
        print("📊 Analizando priorización por riesgo...")
        risk_analysis = self.analyze_risk_prioritization(logs)
        
        print("🔮 Generando análisis predictivo...")
        predictive_analysis = self.generate_predictive_analysis(logs)
        
        # Combinar análisis
        complete_analysis = {
            "analysis_timestamp": datetime.now().isoformat(),
            "logs_analyzed": len(logs),
            "risk_prioritization": risk_analysis,
            "predictive_insights": predictive_analysis
        }
        
        # Guardar análisis
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        analysis_file = self.analysis_dir / f"gpt_analysis_{timestamp}.json"
        
        with open(analysis_file, 'w', encoding='utf-8') as f:
            json.dump(complete_analysis, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Análisis completo guardado en: {analysis_file}")
        
        return complete_analysis

def main():
    """
    Función principal para ejecutar el análisis
    """
    # Configurar API key de OpenAI
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ Error: OPENAI_API_KEY no está configurada en las variables de entorno")
        print("💡 Configura tu API key: set OPENAI_API_KEY=tu_api_key_aqui")
        return
    
    try:
        analyzer = CypressLogAnalyzer(api_key)
        analysis = analyzer.run_complete_analysis()
        
        print("\n" + "="*60)
        print("📋 RESUMEN DEL ANÁLISIS")
        print("="*60)
        
        if "risk_prioritization" in analysis and "risk_analysis" in analysis["risk_prioritization"]:
            risk_data = analysis["risk_prioritization"]["risk_analysis"]
            if "high_risk_tests" in risk_data:
                print(f"🔥 Tests de alto riesgo: {len(risk_data['high_risk_tests'])}")
            if "recommendations" in risk_data:
                print(f"💡 Recomendaciones generadas: {len(risk_data['recommendations'])}")
        
        if "predictive_insights" in analysis and "predictive_analysis" in analysis["predictive_insights"]:
            pred_data = analysis["predictive_insights"]["predictive_analysis"]
            if "automated_test_suggestions" in pred_data:
                print(f"🤖 Nuevas pruebas sugeridas: {len(pred_data['automated_test_suggestions'])}")
        
        print("\n✨ Análisis completo finalizado exitosamente!")
        
    except Exception as e:
        print(f"❌ Error durante el análisis: {e}")

if __name__ == "__main__":
    main()
