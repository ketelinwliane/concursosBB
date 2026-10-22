document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('registrationForm');
    if (!form) return;

    form.addEventListener('submit', event => {
        const name = document.getElementById('name');
        const email = document.getElementById('email');

        if (!name?.value.trim() || !email?.value.trim()) {
            event.preventDefault();
            alert('Por favor, preencha todos os campos obrigatórios.');
        }
    });
});
