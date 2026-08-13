# AgentForge

> An open-source platform for building, testing, evaluating, and monitoring AI agents.

AgentForge is an AI agent engineering platform focused on making agent systems
measurable, testable, and reliable.

The project is designed around a simple idea:

**Building an AI agent is only the beginning. Measuring whether it actually works is the real engineering challenge.**

AgentForge aims to provide the infrastructure required to develop reliable
LLM-powered systems through automated evaluation, failure analysis,
observability, and reproducible testing.

---

## 🚀 Project Status

**Status:** Early Development

### Currently implemented

- FastAPI backend
- Health-check API
- Root API endpoint
- Automated API tests with pytest
- Project-level pytest configuration
- Git-based development workflow
- GitHub repository and CI foundation

### Under development

- Agent orchestration
- LLM integration
- Tool calling
- Agent memory
- Retrieval-Augmented Generation (RAG)
- Evaluation datasets
- Automated agent evaluation
- Failure analysis
- Metrics and observability
- Evaluation dashboard

---

## 🎯 Problem

LLM applications can produce different results for the same task.

Traditional software testing usually checks whether a function returns the
expected value.

AI systems are different.

An agent can:

- produce an incorrect answer
- hallucinate information
- select the wrong tool
- call a tool incorrectly
- retrieve irrelevant information
- consume excessive tokens
- take too long to respond
- fail only on specific classes of inputs

AgentForge is being built to make these failures measurable.

---

## 🏗️ Architecture

The system is being developed around the following architecture:

```text
                         ┌──────────────────────┐
                         │        Client        │
                         │  Web / API / CLI     │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │      FastAPI API     │
                         └──────────┬───────────┘
                                    │
                                    ▼
                    ┌──────────────────────────────┐
                    │      Agent Orchestrator      │
                    │                              │
                    │  ┌────────┐ ┌──────┐        │
                    │  │ Tools  │ │ RAG  │        │
                    │  └────────┘ └──────┘        │
                    │                              │
                    │  ┌────────┐                 │
                    │  │ Memory │                 │
                    │  └────────┘                 │
                    └──────────────┬───────────────┘
                                   │
                                   ▼
                         ┌──────────────────────┐
                         │    LLM / Model       │
                         └──────────┬───────────┘
                                    │
                                    ▼
                    ┌──────────────────────────────┐
                    │      Evaluation Engine       │
                    │                              │
                    │  Accuracy                    │
                    │  Tool-use                    │
                    │  Groundedness                │
                    │  Latency                      │
                    │  Cost                         │
                    └──────────────┬───────────────┘
                                   │
                                   ▼
                         ┌──────────────────────┐
                         │ Metrics & Monitoring │
                         └──────────────────────┘