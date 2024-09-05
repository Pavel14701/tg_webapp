const row = document.querySelector('.kanban-row');
const itemWidth = document.querySelector('.kanban-item').offsetWidth + 20; // Ширина элемента + gap
let scrollPosition = 0;

document.querySelector('.scroll-button.left').addEventListener('click', function() {
    scrollPosition = Math.max(scrollPosition - itemWidth * 3, 0);
    row.style.transform = `translateX(-${scrollPosition}px)`;
});

document.querySelector('.scroll-button.right').addEventListener('click', function() {
    const maxScroll = row.scrollWidth - row.clientWidth;
    scrollPosition = Math.min(scrollPosition + itemWidth * 3, maxScroll);
    row.style.transform = `translateX(-${scrollPosition}px)`;
});