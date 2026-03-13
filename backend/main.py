import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

from routes import analyze, chatbot, tavus, organ, records, appointments, doctor, ipfs, integrations

tags_metadata = [
    {"name": "Infrastructure",    "description": "Health checks and system status"},
    {"name": "AI Analysis",       "description": "Medical report analysis, chatbot, and organ-level AI insights"},
    {"name": "Tavus AI Doctor",   "description": "AI-generated doctor video summaries and CVI conversations"},
    {"name": "Medical Records",   "description": "Patient record CRUD, caching, and cloning"},
    {"name": "Access Control",    "description": "RBAC-based access grants between patients and doctors"},
    {"name": "Appointments",      "description": "Appointment booking, cancellation, and slot management"},
    {"name": "Doctor Dashboard",  "description": "Doctor profiles, appointments, grants, and consultation notes"},
    {"name": "IPFS",              "description": "Decentralized file storage via Pinata/IPFS"},
    {"name": "Integrations",      "description": "Google Calendar OAuth and external service proxies"},
]

app = FastAPI(
    title="MediChain AI Backend",
    version="1.0.0",
    description="AI-powered blockchain-secured medical record platform. Use /openapi.json for Requestly import.",
    openapi_tags=tags_metadata,
)

# --- CORS ---
allowed_origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[o.strip() for o in allowed_origins],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Routers ---
app.include_router(analyze.router,       prefix="/api")
app.include_router(chatbot.router,       prefix="/api")
app.include_router(tavus.router,         prefix="/api")
app.include_router(organ.router,         prefix="/api")
app.include_router(records.router,       prefix="/api")
app.include_router(appointments.router,  prefix="/api")
app.include_router(doctor.router,        prefix="/api")
app.include_router(ipfs.router,          prefix="/api")
app.include_router(integrations.router,  prefix="/api")


@app.get("/health")
def health_check():
    return {"status": "ok", "service": "MediChain AI Backend"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
