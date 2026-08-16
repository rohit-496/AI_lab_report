# Predicate Logic: All humans are mortal

people = ["Socrates", "Plato", "Aristotle"]
Human = {"Socrates", "Plato", "Aristotle"}
print("Rohit Nyaupane 4th sem CSIT")

print("Predicate Logic:")
print("Rule: Human(x) -> Mortal(x)\n")

for person in people:
    if person in Human:
        print(f"Human({person}) = True")
        print(f"Mortal({person}) = True")

# Existential quantifier: ∃x Human(x) ∧ Mortal(x)
if any(person in Human for person in people):
    print("\nThere exists a person who is Human and Mortal.")