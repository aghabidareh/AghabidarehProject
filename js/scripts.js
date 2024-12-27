function scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function location_href(link){
    return window.location.href = link;
}

const backToTopButton = document.querySelector('.back-to-top');

backToTopButton.addEventListener('mouseover', () => {
    backToTopButton.classList.add('rotating');
});

backToTopButton.addEventListener('animationend', () => {
    backToTopButton.classList.remove('rotating');
});



