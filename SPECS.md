# Game subscription
*In order to* start a game
*As a* user
*I want to* join the game

## Scenario I: First user joins a fresh game
*Given* "Jessica" user and a game without players
*When*  "Jessica" joins the game
*Then*  game's player list is "Jessica"

## Scenario II: Second user joins a game with one registred player
*Given* "Robert" user and a game with "Jessica"
*When*  "Robert" joins the game
*Then*  game's player list is "Jessica", "Robert"

## Scenario III: Third user tries to join a game with two registred players
*Given* "Patricia" user and a game with "Jessica", "Robert"
*When*  "Patricia" joins the game
*Then*  An error is raised and game's player list is still "Jessica", "Robert"


# Play a turn
*In order to* try to win the game
*As a* player
*I want to* play a turn

## Scenario I: First player plays first shot
*Given*
* a game with "Jessica", "Robert"
* no shot has been played
* it's "Jessica"'s turn to play
*When* "Jessica" plays in first column
*Then*
* first column contains one "Jessica"'s disc
* all other columns are empties
* it's "Robert"'s turn to play

## Scenario II: Second player tries to play first shot
*Given*
* a game with "Jessica", "Robert"
* no shot has been played
*When* "Robert" plays in first column
*Then*
* an error is raised
* all columns are empties
* it's still "Jessica"'s turn to play
