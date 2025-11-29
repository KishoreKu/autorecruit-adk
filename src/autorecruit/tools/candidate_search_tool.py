import pandas as pd

def search_candidates(job_profile: dict, top_k: int = 5, path: str = "data/processed/candidates.csv"):
    """
    Simple candidate search tool based on skill overlap, experience, and location.
    """
    candidates_df = pd.read_csv(path)

    required = set(s.strip().lower() for s in job_profile.get("must_have_skills", []))
    min_years = job_profile.get("min_years_experience", 0)
    target_location = job_profile.get("location")

    def score_row(row):
        skills = set(s.strip().lower() for s in row["primary_skills"].split(","))
        base_score = len(required & skills)
        location_bonus = 0
        if isinstance(target_location, str) and target_location:
            if target_location.split(",")[-1].strip().lower() in row["location"].lower():
                location_bonus = 1
        exp_bonus = 1 if row["years_experience"] >= min_years else 0
        return base_score + location_bonus + exp_bonus

    df = candidates_df.copy()
    df["score"] = df.apply(score_row, axis=1)
    top = df.sort_values("score", ascending=False).head(top_k)
    return top.to_dict(orient="records")
