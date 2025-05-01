import random  # برای تولید مقادیر تصادفی در کروموزوم‌ها و جهش

# تابع ارزیابی (محاسبه تعداد برخوردها)
def fitness(chromosome):
    n = len(chromosome)
    clashes = 0
    for i in range(n):
        for j in range(i + 1, n):
            if chromosome[i] == chromosome[j] or abs(chromosome[i] - chromosome[j]) == abs(i - j):
                clashes += 1
    return clashes

# تولید جمعیت اولیه
def create_population(population_size, n):
    return [create_chromosome(n) for _ in range(population_size)]

# تولید کروموزوم اولیه به صورت تصادفی
def create_chromosome(n):
    return [random.randint(0, n - 1) for _ in range(n)]
# انتخاب والدین بر اساس امتیاز تناسب
def select_parents(population):
    return sorted(population, key=lambda x: fitness(x))[:2]

# عملگر ترکیب (Crossover)
def crossover(parent1, parent2):
    n = len(parent1)
    crossover_point = random.randint(0, n - 1)
    return parent1[:crossover_point] + parent2[crossover_point:]

