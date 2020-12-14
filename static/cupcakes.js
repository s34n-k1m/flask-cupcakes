"use strict";

const $cupcakesList = $("#cupcakes-list");

const API_BASE_URL = "http://localhost:5000/api"
/* Function makes an API request to get cupcakes in the database
*/
async function getCupcakes() {
  const response = await axios.get(`${API_BASE_URL}/cupcakes`);

  return response.data.cupcakes;
}

/* Function takes the cupcakes data and appends the information 
to the list in the DOM */
function displayCupcakes(cupcakes) {

  for (let cupcake of cupcakes) {
    const $cupcake = $(`<li>
      <img src="${cupcake.image}" alt="Image of ${cupcake.flavor}">
      <div>
          ${cupcake.flavor} ${cupcake.size} ${cupcake.rating}
      </div>
      </li>`);

    $cupcakesList.append($cupcake);
  }
}

/* Function that runs when page is loaded. Gets the cupcakes data
from the API and displays the cupcakes in the DOM */
async function start() {
  let cupcakes = await getCupcakes();

  displayCupcakes(cupcakes);
}

start();