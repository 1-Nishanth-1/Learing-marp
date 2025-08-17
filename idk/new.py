# Author: 23f2002133@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64
import inspect

# Sample dataset (replace with your CSV file if needed)
data = """employee_id,department,region,performance_score,years_experience,satisfaction_rating
EMP001,Marketing,Asia Pacific,82.1,14,3.1
EMP002,IT,Europe,86.18,6,4.2
EMP003,HR,Middle East,83.22,13,4.1
EMP004,IT,Asia Pacific,75.85,8,3.3
EMP005,IT,Africa,83.25,9,4.9
EMP006,HR,Europe,79.4,11,3.8
EMP007,Marketing,Asia Pacific,91.5,5,4.5
EMP008,Finance,North America,87.3,7,4.7
EMP009,HR,Africa,81.6,10,4.0
EMP010,Finance,Europe,84.2,9,3.9
"""

# Load dataset
from io import StringIO
df = pd.read_csv(StringIO(data))

# Frequency count for HR department
hr_count = (df['department'] == 'HR').sum()
print("Frequency count of HR department:", hr_count)

# Create histogram
plt.figure(figsize=(8,5))
sns.countplot(data=df, x="department", palette="Set2")
plt.title("Department Distribution of Employees")
plt.xlabel("Department")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()

# Convert plot to base64 image
buf = BytesIO()
plt.savefig(buf, format="png")
buf.seek(0)
img_base64 = base64.b64encode(buf.read()).decode("utf-8")
buf.close()

# Get the source code of this script
source_code = inspect.getsource(inspect.currentframe().f_code)

# Create HTML content with code + result
html_content = f"""
<html>
<head><title>Employee Performance Analysis</title></head>
<body>
<h2>Employee Performance Analysis</h2>
<p><b>Email:</b> 23f2002133@ds.study.iitm.ac.in</p>
<p><b>Frequency count of HR department:</b> {hr_count}</p>
<h3>Python Code Used:</h3>
<pre style="background:#f4f4f4; padding:10px; border-radius:5px; overflow-x:auto;">{source_code}</pre>
<h3>Department Histogram:</h3>
<img src="data:image/png;base64,{img_base64}" alt="Department Histogram"/>
</body>
</html>
"""

# Save HTML file
with open("employee_performance_analysis.html", "w") as f:
    f.write(html_content)

print("HTML file 'employee_performance_analysis.html' generated successfully.")
