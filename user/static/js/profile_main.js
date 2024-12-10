// Path: static/js/profile_main.js

document.addEventListener("DOMContentLoaded", () => {
    const btnEditar = document.getElementById("btn-editar");
    const btnCancelar = document.getElementById("btn-cancelar");
    const formEdicao = document.getElementById("form-edicao");
    const infoVisualizacao = document.getElementById("info-visualizacao");

    // Exibe o formulário de edição e oculta as informações
    btnEditar.addEventListener("click", () => {
        infoVisualizacao.style.display = "none";
        formEdicao.style.display = "block";
        btnEditar.style.display = "none";
        btnCancelar.style.display = "inline-block";
    });

    // Retorna para a visualização das informações e oculta o formulário de edição
    btnCancelar.addEventListener("click", () => {
        infoVisualizacao.style.display = "block";
        formEdicao.style.display = "none";
        btnEditar.style.display = "inline-block";
        btnCancelar.style.display = "none";
    });
});
