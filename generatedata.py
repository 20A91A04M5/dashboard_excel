import pandas as pd
import numpy as np

def generate_sample_data(num_rows=1000):
    """
    Generates random sample data with columns:
    [Category, Month, Sales, Profit].
    Returns a pandas DataFrame.
    """

    # Possible categories and months
    categories = ['Electronics', 'Clothing', 'Home Decor', 'Books', 'Sports']
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # Generate random data
    np.random.seed(42)  # For reproducible random results
    data = {
        'Category': np.random.choice(categories, num_rows),
        'Month': np.random.choice(months, num_rows),
        'Sales': np.random.randint(100, 2000, size=num_rows),
        'Profit': np.random.randint(10, 500, size=num_rows),
    }

    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    # Generate the sample data
    df = generate_sample_data(1000)

    # Save to Excel in the 'project' subfolder
    output_path = 'project/sampledata.xlsx'
    df.to_excel(output_path, index=False)
    print(f"Sample data generated and saved to {output_path}")
