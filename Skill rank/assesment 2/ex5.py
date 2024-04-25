import json

# Read the JSON file
with open('ex5.json', 'r') as file:
    ex5 = json.load(file)

# Find the donut with name Old Fashioned
for donut in ex5:
    if donut['name'] == 'Old Fashioned':
        # Add a new batter named Tea
        donut['batters']['batter'].append({"id": "1005", "type": "Tea"})

# Write the updated dictionary back to the JSON file
with open('ex5.json', 'w') as file:
    json.dump(ex5, file, indent=4)