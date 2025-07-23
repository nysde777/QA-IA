/// <reference types="cypress" />

describe('Google Page Test', () => {
  it('should visit Google and verify we are on Google page', () => {
    // Visit Google homepage
    cy.visit('https://www.google.com')
    
    // Verify we are on Google by checking the title
    cy.title().should('include', 'Google')
    
    // Verify the Google logo is present (using a more reliable selector)
    cy.get('img[alt*="Google"], [aria-label*="Google"], img[src*="logo"]').should('be.visible')
    
    // Verify the search input is present
    cy.get('input[name="q"], input[title*="Search"], textarea[name="q"]').should('be.visible')
    
    // Verify the URL contains google.com
    cy.url().should('include', 'google.com')
  })
})
