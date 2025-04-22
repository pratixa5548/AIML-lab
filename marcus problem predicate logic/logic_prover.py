import nltk
from nltk import logic
from nltk.inference import ResolutionProver

def get_user_input(prompt):
    try:
        return logic.LogicParser().parse(input(prompt))
    except Exception as e:
        print("Invalid input. Please enter a valid logical statement.")
        return get_user_input(prompt)

def main():
    lp = logic.LogicParser()
    
    # Get the number of premises from the user
    num_premises = int(input("Enter the number of premises: "))
    premises = []
    
    for i in range(num_premises):
        premise = get_user_input(f"Enter premise {i+1}: ")
        premises.append(premise)
    
    # Get the goal statement
    goal = get_user_input("Enter the goal statement: ")
    
    print("\nPremises:")
    for p in premises:
        print(" ", p)
    print("\nGoal:")
    print(" ", goal)
    
    # Use the resolution prover
    prover = ResolutionProver()
    if prover.prove(goal, premises):
        print("\nThe goal is proven.")
    else:
        print("\nThe goal could not be proven.")

if __name__ == "__main__":
    main()
