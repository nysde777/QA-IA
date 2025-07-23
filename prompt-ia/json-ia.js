require('dotenv').config();
const {OpenAI} = require('openai');
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY
});

async function generarCasosDePruebaJSON(historia) {
    const prompt = `Eres un expero QA para generar 3 casos de prueba, para esta historia:
    "${historia}"
    Entrega las respuestas en formato JSON con los campos Id, descripcion, tipo(positvo/negativo).
    `;   

    const respuesta = await openai.chat.completions.create({
        model: "gpt-4o-mini-2024-07-18",
        messages:[
            {role:"user", content: prompt}
        ],
    });

    try{
        const output = JSON.parse(respuesta.choices[0].message.content);
        console.log(output)
    }catch(e){
        console.log("la respues no es un JSON valido aqui esta el texto");
        console.log(respuesta.choices[0].message.content);
    }
    

}

generarCasosDePruebaJSON("El usaurio debe poder cambiar su contraseña desde su perfil");