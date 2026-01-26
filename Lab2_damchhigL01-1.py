"""
Program Name: Restaurant Tip Calculator
Author: Damchhig Lama
Purpose: This program calculates suggested tip amounts for a restaurant bill
         and displays the total bill including a 15% and 20% tip.
Starter Code: None
Date: January 25, 2026
"""

# Prompt the user for the total bill amount
bill_total = float(input("Enter the total amount of your dinner bill: $"))

# Calculate tip amounts
tip_15 = bill_total * 0.15
tip_20 = bill_total * 0.20

# Calculate totals with tips included
total_with_15 = bill_total + tip_15
total_with_20 = bill_total + tip_20

# Display results using f-strings
print(f"\nSuggested 15% tip: ${tip_15:.2f}")
print(f"Total with 15% tip: ${total_with_15:.2f}")

print(f"\nSuggested 20% tip: ${tip_20:.2f}")
print(f"Total with 20% tip: ${total_with_20:.2f}")
