# Dhodraj Sundaram

**Understanding systems. Building useful software.**

Software engineer and tech lead, about four years in industry. I want to know how a mechanism works, why a design was chosen, and what it does not solve. The graph below maps how those interests connect.

<!-- The graph is generated. Edit the model in assets/knowledge-graph.py, then run: python3 assets/knowledge-graph.py -->
<p align="center">
  <img src="assets/knowledge-graph.svg" width="880" alt="A knowledge graph with Dhodraj Sundaram at the centre and six domains around him: Reasoning, Systems, Tools and AI, Open source, Learning and Product. Each domain holds concepts such as first principles, concurrency, agent orchestration, published packages, measured results and scope cuts. Labelled links cross domains, for example concurrency informs agent orchestration and measured results set scope cuts. Backend architecture, operating systems, distributed systems, networking and how mechanisms work are grey: interests with nothing public yet. Three callouts explain inverse thinking, systems first, and turning insight into workflow. A footer lists six decision rules, from first principles to goals.">
</p>

A filled square means the concept shows in public work. An outlined square means it is started but early. A small grey square means an interest with nothing public behind it yet. The repositories and figures behind the graph are in the sections below.

<!-- Drawn daily by .github/workflows/snake.yml and published to the output branch. -->
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Dhodraj/Dhodraj/output/github-snake-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Dhodraj/Dhodraj/output/github-snake.svg">
    <img alt="My GitHub contribution grid for the past year, animated as a snake that eats each day with contributions." src="https://raw.githubusercontent.com/Dhodraj/Dhodraj/output/github-snake.svg">
  </picture>
</p>

## Selected work

### [colony](https://github.com/Dhodraj/colony)

Runs several Claude Code sessions in parallel as one-task workers in Herdr panes. One Master plans, briefs each worker and checks results; each worker reports a single line to a shared event log. The problem is coordination: a long agent session loses context, and a sub-agent cannot ask you a question. The [design docs](https://github.com/Dhodraj/colony/blob/main/docs/colony.md) are the part worth reading, since they give each decision, its reason and its limits. Python standard library only, 33 KB in one file, 95 test cases against a fake Herdr, MIT.

### [seekly](https://github.com/Dhodraj/seekly)

Searches a codebase from the terminal in plain language, using code-aware embeddings instead of string matching. Published on [PyPI](https://pypi.org/project/seekly/) at 1.1.2. Python, test suite, GitHub Actions, MIT.

### [collectweak](https://github.com/Dhodraj/collectweak) and [deep-freeze-utility](https://github.com/Dhodraj/deep-freeze-utility-pkg)

Two small TypeScript packages with no runtime dependencies: chainable typed extensions to `Map` and `Set`, and recursive object freezing. Both on npm, at `1.0.2-beta.3` and `1.0.2`. They keep the typed-collection and immutability helpers I kept rewriting in one place.

### [pmos-companion](https://github.com/Dhodraj/pmos-companion)

Planning and research for a well-being companion for women with PMOS. Built by team War Room at Tech for Good 2026, GDG Coimbatore, 8 to 9 August. The code lives in the team repository; this one holds the thinking. Its feasibility audit cut ten planned capabilities for good, each with a recorded reason. Platform policy, missing sensor wavelengths, a cross-lingual accuracy collapse, an API that does not exist. Not production software.

## One thing the repositories show

My public work splits cleanly in two, and the split is about evidence rather than volume.

| Repositories created | Count | Median README | With test files | Share of code bytes |
|---|---:|---:|---:|---:|
| 2021–2023 | 16 | 214 B | 1 | 14% |
| 2024–2026 | 11 | 5.3 KB | 9 | 86% |

Read from the GitHub REST API on 10 October 2026. Scope: all 27 public repositories, none of them forks, split by creation date. README size is the file GitHub serves. A repository counts as having tests when a file path contains `test` or `spec`, with vendored directories excluded. Code bytes are Linguist counts on the default branch, 2,095,147 in total: Python 42.4%, TypeScript 34.0%, JavaScript 12.0%, everything else 11.6%.

These numbers say where the work sits and how it is documented, not how good it is. Language bytes are not a measure of skill.

## Exploring now

- Multi-agent workflows. colony is the most recent of these and the one with written-up runs.
- Research automation. [ResearchPilot](https://github.com/Dhodraj/ResearchPilot) is four files and a README, so treat it as a sketch.
- Reading, with no public project yet: operating systems, distributed systems, networking.

## Contact

[github.com/dhodraj](https://github.com/dhodraj) · [linkedin.com/in/dhodraj-s-a137a2190](https://linkedin.com/in/dhodraj-s-a137a2190) · [dhodrajsdr192@gmail.com](mailto:dhodrajsdr192@gmail.com)
