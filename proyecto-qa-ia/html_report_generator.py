#!/usr/bin/env python3
"""
Generador de reportes HTML para análisis QA + IA
Lee archivos JSON de análisis y genera reportes visuales
"""

import json
import os
import glob
from datetime import datetime
from pathlib import Path

class HTMLReportGenerator:
    def __init__(self):
        self.analysis_dir = Path("analysis")
        self.reports_dir = Path("reports")
        self.reports_dir.mkdir(exist_ok=True)
    
    def get_latest_analysis(self):
        """Obtener el análisis más reciente"""
        analysis_files = glob.glob(str(self.analysis_dir / "gpt_analysis_*.json"))
        if not analysis_files:
            raise FileNotFoundError("No se encontraron archivos de análisis")
        
        # Obtener el más reciente
        latest_file = max(analysis_files, key=os.path.getmtime)
        
        with open(latest_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        return data, latest_file
    
    def generate_html_report(self, analysis_data, source_file):
        """Generar reporte HTML completo"""
        
        # Extraer datos
        timestamp = analysis_data.get("analysis_timestamp", "")
        logs_analyzed = analysis_data.get("logs_analyzed", 0)
        risk_data = analysis_data.get("risk_prioritization", {}).get("risk_analysis", {})
        predictive_data = analysis_data.get("predictive_insights", {}).get("predictive_analysis", {})
        
        # Formatear timestamp
        if timestamp:
            try:
                dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
                formatted_timestamp = dt.strftime("%d/%m/%Y %H:%M:%S")
            except:
                formatted_timestamp = timestamp
        else:
            formatted_timestamp = "N/A"
        
        html_content = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reporte QA + IA - Análisis de Pruebas</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
            font-weight: 300;
        }}
        
        .header .subtitle {{
            font-size: 1.1em;
            opacity: 0.9;
        }}
        
        .stats-bar {{
            background: #ecf0f1;
            padding: 20px;
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
        }}
        
        .stat-item {{
            text-align: center;
            margin: 10px;
        }}
        
        .stat-number {{
            font-size: 2.5em;
            font-weight: bold;
            color: #3498db;
        }}
        
        .stat-label {{
            color: #7f8c8d;
            font-size: 0.9em;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        
        .content {{
            padding: 30px;
        }}
        
        .section {{
            margin-bottom: 40px;
        }}
        
        .section-title {{
            font-size: 1.8em;
            color: #2c3e50;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 3px solid #3498db;
            display: flex;
            align-items: center;
        }}
        
        .section-title .icon {{
            margin-right: 15px;
            font-size: 1.2em;
        }}
        
        .risk-card {{
            background: #fff;
            border-left: 5px solid #e74c3c;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }}
        
        .risk-card:hover {{
            transform: translateY(-2px);
        }}
        
        .risk-card.high {{
            border-left-color: #e74c3c;
        }}
        
        .risk-card.medium {{
            border-left-color: #f39c12;
        }}
        
        .risk-card.low {{
            border-left-color: #27ae60;
        }}
        
        .test-name {{
            font-size: 1.2em;
            font-weight: bold;
            color: #2c3e50;
            margin-bottom: 10px;
        }}
        
        .risk-score {{
            background: #e74c3c;
            color: white;
            padding: 5px 15px;
            border-radius: 20px;
            font-weight: bold;
            display: inline-block;
            margin-bottom: 15px;
        }}
        
        .risk-score.medium {{
            background: #f39c12;
        }}
        
        .risk-score.low {{
            background: #27ae60;
        }}
        
        .factors-list, .actions-list {{
            margin: 10px 0;
        }}
        
        .factors-list ul, .actions-list ul {{
            list-style: none;
            padding-left: 0;
        }}
        
        .factors-list li, .actions-list li {{
            background: #ecf0f1;
            margin: 5px 0;
            padding: 8px 15px;
            border-radius: 5px;
            position: relative;
            padding-left: 35px;
        }}
        
        .factors-list li:before {{
            content: "⚠️";
            position: absolute;
            left: 10px;
        }}
        
        .actions-list li:before {{
            content: "💡";
            position: absolute;
            left: 10px;
        }}
        
        .prediction-card {{
            background: linear-gradient(135deg, #74b9ff 0%, #0984e3 100%);
            color: white;
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 20px;
        }}
        
        .prediction-title {{
            font-size: 1.3em;
            font-weight: bold;
            margin-bottom: 15px;
        }}
        
        .prediction-metric {{
            background: rgba(255,255,255,0.2);
            padding: 10px 15px;
            border-radius: 8px;
            margin: 10px 0;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        
        .suggestion-card {{
            background: #f8f9fa;
            border: 1px solid #dee2e6;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 15px;
        }}
        
        .suggestion-priority {{
            display: inline-block;
            padding: 4px 12px;
            border-radius: 15px;
            font-size: 0.8em;
            font-weight: bold;
            text-transform: uppercase;
        }}
        
        .priority-alta {{
            background: #ffebee;
            color: #c62828;
        }}
        
        .priority-media {{
            background: #fff3e0;
            color: #ef6c00;
        }}
        
        .priority-baja {{
            background: #e8f5e8;
            color: #2e7d32;
        }}
        
        .trends-box {{
            background: linear-gradient(135deg, #fd79a8 0%, #e84393 100%);
            color: white;
            padding: 25px;
            border-radius: 15px;
            margin-bottom: 20px;
        }}
        
        .footer {{
            background: #2c3e50;
            color: white;
            text-align: center;
            padding: 20px;
        }}
        
        .emoji {{
            font-size: 1.5em;
            margin-right: 10px;
        }}
        
        @media (max-width: 768px) {{
            .stats-bar {{
                flex-direction: column;
            }}
            
            .content {{
                padding: 20px;
            }}
            
            .header h1 {{
                font-size: 2em;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🤖 Reporte QA + IA</h1>
            <div class="subtitle">Análisis Inteligente de Pruebas Automatizadas</div>
        </div>
        
        <div class="stats-bar">
            <div class="stat-item">
                <div class="stat-number">{logs_analyzed}</div>
                <div class="stat-label">Logs Analizados</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">{len(risk_data.get('high_risk_tests', []))}</div>
                <div class="stat-label">Tests Alto Riesgo</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">{len(predictive_data.get('automated_test_suggestions', []))}</div>
                <div class="stat-label">Nuevas Pruebas Sugeridas</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">{formatted_timestamp}</div>
                <div class="stat-label">Fecha de Análisis</div>
            </div>
        </div>
        
        <div class="content">
"""

        # Sección de tests de alto riesgo
        if risk_data.get('high_risk_tests'):
            html_content += """
            <div class="section">
                <h2 class="section-title">
                    <span class="icon">🔥</span>
                    Tests de Alto Riesgo
                </h2>
"""
            for test in risk_data['high_risk_tests']:
                html_content += f"""
                <div class="risk-card high">
                    <div class="test-name">{test.get('test_name', 'N/A')}</div>
                    <div class="risk-score">{test.get('risk_score', 'N/A')}/10</div>
                    
                    <div class="factors-list">
                        <h4>Factores de Riesgo:</h4>
                        <ul>
"""
                for factor in test.get('risk_factors', []):
                    html_content += f"                            <li>{factor}</li>\n"
                
                html_content += """
                        </ul>
                    </div>
                    
                    <div class="actions-list">
                        <h4>Acciones Recomendadas:</h4>
                        <ul>
"""
                for action in test.get('recommended_actions', []):
                    html_content += f"                            <li>{action}</li>\n"
                
                html_content += """
                        </ul>
                    </div>
                </div>
"""
            html_content += "            </div>\n"

        # Sección de tendencias
        if risk_data.get('trends'):
            trends = risk_data['trends']
            html_content += f"""
            <div class="section">
                <h2 class="section-title">
                    <span class="icon">📈</span>
                    Tendencias y Patrones
                </h2>
                
                <div class="trends-box">
                    <h3>📊 Patrones de Fallas</h3>
                    <p>{trends.get('failure_patterns', 'No se encontraron patrones específicos')}</p>
                    
                    <h3>🎯 Tendencia de Estabilidad</h3>
                    <p>Estado: <strong>{trends.get('stability_trend', 'N/A').upper()}</strong></p>
                </div>
            </div>
"""

        # Sección predictiva
        if predictive_data:
            html_content += """
            <div class="section">
                <h2 class="section-title">
                    <span class="icon">🔮</span>
                    Análisis Predictivo
                </h2>
"""
            
            # Métricas de rendimiento
            if predictive_data.get('performance_predictions'):
                perf = predictive_data['performance_predictions']
                html_content += f"""
                <div class="prediction-card">
                    <div class="prediction-title">📊 Predicciones de Rendimiento</div>
                    
                    <div class="prediction-metric">
                        <span>Tasa de fallas esperada:</span>
                        <strong>{perf.get('expected_failure_rate', 'N/A')}</strong>
                    </div>
                    
                    <div class="prediction-metric">
                        <span>Tendencia de duración:</span>
                        <strong>{perf.get('test_duration_trend', 'N/A')}</strong>
                    </div>
                    
                    <div class="prediction-metric">
                        <span>Pronóstico de estabilidad:</span>
                        <strong>{perf.get('stability_forecast', 'N/A')}</strong>
                    </div>
                </div>
"""
            
            # Áreas de riesgo futuro
            if predictive_data.get('future_risk_areas'):
                html_content += """
                <h3>⚠️ Áreas de Riesgo Futuro</h3>
"""
                for area in predictive_data['future_risk_areas']:
                    probability = area.get('risk_probability', 0)
                    probability_percent = f"{probability * 100:.0f}%" if probability else "N/A"
                    
                    html_content += f"""
                <div class="suggestion-card">
                    <h4>{area.get('area', 'N/A')}</h4>
                    <p><strong>Probabilidad de riesgo:</strong> {probability_percent}</p>
                    <p><strong>Impacto:</strong> {area.get('impact', 'N/A').upper()}</p>
                    
                    <h5>Tests Sugeridos:</h5>
                    <ul>
"""
                    for test in area.get('suggested_tests', []):
                        html_content += f"                        <li>{test}</li>\n"
                    
                    html_content += """
                    </ul>
                </div>
"""
            
            html_content += "            </div>\n"

        # Sección de nuevas pruebas sugeridas
        if predictive_data.get('automated_test_suggestions'):
            html_content += """
            <div class="section">
                <h2 class="section-title">
                    <span class="icon">🤖</span>
                    Nuevas Pruebas Automatizadas Sugeridas
                </h2>
"""
            
            for suggestion in predictive_data['automated_test_suggestions']:
                priority = suggestion.get('priority', 'media').lower()
                priority_class = f"priority-{priority}"
                
                html_content += f"""
                <div class="suggestion-card">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                        <h4>{suggestion.get('test_type', 'N/A')}</h4>
                        <span class="suggestion-priority {priority_class}">{suggestion.get('priority', 'N/A')}</span>
                    </div>
                    
                    <p><strong>Escenario:</strong> {suggestion.get('test_scenario', 'N/A')}</p>
                    <p><strong>Valor Esperado:</strong> {suggestion.get('expected_value', 'N/A')}</p>
                </div>
"""
            
            html_content += "            </div>\n"

        # Sección de recomendaciones
        recommendations = []
        if risk_data.get('recommendations'):
            recommendations.extend(risk_data['recommendations'])
        if predictive_data.get('optimization_recommendations'):
            recommendations.extend(predictive_data['optimization_recommendations'])
        
        if recommendations:
            html_content += """
            <div class="section">
                <h2 class="section-title">
                    <span class="icon">💡</span>
                    Recomendaciones de Optimización
                </h2>
                
                <div class="suggestion-card">
                    <ul style="list-style-type: none; padding: 0;">
"""
            
            for rec in recommendations:
                html_content += f"""
                        <li style="margin: 10px 0; padding: 10px; background: #f1f3f4; border-radius: 5px;">
                            <span style="margin-right: 10px;">✅</span>{rec}
                        </li>
"""
            
            html_content += """
                    </ul>
                </div>
            </div>
"""

        # Footer
        html_content += f"""
        </div>
        
        <div class="footer">
            <p>📄 Reporte generado desde: <strong>{os.path.basename(source_file)}</strong></p>
            <p>🤖 Análisis powered by GPT-4 | 🔬 QA Automation</p>
        </div>
    </div>
</body>
</html>
"""
        
        return html_content
    
    def save_report(self, html_content):
        """Guardar reporte HTML"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = self.reports_dir / f"qa_report_{timestamp}.html"
        
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return report_file
    
    def generate_report(self):
        """Generar reporte completo"""
        try:
            print("📊 Cargando datos de análisis...")
            analysis_data, source_file = self.get_latest_analysis()
            
            print("🎨 Generando reporte HTML...")
            html_content = self.generate_html_report(analysis_data, source_file)
            
            print("💾 Guardando reporte...")
            report_file = self.save_report(html_content)
            
            print(f"✅ Reporte generado exitosamente: {report_file}")
            print(f"🌐 Abre el archivo en tu navegador para ver el reporte")
            
            return str(report_file)
            
        except Exception as e:
            print(f"❌ Error generando reporte: {e}")
            return None

def main():
    """Función principal"""
    print("🚀 GENERADOR DE REPORTES QA + IA")
    print("=" * 40)
    
    generator = HTMLReportGenerator()
    report_path = generator.generate_report()
    
    if report_path:
        # Intentar abrir el reporte en el navegador
        import webbrowser
        try:
            webbrowser.open(f"file://{os.path.abspath(report_path)}")
            print("🌐 Reporte abierto en el navegador")
        except:
            print("💡 Abre manualmente el archivo en tu navegador")

if __name__ == "__main__":
    main()
