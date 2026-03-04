import traceback
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from crewai import Crew, Process

app = FastAPI(title="LoveGPT Tamil API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class StoryRequest(BaseModel):
    story: str
    gemini_api_key: str


@app.post("/api/generate_love_plan")
async def generate_love_plan(request: StoryRequest):
    user_story = request.story.strip()
    gemini_api_key = request.gemini_api_key.strip()

    if not user_story:
        raise HTTPException(status_code=400, detail="Story cannot be empty")
    if not gemini_api_key:
        raise HTTPException(status_code=400, detail="Gemini API key cannot be empty")

    try:
      
        from agents import build_agents
        from tasks import build_tasks

        agents = build_agents(gemini_api_key)
        tasks  = build_tasks(agents)

        LoveGPT_Tamil = Crew(
            agents=list(agents.values()),
            tasks=list(tasks.values()),
            process=Process.sequential,
            verbose=True,
        )

        result = LoveGPT_Tamil.kickoff(inputs={"story": user_story})
        return {"plan": str(result.raw)}

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)