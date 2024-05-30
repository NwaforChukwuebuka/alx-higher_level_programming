# jQuery DOM Manipulation Project

This project shows how to manipulate the DOM using jQuery, which will be implemented in the AirBNB project.

## Table of Contents

- [Description](#description)
- [Tests](#tests)
- [Tasks](#tasks)
  - [0. No jQuery](#0-no-jquery)
  - [1. With jQuery](#1-with-jquery)
  - [2. Click and Turn Red](#2-click-and-turn-red)
  - [3. Add .red Class](#3-add-red-class)
  - [4. Toggle Classes](#4-toggle-classes)
  - [5. List of Elements](#5-list-of-elements)
  - [6. Change the Text](#6-change-the-text)
  - [7. Star Wars Character](#7-star-wars-character)
  - [8. Star Wars Movies](#8-star-wars-movies)
  - [9. Say Hello!](#9-say-hello)
  - [10. No jQuery - Document Loaded](#10-no-jquery---document-loaded)
  - [11. List, Add, Remove](#11-list-add-remove)
  - [12. Say Hello to Everybody!](#12-say-hello-to-everybody)
  - [13. And Press ENTER](#13-and-press-enter)

## Description

This project includes various tasks that demonstrate how to manipulate the DOM using both vanilla JavaScript and jQuery. The tasks range from simple DOM manipulations to more complex interactions involving API calls.

## Tests ✔️

The `tests` folder contains HTML files used for testing the DOM manipulation scripts.

## Tasks 📃

### 0. No jQuery

**File:** `0-script.js`
- **Description:** Uses `document.querySelector` to update the text color of the HTML tag `HEADER` to red (#ff0).

### 1. With jQuery

**File:** `1-script.js`
- **Description:** Uses jQuery to update the text color of the HTML tag `HEADER` to red (#ff0).

### 2. Click and Turn Red

**File:** `2-script.js`
- **Description:** Uses jQuery to update the text color of the HTML tag `HEADER` to red (#ff0) when the user clicks on the tag `DIV#red_header`.

### 3. Add .red Class

**File:** `3-script.js`
- **Description:** Uses jQuery to add the class `.red` to the HTML tag `HEADER` when the user clicks on the tag `DIV#red_header`.

### 4. Toggle Classes

**File:** `4-script.js`
- **Description:** Uses jQuery to toggle the class of the HTML tag `HEADER` between `.red` and `.green` when the user clicks on the tag `DIV#red_header`.

### 5. List of Elements

**File:** `5-script.js`
- **Description:** Uses jQuery to add an `LI` element to a list when the user clicks on the tag `DIV#add_item`.
- **Detail:** Adds the element `<li>Item</li>` to `UL.my_list`.

### 6. Change the Text

**File:** `6-script.js`
- **Description:** Uses jQuery to update the text of the HTML tag `HEADER` to "New Header!!!" when the user clicks on the tag `DIV#update_header`.

### 7. Star Wars Character

**File:** `7-script.js`
- **Description:** Uses jQuery to fetch the Star Wars API [https://swapi.co/api/people/5/?format=json](https://swapi.co/api/people/5/?format=json) and display the name in the HTML tag `DIV#character`.

### 8. Star Wars Movies

**File:** `8-script.js`
- **Description:** Uses jQuery to fetch and list all movie titles from the Star Wars API [https://swapi.co/api/films/?format=json](https://swapi.co/api/films/?format=json).
- **Detail:** Titles are listed in the HTML tag `UL#list_movies`.

### 9. Say Hello!

**File:** `9-script.js`
- **Description:** Uses jQuery to fetch and display how to say "Hello" in French using the API [https://fourtonfish.com/hellosalut/?lang=fr](https://fourtonfish.com/hellosalut/?lang=fr).
- **Detail:** Displays the translation in the HTML tag `DIV#hello`.
- **Note:** Works when imported in the `HEAD` tag.

### 10. No jQuery - Document Loaded

**File:** `100-script.js`
- **Description:** Uses `document.querySelector` to update the text color of the HTML tag `HEADER` to red (#ff0).
- **Note:** Works when imported in the `HEAD` tag.

### 11. List, Add, Remove

**File:** `101-script.js`
- **Description:** Uses jQuery to add, remove, and clear `LI` elements from a list based on user click input.
- **Detail:** Adds a new element when the user clicks `DIV#add_item`. Adds `<li>Item</li>` to the HTML tag `UL.my_list`. Removes the last element when the user clicks `DIV#remove_item`. Clears all elements when the user clicks `DIV#clear_list`.
- **Note:** Works when imported in the `HEAD` tag.

### 12. Say Hello to Everybody!

**File:** `102-script.js`
- **Description:** Uses jQuery to fetch and display how to say "Hello" in a given language using the API [https://www.fourtonfish.com/hellosalut/hello/](https://www.fourtonfish.com/hellosalut/hello/).
- **Detail:** Fetches the translation for the language entered in the HTML tag `INPUT#language_code`. Fetches the translation when the user clicks on the HTML tag `INPUT#btn_translate`. Displays the translation in the HTML tag `DIV#hello`.
- **Note:** Works when imported in the `HEAD` tag.

### 13. And Press ENTER

**File:** `103-script.js`
- **Description:** Uses jQuery to fetch and display how to say "Hello" in a given language using the API [https://www.fourtonfish.com/hellosalut/hello/](https://www.fourtonfish.com/hellosalut/hello/).
- **Detail:** Identical to `102-script.js` except that the translation is fetched when either the user clicks on the HTML tag `INPUT#btn_translate` or presses ENTER when hovering over the tag `INPUT#language_code`.
