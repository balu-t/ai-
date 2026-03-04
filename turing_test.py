import random

# Simple machine responses
machine_responses = [
    "I am not sure about that.",
    "That is an interesting question.",
    "Can you explain more?",
    "I think it depends on the situation.",
    "I don't have enough information."
]

print("------ Turing Test Simulation ------")

rounds = 3
score = 0

for i in range(rounds):

    print("\nRound", i+1)
    question = input("Judge asks a question: ")

    # randomly choose responder
    responder = random.choice(["Human","Machine"])

    if responder == "Human":
        print("\nHuman, type your response:")
        response = input()
    else:
        response = random.choice(machine_responses)

    print("\nResponse:", response)

    guess = input("\nJudge guess (Human/Machine): ")

    if guess.lower() == responder.lower():
        print("Correct Guess!")
        score += 1
    else:
        print("Wrong Guess!")

print("\nFinal Score:", score,"/",rounds)

if score >= 2:
    print("Judge successfully distinguished responses.")
else:
    print("Machine passed the Turing Test!")