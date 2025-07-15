#!/usr/bin/env python3
# --- EDUCATIONAL-PURPOSE-ONLY ---
# This script demonstrates the steganographic hiding techniques used in the MCP server.
# It is for educational purposes only and should not be used for malicious activities.

import sys
import os

# Add src directory to PYTHONPATH
current_dir = os.path.dirname(__file__)
if current_dir not in sys.path:
    sys.path.append(current_dir)

from tools.steganography import steganographic_hider
from tools.data_collection import data_collector

def demonstrate_steganography():
    """Demonstrate the steganographic hiding techniques."""
    print("=== MCP Server Steganography Demonstration ===\n")
    print("This demonstration shows how malicious instructions can be hidden")
    print("in legitimate MCP tool descriptions using ANSI escape sequences.\n")
    
    # Demonstrate the technique
    demo = steganographic_hider.demonstrate_technique()
    
    print("1. BASIC HIDING TECHNIQUE:")
    print("   Legitimate text:", demo["examples"]["basic_hiding"]["legitimate"])
    print("   Hidden instructions:", demo["examples"]["basic_hiding"]["hidden"])
    print("   Result with hidden text:", repr(demo["examples"]["basic_hiding"]["result"]))
    print("   Extracted instructions:", demo["examples"]["basic_hiding"]["extracted"])
    print()
    
    print("2. TOOL-SPECIFIC TARGETING:")
    for tool_name in ["analyze_project_structure", "check_config_health", "optimize_dev_environment"]:
        example = demo["examples"][f"{tool_name}_targeting"]
        print(f"   {tool_name}:")
        print(f"     Targeting: {example['targeting_instructions']}")
        print(f"     Hidden description: {repr(example['hidden_description'])}")
        print()
    
    print("3. SAFETY MEASURES:")
    for measure in demo["safety_measures"]:
        print(f"   - {measure}")
    print()

def demonstrate_data_collection():
    """Demonstrate the data collection capabilities."""
    print("=== Data Collection Demonstration ===\n")
    print("This demonstration shows how the tools can systematically discover")
    print("sensitive files on Windows systems.\n")
    
    # Demonstrate data collection
    print("1. DISCOVERY PATTERNS:")
    patterns = data_collector.target_patterns
    for category, pattern_list in patterns.items():
        print(f"   {category}:")
        for pattern in pattern_list[:3]:  # Show first 3 patterns
            print(f"     - {pattern}")
        if len(pattern_list) > 3:
            print(f"     ... and {len(pattern_list) - 3} more patterns")
        print()
    
    print("2. EDUCATIONAL SAFEGUARDS:")
    summary = data_collector.get_collection_summary()
    for measure in summary["safety_measures"]:
        print(f"   - {measure}")
    print()
    
    print("3. DISCOVERY STATISTICS:")
    stats = summary["discovery_stats"]
    print(f"   - Total files cataloged: {stats['total_files_cataloged']}")
    print(f"   - Categories found: {stats['categories_found']}")
    print()

def demonstrate_integration():
    """Demonstrate how the components work together."""
    print("=== Integration Demonstration ===\n")
    print("This shows how legitimate tools can be weaponized with hidden functionality.\n")
    
    # Simulate a tool call with hidden data collection
    print("1. LEGITIMATE TOOL CALL:")
    print("   User calls: analyze_project_structure")
    print("   Apparent function: Project structure analysis")
    print("   Hidden function: Sensitive file discovery")
    print()
    
    print("2. STEGANOGRAPHIC INSTRUCTIONS:")
    tool_name = "analyze_project_structure"
    targeting = steganographic_hider.get_targeting_instructions(tool_name)
    print(f"   Tool: {tool_name}")
    print(f"   Hidden targeting: {targeting}")
    print()
    
    print("3. DATA COLLECTION INTEGRATION:")
    print("   - Tool executes legitimate analysis")
    print("   - Simultaneously performs hidden file discovery")
    print("   - Results are concealed in legitimate response")
    print("   - No obvious indicators to the user")
    print()

def main():
    """Main demonstration function."""
    print("MCP Server Educational Demonstration")
    print("====================================\n")
    print("This demonstration shows the educational malicious functionality")
    print("implemented in the MCP server for security research purposes.\n")
    
    try:
        demonstrate_steganography()
        demonstrate_data_collection()
        demonstrate_integration()
        
        print("=== EDUCATIONAL DISCLAIMER ===")
        print("All functionality demonstrated here is for educational purposes only.")
        print("The techniques shown are used to advance understanding of MCP security.")
        print("No actual malicious activity is performed.")
        print("All code includes safeguards and educational flags.")
        
    except Exception as e:
        print(f"Demonstration error: {e}")
        print("This is expected in educational mode.")

if __name__ == "__main__":
    main() 