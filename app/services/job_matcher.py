def calculate_match(job_skills, resume_skills):

    job_skills_normalized = {
        skill.lower(): skill
        for skill in job_skills
    }

    resume_skills_normalized = {
        skill.lower(): skill
        for skill in resume_skills
    }

    matched_skills = []
    missing_skills = []

    for skill_lower, original_skill in job_skills_normalized.items():

        if skill_lower in resume_skills_normalized:
            matched_skills.append(original_skill)

        else:
            missing_skills.append(original_skill)

    total_required = len(job_skills_normalized)
    total_matched = len(matched_skills)

    if total_required == 0:
        match_percentage = 0

    else:
        match_percentage = round(
            (total_matched / total_required) * 100,
            2
        )

    return {
        "match_percentage": match_percentage,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "total_required_skills": total_required,
        "total_matched_skills": total_matched
    }
