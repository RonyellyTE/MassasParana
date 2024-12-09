document.addEventListener("DOMContentLoaded", function () {
    const menuToggle = document.querySelector(".menu-toggle");
    const mobileMenu = document.querySelector(".mobile-menu");
    const menuClose = document.querySelector(".menu-close");

    if (menuToggle && mobileMenu) {
        // Abrir o menu móvel
        menuToggle.addEventListener("click", function () {
            mobileMenu.classList.add("open");
        });
    }

    if (menuClose && mobileMenu) {
        // Fechar o menu móvel
        menuClose.addEventListener("click", function () {
            mobileMenu.classList.remove("open");
        });
    }
});
