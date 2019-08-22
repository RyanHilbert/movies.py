# Chisel Software Engineer Assessment for HackerX

Create an application using any of Python, Java, Javascript (Node), that allows users to view and purchase movies.

## Details

The user is presented with a menu with the following choices.

1. List all available movies.
2. Show my movies.
3. Purchase a movie.
4. Show credit balance.

 
### List all available movies.
There is a file called available_movies.json. All of the movies in the file should be displayed to the user, as well as 
the rating and the cost. They should be displayed alphabetically and grouped by genre. 
For Example

    Genre: Action

    title: "Die Hard",
    rating: 8,
    cost: 3

    title: "The Dark Knight",
    rating: 10,
    cost: 2

    title: "The Expendables",
    rating: 5,
    cost: 4

After the movies have been displayed the user should be able to make another selection.

### Show my movies
If the user selects this option they are shown the list of movies in the my_movies.json file. They are also shown
the rating of the movie and a boolean to indicate whether they have watched the movie yet.
After movies have been displayed the user can make another selection from the initial menu.

### Show credit balance
The user is shown their current credit balance and then returned to the selection menu.
The user's inital credit balance is 100 credits. 

### Purchase a movie
The user may choose to puchase a movie. The user must type the name of the movie they wish to purchase. If they already own the movie
the string "You have already purchased this movie" should be displayed and the user is returned to the selection. 
Each time the user purchases a movie the cost of the movie is deducted from their credit balance.
If the user does not have enough credit remaining to purchase the movie, display the string "Not enough credit remaining to purchase this movie".
When a movie is purchased it is added to the my_movies.json file.

## Optional (but bonus points for completion)

### List all available movies in a specific genre.
The user should be able to see the list of available genres, select a genre and is then shown all of the movies in that genre.
This data will come from the available_movies.json file. When the results from the user's selection are displayed, the user 
has the option to make another selection.

### Search for a movie.
The user can search for a movie. If the user selects this option they will be asked to type the name 
of the movie. Both the my_movies.json and available_movies.json files should be checked for possible matches. 
The user must type at least three characters for the search to be valid. If no movie matches the search term, 
display the string "no movies found matching <search_term>". The user is then returned to the initial selection.
If a match or matches are found, these are shown to the user. The user can then chose one of movies in the results to purchase.

## Documentation

Please modify README.md to add instructions on how to run your application, especially if you are using Python libraries that are not built-in.

## Submission Instructions
1. Clone the repository.
2. Complete your project as described above within your local repository.
3. Ensure everything you want to commit is committed.
4. Either
    * Create a git bundle: `git bundle create your_name.bundle --all` and email the bundle file to dev.careers@chisel.ai, OR
    * Host the repository on your own GitHub or Bitbucket account, and send / share the link with dev.careers@chisel.ai

## Evaluation
Evaluation of your submission will be based on the following criteria.

1. How well the applications captures the functionality described in the README.
2. Documentation around the process to setup and run the application.
3. How well the concerns of the application are separated.
4. Are the appropriate data types used for the solution

