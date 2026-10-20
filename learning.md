# My Learning Notes

NPTEL course programs + my own practice programs — Python basics, file/JSON handling, FastAPI, and some Java OOP. I just push straight to `main`, no build or test setup.

## How I want to work with the assistant

- Teach first, don't fix. Point out what's wrong and let me correct the code myself.
- Don't rewrite my files "to be helpful" — explain the fix and hand it back to me.
- If I ask for the answer directly, give it. Otherwise give hints/questions that make me think.
- I'm a beginner (Python + FastAPI + SQLite), so explain the *why*, not just the syntax.
- Quiz me with questions after explaining a concept.

## Environment

- Scripts run with my system Python 3.14 (fastapi, uvicorn, requests, pydantic are installed globally).
- `.vnv/` inside the repo is an empty venv — no pip or packages in it, so ignore it; activating it just makes imports fail.
- FastAPI files are run manually, like: `python -m uvicorn calculator_api:app --reload`
- No requirements.txt here — if I install something new I'll note it in this file.

## Common mistakes I keep making

- Some files have no `.py` extension (Calculator, Basic Chatbot, Reverse string, monthy calendar, etc.) but they are still normal Python. Run them with quotes since the names have spaces: `python "Basic Chatbot"`.
- Most scripts wait for `input()`, so they hang if run without typing anything. Pipe the input instead.
- `venv_practice/api_practice.py` hits httpbin.org, so it needs internet. Everything else runs offline.
- No `.gitignore` — running scripts keeps adding `__pycache__/*.pyc` to git status. Some old `.pyc` and `java learning/*.class` files are already committed; leave them but don't add new ones.
- `module2.py` is empty on purpose, and `database.py` is just a first line (sqlite3) — work in progress.

## What's here

- `p1.py`–`p10.py`, `file1.py`–`file6.py`: practice exercises (basics, then file and JSON handling with `human.txt`, `student.json`, `book2.json`)
- `main1.py` shows how to import a module (`mymodule1.py`); `module2.py` is part of that practice
- The no-extension files: one small program per topic/concept
- FastAPI practice: `calculator_api.py`, `Opportunity_api.py` (search/filter opportunities), `main3.py`; `venv_practice/` has my requests + venv experiments
- `java learning/`: OOP lessons (`j1.java`–`j8.java`, `msg.java`, `mypack/msg.java`). Compiled `.class` files sit next to the sources.

## Learning progress (Python backend + Agentic AI)

Goal: Python backend internship + Agentic AI hackathon. Beginner level.

Completed: Python fundamentals (lists, dicts, loops, functions), file handling, JSON, modules, venv, HTTP requests & status codes, FastAPI routes + Pydantic models (GET/POST/PUT/DELETE), query params, search, filtering, HTTPException 404.

Current project: **Student Opportunity Finder API** (FastAPI). Data is a Python list in `Opportunity_api.py` (note the capital O in the filename). Starting SQLite now.

Roadmap (in order):
1. Connect FastAPI to SQLite ← current
2. Database-backed CRUD
3. Prove data persists after server restart
4. SQL + PostgreSQL basics
5. First LLM API call
6. Tool calling → basic agent workflow

Next task: **SQLite step 1 — `database.py` (connection + table) and `test_database.py`**
