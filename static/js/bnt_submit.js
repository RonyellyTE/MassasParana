document.querySelector('form').addEventListener('submit', function (e) {
    const submitBtn = document.querySelector('.submit-btn');
    // Impede o envio do formulário temporariamente para exibir o efeito de loading
    e.preventDefault();
    
    // Adiciona a classe 'loading' ao botão de envio
    submitBtn.classList.add('loading');

    // Simula o envio com um delay de 3 segundos
    setTimeout(function () {
        // Remove o estado de 'loading' após a simulação
        submitBtn.classList.remove('loading');

        // Submete o formulário de fato
        e.target.submit();  // Descomentei isso para garantir que o envio real ocorra
    }, 3000);  // Simulação de 3 segundos (ajuste conforme necessário)
});     