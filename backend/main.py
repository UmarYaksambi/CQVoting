from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Mock Database
projects = [
    {"id": 1, "name": "Project A", "description": "Description A", "image_url": "https://via.placeholder.com/200", "github_url": "https://github.com/example/project-a"},
    {"id": 2, "name": "Project B", "description": "Description B", "image_url": "https://via.placeholder.com/200", "github_url": "https://github.com/example/project-b"},
]
votes_db = []

class VoteSubmission(BaseModel):
    votes: dict

@app.get("/projects")
def get_projects():
    return projects

@app.post("/submit-votes")
def submit_votes(submission: VoteSubmission):
    total_credits = sum(v**2 for v in submission.votes.values())
    if total_credits > 100:
        raise HTTPException(status_code=400, detail="Not enough credits")
    votes_db.append(submission.votes)
    return {"message": "Votes submitted successfully!"}

@app.get("/results")
def get_results():
    results = {}
    for vote in votes_db:
        for project_id, count in vote.items():
            results[project_id] = results.get(project_id, 0) + count
    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
    return {"results": sorted_results}
