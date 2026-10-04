print("complete DNA sequence analyzer")
dna=input("Enter a dna sequence").strip().upper()
if len(dna)==0:
    print("ERROR: You did not enter any sequence!")
count_A=dna.count('A')
count_T=dna.count('T')
count_C=dna.count('C')
count_G=dna.count('G')
total_length=len(dna)
gc_percentage=((count_G+count_C)/total_length)*100
print("\n Nucleotide counts")
print(f"A:{count_A}")
print(f"T:{count_T}")
print(f"C:{count_C}")
print(f"G:{count_G}")
print(f"TOTAL LENGTH:{total_length}")
print("\n GC Analysis")
print(f"GC content:{round(gc_percentage,2)}%")
if gc_percentage<50:
    print("Status : LOW OR MODERATE GC CONTENT. THIS SEQUENCE IS QUITE UNSTABLE")
else:
    print("Status: HIGH GC CONTENT. THIS SEQUENCE IS QUITE STABLE")
