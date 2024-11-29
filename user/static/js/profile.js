function mostrarSecao(secaoId) {
    // Ocultar todas as seções
    const secoes = document.querySelectorAll('.secao');
    secoes.forEach(secao => secao.classList.remove('ativa'));
  
    // Mostrar a seção selecionada
    const secaoAtiva = document.getElementById(secaoId);
    if (secaoAtiva) {
      secaoAtiva.classList.add('ativa');
    } else {
      console.error('Seção não encontrada:', secaoId);
    }
  }
  