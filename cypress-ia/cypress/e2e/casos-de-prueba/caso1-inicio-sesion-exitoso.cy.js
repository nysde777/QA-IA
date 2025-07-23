describe('Caso de Prueba 1: Inicio de sesión exitoso', () => {
  it('Debería permitir al usuario iniciar sesión con credenciales válidas', () => {
    cy.visit('https://www.saucedemo.com/');
    cy.get('[data-test="username"]').type('standard_user');
    cy.get('[data-test="password"]').type('secret_sauce');
    cy.get('[data-test="login-button"]').click();
    cy.url().should('include', '/inventory.html');
    cy.contains('Products').should('be.visible');
  });
});
