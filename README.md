# Open Learning Stack 🚀

> A single repo to learn and master Programming Languages + AI/ML concepts — with examples, hands-on exercises, and structured order.

[![Topics](https://img.shields.io/badge/Topics-146-blue.svg)]()
[![Languages](https://img.shields.io/badge/Languages-5-orange.svg)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success.svg)]()

## What is this?

This is a structured, self-paced learning repository covering **Python, JavaScript, TypeScript, Go, and Rust** — plus a complete **AI/ML track** from math foundations to LLMs and MLOps. Every topic follows a consistent 4-file pattern: read the concept, run the example, solve the exercises, check the solutions. No ambiguity, no guessing where to start.

## How to use this repo

```bash
# 1. Clone the repo
git clone https://github.com/iam-prabha/open-learning-stack.git
cd open-learning-stack

# 2. Pick a language folder (e.g. python/)
cd python/01-fundamentals/01-variables/

# 3. Open a topic folder — read, run, practice
cat README.md              # Read the concept
python example.py          # Run the demo
python exercise.py         # Try the exercises (fill in TODOs)
python solution.py         # Check the answers
```

## Repository structure

```text
open-learning-stack/
├── _templates/          ← boilerplate for new topics
├── python/              ← 🐍 Python (fundamentals → advanced)
├── javascript/          ← 🟨 JavaScript (fundamentals → advanced)
├── typescript/          ← 🔷 TypeScript (fundamentals → advanced)
├── go/                  ← 🐹 Go (fundamentals → advanced)
├── rust/                ← 🦀 Rust (fundamentals → advanced)
├── ai-ml/               ← 🤖 AI/ML (math → ML → DL → LLMs → MLOps)
├── ROADMAP.md           ← Visual learning roadmap
├── GLOSSARY.md          ← Shared terminology
└── README.md            ← You are here
```

## Languages

| Language | Status | Topics | Start here |
|---|---|---|---|
| Python | 🟢 Active | 24 | [python/01-fundamentals/01-variables](python/01-fundamentals/01-variables/) |
| JavaScript | 🟢 Active | 23 | [javascript/01-fundamentals/01-variables](javascript/01-fundamentals/01-variables/) |
| TypeScript | 🟡 Planned | 23 | [typescript/01-fundamentals/01-types-and-annotations](typescript/01-fundamentals/01-types-and-annotations/) |
| Go | 🟡 Planned | 23 | [go/01-fundamentals/01-variables](go/01-fundamentals/01-variables/) |
| Rust | 🟡 Planned | 23 | [rust/01-fundamentals/01-variables](rust/01-fundamentals/01-variables/) |

## AI/ML Roadmap

| Phase | Folder | Focus | Topics | Status |
|---|---|---|---|---|
| 0 | `ai-ml/01-math-foundations/` | Linear algebra, calculus, probability | 5 | 🟢 Active |
| 1 | `ai-ml/02-ml-core/` | Classical ML algorithms | 8 | 🟢 Active |
| 2 | `ai-ml/03-deep-learning/` | Neural networks, CNNs, RNNs | 6 | 🟡 Planned |
| 3 | `ai-ml/04-llms/` | Transformers, fine-tuning, RAG | 6 | 🟡 Planned |
| 4 | `ai-ml/05-mlops/` | Deployment, monitoring, CI/CD | 5 | 🟡 Planned |

## The 4-file pattern

Every topic folder contains the same 4 files:

| File | Purpose |
|---|---|
| `README.md` | Concept explanation with analogy, use cases, common mistakes |
| `example.[ext]` | One clean, runnable demo — annotated with WHY comments |
| `exercise.[ext]` | 6 TODOs + 1 challenge — with assert-based self-checking |
| `solution.[ext]` | Complete answers with WHY comments and alternative approaches |

This pattern ensures every topic is **self-contained** — you never need to look outside the folder.

## Contributing

Everyone is welcome! To add a new topic:

1. Copy `_templates/` to the correct location (e.g. `python/01-fundamentals/11-new-topic/`)
2. Fill in all 4 files following the patterns in existing topics
3. Ensure `example.[ext]` and `solution.[ext]` run with zero errors
4. Ensure `exercise.[ext]` has asserts that fail until TODOs are filled in
5. Open a PR with a short description

See [ROADMAP.md](ROADMAP.md) for topics that need contributors.

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

Made with ❤️ by [@iam-prabha](https://github.com/iam-prabha) — Happy learning! 🎓✨