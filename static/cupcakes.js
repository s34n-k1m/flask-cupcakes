"use strict";

const $cupcakesList = $("#cupcakes-list");
const $form = $('#new-cupcake-form')

const API_BASE_URL = "http://127.0.0.1:5000/api"

/* Function makes an API request to get cupcakes in the database
*/

async function getCupcakes() {
  const response = await axios.get(`${API_BASE_URL}/cupcakes`);

  return response.data.cupcakes;
}

/* Function takes the cupcakes data calls displayCupcake on each cupcake */

function displayCupcakes(cupcakes) {
  for (let cupcake of cupcakes) {
   displayCupcake(cupcake);
  }
}

/** Function takes in a single cupcake and create HTML list item, append to 
 * DOM*/ 

function displayCupcake(cupcake) {
  const $cupcake = $(`
    <li>
      <img src="${cupcake.image}" alt="Image of ${cupcake.flavor}">
        <div>
          ${cupcake.flavor} ${cupcake.size} ${cupcake.rating}
        </div>
    </li>`);
  // TODO: return HTML an append in loop (line 22)
  $cupcakesList.append($cupcake);
}


/** Handles a form submission. Takes the submitted data, makes a POST request 
 * to api and displays new cupcake.*/  

async function handleFormSubmit(evt) {
  evt.preventDefault();

  const cupcakeData = {
    flavor: $('#flavor').val(),
    size :$('#size').val(),
    rating: $('#rating').val(),
    image: $('#image-url').val()
  };

  const response = await axios({
    url: `${API_BASE_URL}/cupcakes`,
    method: "POST",
    data: cupcakeData
  });

  displayCupcake(response.data.cupcake);
}


/* Function that runs when page is loaded. Gets the cupcakes data
from the API and displays the cupcakes in the DOM */

async function start() {
  let cupcakes = await getCupcakes();
  displayCupcakes(cupcakes);
}


$form.on('submit', handleFormSubmit);

start();

