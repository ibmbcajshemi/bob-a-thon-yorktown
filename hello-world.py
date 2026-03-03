#!/usr/bin/env python3
"""
Hello World Example
A simple Python script to demonstrate GitHub integration
"""

def greet(name: str = "World") -> str:
    """
    Generate a greeting message
    
    Args:
        name: The name to greet (default: "World")
    
    Returns:
        A greeting string
    """
    return f"Hello, {name}!"


def main():
    """Main function"""
    print(greet())
    print(greet("GitHub"))
    print(greet("Bob MCP"))
    
    # Display some info
    print("\n" + "="*40)
    print("GitHub MCP Integration Test")
    print("Repository: bob-a-thon-yorktown")
    print("Status: Successfully connected!")
    print("="*40)


if __name__ == "__main__":
    main()

# Made with Bob
