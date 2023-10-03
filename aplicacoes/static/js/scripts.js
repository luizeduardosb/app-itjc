function openMenu() {
  var dropdown = document.querySelector('.dropdown');
  dropdown.classList.toggle('open'); // qnd a função é chamada a classe é adicionada 
  if (dropdown.classList.contains('open')) {
    dropdown.style.height = '100vh';
}
}

document.addEventListener('click', function (event) {
  var dropdown = document.querySelector('.dropdown');
  var menuIcon = document.querySelector('.drop');

  if (!dropdown.contains(event.target) && !menuIcon.contains(event.target)) {
    var dropdown = document.querySelector('.dropdown');
    dropdown.classList.remove('open');
  }// monitorando algum click fora do menu para fechar ele

  if (event.target.tagName === 'P' && dropdown.contains(event.target)) {
    openMenu();
  }// monitorando algum click em uma tag p
});


