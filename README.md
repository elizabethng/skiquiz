# Mission Ridge Interactive Ski Map & Quiz
#### Video Demo:  [URL](https://youtu.be/d3yJ8I3gk3k)
#### Description:


## Overview
[Mission Ridge](https://www.missionridge.com/) is an alpine ski area located in Wenatchee, Washington. Downhill ski areas typically name their runs to help mountain visitors understand and navigate the terrain. One group of users for whom this is particularly important are ski patrol member. Ski patrol members must know the run names and locations and be able to recall these quickly in case of emergencies and for day-to-day communication.

The Mission Ridge Interactive Ski Map & Quiz is an interactive web application that allows users to test their knowledge and learn about the ski runs at Mission Ridge. This training tool was designed for candidate ski patrollers to help them learn the run names and locations during training.

## Running the App
The app uses the Python framework Flask, Bootstrap, and JavaScript. To run the app locally, the app needs to be downloaded. The user can then navigate to the project root directory and run `flask run` to launch the app.

TODO look into other requirements if not running from already-set up Codespaces environment.

## Structure of the Application
The app is structured around four main pages: homepage, Explore, Run Names, and Run Locations.

### Homepage
The homepage is the landing page for the application. It includes two ways to navigate to the desired page, either through the top navigation bar or through the large buttons on the homescreen. It also includes a labeled, static run map (borrowed from the Mission Ridge website). This allows users to study the map if needed before using any of the interactive pages.

The homepage can be accessed from any other page by clicking the "Mission Ridge" logo on the far left of the navigation page. The logo was also borrowed from the Mission Ridge website.

### Explore
The Explore page allows users to interactively explore the ski area map. The run names have been removed. Hovering over different parts of the map highlights available runs. Clicking the desired run displays the name in the upper left corner of the screen. If an area of the map is selected that is not a run, the page prompts the user to select a run.

### Run Names
The Run Names page provides users with a quiz to test their knowledge of the names of runs. On the map, a random run is highlighted. Users then input names into the form field at the top of the page. An autocomplete function helps them narrow down the possible run names, making it easier to located the correct name.

Once the user has selected a guess, they hit Enter to check if it is correct. If the guess is incorrect, the field empties and is available for another selection.

If the guess is correct, a new random run is loaded and displayed on the map.

### Run Locations
The Run Locations page provides users with a quiz to test their knowledge of the locations of runs. In the left hand corner of the screen, a run is displayed. The user must then select the correct run location on the map.

As the user mouses over potential runs, they are highlighted in blue. Upon click, the run is checked. If it is not correct, the user must continue searching. If the correct run is selected, then a new option is loaded.

## Future Directions
There are a number of ways that I would like to continue development of the app.

### UI and Functionality Updates

- Improve how the user is informed of a correct vs. incorrect guess. It would be ideal to have a color indicator or more prominent indicator of the status of the guess.
- Provide more information about incorrect guesses. To facilitate learning, it would be beneficial to provide the location or name of the incorrect guess, so users get more opportunities to link run names and locations.
- Implement scorekeeping. Either by using session cookies or developing a login framework (and corresponding database), users could track their success rate in both quizzes.
- Implement adaptive quizzing. Once user data is being stored, an adaptive quiz can be developed to help users focus on learning runs they tend to get wrong. Instead of using simple random sampling to suggest quiz questions (currently implemented), the app could weight the sampling by the inverse of the accuracy rate. This would allow users to see more of the runs they get wrong.

### Code and App Structure Updates

- Clean up the html and JavaScript code. Currently, there are repeated instances of functions and other code that could likely be streamlined.
- Improve appearance of the app with better CSS implementation.
- Currently, the SVG for the map is embedded within each page so that the elements can be accessed. It would be ideal to research if this code could be ported into a single file to be referenced, rather than having repeated code.
