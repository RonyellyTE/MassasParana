document.addEventListener('DOMContentLoaded', () => {
  const toggleMenuButton = document.getElementById('toggle-menu');
  const closeMenuButton = document.getElementById('close-menu');
  const menuLateral = document.querySelector('.menu-lateral');

  // Abre ou fecha o menu
  const toggleMenu = () => {
    const isOpen = menuLateral.classList.toggle('aberto');
    toggleMenuButton.setAttribute('aria-expanded', isOpen);
  };

  // Adiciona eventos aos botões
  toggleMenuButton.addEventListener('click', toggleMenu);
  closeMenuButton.addEventListener('click', toggleMenu);
});
document.addEventListener("DOMContentLoaded", () => {
  const btnEditar = document.getElementById("btn-editar");
  const btnCancelar = document.getElementById("btn-cancelar");
  const infoVisualizacao = document.getElementById("info-visualizacao");
  const formEdicao = document.getElementById("form-edicao");

  btnEditar.addEventListener("click", () => {
    // Alterna para o modo de edição
    infoVisualizacao.style.display = "none";
    formEdicao.style.display = "block";
    btnEditar.style.display = "none";
    btnCancelar.style.display = "inline-block";
  });

  btnCancelar.addEventListener("click", () => {
    // Alterna para o modo de visualização
    infoVisualizacao.style.display = "block";
    formEdicao.style.display = "none";
    btnEditar.style.display = "inline-block";
    btnCancelar.style.display = "none";
  });
});
