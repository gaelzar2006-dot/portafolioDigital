const navButtons = document.querySelectorAll('.btn-nav');
const backButtons = document.querySelectorAll('.btn-back');
const cardIndex = document.getElementById('card-index');

// Evento para ir desde el Índice hacia una Carta específica
navButtons.forEach(button => {
    button.addEventListener('click', () => {
        const targetId = button.getAttribute('data-target');
        const targetCard = document.getElementById(targetId);
        
        if (targetCard) {
            // Mandamos el índice hacia atrás con animación
            cardIndex.classList.add('send-back');
            cardIndex.classList.remove('active');
            
            // Esperamos que termine la animación para posicionar la nueva al frente
            setTimeout(() => {
                targetCard.classList.add('active');
                cardIndex.classList.remove('send-back');
            }, 550);
        }
    });
});

// Evento para regresar desde cualquier Carta hacia el Índice
backButtons.forEach(button => {
    button.addEventListener('click', () => {
        const currentCard = button.closest('.card');
        
        if (currentCard) {
            // Mandamos la carta actual hacia atrás del mazo
            currentCard.classList.add('send-back');
            currentCard.classList.remove('active');
            
            // Volvemos a traer el Índice al frente
            setTimeout(() => {
                cardIndex.classList.add('active');
                currentCard.classList.remove('send-back');
            }, 550);
        }
    });
});