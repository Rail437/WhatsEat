let recipes = document.querySelectorAll('.recipe')
let details = document.querySelector('.details')
details.querySelector('.btn-close').addEventListener('click', function (event) {
    details.style.display = 'none'
})
recipes.forEach(function (recipe) {
    recipe.addEventListener('click', function (event) {
        details.style.display = 'block'
    })
})