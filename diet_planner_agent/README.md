# Diet Planner Agent

This project implements a multi-agent system that helps users generate simple diet plans.  
It was built using the Google Agent Development Kit as part of the 5-Day AI Agents Intensive.

## Problem
Many people struggle with structuring balanced meals, understanding nutritional guidelines, and staying consistent. Manual diet planning is repetitive and often confusing.

## Solution
The Diet Planner Agent coordinates several small sub-agents to:
- gather basic nutrition information,
- generate a daily or weekly meal plan,
- adjust the plan based on user constraints,
- summarize final recommendations.

## Architecture
The system uses:
- a **root agent** that guides the workflow,
- a **meal planner agent** for the meal structure,
- a **nutrition analyzer agent** for checking calories/macros,
- a **diet writer agent** that formats the final plan,
- a **summary generator agent** for short wrap-ups,
- simple custom tools for saving plans and parsing preferences.

All agents use Gemini models and communicate through shared session state.

## Setup
