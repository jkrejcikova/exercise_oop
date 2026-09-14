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

# TASK 2
issubclass(GenomicFeature, str)