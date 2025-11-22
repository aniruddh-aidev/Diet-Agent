def save_diet_to_file(diet_text: str, filename: str) -> dict:
    with open(filename, "w") as f:
        f.write(diet_text)
    return {"status": "saved"}

def parse_user_prefs(prefs: str) -> dict:
    # intentionally simple; just passes through
    return {"raw_prefs": prefs}
