def find_s_algorithm(training_data): 
    """ 
    Implements the Find-S algorithm. 
     
    Args: 
        training_data: A list of tuples (example, label), where: 
            - example is a list of attribute values. 
            - label is a boolean (True for positive, False for 
negative). 
     
    Returns: 
        The most specific hypothesis (a list) consistent with all 
positive examples. 
        Attributes that differ among positive examples are generalized 
to '?'. 
    """ 
    # Initialize the hypothesis to None (no hypothesis yet) 
    hypothesis = None 
 
    for example, label in training_data: 
        if label:  # Only consider positive examples 
            # For the first positive example, initialize hypothesis to its attribute values. 
            if hypothesis is None: 
                hypothesis = example.copy() 
            else: 
                # Generalize the hypothesis by comparing each attribute. 
                for i in range(len(example)): 
                    if hypothesis[i] != example[i]: 
                        hypothesis[i] = '?'  # Use '?' to denote "any value" 
    return hypothesis 
 
def main(): 
    # Accept number of training instances from user
    n = int(input("Enter number of training examples: "))
    training_data = []

    print("\nEnter training examples one by one:")
    print("Each attribute example should be space-separated, followed by label (True/False)")
    print("Example: Sunny Warm Normal Strong Warm Same True")

    for _ in range(n):
        parts = input().strip().split()
        example = parts[:-1]
        label = parts[-1].lower() == 'true'
        training_data.append((example, label))

    final_hypothesis = find_s_algorithm(training_data) 
    print("Final hypothesis learned by Find-S:") 
    print(final_hypothesis) 

if __name__ == "__main__": 
    main()