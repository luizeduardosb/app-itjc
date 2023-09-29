function openMenu() {
  var dropdown = document.querySelector('.dropdown');
  dropdown.classList.toggle('open'); // qnd a função é chamada a classe é adicionada 
}

var menuIcon = document.querySelector('.drop');
menuIcon.addEventListener('click', openMenu); // monitoramento do botão .drop


document.addEventListener('click', function (event) {
  var dropdown = document.querySelector('.dropdown');
  var menuIcon = document.querySelector('.drop');

  if (!dropdown.contains(event.target) && !menuIcon.contains(event.target)) {
    openMenu();
  }// monitorando algum click fora do menu para fechar ele

  if (event.target.tagName === 'P' && dropdown.contains(event.target)) {
    openMenu();
  }// monitorando algum click em uma tag p
}); 


