def clean_sequence(seq: str) -> str:
    """Strip whitespace and convert sequence to uppercase."""
    return seq.strip().upper()


def transcribe(dna: str) -> str:
    """Convert DNA coding strand to mRNA by replacing T with U."""
    return dna.replace("T", "U")


def calculate_gc(dna: str) -> float:
    """Calculate GC percentage of a DNA sequence."""
    if len(dna) == 0:
        return 0.0
    g_count = dna.count("G")
    c_count = dna.count("C")
    return ((g_count + c_count) / len(dna)) * 100


def reverse_complement(dna: str) -> str:
    """
    Generate the reverse complement of a 5' -> 3' DNA strand.
    A <-> T, C <-> G, then read in reverse (3' -> 5' becomes 5' -> 3').
    """
    complement_map = str.maketrans("ATCG", "TAGC")
    complement = dna.translate(complement_map)
    return complement[::-1]  # [::-1] reverses the string in Python


# Test with sample input
sample_input = "  atgTacTGatcGTAGcTagcTag  "
dna = clean_sequence(sample_input)

print("=" * 45)
print("             GENOMIC SEQUENCE REPORT")
print("=" * 45)
print(f"Original 5'->3' DNA : {dna}")
print(f"Reverse Complement  : {reverse_complement(dna)}")
print(f"Transcribed mRNA    : {transcribe(dna)}")
print(f"Length              : {len(dna)} bp")
print(f"GC-Content          : {calculate_gc(dna):.2f}%")
print("=" * 45)