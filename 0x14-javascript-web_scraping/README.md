vaScript Web Scraping Project
This project involves practicing file I/O operations in Node.js and using the NPM request library to interact with various APIs, including Star Wars, JSONPlaceholder, and Twitter.

Tasks
0. Readme
File: 0-readme.js
Description:
A JavaScript script that reads and prints the contents of a file.
Usage:
./0-readme.js <file path>

1. Write me
File: 1-writeme.js
Description:
A JavaScript script that writes a string to a file.
Usage:
./1-writeme.js <file path> <string to write>

2. Status code
File: 2-statuscode.js
Description:
A JavaScript script that displays the status code of a GET request using the request library.
Usage:
./2-statuscode.js <URL to GET>
Output:
code: <status code>

3. Star Wars Movie Title
File: 3-starwars_title.js
Description:
A JavaScript script that uses the Star Wars API to print the title of the Star Wars movie for a given integer episode number.
Usage:
./3-starwars_title.js <episode number>

4. Star Wars Wedge Antilles
File: 4-starwars_count.js
Description:
A JavaScript script that uses the Star Wars API to print the number of movies featuring the character "Wedge Antilles".
Usage:
./4-starwars_count.js http://swapi.co/api/films/

5. Loripsum
File: 5-request_store.js
Description:
A JavaScript script that stores the contents of a webpage in a file.
Usage:
./5-request_store.js <URL to get> <file path to store content in>

6. How Many Completed?
File: 6-completed_tasks.js
Description:
A JavaScript script that uses the JSONPlaceholder API to compute the number of tasks completed per user ID.
Usage:
./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos

7. Who Was Playing in This Movie?
File: 100-starwars_characters.js
Description:
A JavaScript script that uses the Star Wars API to print all characters featured in a given movie.
Usage:
./100-starwars_characters.js <movie ID>

8. Right Order
File: 101-starwars_characters.js
Description:
A JavaScript script that uses the Star Wars API to print all characters featured in a given movie in the same order as they are listed in the characters list of the /films/ response.
Usage:
./101-starwars_characters.js <movie ID>

9. Twitter Auth
File: 102-search_twitter.js
Description:
A JavaScript script that sends a search request to the Twitter API with a given search string. Outputs 5 results in the format [<Tweet ID>] <Tweet text> by <Tweet owner name>.
Usage:
./102-search_twitter.js <search string>
