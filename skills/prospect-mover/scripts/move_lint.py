#!/usr/bin/env python3
"""Flag the mechanical leaks in prospect-facing copy.

  move_lint.py <file> [--json]

Reads plain text or Markdown. Reports em dashes, sender focus (we/our/I vs
you), weak openers, hedges, empty superlatives, pressure words that need a
real reason, stacked asks, long sentences and the reading grade. Exit code 1
when a hard leak is found (em dash, weak opener, sender focus, zero "you").
It catches leaks. It does not score persuasion.
"""
import json
import re
import sys

WEAK_OPENERS = [
    "i hope this finds you", "i hope you are", "i hope you're", "my name is",
    "i wanted to reach out", "i am reaching out", "i'm reaching out",
    "just checking in", "just following up", "sorry to bother", "dear sir",
    "to whom it may concern", "we are a", "we're a", "at our company",
]
HEDGES = ["just", "kind of", "sort of", "maybe", "i think", "possibly",
          "a bit", "hopefully", "perhaps", "i feel like"]
EMPTY = ["best-in-class", "best in class", "world-class", "world class",
         "industry-leading", "industry leading", "cutting-edge", "cutting edge",
         "solutions", "one-stop shop", "synergy", "leverage", "utilize",
         "seamless", "robust", "state-of-the-art", "top-notch", "second to none"]
PRESSURE = ["act now", "limited time", "don't miss out", "last chance",
            "hurry", "only a few left", "expires", "urgent", "today only",
            "before it's too late", "guaranteed", "risk-free", "risk free"]
ASK_PATTERNS = [
    r"\bcall (me|us|now)\b", r"\breply\b", r"\bbook\b", r"\bschedule\b",
    r"\bclick\b", r"\bsign up\b", r"\bregister\b", r"\bbuy\b", r"\bvisit\b",
    r"\btext (me|us|back)\b", r"\bdownload\b", r"\bget (my|your) (quote|number)\b",
    r"\bfill out\b", r"\bsubscribe\b",
]


def words(text):
    return re.findall(r"[A-Za-z']+", text.lower())


def sentences(text):
    flat = re.sub(r"\s+", " ", text)
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", flat) if re.search(r"[A-Za-z]", s)]


def syllables(word):
    w = word.lower().strip("'")
    if len(w) <= 3:
        return 1
    w = re.sub(r"(?:[^laeiouy]es|ed|[^laeiouy]e)$", "", w)
    w = re.sub(r"^y", "", w)
    return max(1, len(re.findall(r"[aeiouy]{1,2}", w)))


def grade(text):
    ws = words(text)
    ss = sentences(text)
    if not ws or not ss:
        return 0.0
    syl = sum(syllables(w) for w in ws)
    return round(0.39 * len(ws) / len(ss) + 11.8 * syl / len(ws) - 15.59, 1)


def phrase_hits(text, phrases):
    low = " " + re.sub(r"\s+", " ", text.lower()) + " "
    hits = []
    for p in phrases:
        n = len(re.findall(r"(?<![a-z])" + re.escape(p) + r"(?![a-z])", low))
        if n:
            hits.append(f"{p} x{n}" if n > 1 else p)
    return hits


def lint(text):
    ws = words(text)
    you = sum(w in ("you", "your", "you're", "yours", "yourself") for w in ws)
    me = sum(w in ("we", "our", "us", "i", "me", "my", "we're", "i'm", "ours") for w in ws)
    first = ""
    for line in text.splitlines():
        line = line.strip().lower()
        if not line or line.startswith(("subject:", "#")):
            continue
        line = re.sub(r"^(hi|hey|hello|dear)\b[^,\n]*,\s*", "", line)
        if line:
            first = line
            break
    opener = [o for o in WEAK_OPENERS if first.startswith(o)]
    long_s = [s for s in sentences(text) if len(words(s)) > 25]
    asks = sorted({p for p in ASK_PATTERNS if re.search(p, text.lower())})
    report = {
        "words": len(ws),
        "em_dashes": text.count("\u2014"),
        "you_count": you,
        "sender_count": me,
        "you_ratio": round(you / me, 2) if me else None,
        "weak_opener": opener,
        "hedges": phrase_hits(text, HEDGES),
        "empty_phrases": phrase_hits(text, EMPTY),
        "pressure_words": phrase_hits(text, PRESSURE),
        "ask_types": len(asks),
        "long_sentences": len(long_s),
        "reading_grade": grade(text),
        "exclamations": text.count("!"),
    }
    hard, soft = [], []
    if report["em_dashes"]:
        hard.append(f"{report['em_dashes']} em dash(es): rewrite (ghost-mode)")
    if opener:
        hard.append(f"weak opener: '{opener[0]}'. Open on the reader")
    if ws and you == 0:
        hard.append("zero 'you': the reader isn't in it")
    elif me and you / me < 1:
        hard.append(f"sender focus: you {you} vs we/I {me}. Aim for 2 to 1")
    elif me and you / me < 2:
        soft.append(f"you {you} vs we/I {me}: close, aim for 2 to 1")
    if report["hedges"]:
        soft.append("hedges: " + ", ".join(report["hedges"]))
    if report["empty_phrases"]:
        soft.append("empty phrases: " + ", ".join(report["empty_phrases"]))
    if report["pressure_words"]:
        soft.append("pressure words, each needs a true stated reason: " + ", ".join(report["pressure_words"]))
    if report["ask_types"] > 2:
        soft.append(f"{report['ask_types']} kinds of ask: keep one")
    if report["long_sentences"]:
        soft.append(f"{report['long_sentences']} sentence(s) over 25 words")
    if report["reading_grade"] > 8:
        soft.append(f"reading grade {report['reading_grade']}: aim for 5 to 7 for consumers")
    if report["exclamations"] > 1:
        soft.append(f"{report['exclamations']} exclamation points: one max")
    report["hard"] = hard
    report["soft"] = soft
    return report


def main(argv):
    if len(argv) < 2:
        sys.exit(__doc__)
    text = open(argv[1], encoding="utf-8").read()
    r = lint(text)
    if "--json" in argv:
        print(json.dumps(r, indent=2))
    else:
        print(f"move-lint: {r['words']} words, grade {r['reading_grade']}, you {r['you_count']} vs we/I {r['sender_count']}")
        for h in r["hard"]:
            print("  HARD  " + h)
        for s in r["soft"]:
            print("  soft  " + s)
        if not r["hard"] and not r["soft"]:
            print("  clean")
    return 1 if r["hard"] else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
