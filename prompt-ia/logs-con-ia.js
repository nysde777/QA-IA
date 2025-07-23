require('dotenv').config();
const {OpenAI} = require('openai');
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY
});

async function generarCasosDePrueba() {
    const log = `2024-10-01 12:00:00 INFO: Usuario ingreso al sistema pero el sistema le retorno un error "su usuarioo no pudo ingresar porque ingreso varias veces una contraseña que no existe su cuenta fue bloqueada".`;

    const prompt = `Eres un expero QA en revisar logs de aplicaciones.
    Tu tarea es analizar el siguiente log y nos de una sugerencia de solucion. ${log}`;   


    //Llamada a la API de OpenAI para generar el reporte
    const respuesta = await openai.chat.completions.create({
        model: "gpt-4o-mini-2024-07-18",
        messages:[
            {role:"user", content: prompt}
        ],
    });
    console.log(respuesta.choices[0].message.content);
}

generarCasosDePrueba();