describe('Caso de Prueba 3: Inicio de sesión con contraseña incorrecta', () => {
  it('Debería mostrar un mensaje de error para una contraseña incorrecta', () => {
    cy.visit('https://www.saucedemo.com/');
    cy.get('[data-test="username"]').type('standard_user');
    cy.get('[data-test="password"]').type('wrong_password');
    cy.get('[data-test="login-button"]').click();
    cy.get('[data-test="error"]').should('contain', 'Username and password do not match any user in this service');
  });
});
