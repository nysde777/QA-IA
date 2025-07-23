Fase 1 – Inicializar proyecto Cypress PASS
Fase 2 – Escribir los primeros tests (Login)
    a.1 Test de login (Cypress)
        data: 
        https://www.saucedemo.com
        user: standard_user
        password: secret_sauce
    a.2 Agregar un producto al carrito (Cypress)
        data:
        https://www.saucedemo.com/inventory.html
        producto: Sauce Labs Backpack
    a.3 Test de checkout (Cypress)
        data: 
        https://www.saucedemo.com/cart.html
        clic en <button class="btn btn_action btn_medium checkout_button " data-test="checkout" id="checkout" name="checkout">Checkout</button>
    a.4 Test llenar el Checkout: Your Information
        data: 
        https://www.saucedemo.com/checkout-step-one.html
        firstName: John
        lastName: Doe
        postalCode: 12345
        elemento html:
        <div class="checkout_info"><div class="form_group"><input class="input_error form_input" placeholder="First Name" type="text" data-test="firstName" id="first-name" name="firstName" autocorrect="off" autocapitalize="none" value=""></div><div class="form_group"><input class="input_error form_input" placeholder="Last Name" type="text" data-test="lastName" id="last-name" name="lastName" autocorrect="off" autocapitalize="none" value=""></div><div class="form_group"><input class="input_error form_input" placeholder="Zip/Postal Code" type="text" data-test="postalCode" id="postal-code" name="postalCode" autocorrect="off" autocapitalize="none" value=""></div><div class="error-message-container"></div></div>
    a.5 Test Finalizar compra Checkout: Overview
        data: 
        https://www.saucedemo.com/checkout-step-two.html
        clic en <button class="btn btn_action btn_medium cart_button" data-test="finish" id="finish" name="finish">Finish</button>
Fase 3 – Generar logs y análisis IA
    3.1 Registrar resultados en JSON
    3.2 Procesar logs (Python)
    3.3 Priorización por riesgo & generación automática de tests (GPT‑4o)

"Actua como un ingeniero QA especialista en automatizacion y analisis de logs
tengo una fase 3 llamada genera logs de las pruebas en cypress y analizaras con la api de GPT
lo que se tiene que hacer es: 
1. Registrar los resultados de las pruebas de cypress en un archivo JSON ya sean si las pruebas pasaron o fallaron
2. Procesar los logs generados por cypress con un script en Python y que la api de GPT analice los logs y genere una lista de pruebas que deberian ser priorizadas por riesgo
3. Genrar analisis predictivo de las pruebas con la api de GPT y generar una lista de pruebas que deberian ser generadas automaticamente

Contexto: 
- Ya tengo test automatizados en cypress
- quiero guardar los resultados de ejecucion en formato json(uno por cada corrida de test)
- luego el script de python procesara los logs y los enviara a la api de GPT
- la api de GPT analizara los logs y generara una lista de pruebas que deberian ser priorizadas por riesgo
- tambien la api de gpt me entregara un analisis predictivo en base a los logs"

Fase 4 – Análisis predictivo con ML ligero
Fase 5 – Dockerizar todo (imagen reproducible)
Fase 6 – Pipeline Jenkins (CI/CD clásico)
