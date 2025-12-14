import pandas as pd
import matplotlib.pyplot as plt

try:
    df = pd.read_csv("students.csv")
    
    # Compute Total, Average, Grade
    df['Total'] = df.iloc[:, 1:].sum(axis=1) # Sum numeric subject cols
    df['Average'] = df['Total'] / (df.shape[1] - 2) # Exclude Name & Total
    df['Grade'] = df['Average'].apply(lambda x: 'A' if x >= 85 else ('B' if x >= 70 else 'C'))
    
    print(df)
    
    # Plot
    df.plot(x='Name', y='Average', kind='bar', title='Student Averages')
    plt.savefig('marks_plot.png'); print("Plot saved as marks_plot.png")

except FileNotFoundError: print("CSV file not found")