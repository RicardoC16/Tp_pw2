/*
Herramienta usada: start-server-and-test
Instalación (parado dentro de Tests/):
npm install --save-dev start-server-and-test

como app.py está un nivel arriba de Tests/ hay que modificar el package.json
para subir un nivel y ejecutarlo correctamente.

"scripts": {
    "start": "python ../app.py",
    "cy:open": "cypress open",
    "cy:run": "cypress run",
    "test:e2e": "start-server-and-test start http://localhost:5000 cy:open"
  }


Comando de uso
Parado dentro de Tests/:
npm run test:e2e

*/

describe("Test de carga de sitio", () => {
  beforeEach(() => {
    cy.visit("http://127.0.0.1:5000/");
  });

  it("deberia mostrar navbar", () => {
    cy.get("nav.navbar").should("be.visible");
  });
});

describe("tests con cursos en el carrito", () => {
  beforeEach(() => {
    //Antes de cada test va a vaciar el carrito
    cy.request("DELETE", "http://127.0.0.1:5000/carrito/vaciar");
    cy.visit("http://127.0.0.1:5000/");
  });
  it("deberia agregar un curso y en el carrito mostrar el total", () => {
    cy.get(".btn-agregar").first().click();
    cy.visit("http://127.0.0.1:5000/cart");
    cy.get("div.total-box").should("contain", "1500");
  });
  it("deberia agregar varios cursos al carrito y mostrar el total", () => {
    cy.get(".btn-agregar").eq(1).click();
    cy.get(".btn-agregar").eq(2).click();
    cy.get(".btn-agregar").eq(6).click();
    cy.get(".btn-agregar").eq(8).click();
    cy.visit("http://127.0.0.1:5000/cart");
    cy.get("div.total-box").should("contain", "16600");
  });
  it("deberia agregar dos cursos y eliminar uno", () => {
    cy.get(".btn-agregar").eq(3).click();
    cy.get(".btn-agregar").eq(5).click();
    cy.visit("http://127.0.0.1:5000/cart");
    cy.get(".btn-outline-danger").eq(1).click();
    cy.get("div.total-box").should("contain", "2950");
  });
  it("deberia mostrar el msje del carrito vacio", () => {
    cy.visit("http://127.0.0.1:5000/cart");
    cy.get("#carritoVacio").should("be.visible");
  });
  it("deberia aumentar cantidad y no duplicar el curso", () => {
    cy.get(".btn-agregar").eq(3).click();
    cy.get(".btn-agregar").eq(3).click();
    cy.visit("http://127.0.0.1:5000/cart");
    cy.get("tr").eq(1).find("td:nth-child(2)").should("contain", "2");
  });
  it("deberia aparecer correctamente el nombre del curso", () => {
    cy.get(".btn-agregar").eq(1).click();
    cy.visit("http://127.0.0.1:5000/cart");
    cy.get("tr")
      .eq(1)
      .find("td:nth-child(1)")
      .should("contain", "Ruso intermedio");
  });
});
