import csv
from collections import defaultdict

def load_data(filename):
    data = []
    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            drug = row['Drug'].strip()
            condition = row['Condition'].strip()
            side_effect = row['SideEffect'].strip()
            data.append((drug, condition, side_effect))
    return data

def analyze_data(data):
    drug_conditions = defaultdict(set)
    drug_sideeffects = defaultdict(set)
    sideeffect_count = defaultdict(int)

    for drug, condition, side_effect in data:
        drug_conditions[drug].add(condition)
        drug_sideeffects[drug].add(side_effect)
        sideeffect_count[side_effect] += 1

    return drug_conditions, drug_sideeffects, sideeffect_count

def print_summary(drug_conditions, drug_sideeffects, sideeffect_count):
    print("=== Drug Summary ===\n")
    for drug in sorted(drug_conditions.keys()):
        print(f"Drug: {drug}")
        print(f"  Used for: {', '.join(drug_conditions[drug])}")
        print(f"  Side Effects: {', '.join(drug_sideeffects[drug])}\n")

    print("=== Most Common Side Effects ===")
    for effect, count in sorted(sideeffect_count.items(), key=lambda x: -x[1]):
        print(f"{effect}: {count} times")

# Main
if __name__ == "__main__":
    filename = "drugs_data.csv"
    data = load_data(filename)
    drug_conditions, drug_sideeffects, sideeffect_count = analyze_data(data)
    print_summary(drug_conditions, drug_sideeffects, sideeffect_count)
