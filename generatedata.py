import pandas as pd
import numpy as np

def generate_sample_data(num_rows=1000):
    """
    Generates random sample data with columns:
    [Category, Month, Sales, Profit].
    Returns a pandas DataFrame.
    """

  
    categories = ['Electronics', 'Clothing', 'Home Decor', 'Books', 'Sports']
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    
    np.random.seed(42) 
    data = {
        'Category': np.random.choice(categories, num_rows),
        'Month': np.random.choice(months, num_rows),
        'Sales': np.random.randint(100, 2000, size=num_rows),
        'Profit': np.random.randint(10, 500, size=num_rows),
    }

    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    
    df = generate_sample_data(1000)

   
    output_path = 'project/sampledata.xlsx'
    df.to_excel(output_path, index=False)
    print(f"Sample data generated and saved to {output_path}")
