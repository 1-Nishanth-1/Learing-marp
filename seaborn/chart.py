import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set Seaborn style and context for professional look
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate realistic synthetic data for equipment efficiency analysis
# Let's assume we have data for multiple equipment types over multiple shifts

np.random.seed(42)

equipment_types = ['Press', 'Lathe', 'Milling', 'Welding']
shifts = ['Morning', 'Afternoon', 'Night']

data = []
for eq in equipment_types:
    for shift in shifts:
        # Synthetic data: efficiency rates vary by equipment and shift with some noise
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

        efficiencies = np.random.normal(loc=base_efficiency + shift_modifier, scale=4, size=50)
        # Clip efficiency between 60 and 95 for realism
        efficiencies = np.clip(efficiencies, 60, 95)
        
        for eff in efficiencies:
            data.append({'Equipment': eq, 'Shift': shift, 'Efficiency': eff})

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(8, 8))  # 512x512 pixels at dpi=64

# Violinplot: Equipment on x-axis, Efficiency on y-axis, hue by Shift
sns.violinplot(data=df, x='Equipment', y='Efficiency', hue='Shift', palette='Set2', split=True)

plt.title('Equipment Efficiency Distribution by Shift')
plt.xlabel('Equipment Type')
plt.ylabel('Efficiency Rate (%)')
plt.ylim(55, 100)
plt.legend(title='Shift', loc='upper right')

# Save the figure as 512x512 PNG
plt.savefig('chart.png', dpi=64, bbox_inches='tight')
plt.close()
