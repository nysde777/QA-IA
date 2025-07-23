describe('Caso de Prueba 4: Campos de entrada vacíos', () => {
  it('Debería mostrar un mensaje de error si los campos están vacíos', () => {
    cy.visit('https://www.saucedemo.com/');
    cy.get('[data-test="login-button"]').click();
    cy.get('[data-test="error"]').should('contain', 'Username is required');
  });
});
