from .minimization import minimize

def estimate_delay(truth_table, and_delay=2, or_delay=2, not_delay=1):
    minimized = minimize(truth_table, False)
    delay = 0

    if len(minimized) >= 1:
        delay += and_delay

    if len(minimized) > 1:
        delay += or_delay

    for term in minimized:
        if "0" in term:
            delay += not_delay
            break

    print(f"Estimated delay: {delay} ns")
    return delay