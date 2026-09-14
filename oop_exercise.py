import csv


# TASK 1
class GenomicFeature:
    def __init__(self, chromosome, start, end, strand):
        self.chromosome = chromosome
        self.start = start
        self.end = end
        self.strand = strand

        self.is_usable()

    def is_usable(self):
        if not isinstance(self.chromosome, str) or not self.chromosome.strip():
            raise ValueError("Chromosome must be a non-empty string.")

        if not isinstance(self.start, int) or isinstance(self.start, bool) or self.start < 1:
            raise ValueError("Start must be a positive integer (1-based).")

        if not isinstance(self.end, int) or isinstance(self.end, bool) or self.end < 1:
            raise ValueError("End must be a positive integer (1-based).")

        if self.start > self.end:
            raise ValueError(f"Start ({self.start}) must be <= end ({self.end}).")

        if self.strand not in ("+", "-"):
            raise ValueError("Strand must be '+' or '-'.")

        return True

    def length(self):
        return self.end - self.start + 1

    def overlaps(self, other):
        if not isinstance(other, GenomicFeature):
            return False
        if self.chromosome != other.chromosome:
            return False
        return max(self.start, other.start) <= min(self.end, other.end)

    def describe(self):
        return f"{type(self).__name__} {self.chromosome}:{self.start}-{self.end}({self.strand})"


if __name__ == "__main__":
    a = GenomicFeature("chr1", 1000, 5000, "+")
    b = GenomicFeature("chr1", 4800, 6000, "+")
    c = GenomicFeature("chr2", 1000, 5000, "+")

    print(a.describe())     # GenomicFeature chr1:1000-5000(+)
    print(a.length())        # 4001
    print(a.overlaps(b))     # True
    print(a.overlaps(c))     # False (different chromosome)

    # GenomicFeature("chr1", 5000, 1000, "+") #Testing the error

# git add oop_exercise.py           # nahrání na GitHub (mimo práci)
# git commit -m 'Adding task 1'
# git push



# TASK 2
class Exon(GenomicFeature):
    def __init__(self, chromosome, start, end, strand, exon_number):
        super().__init__(chromosome, start, end, strand)

        if not isinstance(exon_number, int):
            raise ValueError("exon_number must be an integer.")
        self.exon_number = exon_number
        self.exon_number = exon_number

    def describe(self):
        return f"{super().describe()} exon #{self.exon_number}"

if __name__ == "__main__":
    features = [
        GenomicFeature("chr1", 1000, 5000, "+"),
        Exon("chr1", 1000, 1200, "+", 1),
        Exon("chr1", 3000, 3300, "+", 2),
    ]

    for feature in features:
        print(feature.describe())


# TASK 3

class Gene(GenomicFeature):
    def __init__(self, chromosome, start, end, strand, name):
        super().__init__(chromosome, start, end, strand)
        self.name = name
        self.exons = []

        def add_exon(self, exon: Exon):
            self.exons.append(exon)

        def total_exon_length(self):
            return sum([exon.length() for exon in self.exons])

        def describe(self):
            return f"{type(self).__name__} {self.name} {self.chromosome}:{self.start}-{self.end}({self.strand}), {len(self.exons)} exon(s)"


class Variant(GenomicFeature):
    def __init__(self, chromosome, start, end, strand, ref_allele, alt_allele):
        super().__init__(chromosome, start, end, strand)
        self.ref_allele = ref_allele
        self.alt_allele = alt_allele

        def variant_type(self):
            if not isinstance(self.ref_allele, str) or not isinstance(self.alt_allele, str):
                raise ValueError("ref_allele and alt_allele must be strings.")

            len_ref = len(self.ref_allele)
            len_alt = len(self.alt_allele)

            if len_ref == 1 and len_alt == 1:
                return "SNP"
            elif len_alt > len_ref:
                return "insertion"
            elif len_alt < len_ref:
                return "deletion"
            else:
                return "MNV"

        def describe(self):
            return f"{super().describe()} {self.ref_allele}>{self.alt_allele} ({self.variant_type()})"

# TASK 3 - work with the file "oop_data.tsv"
if __name__ == "__main__":
    genes = {}
    gene_list = []
    variants = []

    with open("oop_data.tsv", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue


