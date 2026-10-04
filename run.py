import os
import sys
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def check_and_train_models():
    """Checks if trained ML models exist. If not, automatically trains them on the curated dataset."""
    model_file = BASE_DIR / "ml" / "saved_models" / "text_model.pkl"
    if not model_file.exists():
        print("\n[STARTUP] Trained ML model not found. Initializing training pipeline on curated dataset...")
        try:
            from ml.train_text_model import train_and_compare_models
            train_and_compare_models()
            print("[STARTUP] ML models trained and saved successfully.\n")
        except Exception as e:
            print(f"[STARTUP WARNING] Could not auto-train models ({e}). Application will start using heuristic fallback engine.\n")


def init_database_and_admin():
    """Initializes tables and default admin."""
    from backend.database import engine, Base, SessionLocal
    from backend.auth import seed_admin_if_needed
    Base.metadata.create_all(bind=engine)
    with SessionLocal() as db:
        seed_admin_if_needed(db)


def main():
    print("=" * 70)
    print("      SCAMSHIELD AI – MULTI-MODAL SCAM RISK INTELLIGENCE PLATFORM     ")
    print("=" * 70)
    
    # 1. Initialize DB and Admin
    init_database_and_admin()

    # 2. Check / Train ML models
    check_and_train_models()

    # 3. Launch Uvicorn Server
    import uvicorn
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", 8000))
    print(f"\n[SERVER] Launching ScamShield AI Web Application on http://{host}:{port}")
    print(f"[SERVER] Public Web Portal:     http://{host}:{port}")
    print(f"[SERVER] Multi-Modal Analyzer:  http://{host}:{port}/analyzer")
    print(f"[SERVER] Threat Dashboard:      http://{host}:{port}/dashboard")
    print(f"[SERVER] Scam Reports Feed:     http://{host}:{port}/reports")
    print(f"[SERVER] Admin Security Portal: http://{host}:{port}/admin")
    print(f"[SERVER] Interactive API Docs:  http://{host}:{port}/docs\n")
    print(f"[ADMIN CREDENTIALS] Email: admin@scamshield.ai | Password: Admin@123\n")

    uvicorn.run("backend.main:app", host=host, port=port, reload=False)


if __name__ == "__main__":
    main()
