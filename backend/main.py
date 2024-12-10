import os
import base64
import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from dotenv import load_dotenv

app = FastAPI()

# Initialize the mock database for storing projects
projects = []

votes_db = []

# GitHub API Base URL
GITHUB_API_URL = "https://api.github.com/repos"

load_dotenv(dotenv_path='../.env')
# GitHub Personal Access Token (make sure to replace with your own token)
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Replace with your actual token

# Pydantic Model for Project
class Project(BaseModel):
    id: Optional[int] = None
    name: str
    description: str
    github_url: str
    youtube_url: Optional[str] = None
    preview_image_url: Optional[str] = None
    readme_content: Optional[str] = None
    main_code_file: Optional[str] = None

class VoteSubmission(BaseModel):
    votes: dict
    votes: dict  

# Helper function to fetch repository data from GitHub (with authentication)
def fetch_github_project_details(github_url):
    # Strip '.git' suffix if present
    if github_url.endswith(".git"):
        github_url = github_url[:-4]

    # Extract the repository owner and name from the GitHub URL
    try:
        # Extract the part after 'github.com/'
        repo_path = github_url.split("github.com/")[1]
        repo_owner, repo_name = repo_path.split("/")  # Unpack the owner and repo name

        # Construct the API URL
        repo_api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}"
        print(f"Fetching data from: {repo_api_url}")  # Debugging line

        # Make a request to GitHub's API to get repository details
        response = requests.get(repo_api_url)
        print(f"GitHub API response status: {response.status_code}")  # Debugging line
        response.raise_for_status()  # This will raise an exception for 4xx/5xx status codes
        repo_data = response.json()

        # Ensure we are getting the expected response structure
        print(f"GitHub API response data: {repo_data}")  # Debugging line

        # Get the README file content (if available)
        readme_url = f"{repo_api_url}/contents/README.md"
        readme_response = requests.get(readme_url)
        print(f"GitHub README response status: {readme_response.status_code}")  # Debugging line
        readme_response.raise_for_status()  # Check for errors
        readme_content = readme_response.json()

        # Decode base64 README content if present
        readme = base64.b64decode(readme_content.get("content", "")).decode("utf-8")  # Decode base64
        print(f"README content fetched successfully.")  # Debugging line

        # Get the preview image (use the repository owner's avatar as a placeholder)
        preview_image = repo_data.get("owner", {}).get("avatar_url", "")

        # Fetch the main code file (if available)
        code_files_url = f"{repo_api_url}/contents/"
        code_response = requests.get(code_files_url)
        code_response.raise_for_status()
        code_files = code_response.json()
        main_code_file = None
        
        # Loop through the files in the repository and try to find the main code file (for example, Python file)
        for file in code_files:
            if file['name'].endswith(('.py', '.js', '.java', '.cpp', '.js')):  # You can adjust extensions
                main_code_file = file['download_url']
                break
        
        print(f"Main code file: {main_code_file}")  # Debugging line

        # Set default values if any field is missing
        return preview_image, readme, main_code_file
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching GitHub project details: {str(e)}")  # Debugging line
        raise Exception("GitHub repository not found or invalid repository URL")

# Endpoint to get all projects
@app.get("/projects", response_model=List[Project])
def get_projects():
    return projects

# Endpoint to add a project
@app.post("/projects", response_model=Project)
def create_project(project: Project):
    # Ensure the GitHub URL is valid
    if not project.github_url.startswith("https://github.com/"):
        raise HTTPException(status_code=400, detail="Invalid GitHub URL.")

    # Fetch GitHub data (social preview, README, main code file)
    preview_image_url, readme_content, main_code_file = fetch_github_project_details(project.github_url)

    # Add the project with the fetched data
    new_project = project.dict()
    new_project["preview_image_url"] = preview_image_url
    new_project["readme_content"] = readme_content
    new_project["main_code_file"] = main_code_file

    projects.append(new_project)  # Save the project to the mock database
    return new_project

@app.post("/submit-votes")
def submit_votes(submission: VoteSubmission):
    total_credits = sum(v**2 for v in submission.votes.values())
    if total_credits > 100:
        raise HTTPException(status_code=400, detail="Not enough credits")
    total_credits_used = 0
    # Calculate the total cost of votes
    for project_id, votes in submission.votes.items():
        # Calculate the cumulative quadratic cost for votes per project
        cumulative_cost = sum(i**2 for i in range(1, votes + 1))
        total_credits_used += cumulative_cost
    # Check if total credits exceed the limit
    if total_credits_used > 100:
        raise HTTPException(
            status_code=400, detail="Not enough credits to submit these votes."
        )
    # Store the votes in the mock database
    votes_db.append(submission.votes)
    return {"message": "Votes submitted successfully!"}

@app.get("/results")
def get_results():
    results = {}