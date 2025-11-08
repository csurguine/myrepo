# Autonomous Interactive Prompt Optimizer

An intelligent system that uses genetic algorithms and elegance metrics to optimize prompts for large language models (LLMs).

## Overview

This prompt optimizer uses evolutionary algorithms to iteratively improve prompts based on multiple quality metrics:
- **Efficiency**: Output conciseness relative to prompt length
- **Entropy/Consistency**: Consistency of outputs across multiple runs
- **Alignment**: Match with desired reference keywords
- **Robustness**: Stability of outputs under repeated sampling

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Before running, configure your OpenAI API key:

```bash
export OPENAI_API_KEY='your-api-key-here'
```

### Advanced Configuration

For advanced configuration, copy the example config file and customize:

```bash
cp config.example.py config.py
# Edit config.py with your preferred settings
```

You can also modify the following parameters in `prompt_optimizer.py`:
- `MODEL`: The GPT model to use (default: "gpt-4")
- `POP_SIZE`: Number of prompt variants per generation (default: 10)
- `GENERATIONS`: Number of optimization iterations (default: 50)
- `MUTATION_RATE`: Probability of mutation (default: 0.3)
- `TOP_K`: Number of top prompts retained each generation (default: 3)

## Usage

### Demo (No API Key Required)

Run the demo to see how the metrics work without needing OpenAI API access:

```bash
python demo.py
```

### Basic Usage

Run the optimizer with default settings:

```bash
python prompt_optimizer.py
```

### Programmatic Usage

```python
from prompt_optimizer import optimize_prompt

# Define your base prompt and reference keywords
base_prompt = "Summarize any text into concise, clear bullet points that retain all essential meaning."
reference_keywords = ["concise", "clear", "summary"]

# Optimize the prompt
optimized_prompt = optimize_prompt(base_prompt, reference_keywords)
print("Optimized Prompt:", optimized_prompt)
```

## How It Works

1. **Initialization**: Creates a population of prompt variants through mutation
2. **Evaluation**: Each prompt is tested multiple times and scored on elegance metrics
3. **Selection**: Top-performing prompts are retained
4. **Reproduction**: New variants are created from successful prompts
5. **Iteration**: Process repeats for specified generations
6. **Result**: Returns the best-scoring prompt from all generations

## Elegance Metrics

The composite elegance score is calculated as:
```
Score = 0.3 × Efficiency + 0.2 × Consistency + 0.3 × Alignment + 0.2 × Robustness
```

## Features

- **Genetic Algorithm**: Evolutionary approach to prompt optimization
- **Multi-metric Evaluation**: Balances multiple quality dimensions
- **Memory System**: Retains best prompts across all generations
- **Configurable**: Easy to adjust hyperparameters
- **Extensible**: Add custom metrics or mutation strategies

## Requirements

- Python 3.7+
- OpenAI API key
- Dependencies listed in requirements.txt

## License

MIT
