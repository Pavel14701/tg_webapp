window.addEventListener('scroll', function() {
    const stars = document.getElementById('stars');
    stars.style.top = `${window.scrollY}px`;
});