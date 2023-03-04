import chess as ch
import openai
from IPython.display import display

openai.api_key = "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"

board = ch.Board()
display(board)
n=0
moves =[]
#setting first move
move = input("\nEnter your move: ")
board.push_san(move)
moves.append(move)
display(board)
start_move=move


complete = openai.Completion.create(
    engine = "davinci",
    n=5,
    max_tokens=6,
    prompt = "Play chess 1."+start_move,
)

text = complete['choices'][0]['text']
print(text)
aimove = text
board.push_san(aimove)
moves.append(aimove)
display(board)

while n!=1:
    move = input("\nEnter your move: ")
    board.push_san(move)
    moves.append(move)
    display(board)
    text = complete(prompt=moves)['choices'][0]['text']
    aimove = text
    if(aimove in board.legal_moves):
        board.push_san(aimove)
        moves.append(aimove)
        display(board)
    else:
        print("Ai error retunr not legal move")
        n=1
    if(board.is_checkmate()):
        n=1
