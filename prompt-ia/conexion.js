require('dotenv').config();
const {OpenAI} = require('openai');
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY
});

async function generarCasosDePrueba() {
    const prompt = `Eres un expero QA para reportar defectos. escribe un reporte claro y profesional sobre este bug: al ingresar una contraseña ionvalida en el login, el sistem no muestra un mensaje de error adecuado.
    incluye: resumen, pasos para reproducir, resultado esperado, resultado actual, y severidad del bug.`;   

    const respuesta = await openai.chat.completions.create({
        model: "gpt-4o-mini-2024-07-18",
        messages:[
            {role:"user", content: prompt}
        ],
    });
    console.log(respuesta.choices[0].message.content);
}

generarCasosDePrueba();