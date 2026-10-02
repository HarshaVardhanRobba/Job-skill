---
name: "write-without-ai-tells"
description: "Use when writing or editing any prose the user will send as their own, such as resumes, emails, posts, documentation or reports, to strip the patterns that mark text as machine generated."
---

# Write without AI tells

Apply these rules to any prose the user will send as their own work. They remove the
patterns that readers and detection tools key on. They do not guarantee a detector
outcome, and no rule set can, because those tools misfire in both directions.

## Banned words

delve, tapestry, pivotal, crucial, realm, intricate, nuanced, robust, leverage,
foster, showcase, seamless, holistic, myriad, plethora, embark, elevate, unlock,
harness, underscore, testament, cornerstone, vibrant, breathtaking, stunning,
captivating, world-class, state-of-the-art, cutting-edge, groundbreaking,
game-changing, ever-evolving.

## Banned constructions

- Negative parallelism: "not just X, but Y", "it's not about X, it's about Y".
- Trailing analysis clause: a comma followed by ensuring, highlighting, reflecting,
  showcasing, demonstrating, emphasizing.
- Transition words as connective tissue: moreover, furthermore, additionally,
  consequently, nevertheless, on the other hand, that said, importantly.
- Closing summaries: "In summary", "Overall", "In conclusion", "Ultimately",
  "To sum up". If a piece is short enough to read, it ends without a recap.
- False ranges: "from X to Y" unless both ends are real points on a real scale.
- Editorial throat-clearing: "it's important to note", "it is worth noting".
- Vague attribution: "experts say", "studies show", "some critics argue",
  "research suggests". Name the source or drop the claim.

## Typography

No em dashes. Straight quotes, never curly. No emoji. En dash for numeric ranges,
not a hyphen.

## Formatting

Never write a bullet as a bold label, a colon, then a sentence restating the label.
Sentence case headings, not Title Case. At most one bold phrase per bullet. Prose by
default; use a list only when the content is a real list.

## Rhythm

This matters more than word choice. Vary sentence length deliberately. In any passage
over eight sentences, include at least one under six words and at least one over
twenty five. Even pacing is the strongest machine signal in a text. Do not default to
groups of three; use two, four or five.

## Substance

Concrete nouns and real numbers instead of adjectives. Cut adverbs that do not change
meaning. One idea per sentence. Never invent a statistic, a source or a citation. If a
number is not verified, leave it out.

## Voice

Active voice. Say the thing, then stop. Do not restate the question, do not announce
what you are about to do, and do not close with an offer to help further.

## Checking the draft

If `human_check.py` is available in the working directory or the user's outputs, run
`python3 human_check.py <file>` before delivering. It flags twenty one patterns plus
sentence-length uniformity and exits non-zero when it finds something. Fix every hit,
then rerun. Where a hit is a false positive, such as a phone number read as a date
range, say so rather than silently ignoring it.