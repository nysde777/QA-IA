describe('Caso de Prueba 2: Inicio de sesión con usuario incorrecto', () => {
  it('Debería mostrar un mensaje de error para un usuario incorrecto', () => {
    cy.visit('https://www.saucedemo.com/');
    cy.get('[data-test="username"]').type('wrong_user');
    cy.get('[data-test="password"]').type('secret_sauce');
    cy.get('[data-test="login-button"]').click();
    cy.get('[data-test="error"]').should('contain', 'Username and password do not match any user in this service');
  });
});
