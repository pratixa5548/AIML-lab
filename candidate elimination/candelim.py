def more_general(h1, h2): 
    return all(x == "?" or (x != "0" and (x == y or y == "0")) for x, y in zip(h1, h2)) 

def fulfills(example, hypothesis): 
    return all(h == "?" or h == e for h, e in zip(hypothesis, example)) 

def min_generalizations(h, x): 
    new_h = list(h) 
    for i in range(len(h)): 
        if h[i] == "0": 
            new_h[i] = x[i] 
        elif h[i] != x[i]: 
            new_h[i] = "?" 
    return [tuple(new_h)] 

def min_specializations(h, domains, x): 
    results = [] 
    for i in range(len(h)): 
        if h[i] == "?": 
            for val in domains[i]: 
                if val != x[i]: 
                    new_h = list(h) 
                    new_h[i] = val 
                    results.append(tuple(new_h)) 
        elif h[i] != "0": 
            new_h = list(h) 
            new_h[i] = "0" 
            results.append(tuple(new_h)) 
    return results 

def candidate_elimination(examples, domains): 
    n_attributes = len(examples[0][0]) 
    S = {tuple("0" for _ in range(n_attributes))} 
    G = {tuple("?" for _ in range(n_attributes))} 

    for x, label in examples: 
        if label:  # Positive example 
            G = {g for g in G if fulfills(x, g)} 
            S_updated = set() 
            for s in S: 
                if fulfills(x, s): 
                    S_updated.add(s) 
                else: 
                    S_updated.update(min_generalizations(s, x)) 
            S = {s for s in S_updated if any(more_general(g, s) for g in G)} 
        else:  # Negative example 
            S = {s for s in S if not fulfills(x, s)} 
            G_updated = set() 
            for g in G: 
                if fulfills(x, g): 
                    G_updated.update(min_specializations(g, domains, x)) 
                else: 
                    G_updated.add(g) 
            G = {g for g in G_updated if any(more_general(g, s) for s in S)} 

    return S, G 

def main(): 
    num_attrs = int(input("Enter number of attributes: "))
    domains = []
    for i in range(num_attrs):
        dom = input(f"Enter possible values for attribute {i+1} (comma separated): ").split(",")
        domains.append([d.strip() for d in dom])

    num_examples = int(input("Enter number of training examples: "))
    examples = []
    for i in range(num_examples):
        values = input(f"Enter values for example {i+1} (comma separated): ").split(",")
        values = [v.strip() for v in values]
        label = input("Is this a positive example? (y/n): ").strip().lower() == 'y'
        examples.append((values, label))

    S_final, G_final = candidate_elimination(examples, domains)

    print("\nFinal Specific Boundary (S):")
    for s in S_final:
        print(" ", s)
    print("\nFinal General Boundary (G):")
    for g in G_final:
        print(" ", g)

if __name__ == "__main__": 
    main()