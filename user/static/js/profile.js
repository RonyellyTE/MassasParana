// navigation_profile.js

document.addEventListener("DOMContentLoaded", () => {
  const navigationButtons = document.querySelectorAll(".btn-navegacao");
  const toggleMenuButton = document.getElementById("toggle-menu");
  const asideMenu = document.querySelector(".menu-lateral");

  // Adicionar interação nos botões de navegação
  navigationButtons.forEach(button => {
      button.addEventListener("click", () => {
          const sectionId = button.getAttribute("data-secao");
          const section = document.getElementById(sectionId);

          // Seções podem ser manipuladas aqui (exemplo: scroll ou exibir conteúdo específico)
          if (section) {
              section.scrollIntoView({ behavior: "smooth" });
          }

          // Opcional: fechar o menu após selecionar
          asideMenu.setAttribute("aria-hidden", "true");
          toggleMenuButton.setAttribute("aria-expanded", "false");
      });
  });
});
