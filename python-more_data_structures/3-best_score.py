def best_score(a_dictionary):
    highest_score = (0)  # Initialize with zero
    best_key = None

    for name, score in a_dictionary.items():
        if score > highest_score:
            highest_score = score
            best_key = name
           
    return best_key, highest_score

# Example usage:
a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))

# highest_name, highest_score = best_score(a_dictionary)
# print(f"The highest score is {highest_score} by {highest_name}")