document.addEventListener('DOMContentLoaded', () => {
    const cookieBanner = document.getElementById('cookieBanner');
    const allowCookies = document.getElementById('allowCookies');
    const configureCookies = document.getElementById('configureCookies');

    if (localStorage.getItem('bbCookiesAccepted') === '1') {
        cookieBanner?.remove();
    }

    allowCookies?.addEventListener('click', () => {
        localStorage.setItem('bbCookiesAccepted', '1');
        cookieBanner?.remove();
    });

    configureCookies?.addEventListener('click', () => {
        alert('Aqui você pode abrir o painel de preferências de cookies.');
    });
});
