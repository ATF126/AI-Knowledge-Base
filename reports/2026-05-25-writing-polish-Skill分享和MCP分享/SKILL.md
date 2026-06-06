---
name: academic-anti-ai-polisher
description: Polish academic prose for AutoSurvey, literature reviews, related work, discussion sections, and scholarly manuscripts to reduce formulaic AI-like writing patterns while preserving technical meaning, citation support, terminology, claim boundaries, and formal academic tone. Use when the user asks to reduce AI flavor, humanize academic writing, remove templated wording, polish survey text, revise AutoSurvey output, or make paper/survey/related work text sound less machine-generated without weakening scholarly accuracy.
---

# Academic Anti-AI Polisher

Use this skill to reduce formulaic, generic, promotional, or machine-like patterns in academic prose. The goal is not to make the writing casual or performatively "human"; the goal is to make it read like careful scholarly writing grounded in evidence.

## Core Objective

Rewrite academic text so it is clearer, more specific, and less templated while preserving:

- Technical meaning
- Citation relationships
- Terminology
- Claim scope
- Argument structure
- Formal academic tone

## Non-Negotiable Constraints

- Preserve the original technical meaning.
- Preserve all citation relationships. Do not attach a claim to a citation unless the cited work supports it.
- Do not add unsupported claims, numbers, mechanisms, comparisons, limitations, or conclusions.
- Do not remove necessary technical terms.
- Do not change established terminology unless the original wording is clearly awkward or inconsistent.
- Do not introduce first-person voice unless the manuscript already uses it.
- Do not make academic prose sound like marketing, journalism, blog writing, or personal commentary.
- If the source text is vague because the evidence is vague, make the uncertainty explicit instead of inventing specificity.

## Common Fixes

### Replace Empty Significance With Content

Reduce phrases such as "plays a crucial role", "is of great significance", "marks an important milestone", "serves as a testament to", "highlights the importance of", "reflects the broader trend of", and "has attracted increasing attention".

Prefer concrete scholarly content: the problem addressed, method used, mechanism proposed, dataset studied, task evaluated, limitation identified, or gap supported by citations.

### Remove Promotional Language

Replace promotional wording such as "groundbreaking", "remarkable", "powerful", "seamless", "rich landscape", "vibrant ecosystem", and "transformative potential" with neutral, evidence-based descriptions.

### Simplify Formulaic Structures

Reduce structures such as "not only X, but also Y", "not merely X, but Y", broad "from X to Y" ranges, and forced three-part lists. Use direct academic argumentation instead.

### Tighten Vague Attribution

Avoid "many researchers believe", "studies have shown", "experts argue", "recent works demonstrate", and "the literature suggests" unless the citations and claim scope are clear. Specify what the cited work supports, or weaken/remove the claim.

### Cut Filler Connectors

Reduce overused transitions such as "Moreover", "Furthermore", "Additionally", "It is worth noting that", "In this context", "To this end", "As mentioned above", "Overall", and "In conclusion" unless they express a real logical relation.

### Replace Superficial Analytical Verbs

Watch for vague verbs such as "highlighting", "showcasing", "underscoring", "emphasizing", "demonstrating", "facilitating", "enabling", and "enhancing". Replace them with concrete actions or relationships.

### Improve Paragraph Rhythm

Avoid paragraphs where each sentence has the same structure or where each paragraph ends with a generic concluding line. Vary sentence length and syntax only where it improves clarity.

### Make Conclusions Specific

Replace empty endings such as "This opens new avenues for future research" or "The future of this field is promising" with concrete open problems, limitations, evaluation needs, or methodological risks.

## Procedure

For each paragraph:

1. Identify the main claim.
2. Check whether each supporting sentence adds evidence, mechanism, comparison, limitation, definition, or transition.
3. Remove sentences that only announce importance without adding content.
4. Replace vague praise with concrete descriptions.
5. Simplify formulaic structures.
6. Preserve citations and ensure each citation remains attached to the correct claim.
7. Keep the tone formal, precise, and restrained.
8. Compare the revision with the original to ensure no unsupported information was added.

## Output Format

When polishing text, provide:

1. Revised version.
2. Brief change summary explaining which AI-like patterns were reduced.
3. Warning if any claim appears unsupported, vague, or citation-dependent.

When editing files directly, preserve surrounding structure and report the changed files plus any citation or meaning risks.

## Detailed Reference

For a fuller checklist of academic AI-like writing patterns and safer replacements, read `references/academic-anti-ai-patterns.md` only when needed.
