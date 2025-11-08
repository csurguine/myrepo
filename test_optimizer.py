#!/usr/bin/env python3
"""
Test script for prompt optimizer core functions.
Tests functions that don't require OpenAI API access.
"""

import sys
sys.path.insert(0, '/home/runner/work/myrepo/myrepo')

from prompt_optimizer import (
    measure_efficiency,
    measure_entropy,
    measure_alignment,
    measure_robustness,
    similarity,
    composite_elegance,
    mutate_prompt
)

def test_measure_efficiency():
    """Test efficiency metric"""
    prompt = "Summarize this text"
    output = "Here is a summary with more words"
    efficiency = measure_efficiency(prompt, output)
    assert 0 <= efficiency <= 1, f"Efficiency should be between 0 and 1, got {efficiency}"
    print(f"✓ test_measure_efficiency passed: {efficiency:.3f}")

def test_measure_entropy():
    """Test entropy/consistency metric"""
    outputs = ["hello world", "hello world", "hello world"]
    entropy = measure_entropy(outputs)
    assert 0 <= entropy <= 1, f"Entropy should be between 0 and 1, got {entropy}"
    print(f"✓ test_measure_entropy passed: {entropy:.3f}")

def test_measure_alignment():
    """Test alignment metric"""
    output = "This is a concise and clear summary"
    keywords = ["concise", "clear", "summary"]
    alignment = measure_alignment(output, keywords)
    assert alignment == 1.0, f"Expected 1.0 alignment, got {alignment}"
    print(f"✓ test_measure_alignment passed: {alignment:.3f}")

def test_similarity():
    """Test similarity function"""
    a = "hello world foo bar"
    b = "hello world baz qux"
    sim = similarity(a, b)
    assert 0 <= sim <= 1, f"Similarity should be between 0 and 1, got {sim}"
    print(f"✓ test_similarity passed: {sim:.3f}")

def test_measure_robustness():
    """Test robustness metric"""
    prompt = "Test prompt"
    base_output = "hello world foo"
    test_variants = ["hello world bar", "hello world baz"]
    robustness = measure_robustness(prompt, base_output, test_variants)
    assert 0 <= robustness <= 1, f"Robustness should be between 0 and 1, got {robustness}"
    print(f"✓ test_measure_robustness passed: {robustness:.3f}")

def test_composite_elegance():
    """Test composite elegance score"""
    prompt = "Summarize this"
    outputs = ["concise summary", "concise summary", "clear summary"]
    keywords = ["concise", "clear"]
    score = composite_elegance(prompt, outputs, keywords)
    assert 0 <= score <= 1, f"Composite score should be between 0 and 1, got {score}"
    print(f"✓ test_composite_elegance passed: {score:.3f}")

def test_mutate_prompt():
    """Test prompt mutation"""
    prompt = "This is a test prompt with several words"
    mutated = mutate_prompt(prompt)
    assert isinstance(mutated, str), "Mutated prompt should be a string"
    # Mutation might or might not change the prompt
    print(f"✓ test_mutate_prompt passed: '{prompt}' -> '{mutated}'")

def test_edge_cases():
    """Test edge cases"""
    # Empty strings
    assert measure_efficiency("", "") >= 0
    assert measure_entropy([""]) >= 0
    assert measure_alignment("", []) >= 0
    assert similarity("", "") >= 0
    
    # Single word
    assert mutate_prompt("hello") == "hello" or mutate_prompt("hello") == ""
    
    print("✓ test_edge_cases passed")

if __name__ == "__main__":
    print("Running prompt optimizer tests...\n")
    
    test_measure_efficiency()
    test_measure_entropy()
    test_measure_alignment()
    test_similarity()
    test_measure_robustness()
    test_composite_elegance()
    test_mutate_prompt()
    test_edge_cases()
    
    print("\n✅ All tests passed!")
