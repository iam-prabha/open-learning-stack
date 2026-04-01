# Roadmap — Open Learning Stack 🗺️

This roadmap shows the learning order across all tracks. Start at the top, work your way down.

## Learning Order

```text
                    ┌─────────────────────────┐
                    │   Pick a starting track  │
                    └────────┬────────────────┘
           ┌─────────┬──────┴──────┬──────────┬──────────┐
           ▼         ▼            ▼          ▼          ▼
       Python    JavaScript  TypeScript     Go        Rust
           │         │            │          │          │
    01-fundamentals  │     01-fundamentals   │   01-fundamentals
           │         │            │          │          │
    02-intermediate  │     02-intermediate   │   02-intermediate
           │         │            │          │          │
    03-advanced      │     03-advanced       │   03-advanced
           │         │            │          │          │
           └─────────┴──────┬─────┴──────────┴──────────┘
                            ▼
                    ┌───────────────┐
                    │    AI / ML    │
                    └───────┬───────┘
                            │
              01-math-foundations (Phase 0)
                            │
              02-ml-core (Phase 1)
                            │
              03-deep-learning (Phase 2)
                            │
              04-llms (Phase 3)
                            │
              05-mlops (Phase 4)
```

## Track Status

| Track | Fundamentals | Intermediate | Advanced |
|---|---|---|---|
| Python | 🟢 10 topics | 🟢 8 topics | 🟢 6 topics |
| JavaScript | 🟢 10 topics | 🟢 8 topics | 🟢 5 topics |
| TypeScript | 🟢 10 topics | 🟢 8 topics | 🟢 5 topics |
| Go | 🟡 10 topics | 🟡 8 topics | 🟡 5 topics |
| Rust | 🟡 10 topics | 🟡 8 topics | 🟡 5 topics |

| AI/ML Phase | Status | Topics |
|---|---|---|
| 01-math-foundations | 🟢 Active | 5 |
| 02-ml-core | 🟢 Active | 8 |
| 03-deep-learning | 🟢 Active | 6 |
| 04-llms | 🟡 Planned | 6 |
| 05-mlops | 🟡 Planned | 5 |

🟢 = Content available  🟡 = Planned — contributions welcome!

## How to contribute

1. Pick a 🟡 topic from the tables above
2. Copy `_templates/` to the correct folder
3. Follow the 4-file pattern (README, example, exercise, solution)
4. Open a PR
