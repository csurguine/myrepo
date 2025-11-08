# Example Configuration for Prompt Optimizer
# Copy this file to config.py and customize as needed

# OpenAI Model Configuration
MODEL = "gpt-4"  # Options: "gpt-4", "gpt-3.5-turbo", etc.

# Genetic Algorithm Parameters
POP_SIZE = 10        # Population size (number of variants per generation)
GENERATIONS = 50     # Number of optimization iterations
MUTATION_RATE = 0.3  # Probability of mutation (0.0 to 1.0)
TOP_K = 3           # Number of top prompts to retain each generation

# Metric Weights (must sum to 1.0)
WEIGHT_EFFICIENCY = 0.3    # Weight for efficiency metric
WEIGHT_CONSISTENCY = 0.2   # Weight for consistency/entropy metric
WEIGHT_ALIGNMENT = 0.3     # Weight for keyword alignment metric
WEIGHT_ROBUSTNESS = 0.2    # Weight for robustness metric

# OpenAI API Parameters
TEMPERATURE = 0.7    # Sampling temperature (0.0 to 2.0)
MAX_TOKENS = 300     # Maximum tokens in response
NUM_SAMPLES = 3      # Number of samples per prompt for evaluation

# Example Usage:
# To use this configuration, you can:
# 1. Copy this file to config.py
# 2. Modify the values above
# 3. Import in your code:
#    from config import *
# 4. Use the values in your optimization
