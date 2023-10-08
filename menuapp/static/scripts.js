document.addEventListener('DOMContentLoaded', function () {
    // Получаем все пункты меню, у которых есть дочерние элементы
    const menuItemsWithChildren = document.querySelectorAll('li > a[href="javascript:void(0)"]');

    menuItemsWithChildren.forEach(function (menuItem) {
        menuItem.addEventListener('click', function (event) {
            // Находим ближайший родительский элемент li
            const parentLi = event.target.closest('li');
            // Находим дочерний ul
            const childUl = parentLi.querySelector('ul');
            // Переключаем видимость
            childUl.style.display = (childUl.style.display === 'none' || childUl.style.display === '') ? 'block' : 'none';
        });
    });
});