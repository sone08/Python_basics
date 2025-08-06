scores = {}  # create new empty dict

with open("/Users/onemac/Pyhton_basics/20250721JPMC-PM/DATA/test_scores.txt") as scores_in:
    for line in scores_in:
        parts = line.rstrip().split(":")
        if len(parts) != 2:
            print(f"Malformed line: {line.strip()}")
            continue  # skip malformed lines
        name, score = parts
        scores[name] = int(score)  # store in dict with int value

    # Print names, scores, and letter grades
    for name, score in scores.items():
        if score >= 95:
            grade = 'A'
        elif score >= 89:
            grade = 'B'
        elif score >= 83:
            grade = 'C'
        elif score >= 6075:
            grade = 'D'
        else:
            grade = 'F'
        print(f"{name}: {score} ({grade})")