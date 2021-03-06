# Provenance (and Directed Acyclic) Graph Query Language
### Background context
https://arxiv.org/pdf/1808.06049.pdf
### Presentation version
https://docs.google.com/presentation/d/1Khc3VdPbi5OVnI3OE-yPni6IApE-H91GREO4hTSUCOc/edit

### Message from the idea maker
A professor at UBC, Margo Seltzer (who did this work at Harvard), did some work in whole-system provenance in the kernel, and what it does is trace the origin of information inside the OS. She said it would be cool to have a DSL that queries a provenance graph. Understanding the research requires a bit of ramp-up so I'm not sure how feasible it is, but it sounded like a sexy idea

### Mentioned graph-querying languages
Steve: https://en.wikipedia.org/wiki/Cypher_Query_Language  
Margo:https://people.seas.harvard.edu/~chong/pubs/pldi15-pidgin.pdf  
Paper: https://arxiv.org/pdf/1806.09339.pdf

### Usage
DAGQL can be run from the command-line using `python3 -m dagql sample.dag`, where `python3` is any Python 3 interpreter, and `sample.dag` is any file containing a DAGQL query. Note that the interpreter provided here is hooked up to mock data for testing purposes, but it can be easily modified to use real data.

### Language reference
The language is briefly explained (with an example!) on the GH wiki pages for this repo.
