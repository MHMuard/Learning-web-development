const loadData = (global) => {
    const searchText = document.getElementById("search-box").value;
    fetch(`https://www.themealdb.com/api/json/v1/1/search.php?f=${searchText? searchText: global}`)
    .then((res) => res.json())
    .then((data) => displayData(data.meals));
}

const displayData = (data) => {
    document.getElementById("total-meal").innerHTML = data.length;
    
    const mealContainer = document.getElementById("meals-container");
    data.forEach((meal) => {
        const card = document.createElement("div");
        card.classList.add("card-box")
        card.innerHTML = `
            <img class="card-img" src=${meal.strMealThumb} alt="">
            <h1>${meal?.strMeal}</h1>
            <p>${meal?.strInstructions.slice(0,50)}</p>
            <button onclick="displaymodal('${meal.idMeal}')" type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
                Details
            </button>
            `;
    
        mealContainer.appendChild(card);
    });

}

const displaymodal = async (id) => {
    console.log(id);
    try {
        const response = await fetch(`https://www.themealdb.com/api/json/v1/1/lookup.php?i=${id}`);
        const data = await response.json();
        console.log(data.meals[0].strInstructions);

    }
    catch{
        (err) => {
            console.log(err);
        };
    }
};
loadData("a");
