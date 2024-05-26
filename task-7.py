import random
import matplotlib.pyplot as plt

def roll_dice():
    return random.randint(1, 6)

def monte_carlo_simulation(num_trials):
    results = [0] * 13
    for _ in range(num_trials):
        sum_of_dice = roll_dice() + roll_dice()
        results[sum_of_dice] += 1
    
    probabilities = [count / num_trials for count in results]
    return probabilities

def print_probabilities(probabilities):
    print("Sum\Probability")
    for sum_of_dice, probability in enumerate(probabilities[2:], start=2):
        print(f"{sum_of_dice}\t{probability * 100:.2f}% ({probability:.4f})")

def plot_probabilities(probabilities):
    plt.figure(figsize=(10, 6))
    plt.bar(range(2, 13), probabilities[2:])
    plt.xlabel('Sum')
    plt.ylabel('Probability')
    plt.title('Probability of sum throwing two dice (the Monte Carlo algorithm 1000000 times)')
    plt.xticks(range(2, 13))
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

num_trials = 1000000
probabilities = monte_carlo_simulation(num_trials)

print_probabilities(probabilities)
plot_probabilities(probabilities)
