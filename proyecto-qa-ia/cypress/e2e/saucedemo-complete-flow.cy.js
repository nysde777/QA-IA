describe('SauceDemo - Flujo completo de compra', () => {
  
  beforeEach(() => {
    // Configuración inicial antes de cada test
    cy.visit('https://www.saucedemo.com')
  })

  it('a.1 Test de login', () => {
    // Login con credenciales válidas
    cy.get('[data-test="username"]').type('standard_user')
    cy.get('[data-test="password"]').type('secret_sauce')
    cy.get('[data-test="login-button"]').click()
    
    // Verificar que el login fue exitoso
    cy.url().should('include', '/inventory.html')
    cy.get('.title').should('contain', 'Products')
  })

  it('a.2 Agregar un producto al carrito', () => {
    // Login primero
    cy.get('[data-test="username"]').type('standard_user')
    cy.get('[data-test="password"]').type('secret_sauce')
    cy.get('[data-test="login-button"]').click()
    
    // Navegar al inventario y agregar producto
    cy.visit('https://www.saucedemo.com/inventory.html')
    cy.get('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    
    // Verificar que el producto fue agregado
    cy.get('.shopping_cart_badge').should('contain', '1')
  })

  it('a.3 Test de checkout', () => {
    // Login y agregar producto
    cy.get('[data-test="username"]').type('standard_user')
    cy.get('[data-test="password"]').type('secret_sauce')
    cy.get('[data-test="login-button"]').click()
    cy.get('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    
    // Ir al carrito y hacer checkout
    cy.visit('https://www.saucedemo.com/cart.html')
    cy.get('[data-test="checkout"]').click()
    
    // Verificar que llegamos al checkout
    cy.url().should('include', '/checkout-step-one.html')
    cy.get('.title').should('contain', 'Checkout: Your Information')
  })

  it('a.4 Test llenar el Checkout: Your Information', () => {
    // Login, agregar producto y ir al checkout
    cy.get('[data-test="username"]').type('standard_user')
    cy.get('[data-test="password"]').type('secret_sauce')
    cy.get('[data-test="login-button"]').click()
    cy.get('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    cy.get('.shopping_cart_link').click()
    cy.get('[data-test="checkout"]').click()
    
    // Llenar información del checkout
    cy.visit('https://www.saucedemo.com/checkout-step-one.html')
    cy.get('[data-test="firstName"]').type('John')
    cy.get('[data-test="lastName"]').type('Doe')
    cy.get('[data-test="postalCode"]').type('12345')
    cy.get('[data-test="continue"]').click()
    
    // Verificar que llegamos al overview
    cy.url().should('include', '/checkout-step-two.html')
    cy.get('.title').should('contain', 'Checkout: Overview')
  })

  it('a.5 Test Finalizar compra Checkout: Overview', () => {
    // Login, agregar producto, llenar checkout
    cy.get('[data-test="username"]').type('standard_user')
    cy.get('[data-test="password"]').type('secret_sauce')
    cy.get('[data-test="login-button"]').click()
    cy.get('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    cy.get('.shopping_cart_link').click()
    cy.get('[data-test="checkout"]').click()
    cy.get('[data-test="firstName"]').type('John')
    cy.get('[data-test="lastName"]').type('Doe')
    cy.get('[data-test="postalCode"]').type('12345')
    cy.get('[data-test="continue"]').click()
    
    // Finalizar compra
    cy.visit('https://www.saucedemo.com/checkout-step-two.html')
    cy.get('[data-test="finish"]').click()
    
    // Verificar que la compra fue completada
    cy.url().should('include', '/checkout-complete.html')
    cy.get('.complete-header').should('contain', 'Thank you for your order!')
  })

  // Test completo del flujo end-to-end
  it('Flujo completo de compra - E2E', () => {
    // 1. Login
    cy.get('[data-test="username"]').type('standard_user')
    cy.get('[data-test="password"]').type('secret_sauce')
    cy.get('[data-test="login-button"]').click()
    
    // 2. Agregar producto al carrito
    cy.get('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    cy.get('.shopping_cart_badge').should('contain', '1')
    
    // 3. Ir al carrito
    cy.get('.shopping_cart_link').click()
    cy.url().should('include', '/cart.html')
    
    // 4. Checkout
    cy.get('[data-test="checkout"]').click()
    
    // 5. Llenar información
    cy.get('[data-test="firstName"]').type('John')
    cy.get('[data-test="lastName"]').type('Doe')
    cy.get('[data-test="postalCode"]').type('12345')
    cy.get('[data-test="continue"]').click()
    
    // 6. Finalizar compra
    cy.get('[data-test="finish"]').click()
    
    // 7. Verificar compra completada
    cy.get('.complete-header').should('contain', 'Thank you for your order!')
    cy.get('.complete-text').should('be.visible')
  })
})
