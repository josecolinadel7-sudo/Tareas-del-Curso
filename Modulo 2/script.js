const sideMenu = document.querySelector('#sideMenu');
const navBar = document.querySelector('nav');
const navLinks = document.querySelectorAll('nav ul');

function openMenu(){
    sideMenu.style.transform = 'translateX(-16rem)';
}
function closeMenu(){
    sideMenu.style.transform = 'translateX(16rem)';
}

window.addEventListener('scroll', ()=>{
    if(scrollY > 50){
        navBar.classList.add('bg-white', 'bg-opacity-50', 'backdrop-blur-lg', 'shadow-sm');
        navLinks.remove('bg-white', 'shadow-sm', 'bg-opacity-50')
    }   else{
        navBar.classList.remove('bg-white', 'bg-opacity-50', 'backdrop-blur-lg', 'shadow-sm');
        navLinks.add('bg-white', 'shadow-sm', 'bg-opacity-50')
    }
})