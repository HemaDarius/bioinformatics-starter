# A sample DNA coding strand
dna_sequence = "ATGTACTGATCGTAGCTAGCTAG"

# Transcription: replace Thymine (T) with Uracil (U)
rna_sequence = dna_sequence.replace("T", "U")

# Display the output
print("--- Transcription Output ---")
print(f"DNA: {dna_sequence}")
print(f"RNA: {rna_sequence}")