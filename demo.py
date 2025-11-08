#!/usr/bin/env python3
"""
Example/Demo script for the prompt optimizer.

This script demonstrates how to use the prompt optimizer
with mock data (without requiring OpenAI API access).
"""

from prompt_optimizer import (
    measure_efficiency,
    measure_entropy,
    measure_alignment,
    measure_robustness,
    similarity,
    composite_elegance,
    mutate_prompt
)

def demo_metrics():
    """Demonstrate how the elegance metrics work"""
    print("=" * 60)
    print("PROMPT OPTIMIZER METRICS DEMO")
    print("=" * 60)
    
    # Example prompt and outputs
    prompt = "Summarize the key points"
    outputs = [
        "Key points: efficiency, clarity, conciseness",
        "Main ideas: efficiency, clarity, brevity", 
        "Summary: efficient, clear, concise"
    ]
    reference_keywords = ["efficiency", "clarity", "concise"]
    
    print("\n📝 Prompt:", prompt)
    print("📊 Sample Outputs:")
    for i, output in enumerate(outputs, 1):
        print(f"   {i}. {output}")
    print("🎯 Reference Keywords:", reference_keywords)
    
    # Calculate metrics
    print("\n" + "─" * 60)
    print("METRIC CALCULATIONS")
    print("─" * 60)
    
    efficiency = measure_efficiency(prompt, outputs[0])
    print(f"\n⚡ Efficiency: {efficiency:.3f}")
    print(f"   (Output words / Total words)")
    
    entropy = measure_entropy(outputs)
    print(f"\n🔄 Consistency: {1-entropy:.3f} (entropy: {entropy:.3f})")
    print(f"   (Higher = more consistent outputs)")
    
    alignment = measure_alignment(outputs[0], reference_keywords)
    print(f"\n🎯 Alignment: {alignment:.3f}")
    print(f"   (Proportion of keywords found)")
    
    robustness = measure_robustness(prompt, outputs[0], outputs[1:])
    print(f"\n🛡️  Robustness: {robustness:.3f}")
    print(f"   (Similarity across runs)")
    
    composite = composite_elegance(prompt, outputs, reference_keywords)
    print(f"\n⭐ Composite Elegance: {composite:.3f}")
    print(f"   (Weighted: 30% eff + 20% cons + 30% align + 20% robust)")

def demo_mutation():
    """Demonstrate prompt mutation"""
    print("\n\n" + "=" * 60)
    print("PROMPT MUTATION DEMO")
    print("=" * 60)
    
    original = "Please provide a comprehensive and detailed summary of the main ideas"
    print(f"\n📝 Original Prompt:\n   '{original}'")
    print(f"\n🧬 Mutations:")
    
    for i in range(5):
        mutated = mutate_prompt(original)
        print(f"   {i+1}. '{mutated}'")

def demo_similarity():
    """Demonstrate similarity calculations"""
    print("\n\n" + "=" * 60)
    print("SIMILARITY DEMO")
    print("=" * 60)
    
    pairs = [
        ("hello world", "hello world"),
        ("hello world", "hello universe"),
        ("hello world foo bar", "hello world baz qux"),
        ("completely different", "totally unrelated"),
    ]
    
    print("\n📊 Jaccard Similarity Scores:\n")
    for a, b in pairs:
        sim = similarity(a, b)
        print(f"   '{a}' ↔️ '{b}'")
        print(f"   Similarity: {sim:.3f}\n")

def main():
    """Run all demos"""
    print("\n")
    demo_metrics()
    demo_mutation()
    demo_similarity()
    
    print("\n" + "=" * 60)
    print("💡 To use with real OpenAI API:")
    print("=" * 60)
    print("""
1. Install dependencies:
   pip install -r requirements.txt

2. Set your API key:
   export OPENAI_API_KEY='your-key-here'

3. Run the optimizer:
   python prompt_optimizer.py

4. Or use programmatically:
   from prompt_optimizer import optimize_prompt
   best = optimize_prompt(base_prompt, keywords)
    """)
    
    print("\n✅ Demo complete!\n")

if __name__ == "__main__":
    main()
