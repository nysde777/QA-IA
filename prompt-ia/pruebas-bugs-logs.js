require('dotenv').config();
const {OpenAI} = require('openai');
const fs = require('fs');

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY
});

async function generarCasosDePruebaJSON(historia) {
    const prompt = `Eres un expero QA en analizar logs, dame un resumen de los errores y sus causas y dame una sugerencia para corregirlos
    "${historia}"
    `;   

    const respuesta = await openai.chat.completions.create({
        model: "gpt-4o-mini-2024-07-18",
        messages:[
            {role:"user", content: prompt}
        ],
    });

    if(!fs.existsSync('pruebas')) fs.mkdirSync('pruebas');
    fs.writeFileSync('pruebas/reporte-logs.md', respuesta.choices[0].message.content);
    console.log("Logs creados existosamente")
    
}

generarCasosDePruebaJSON("log1 el sistema fallo porque el servidor perdio la conexion log2 el sistema fallo porque se termino el espacio disponible en disco");