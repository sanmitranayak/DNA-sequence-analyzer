dna_sequence=input("Enter Dna sequence:").upper()
enzyme= input("Enter restriction enzyme(ECORI,BAMHI,HINDIII):")
sites={
    "ECORI":"GAATTC",
    "BAMHI":"GGATCC",
    "HINDIII":"AAGCTT"
}
if enzyme.upper()in sites:
    target_site=sites[enzyme.upper()]
    cut_count=dna_sequence.count(target_site)
    print(f"Enzyme {enzyme} targets:{target_site}")
    print(f"Number of cleavage sites found:{cut_count}")
    if cut_count>0:
         print("The restriction enzyme can successfully cut this DNA sequence.")
    else:
         print("No cleavage sites found for this enzyme.")
else:
     print("Unknown enzyme name.")




