function toggleDescription(button, counter) {
    var cardBody = button.parentElement;
    var shortDescription = cardBody.querySelector('#shortDesc_' + counter);
    var fullDescription = cardBody.querySelector('#fullDesc_' + counter);

    if (shortDescription.style.display === 'none') {
        shortDescription.style.display = 'block';
        fullDescription.style.display = 'none';
        button.innerText = 'Details';
    } else {
        shortDescription.style.display = 'none';
        fullDescription.style.display = 'block';
        button.innerText = 'Hide Details';
    }
}
