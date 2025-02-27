// Когда DOM загрузится, выполним некоторый код
document.addEventListener('DOMContentLoaded', function() {
  console.log('Страница загружена!');

  // Пример: Найдем кнопку с id="my-button" и повесим alert на клик
  const myButton = document.getElementById('my-button');
  if (myButton) {
      myButton.addEventListener('click', function() {
          alert('Вы нажали на кнопку!');
      });
  }
});
