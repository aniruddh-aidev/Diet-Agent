# Diet Planner Agent

A simple AI agent that generates daily vegetarian diet plans.

---

## Problem Statement

Many people want a quick, simple veg-friendly diet plan without spending time reading articles or calculating nutrition. This agent provides a minimal, realistic daily diet plan with breakfast, lunch, dinner, and a snack.

---

## Why Agents?

The workflow is broken into small focused agents:

- **Meal Planner** – creates a daily meal plan  
- **Nutrition Analyzer** – checks basic nutrition facts using Google Search  
- **Diet Writer** – formats the plan into Markdown  
- **Summary Generator** – produces a short summary  

Using multiple small agents keeps the system modular, readable, and easy to maintain.

---

## Architecture


User → Main Diet Agent →
Meal Planner →
Nutrition Analyzer →
Diet Writer →
Summary Generator → Final Output

---
