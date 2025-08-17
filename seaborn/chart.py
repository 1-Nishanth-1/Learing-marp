import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set Seaborn style and context for professional presentation
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic data for equipment efficiency analysis
np.random.seed(42)

# Define equipment types and shifts
equipment_types = ['Press', 'Lathe', 'Milling', 'Welding']
shifts = ['Morning', 'Afternoon', 'Night']

data = []

# Create synthetic data: simulate efficiency for each equipment type and shift
for eq in equipment_types:
    for shift in shifts:
        base_efficiency = {
            'Press': 75,
            'Lathe': 80,
            'Milling': 78,
            'Welding': 74
        }[eq]

        shift_modifier = {
            'Morning': 2,
            'Afternoon': 0,
            'Night': -3
        }[shift]

        # Generate efficiency values with some random noise
        efficiencies = np.random.normal(loc=base_efficiency + shift_modifier, scale=4, size=50)
        efficiencies = np.clip(efficiencies, 60, 95)  # Limit values to realistic range
        
        for eff in efficiencies:
            data.append({'Equipment': eq, 'Shift': shift, 'Efficiency': eff})

# Convert data to a pandas DataFrame
df = pd.DataFrame(data)

# Set figure size for 8x8 inches and DPI 64, ensuring 512x512 pixels when saved
plt.figure(figsize=(8, 8), dpi=64)  # Set DPI to 64 to achieve 512x512 pixels

# Create the violinplot
sns.violinplot(data=df, x='Equipment', y='Efficiency', hue='Shift', palette='Set2', split=True)

# Add title and labels
plt.title('Equipment Efficiency Distribution by Shift')
plt.xlabel('Equipment Type')
plt.ylabel('Efficiency Rate (%)')
plt.ylim(55, 100)  # Limit the y-axis for better readability

# Save the plot as PNG with the correct dimensions (512x512)
plt.savefig('chart.png', dpi=64, bbox_inches='tight')
plt.close()
