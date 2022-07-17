const menumobile = document.getElementById('menumobile');

function toglleMenu(){
    const nav = document.getElementById('navbar');
    navbar.classList.toggle('active');
}
menumobile.addEventListener('click', toglleMenu);
