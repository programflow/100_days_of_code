import random

def simulate_b_less_y_less_r(trials=10000):
    count_success = 0

    for _ in range(trials):
        B = random.randint(1, 6)
        Y = random.randint(1, 6)
        R = random.randint(1, 6)
        if B < Y < R:
            count_success += 1

    return count_success / trials

# Run the simulation
estimated_probability = simulate_b_less_y_less_r()
print(f"Estimated P(B < Y < R): {estimated_probability:.4f}")
