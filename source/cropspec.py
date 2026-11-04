import re
from items import L
E = re.escape
# id -> (starts, end, level). Lecture items default to their label needle.
O = {
 "L9.CA": (["^Completeness axiom for"], "auto", "lec"),
 "L10.GM": (["^Geometric meaning"], r"^Proof\.", "lec"),
 "L10.Q": ([r"^Question\. Are the irrationals"], "auto", "lec"),
 "L11.S1": ([r"^1 Motivation for complex"], "auto", "lec"),
 "L11.S2": ([r"^2 Interlude"], "auto", "lec"),
 "L11.EX": ([r"^Examples$"], "auto", "lec"),
 "L11.PR": ([r"^Properties of the conjugate"], "auto", "lec"),
 "L12.PR": ([r"^1 Properties of the complex"], r"^\(xii\) For the triangle", "lec"),
 "L12.PX": ([r"^\(xii\) For the triangle"], r"^Proposition 1\.1", "lec"),
 "L12.P11": ([r"^Proposition 1\.1"], "auto", "lec"),
 "L12.ADD": ([r"^The geometry of addition in C"], r"^The triangle inequality also has", "lec"),
 "L12.TRI": ([r"^The triangle inequality also has"], "auto", "lec"),
 "L12.QEQ": ([r"^Question\. When does equality"], r"^To see the geometry of multiplication", "lec"),
 "L12.MUL": ([r"^To see the geometry of multiplication"], r"^Applying this rule repeatedly", "lec"),
 "L12.DM": ([r"^Applying this rule repeatedly"], "auto", "lec"),
 "L12.QI": ([r"^Question\. What is the effect"], "auto", "lec"),
 "L12.RU": ([r"^To find these roots"], "auto", "lec"),
 "L12.GI": ([r"^Geometric interpretation"], "auto", "lec"),
 "L12.E41": ([r"^Example 4\.1"], "auto", "lec"),
 "L13.R11": ([r"^Remark 1\.1"], r"^Properties$", "lec"),
 "L13.PR": ([r"^Properties$"], "auto", "lec"),
 "L13.MAN": ([r"^Same points"], "auto", "lec"),
 "L14.EX": ([r"^Examples$"], "auto", "lec"),
 "L14.R2": ([r"^Remark 2\."], "auto", "lec"),
 "L14.TPL": ([r"^Proof template"], "auto", "lec"),
 "L14.NEG": ([r"^3 Negating"], "auto", "lec"),
 "L15.R11": ([r"^Remark 1\.1"], r"^Theorem 1\.1", "lec"),
 "L15.EX": ([r"^Examples$"], "auto", "lec"),
 "L15.P3X": ([r"Algebra of limits"], r"^Example 3\.1", "lec"),
 "L16.R12": ([r"^Remark 1\.2"], r"^Examples$", "lec"),
 "L16.EX": [([r"^Examples$"], r"^Figure 1", "lec", None, True), ([r"^\(ii\) x"], r"^Exercise$", "lec")],
 "L16.XR": ([r"^Exercise$"], "auto", "lec"),
 "L16.P21": ([r"^Proposition 2\.1"], "auto", "lec"),
 "L16.R3X": ([r"^Remark 3\.1"], r"^Proposition 3\.2", "lec"),
 "L16.X1": ([r"^Predicting limits"], "auto", "lec"),
 "L16.AP": ([r"^Additional practice"], "auto", "lec"),
 # Homework
 "HW5.1a": ([r"^Problem 1", r"^1\."], "auto", "part"), "HW5.1b": ([r"^Problem 1", r"^2\."], "auto", "part"),
 "HW5.1c": ([r"^Problem 1", r"^3\."], "auto", "part"), "HW5.2a": ([r"^Problem 2", r"^1\."], "auto", "part"),
 "HW5.2b": ([r"^Problem 2", r"^2\."], "auto", "part"), "HW5.3": ([r"^Problem 3"], "auto", "prob"),
 "HW5.3b": ([r"^Problem 3", r"^\(b\)"], "auto", "part"),
 "HW6.1": ([r"^Problem 1"], "auto", "prob"), "HW6.2": ([r"^Problem 2"], "auto", "prob"), "HW6.3": ([r"^Problem 3"], "auto", "prob"),
 "HW6.4a": ([r"^Problem 4", r"^\(a\)"], "auto", "part"), "HW6.4b": ([r"^Problem 4", r"^\(b\)"], "auto", "part"),
 "HW6.4c": ([r"^Problem 4", r"^\(c\)"], "auto", "part"), "HW6.4d": ([r"^Problem 4", r"^\(d\)"], "auto", "part"),
 "HW6.4e": ([r"^Problem 4", r"^\(e\)"], "auto", "part"), "HW6.5": ([r"^Problem 5"], "auto", "prob"), "HW6.5c": ([r"^Problem 5"], "auto", "prob"),
 "HW7.1ab": ([r"^Problem 1"], r"^\(c\)", "prob"), "HW7.1c": ([r"^Problem 1", r"^\(c\)"], "auto", "part"),
 "HW7.2": ([r"^Problem 2"], "auto", "prob"), "HW7.3a": ([r"^Problem 3"], r"^\(b\)", "prob"),
 "HW7.3bc": ([r"^Problem 3", r"^\(b\)"], r"^Problem 4", "part"),
 "HW7.4a": ([r"^Problem 4", r"^\(a\)"], "auto", "part"), "HW7.4b": ([r"^Problem 4", r"^\(b\)"], "auto", "part"),
 "HW7.4c": ([r"^Problem 4", r"^\(c\)"], "auto", "part"), "HW7.5": ([r"^Problem 5"], "auto", "prob"),
 "HW7.6a": ([r"^Problem 6", r"^\(a\)"], "auto", "part"), "HW7.6bc": ([r"^Problem 6", r"^\(b\)"], r"^XXXEND", "part"),
 "HW8.1": ([r"^Problem 1"], "auto", "prob"), "HW8.1b": ([r"^Problem 1", r"^\(b\)"], "auto", "part"),
 "HW8.2": ([r"^Problem 2"], "auto", "prob"), "HW8.2a": ([r"^Problem 2", r"^\(a\)"], "auto", "part"),
 "HW8.3": ([r"^Problem 3"], "auto", "prob"), "HW8.4": ([r"^Problem 4"], "auto", "prob"),
 "HW8.5": ([r"^Problem 5"], "auto", "prob"), "HW8.6": ([r"^Problem 6"], "auto", "prob"),
 "HW9.1a": ([r"^Problem 1", r"^\(a\)"], "auto", "part"), "HW9.1bcd": ([r"^Problem 1", r"^\(b\)"], r"^Problem 2", "part"),
 "HW9.2": ([r"^Problem 2"], "auto", "prob"), "HW9.3": ([r"^Problem 3"], "auto", "prob"),
 "HW9.45": ([r"^Problem 4"], r"^Problem 6", "prob"), "HW9.6a": ([r"^Problem 6", r"^\(a\)"], "auto", "part"),
 "HW9.6b": ([r"^Problem 6", r"^\(b\)"], r"^XXXEND", "part"),
}
# Practice exam parts
for ex in ("PA","PB"):
    for iid in L:
        if not iid.startswith(ex+"."): continue
        key = iid.split(".")[1]  # e.g. 1a, 2, 7c
        m = re.fullmatch(r"(\d)([a-h]?)", key)
        prob, part = m.group(1), m.group(2)
        if part: O[iid] = ([rf"^Problem\s*{prob}\b", rf"^\(\s?{part}\s?\)"], "auto", "part")
        else: O[iid] = ([rf"^Problem\s*{prob}\b"], "auto", "prob")
# PA 2 and others with sub parts kept whole
def spec(iid):
    if iid in O: return O[iid]
    fk, label, needle, text = L[iid]
    return (["^" + E(needle)], "auto", "lec")
