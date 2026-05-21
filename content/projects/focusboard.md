---
title: "FocusBoard"
summary: "A Flask and SQLite productivity platform with Kanban workflows, dashboard analytics, and an explainable smart planner."
order: 2
featured: true
year: "2026"
status: "Completed"
area: "Full-Stack Python"
tools:
  - Python
  - Flask
  - SQLite
  - Jinja
  - Bootstrap
  - JavaScript
  - pytest
links:
  github: "https://github.com/your-github/focusboard"
  demo: ""
metrics:
  - label: "Backend"
    value: "Flask"
  - label: "Database"
    value: "SQLite"
  - label: "Planner"
    value: "Rule-based"
---

## Problem

Task management tools are useful only when they reduce decision friction. I
wanted to build a productivity app that supports the usual project and task
workflows, but also helps a user decide what to work on next.

## Approach

FocusBoard is a full-stack Flask application with user authentication, project
and task CRUD workflows, labels, Kanban-style status management, deadline
tracking, CSV export, and dashboard analytics. The backend uses SQLite with
user-level data isolation and a structured route organization based on Flask
blueprints.

The most interesting feature is the smart planner: an explainable rule-based
scoring system that ranks unfinished tasks by priority, deadline urgency,
status, overdue state, and estimated workload.

## Implementation Notes

- Implemented session-based authentication with password hashing.
- Designed relational tables for users, projects, tasks, labels, task-label
  relationships, and activity logs.
- Added SQL aggregation for dashboard metrics such as completed tasks,
  in-progress tasks, overdue tasks, upcoming deadlines, and project progress.
- Built CSV export for user tasks with Python's standard CSV tools and HTTP
  download headers.
- Added pytest smoke tests for authentication, CRUD workflows, smart planning,
  CSV export, and login-required redirects.

## What I Learned

FocusBoard helped me connect backend structure, SQL design, UI workflow, and
product reasoning. The rule-based planner was intentionally simple and
explainable, which made it easier to justify recommendations without needing
historical training data.
