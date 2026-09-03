# Raw DNA input with mixed casing and whitespaces
raw_dna = "  atgTacTGatcGTAGcTagcTag  "

# Step 1: Clean and standardize input (crucial engineering step: normalize data)
dna = raw_dna.strip().upper()

# Step 2: Transcribe
rna = dna.replace("T", "U")

# Step 3: Calculate biological metrics
seq_len = len(dna)
g_count = dna.count("G")
c_count = dna.count("C")
gc_content = ((g_count + c_count) / seq_len) * 100

# Step 4: Display formatted report
print("=" * 35)
print("       SEQUENCE ANALYSIS")
print("=" * 35)
print(f"Cleaned DNA : {dna}")
print(f"RNA Output  : {rna}")
print(f"Length      : {seq_len} bp")
print(f"GC-Content  : {gc_content:.2f}%")
print("=" * 35)