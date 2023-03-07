# Ai_chessbot
This is an entry-level practice with the open-ai plugin; in the future, I will be expanding the use to encompass future machine learning directives such as decision trees and mapping to calculate errobility with the use of linguistic machines. 
This project uses the chess python library and the open ai library to call on the diavollo engine in the gpt3 open source to generate a chess move to be played in the terminal. This required string parsing and other await URL commands to convey the messages back into moves. 
I also used a list to keep track of all of the moves made during the chess match. This design did have one potential flaw: the illegal moves tried by the GPT3 engine. Due to the nature of the chess library whenever a nonlegal move was made, I would terminate and restart the chess match, which when working with multiple attempts, which was a common flaw when using this engine. 
Apart from that, at the time when the moves made were legal, I was able to play a full game against the chat engine.
