document.addEventListener('DOMContentLoaded', () => {
  // Realça as categorias com animação mais fluida
  const categoryLinks = document.querySelectorAll('#categorias a');
  categoryLinks.forEach(link => {
      link.addEventListener('mouseover', () => {
          link.style.transition = 'all 0.5s ease';
          link.style.boxShadow = '0 8px 25px rgba(0, 0, 0, 0.3)';
          link.style.transform = 'rotate(3deg) scale(1.2)';
      });

      link.addEventListener('mouseout', () => {
          link.style.boxShadow = 'none';
          link.style.transform = 'rotate(0deg) scale(1)';
      });
  });

  // Produtos: animação de zoom nos cards ao interagir
  const products = document.querySelectorAll('.product');
  products.forEach(product => {
      product.addEventListener('mouseover', () => {
          product.style.transition = 'transform 0.5s ease, box-shadow 0.5s ease';
          product.style.boxShadow = '0 12px 30px rgba(0, 0, 0, 0.3)';
          product.style.transform = 'translateY(-10px) scale(1.05)';
      });

      product.addEventListener('mouseout', () => {
          product.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.1)';
          product.style.transform = 'translateY(0) scale(1)';
      });
  });

  // Botões: animação de pulsação quando clicados
  const actionButtons = document.querySelectorAll('.actions button');
  actionButtons.forEach(button => {
      button.addEventListener('mousedown', () => {
          button.style.transition = 'transform 0.2s ease';
          button.style.transform = 'scale(0.9)';
      });

      button.addEventListener('mouseup', () => {
          button.style.transform = 'scale(1)';
      });

      button.addEventListener('mouseover', () => {
          button.style.transition = 'background 0.3s ease, box-shadow 0.3s ease';
          button.style.boxShadow = '0 6px 20px rgba(0, 0, 0, 0.2)';
      });

      button.addEventListener('mouseout', () => {
          button.style.boxShadow = 'none';
      });
  });

  // Banner: Texto com efeito de digitação
  const bannerText = document.querySelector('.banner h1');
  const textContent = bannerText.textContent;
  bannerText.textContent = '';
  let charIndex = 0;

  function typeEffect() {
      if (charIndex < textContent.length) {
          bannerText.textContent += textContent.charAt(charIndex);
          charIndex++;
          setTimeout(typeEffect, 100); // Controla a velocidade da digitação
      }
  }
  typeEffect();

  // Adiciona animação ao rolar a página
  const scrollElements = document.querySelectorAll('.product, .categories a, .banner h1, .banner p');

  const elementInView = (el, dividend = 1) => {
      const elementTop = el.getBoundingClientRect().top;
      return (
          elementTop <=
          (window.innerHeight || document.documentElement.clientHeight) / dividend
      );
  };

  const displayScrollElement = (element) => {
      element.classList.add('scrolled');
  };

  const handleScrollAnimation = () => {
      scrollElements.forEach((el) => {
          if (elementInView(el, 1.25)) {
              displayScrollElement(el);
          }
      });
  };

  window.addEventListener('scroll', () => {
      handleScrollAnimation();
  });

  // Botão "Voltar ao Topo" animado
  const backToTopButton = document.createElement('button');
  backToTopButton.id = 'back-to-top';
  backToTopButton.innerHTML = '⬆️';
  backToTopButton.style.transition = 'opacity 0.5s ease';
  backToTopButton.style.opacity = '0';
  document.body.appendChild(backToTopButton);

  window.addEventListener('scroll', () => {
      if (window.scrollY > 300) {
          backToTopButton.style.opacity = '1';
      } else {
          backToTopButton.style.opacity = '0';
      }
  });

  backToTopButton.addEventListener('click', () => {
      window.scrollTo({
          top: 0,
          behavior: 'smooth'
      });
  });
  
});

       // Função para verificar se o elemento está visível na tela
function isElementInView(element) {
        const rect = element.getBoundingClientRect();
        return rect.top <= window.innerHeight && rect.bottom >= 0; // Verifica se o elemento está visível
    }

    // Adiciona a classe 'visible' quando o elemento entra na tela
function fadeInOnScroll() {
        const fadeInElements = document.querySelectorAll('.fade-in');

        fadeInElements.forEach(element => {
            if (isElementInView(element)) {
                element.classList.add('visible');
            }
        });
    }

    // Dispara a verificação durante o scroll
    window.addEventListener('scroll', fadeInOnScroll);

    // Chamando a função uma vez para garantir que a animação ocorra logo ao carregar
    fadeInOnScroll();