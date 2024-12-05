document.addEventListener('DOMContentLoaded', () => {
    const toggleButton = document.getElementById('toggle-menu');
    const closeButton = document.getElementById('close-menu');
    const menuLateral = document.querySelector('.menu-lateral');

    const toggleMenu = () => {
        const isOpen = menuLateral.classList.toggle('menu-aberto');
        toggleButton.setAttribute('aria-expanded', isOpen);
    };

    toggleButton.addEventListener('click', toggleMenu);
    closeButton.addEventListener('click', toggleMenu);

    const botoesNavegacao = document.querySelectorAll('.btn-navegacao');

    botoesNavegacao.forEach(botao => {
        botao.addEventListener('click', () => {
            const secaoId = botao.dataset.secao;
            document.querySelectorAll('.secao').forEach(secao => secao.classList.remove('ativa'));

            const secaoAtiva = document.getElementById(secaoId);
            if (secaoAtiva) {
                secaoAtiva.classList.add('ativa');
            } else {
                console.error('Seção não encontrada:', secaoId);
            }
        });
    });
});
