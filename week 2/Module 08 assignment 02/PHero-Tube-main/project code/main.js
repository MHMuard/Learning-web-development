let currentCategory = null;
let currentSortOrder = 'normal';

const loadData = (category) => {
    if (currentCategory !== category) {
        currentCategory = category;
        clearCards();
        fetchAndDisplayData(category);
        highlightButton(getButtonId(category));
    }
};


const clearCards = () => {
    const cardsContainer = document.querySelector(".cardsContainer");
    cardsContainer.innerHTML = '';
};
let fetchedVideos = [];
const fetchAndDisplayData = (category) => {
    let apiData = {};

    fetch(`https://openapi.programming-hero.com/api/videos/category/${category}`)
        .then((response) => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then((data) => {
            apiData = data;
            displayData(apiData.data);
            fetchedVideos = data;
        })
        .catch((error) => {
            console.error("Error fetching data:", error);
        });
};

const displayData = (data) => {
    let cardsContainer = document.querySelector(".cardsContainer");

    data.forEach((item) => {
        const card = document.createElement("div");
        card.classList.add("itemCard");
        card.innerHTML = `
            <img src=${item.thumbnail} id="thumbnail" alt=${item.others.title} />
            <div class="cardBottom">
                <div class="cardTitle">
                    <img src=${item.authors[0].profile_picture} id="profilePic" alt=${item.authors[0].profile_name} />
                    <p class="title">${item.title}</p>
                </div>
                <div class='verify'>
                    <p class="id">${item.authors[0].profile_name}</p>
                </div>
                <p class="views">${item.others.views} views</p>
            </div>
        `;

        cardsContainer.appendChild(card);

        const verification = card.querySelector(".verify");

        const verifyImage = document.createElement("img");
        verifyImage.src = "fi_10629607.svg";

        if (item.authors[0].verified == true) {
            verification.appendChild(verifyImage);
        }
    });
};

const highlightButton = (buttonId) => {
    document.querySelectorAll('.buttons button').forEach(btn => {
        btn.classList.remove('active');
    });

    const activeButton = document.getElementById(buttonId);
    if (activeButton) {
        activeButton.classList.add('active');
    }
};

const getButtonId = (category) => {
    const idMap = {
        1000: 'allBtn',
        1001: 'musicBtn',
        1003: 'comedyBtn',
    };
    return idMap[category];
};
const showEmpty = () => {
  const emptyContainer = document.getElementById("empty");
  const div = document.createElement("div");
  div.innerHTML = `  <div class="flex flex-col mt-20 items-center justify-center">
  <img src="./img/Icon.png" alt="">
  <h2
    class="mt-8 text-3xl text-center font-bold md:w-[400px] w-[80%] mx-auto"
  >
    Oops!! Sorry, There is no content here
  </h2>
</div>`;
  emptyContainer.appendChild(div);
};


// sorting videos by views
const handleSort = () => {
  isAscending = !isAscending;
  if (!isAscending) {
    document
      .getElementById("sort-container")
      .setAttribute("data-tip", "Highest to Lowest");
  } else {
    document
      .getElementById("sort-container")
      .setAttribute("data-tip", "Lowest to Highest");
  }
  const sortedVideo = sortViews(videos, isAscending);
  displayData(sortedVideo);
};

// hour calculator
const convertTimeToHr = (seconds) => {
    const hour = seconds / 3600;
    const exectHr = Math.floor(hour)
    const min = hour - exectHr;
    const exectMin = Math.floor(min * 60)
    return exectHr;
};
// min calculator
const convertTimeToMin = (seconds) => {
    const hour = seconds / 3600;
    const exectHr = Math.floor(hour)
    const min = hour - exectHr;
    const exectMin = Math.floor(min * 60)
    return exectMin;
};
// Set the default category as "All" when the page loads
window.onload = function() {
    loadData(1000);
};

