# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

LangGraph practice repository containing Jupyter notebooks demonstrating various LangGraph workflow patterns.

## Environment Setup

Activate the virtual environment:
```bash
source graphenv/bin/activate
```

The project uses Python 3.12 with LangChain, LangGraph, and multiple LLM providers (Groq, Google Gemini). API keys are stored in `.env` file.

## Key Dependencies

- **langgraph**: State machine orchestration for LLM workflows
- **langchain_google_genai**: Google Gemini integration
- **langchain_groq**: Groq LLM integration
- **python-dotenv**: Environment variable management

## Architecture Pattern

All notebooks follow the LangGraph StateGraph pattern:

1. **Define State**: TypedDict specifying the data flow schema
2. **Create Nodes**: Functions that receive state, process it, and return updated state
3. **Add Edges**: Connect nodes with `add_edge()` or use `add_conditional_edges()` for branching logic
4. **Compile**: `graph.compile()` creates the executable workflow
5. **Execute**: `workflow.invoke(initial_state)` runs the graph

## Common Workflow Patterns

- **Sequential**: START → node1 → node2 → END
- **Conditional**: Use `add_conditional_edges(node, router_function)` for branching based on state
- **Iterative**: Conditional edges that loop back to previous nodes (e.g., evaluate → optimize → evaluate)

## Running Notebooks

Execute any notebook using Jupyter:
```bash
jupyter notebook <notebook_name>.ipynb
```
