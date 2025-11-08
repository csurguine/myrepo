import random
import numpy as np

try:
    import openai
except ImportError:
    openai = None

# ---------- CONFIGURATION ----------
MODEL = "gpt-4"  # Replace with actual deployed model name
POP_SIZE = 10     # Number of prompt variants per generation
GENERATIONS = 50  # Iterations
MUTATION_RATE = 0.3
TOP_K = 3         # Number of top prompts retained

# ---------- ELEGANCE METRICS ----------
def measure_efficiency(prompt, output):
    """
    Measure prompt efficiency as the ratio of output length to total length.
    Higher values indicate more concise outputs relative to input.
    """
    prompt_len = len(prompt.split())
    output_len = len(output.split())
    total_len = prompt_len + output_len
    
    if total_len == 0:
        return 0.0
    
    return output_len / total_len

def measure_entropy(outputs):
    """
    Estimate consistency via token diversity across runs.
    Lower diversity indicates more consistent outputs.
    """
    # Estimate consistency via token diversity across runs
    all_tokens = " ".join(outputs).split()
    if len(all_tokens) == 0:
        return 0
    unique_ratio = len(set(all_tokens)) / len(all_tokens)
    return 1 - unique_ratio  # lower diversity = more consistent

def measure_alignment(output, reference_keywords):
    """
    Measure how well the output aligns with reference keywords.
    Returns the proportion of keywords found in the output.
    """
    if len(reference_keywords) == 0:
        return 1.0
    hits = sum(kw in output for kw in reference_keywords)
    return hits / len(reference_keywords)

def measure_robustness(prompt, base_output, test_variants):
    """
    Measure robustness by comparing similarity of outputs across multiple runs.
    Higher values indicate more consistent behavior.
    """
    if len(test_variants) == 0:
        return 1.0
    diffs = [similarity(base_output, o) for o in test_variants]
    return np.mean(diffs)

def similarity(a, b):
    """
    Calculate Jaccard similarity between two strings.
    Returns value between 0 and 1.
    """
    tokens_a = set(a.split())
    tokens_b = set(b.split())
    if len(tokens_a | tokens_b) == 0:
        return 1.0
    return len(tokens_a & tokens_b) / len(tokens_a | tokens_b)

def composite_elegance(prompt, outputs, reference_keywords):
    """
    Compute composite elegance score from multiple metrics.
    Weights: 30% efficiency, 20% consistency, 30% alignment, 20% robustness
    """
    eff = measure_efficiency(prompt, outputs[0])
    ent = measure_entropy(outputs)
    align = measure_alignment(outputs[0], reference_keywords)
    robust = measure_robustness(prompt, outputs[0], outputs[1:])
    return 0.3*eff + 0.2*(1-ent) + 0.3*align + 0.2*robust

# ---------- PROMPT OPTIMIZATION LOOP ----------
def optimize_prompt(base_prompt, reference_keywords):
    """
    Optimize a prompt using a genetic algorithm approach.
    
    Args:
        base_prompt: Initial prompt to optimize
        reference_keywords: List of keywords to align with
    
    Returns:
        Best optimized prompt found
    """
    population = [base_prompt] + [mutate_prompt(base_prompt) for _ in range(POP_SIZE-1)]
    memory = []

    for g in range(GENERATIONS):
        scored = []
        for prompt in population:
            outputs = [call_gpt(prompt) for _ in range(3)]
            score = composite_elegance(prompt, outputs, reference_keywords)
            scored.append((score, prompt))
        
        scored.sort(reverse=True)
        best = scored[:TOP_K]
        memory.extend(best)
        
        parents = [p for _, p in best]
        population = parents + [mutate_prompt(random.choice(parents)) for _ in range(POP_SIZE - TOP_K)]

    best_prompt = max(memory, key=lambda x: x[0])[1]
    return best_prompt

# ---------- SUPPORT FUNCTIONS ----------
def mutate_prompt(prompt):
    """
    Mutate a prompt by randomly dropping words to explore brevity.
    
    Args:
        prompt: The prompt string to mutate
    
    Returns:
        Mutated prompt string
    """
    words = prompt.split()
    if len(words) == 0:
        return prompt
    if random.random() < MUTATION_RATE and len(words) > 1:
        # Drop or swap words randomly to explore brevity
        idx = random.randint(0, len(words)-1)
        words.pop(idx)
    return " ".join(words)

def call_gpt(prompt):
    """
    Call GPT API with the given prompt.
    
    Args:
        prompt: The prompt to send to the model
    
    Returns:
        Generated response text
    """
    if openai is None:
        raise ImportError("OpenAI package not installed. Install with: pip install openai")
    
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=300
    )
    return response["choices"][0]["message"]["content"]

# ---------- EXECUTION ----------
if __name__ == "__main__":
    base_prompt = "Summarize any text into concise, clear bullet points that retain all essential meaning."
    reference_keywords = ["concise", "clear", "summary"]
    optimized_prompt = optimize_prompt(base_prompt, reference_keywords)
    print("Optimized Prompt:", optimized_prompt)
