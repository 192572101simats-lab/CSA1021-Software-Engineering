# Python equivalent of the RAPTOR flowchart (Exp 5)
# Swap every occurrence of ch1 with ch2 (and vice versa), at most once.
def swap_chars(s, ch1, ch2):
    out = []
    i, n = 0, len(s)
    while i < n:                    # Loop  i <= n
        c = s[i]
        if c == ch1:                # Selection 1
            out.append(ch2)
        elif c == ch2:              # Selection 2
            out.append(ch1)
        else:
            out.append(c)
        i += 1                      # i <- i + 1
    return "".join(out)

def smallest_pair(s):
    """First char that has a smaller char later, paired with the smallest such char."""
    for i, c in enumerate(s):
        later = [x for x in s[i + 1:] if x < c]
        if later:
            return c, min(later)
    return None

if __name__ == "__main__":
    for s in ["ccad", "abcd", "dcba", "bbaac"]:
        pair = smallest_pair(s)
        if pair is None:
            print(f"str = {s:6} no swap needed          -> {s}")
        else:
            ch1, ch2 = pair
            print(f"str = {s:6} ch1 = {ch1}, ch2 = {ch2} -> Modified string = {swap_chars(s, ch1, ch2)}")
