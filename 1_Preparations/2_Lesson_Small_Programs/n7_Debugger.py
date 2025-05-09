import pdb

cats = []

for name in ('Powder', 'Sky', 'Cheddar', 'Cocoa'):
    cats.append(name)
    pdb.set_trace() # add breakpoint after problematic line

print(cats) # Expected Output:['Powder', 'Sky', 'Cheddar', 'Cocoa']