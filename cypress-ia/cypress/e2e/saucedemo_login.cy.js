describe('SauceDemo Login Test', () => {
  // Constantes para credenciales
  const VALID_USER = 'standard_user'
  const VALID_PASSWORD = 'secret_sauce'
  const LOGIN_URL = '/'
  const INVENTORY_URL = '/inventory.html'

  // Función auxiliar para realizar login
  const performLogin = (username = VALID_USER, password = VALID_PASSWORD) => {
    cy.visit(LOGIN_URL)
    cy.get('[data-test="username"]').type(username)
    cy.get('[data-test="password"]').type(password)
    cy.get('[data-test="login-button"]').click()
  }

  // Función auxiliar para verificar que la página de login se cargó
  const verifyLoginPageLoaded = () => {
    cy.url().should('include', 'saucedemo.com')
    cy.get('.login_logo').should('be.visible')
    cy.get('[data-test="username"]').should('be.visible')
    cy.get('[data-test="password"]').should('be.visible')
    cy.get('[data-test="login-button"]').should('be.visible')
  }

  // Función auxiliar para verificar login exitoso
  const verifySuccessfulLogin = () => {
    cy.url().should('include', INVENTORY_URL)
    cy.get('.title').should('contain', 'Products')
    cy.get('.shopping_cart_link').should('be.visible')
    cy.get('.inventory_list').should('be.visible')
  }

  beforeEach(() => {
    // Visitar la página antes de cada prueba
    cy.visit(LOGIN_URL)
  })

  it('debería cargar la página de login correctamente', () => {
    verifyLoginPageLoaded()
  })

  it('debería permitir iniciar sesión con credenciales válidas', () => {
    // Verificar que la página se cargó
    verifyLoginPageLoaded()
    
    // Realizar login con credenciales válidas
    cy.get('[data-test="username"]').type(VALID_USER)
    cy.get('[data-test="password"]').type(VALID_PASSWORD)
    cy.get('[data-test="login-button"]').click()
    
    // Verificar login exitoso
    verifySuccessfulLogin()
  })

  it('debería mostrar la página de productos después del login exitoso', () => {
    // Realizar login usando función auxiliar
    performLogin()
    
    // Verificaciones específicas de la página de productos
    cy.get('.inventory_list').should('be.visible')
    cy.get('.inventory_item').should('have.length.greaterThan', 0)
    cy.get('.header_secondary_container').should('contain', 'Products')
    
    // Verificar elementos específicos de la tienda
    cy.get('.shopping_cart_container').should('be.visible')
    cy.get('.product_sort_container').should('be.visible')
  })

  it('debería mostrar error con credenciales inválidas', () => {
    // Intentar login con credenciales incorrectas
    cy.get('[data-test="username"]').type('invalid_user')
    cy.get('[data-test="password"]').type('wrong_password')
    cy.get('[data-test="login-button"]').click()
    
    // Verificar que aparece el mensaje de error
    cy.get('[data-test="error"]').should('be.visible')
    cy.get('[data-test="error"]').should('contain', 'Username and password do not match')
    
    // Verificar que sigue en la página de login
    cy.url().should('not.include', INVENTORY_URL)
  })

  it('debería mostrar error cuando faltan credenciales', () => {
    // Intentar login sin credenciales
    cy.get('[data-test="login-button"]').click()
    
    // Verificar mensaje de error
    cy.get('[data-test="error"]').should('be.visible')
    cy.get('[data-test="error"]').should('contain', 'Username is required')
  })

  it('debería poder cerrar sesión después del login', () => {
    // Realizar login
    performLogin()
    verifySuccessfulLogin()
    
    // Abrir menú y cerrar sesión
    cy.get('#react-burger-menu-btn').click()
    cy.get('#logout_sidebar_link').click()
    
    // Verificar que regresó a la página de login
    cy.url().should('not.include', INVENTORY_URL)
    verifyLoginPageLoaded()
  })

  it('debería poder agregar un producto al carrito', () => {
    // Realizar login
    performLogin()
    verifySuccessfulLogin()
    
    // Verificar que el carrito está vacío inicialmente
    cy.get('.shopping_cart_badge').should('not.exist')
    
    // Agregar el primer producto al carrito
    cy.get('.inventory_item').first().find('button[data-test^="add-to-cart"]').click()
    
    // Verificar que el badge del carrito muestra "1"
    cy.get('.shopping_cart_badge').should('be.visible')
    cy.get('.shopping_cart_badge').should('contain', '1')
    
    // Verificar que el botón cambió a "Remove"
    cy.get('.inventory_item').first().find('button[data-test^="remove"]').should('be.visible')
    
    // Ir al carrito
    cy.get('.shopping_cart_link').click()
    
    // Verificar que estamos en la página del carrito
    cy.url().should('include', '/cart.html')
    cy.get('.title').should('contain', 'Your Cart')
    
    // Verificar que hay un producto en el carrito
    cy.get('.cart_item').should('have.length', 1)
    cy.get('.inventory_item_name').should('be.visible')
    
    // Verificar botones del carrito
    cy.get('[data-test="continue-shopping"]').should('be.visible')
    cy.get('[data-test="checkout"]').should('be.visible')
  })

  it('debería poder agregar múltiples productos al carrito', () => {
    // Realizar login
    performLogin()
    verifySuccessfulLogin()
    
    // Agregar los primeros 3 productos al carrito
    for (let i = 0; i < 3; i++) {
      cy.get('.inventory_item').eq(i).find('button[data-test^="add-to-cart"]').click()
    }
    
    // Verificar que el badge del carrito muestra "3"
    cy.get('.shopping_cart_badge').should('contain', '3')
    
    // Ir al carrito y verificar
    cy.get('.shopping_cart_link').click()
    cy.get('.cart_item').should('have.length', 3)
  })

  it('debería poder remover un producto del carrito', () => {
    // Realizar login
    performLogin()
    verifySuccessfulLogin()
    
    // Agregar un producto al carrito
    cy.get('.inventory_item').first().find('button[data-test^="add-to-cart"]').click()
    
    // Verificar que se agregó
    cy.get('.shopping_cart_badge').should('contain', '1')
    
    // Remover el producto desde la página de productos
    cy.get('.inventory_item').first().find('button[data-test^="remove"]').click()
    
    // Verificar que el carrito está vacío
    cy.get('.shopping_cart_badge').should('not.exist')
    
    // Verificar que el botón volvió a "Add to cart"
    cy.get('.inventory_item').first().find('button[data-test^="add-to-cart"]').should('be.visible')
  })
})
