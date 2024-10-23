import csv
import random

def estimate_annual_income(engagement_level, location):
    income_ranges = {
        ('High', 1): (80000, 150000),
        ('High', 0): (60000, 120000),
        ('Medium', 1): (50000, 100000),
        ('Medium', 0): (40000, 80000),
        ('Low', 1): (30000, 70000),
        ('Low', 0): (0, 50000)
    }
    
    min_income, max_income = income_ranges.get((engagement_level, location), (0, 0))
    estimated_income = random.randint(min_income, max_income)
    
    return estimated_income

def process_csv(input_file, output_file):
    conv = {"Europe" : 1, "USA": 1 , "Asia":0, "Other":0}
    
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ['EstimatedAnnualIncome']
        
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in reader:
            engagement_level = row['EngagementLevel']
            co = conv[row['Location']]
            
            estimated_income = estimate_annual_income(engagement_level, co)
            row['EstimatedAnnualIncome'] = estimated_income
            
            writer.writerow(row)

    print(f"Processing complete. Results saved to {output_file}")

input_file = 'online_gaming_behavior_dataset.csv'
output_file = 'online_gaming_behavior_dataset_updated.csv'
process_csv(input_file, output_file)