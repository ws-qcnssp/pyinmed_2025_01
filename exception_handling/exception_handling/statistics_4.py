def calculate_statistics(values):
    total = sum(values)
    count = len(values)
    mean = total / count
    
    differences = [(value - mean) ** 2 for value in values]
    variance = sum(differences) / count
    return mean, variance

data = [5, 10, 15, 20, 25]
average, variance_value = calculate_statistics(data)
print(f"Mean: {average}, Variance: {variance_value}")

additional_data = []
mean_additional, var_additional = calculate_statistics(additional_data)
print(f"Mean of additional data: {mean_additional}, Variance of additional data: {var_additional}")
