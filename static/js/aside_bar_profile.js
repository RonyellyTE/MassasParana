// aside_bar_profile.js

document.addEventListener("DOMContentLoaded", () => {
    const toggleMenuButton = document.getElementById("toggle-menu");
    const closeMenuButton = document.getElementById("close-menu");
    const asideMenu = document.querySelector(".menu-lateral");

    // Alternar o menu lateral ao clicar no botão "☰"
    toggleMenuButton.addEventListener("click", () => {
        const isExpanded = toggleMenuButton.getAttribute("aria-expanded") === "true";
        toggleMenuButton.setAttribute("aria-expanded", !isExpanded);
        asideMenu.setAttribute("aria-hidden", isExpanded);
    });

    // Fechar o menu lateral ao clicar no botão "×"
    closeMenuButton.addEventListener("click", () => {
        toggleMenuButton.setAttribute("aria-expanded", "false");
        asideMenu.setAttribute("aria-hidden", "true");
    });
});
