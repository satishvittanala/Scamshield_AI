# ScamShield AI – Multi-Modal AI Scam Detection & Risk Intelligence Platform

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/FastAPI-0.104%2B-009688.svg)](https://fastapi.tiangolo.com/)
[![Machine Learning](https://img.shields.io/badge/scikit--learn%20%7C%20XGBoost-Powered-orange.svg)](https://scikit-learn.org/)
[![Explainable AI](https://img.shields.io/badge/SHAP-Non--Fabricated-purple.svg)](https://shap.readthedocs.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An end-to-end, enterprise-grade multi-modal artificial intelligence platform designed to detect, analyze, and mitigate cyber fraud across **Text/SMS**, **Email**, **URLs & Typosquatting Domains**, **Screenshot OCR Images**, and **Multi-Turn Social Engineering Conversations**.

Developed as a comprehensive final-year Engineering Capstone / B.Tech Computer Science & AI project.

---

## 1. Problem Statement

Digital financial fraud and social engineering scams have surged exponentially worldwide, particularly targeting mobile payment systems (UPI), online banking users, and e-commerce consumers. Fraudsters frequently evade traditional signature-based security filters by combining multiple deceptive vectors:
- Sending urgent SMS messages with disguised typosquatting links.
- Posing as bank or customs officials and progressively escalating psychological pressure across sequential dialogue turns.
- Sharing fraudulent QR codes, fake payment receipts, or account suspension notices via screenshot images on messaging apps.

Existing defenses typically output an opaque binary "Safe vs. Spam" label without actionable rationale or context. **ScamShield AI** addresses this gap by combining **machine learning pipelines**, **lexical/structural URL forensics**, **optical character recognition (OCR)**, **behavioral progression tracking**, **SHAP explainability**, and a **centralized weighted risk intelligence engine** (scoring 0–100 with actionable security recommendations).

---

## 2. Objectives

1. **Multi-Modal Threat Detection**: Unified ingestion and inspection of raw text, emails, URLs, screenshot images, phone numbers, and multi-turn dialogues.
2. **Standardized Risk Scoring**: Calculate a continuous, normalized **Risk Score (0–100)**, **Threat Level** (LOW, MEDIUM, HIGH, CRITICAL), **Scam Category**, **Forensic Indicators**, and **Dynamic Recommendations**.
3. **Safety-First Machine Learning**: Prioritize high **Recall** and minimization of false negatives in machine learning models across Logistic Regression, Random Forest, and XGBoost.
4. **Explainable AI (XAI)**: Dual-layer transparency delivering genuine mathematical SHAP feature attribution alongside explicit macro risk contributor point additions (+18 Urgent language, +25 Suspicious URL, +20 OTP request, +22 Bank impersonation).
5. **Human-in-the-Loop Governance**: Secure community incident reporting, prediction feedback loops (YES / NO), and administrator moderation preventing adversarial retraining poisoning.

---

## 3. Features

- **Text & SMS Scam Detection**: Identifies 13 scam categories (Phishing, Banking, UPI, KYC, Job, Investment, Lottery, Shopping, Loan, Romance, Tech Support, Impersonation, Other) and 9 fraudulent intents (`REQUEST_OTP`, `REQUEST_PASSWORD`, `REQUEST_BANK_DETAILS`, `REQUEST_PAYMENT`, `REQUEST_KYC`, `REQUEST_LOGIN`, `REQUEST_CRYPTO`, `REQUEST_GIFT_CARD`, `REQUEST_INSTALLATION`).
- **URL & Domain Forensics**: Extracts 14 structural features, evaluates Shannon entropy, flags suspicious TLDs, and detects typosquatting against top global and Indian institutions (Google, Microsoft, Apple, Amazon, PayPal, SBI, HDFC, ICICI, Axis Bank, Paytm, PhonePe, Flipkart).
- **Screenshot Image OCR**: Validates uploaded PNG/JPG images (size capping, MIME inspection, sanitized UUID filenames), extracts textual pretexts and embedded URLs via Tesseract OCR, and passes them through the unified scoring pipeline.
- **Multi-Turn Social Engineering Conversation Analysis**: Ingests sequential dialogue turns, detects psychological escalation patterns (`IMPERSONATION` &rarr; `TRUST_BUILDING` &rarr; `URGENCY` &rarr; `THREAT` &rarr; `CREDENTIAL_REQUEST` &rarr; `PAYMENT_REQUEST`), and computes conversation-level risk.
- **Multilingual Indic Support**: Native Unicode script and romanized lexicon recognition for **English**, **Hindi (Devanagari & Hinglish)**, **Tamil (Tamil script & Tanglish)**, and **Telugu (Telugu script & Teluglish)**.
- **Explainable AI (XAI)**: Non-fabricated SHAP Shapley values and human-readable feature contribution breakdowns.
- **Interactive Cyberpunk Dashboard & Scan History**: Live Chart.js telemetry charts, deep scan inspection modals, and "Open in AI Analyzer" replay functionality.
- **Community Incident Reporting & Verification**: Community scam incident reports with optional screenshot evidence, moderation queue, and feedback tracking.
- **Administrator Security Console**: Strict RBAC (403 Forbidden for non-admin users), 6 top-level telemetry cards, indicator rule management, and retraining candidate curation.

---

## 4. Architecture

```mermaid
flowchart TD
    subgraph ClientLayer["Frontend Client Layer"]
        UI["Cyber Glassmorphism Web Portal (HTML5 / Bootstrap 5 / Chart.js / ES6 JS)"]
    end

    subgraph APILayer["FastAPI Application Layer"]
        AUTH["Bcrypt & PyJWT RBAC (/api/auth)"]
        ROUTER["API Routers (Text, URL, Image, Conversation, Dashboard, Admin)"]
        SEC["Security & Sanitization Middleware (CORS, Safe Uploads, Masked Exceptions)"]
    end

    subgraph EngineLayer["Multi-Modal Intelligence Pipelines"]
        TEXT_ENG["NLP & Intent Engine (TF-IDF + ML Models + Multilingual Lexicons)"]
        URL_ENG["URL Forensics & Brand Typosquatting Engine (14 Features + Levenshtein)"]
        OCR_ENG["Vision & OCR Engine (Pillow Sanitizer + Tesseract OCR)"]
        CONV_ENG["Multi-Turn Dialogue Escalation Engine (6 Canonical Tactic Stages)"]
        XAI_ENG["Explainable AI Engine (shap.LinearExplainer + Risk Contributors)"]
    end

    subgraph CentralEngine["Centralized AI Risk Scoring Engine"]
        RISK["Weighted Aggregation: Text (30%) + URL (25%) + Intent (15%) + Brand (15%) + Rules (15%)"]
        THRESH["Threat Classification: 0-30 LOW | 31-60 MEDIUM | 61-80 HIGH | 81-100 CRITICAL"]
    end

    subgraph StorageLayer["Persistence & Database Layer"]
        DB[(SQLAlchemy ORM • SQLite / PostgreSQL)]
        MODELS["Users • Scans • URL Analyses • Scam Reports • Feedbacks • Managed Indicators"]
        RETRAIN["Retraining Candidate Queue (Supervised Human-in-the-Loop)"]
    end

    UI --> AUTH & ROUTER
    ROUTER --> SEC
    SEC --> TEXT_ENG & URL_ENG & OCR_ENG & CONV_ENG
    TEXT_ENG & URL_ENG & OCR_ENG & CONV_ENG --> RISK
    RISK --> THRESH
    RISK --> XAI_ENG
    THRESH & XAI_ENG --> DB
    DB --> MODELS
    MODELS --> RETRAIN
```

---

## 5. Technology Stack

- **Backend Framework**: Python 3.10+, FastAPI, Uvicorn, Pydantic v2
- **Database & ORM**: SQLAlchemy 2.0+ (SQLite default; compatible with PostgreSQL/MySQL)
- **Authentication & Security**: PyJWT (HS256), Bcrypt password hashing, python-multipart
- **Machine Learning & NLP**:
  - `scikit-learn` (Logistic Regression, Random Forest, TF-IDF Vectorizer)
  - `XGBoost` (Gradient boosted decision trees)
  - `shap` (SHAP LinearExplainer and TreeExplainer)
  - `pandas`, `numpy`, `joblib`
- **Computer Vision & OCR**:
  - `Pillow (PIL)` (Image sanitization and format verification)
  - `pytesseract` (Tesseract OCR wrapper with English, Hindi, Tamil, and Telugu language packs)
- **URL & Domain Forensics**:
  - `tldextract`, standard `urllib.parse`, Levenshtein distance, Shannon entropy
- **Frontend & Visualizations**:
  - HTML5, CSS3 with cybernetic glassmorphism theme
  - Bootstrap 5 & Bootstrap Icons
  - Chart.js (Real-time telemetry and category distribution visualizations)
  - Vanilla JavaScript (Modular ES6 architecture)
- **Testing**:
  - `pytest`, `httpx` (75+ comprehensive automated tests)
- **Containerization**:
  - Docker, Docker Compose

---

## 6. Installation

### Prerequisites
- Python 3.10 or higher
- Git
- (Optional) Tesseract OCR engine (for screenshot image OCR)

### Clone the Repository
```bash
git clone https://github.com/your-username/scamshield-ai.git
cd scamshield-ai
```

### Create and Activate Virtual Environment
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 7. Environment Setup

Copy `.env.example` to create your local `.env` configuration:

```bash
cp .env.example .env
```

### Core Configuration Variables:
```ini
# Application & Security
PROJECT_NAME="ScamShield AI"
SECRET_KEY=your-secure-random-32-byte-hex-string
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440

# Database
DATABASE_URL=sqlite:///./scamshield.db

# Storage & Uploads
UPLOAD_FOLDER=./uploads
MAX_UPLOAD_SIZE_MB=5

# ML Models
MODEL_DIR=./ml/saved_models

# Default Administrator Credentials (auto-seeded on first run)
ADMIN_NAME="System Administrator"
ADMIN_EMAIL=admin@scamshield.ai
ADMIN_PASSWORD=Admin@123

# Tesseract OCR Path (leave blank if installed in standard PATH)
# Windows: TESSERACT_CMD="C:\Program Files\Tesseract-OCR\tesseract.exe"
# Linux:   TESSERACT_CMD="/usr/bin/tesseract"
TESSERACT_CMD=

# Server
HOST=127.0.0.1
PORT=8000
```

---

## 8. Database

ScamShield AI uses SQLAlchemy ORM with automatic schema initialization on startup.
- **Default Database**: SQLite (`scamshield.db`), requiring zero configuration.
- **Enterprise Databases**: Easily switch to PostgreSQL or MySQL by updating `DATABASE_URL` in `.env`:
  ```ini
  DATABASE_URL=postgresql://user:password@localhost:5432/scamshield
  ```
- **Relational Models**:
  - `User`: Registered platform accounts with Bcrypt password hashes and role-based permissions (`USER`, `ADMIN`).
  - `Scan`: Comprehensive log of all multi-modal scans (text, URL, screenshot, dialogue), scores, threat levels, and grounded explanations.
  - `URLAnalysis`: Detailed structural feature extraction, entropy, and brand matching logs.
  - `ScamReport`: Community fraud reports with status moderation (`PENDING`, `VERIFIED`, `REJECTED`).
  - `Feedback`: User prediction validation (`YES`, `NO`) tracking False Positives and False Negatives.
  - `DomainList`: Managed allowlist/blocklist domains.
  - `ManagedIndicator`: Configurable suspicious indicator rules with dynamic point weights.

---

## 9. Machine Learning Training

The platform includes an automated ML training, comparison, and evaluation pipeline that benchmarks multiple algorithms:

```bash
python ml/train_text_model.py
```

### Training Pipeline Architecture:
1. **Dataset**: Ingests balanced corpus from `ml/datasets/scam_dataset.csv`.
2. **Text Preprocessing**: Normalization, URL token extraction, special character sanitization.
3. **Feature Extraction**: Sub-linear TF-IDF vectorization (unigrams + bigrams).
4. **Model Comparison**: Trains and evaluates:
   - **Logistic Regression** (Optimized for interpretability & linear SHAP explainability)
   - **Random Forest** (Ensemble bagging)
   - **XGBoost** (Gradient boosted decision trees)
5. **Selection Criteria**: Evaluates Accuracy, Precision, Recall, F1-Score, and ROC-AUC. Prioritizes high Recall to minimize missed fraudulent threats.
6. **Artifact Persistence**: Serializes production model and vectorizer into `ml/saved_models/`.

---

## 10. Running the Backend Server

Start the application using the master runner (which validates DB initialization, auto-trains baseline models if absent, and boots Uvicorn):

```bash
python run.py
```

Alternatively, launch directly via Uvicorn:
```bash
uvicorn backend.main:app --host 127.0.0.1 --port 8000 --reload
```

- **Backend API**: `http://127.0.0.1:8000/api`
- **Interactive Swagger Docs**: `http://127.0.0.1:8000/docs`
- **Alternative ReDoc UI**: `http://127.0.0.1:8000/redoc`

---

## 11. Running the Frontend Portal

The frontend is served directly by FastAPI without needing a separate Node.js server:

- **Landing Portal**: `http://127.0.0.1:8000/`
- **Multi-Modal AI Analyzer**: `http://127.0.0.1:8000/analyzer`
- **Conversation Escalation Studio**: `http://127.0.0.1:8000/conversation`
- **Threat Intelligence Dashboard**: `http://127.0.0.1:8000/dashboard`
- **Scan History**: `http://127.0.0.1:8000/history`
- **Report Incident**: `http://127.0.0.1:8000/reports`
- **Admin Security Console**: `http://127.0.0.1:8000/admin`
- **User Authentication**: `http://127.0.0.1:8000/login` & `http://127.0.0.1:8000/register`

---

## 12. API Endpoints Reference

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| `POST` | `/api/auth/register` | Register new user account | None |
| `POST` | `/api/auth/login` | Authenticate user and issue JWT | None |
| `GET` | `/api/auth/me` | Fetch authenticated user profile | Bearer JWT |
| `POST` | `/api/analyze/text` | Deep SMS & text scam analysis | Optional |
| `POST` | `/api/analyze/url` | URL forensics, structural features & typosquatting | Optional |
| `POST` | `/api/analyze/image` | Screenshot OCR text & embedded link analysis | Optional |
| `POST` | `/api/analyze/conversation` | Multi-turn dialogue escalation trajectory analysis | Optional |
| `POST` | `/api/analyze/phone` | Phone number reputation & prefix check | Optional |
| `GET` | `/api/scans` | List recent scans (Date, Type, Pred, Risk, Cat, Threat) | Optional |
| `GET` | `/api/scans/{id}` | Deep scan detail with SHAP & risk contributors | Optional |
| `POST` | `/api/reports` | Submit community scam report (JSON or multipart screenshot) | Optional |
| `GET` | `/api/reports` | List community verified scam reports | None |
| `POST` | `/api/feedback` | Submit prediction validation feedback (`YES` / `NO`) | Optional |
| `GET` | `/api/dashboard/stats` | Real-time aggregate statistics from database | None |
| `GET` | `/api/dashboard/categories` | Scam categories breakdown from database | None |
| `GET` | `/api/dashboard/trends` | Chronological date-grouped scan volume | None |
| `GET` | `/api/dashboard/charts` | 4 live Chart.js datasets | None |
| `GET` | `/api/admin/stats` | 6 telemetry metrics (Reports, Pending, Verified, Rejected, FP, FN) | Admin JWT (403 otherwise) |
| `GET` | `/api/admin/users` | List registered platform users | Admin JWT |
| `GET` | `/api/admin/reports` | Moderation queue with optional status filter | Admin JWT |
| `POST` | `/api/admin/reports/{id}/verify` | 1-click verify incident report | Admin JWT |
| `POST` | `/api/admin/reports/{id}/reject` | 1-click reject incident report | Admin JWT |
| `GET` | `/api/admin/indicators` | List configurable suspicious indicator rules | Admin JWT |
| `POST` | `/api/admin/indicators` | Create new suspicious indicator rule | Admin JWT |
| `DELETE` | `/api/admin/indicators/{id}` | Remove suspicious indicator rule | Admin JWT |
| `GET` | `/api/admin/retraining/candidates` | View curated retraining candidate summary | Admin JWT |
| `POST` | `/api/admin/retraining/export` | Export verified reports & corrections to CSV | Admin JWT |
| `GET` | `/api/health` | Application healthcheck endpoint | None |

---

## 13. Testing

ScamShield AI features a comprehensive automated test suite with **75 unit, integration, and security tests** across 11 test modules:

```bash
# Run complete test suite
python -m pytest tests/ -v

# Run Phase 12 validation suite specifically
python -m pytest tests/test_phase12_final_validation.py -v
```

### Test Suite Breakdown:
- `tests/test_phase12_final_validation.py` (16 tests): Full end-to-end journey, security audits, SQL injection resilience, and RBAC.
- `tests/test_phase10_and_11.py` (10 tests): Explainable AI, non-fabricated SHAP, dashboard APIs, and admin moderation.
- `tests/test_conversation.py` (9 tests): Multi-turn social engineering progression and Indic multilingual parsing (EN/HI/TA/TE).
- `tests/test_image_ocr.py` (8 tests): OCR pipeline, format whitelisting, file size caps, and text extraction.
- `tests/test_risk_engine.py` (5 tests): Centralized 5-signal composite risk aggregation and threat grading.
- `tests/test_url_detection.py` (5 tests): URL feature extraction, entropy, and brand typosquatting.
- `tests/test_text_detection.py` (6 tests): Text scam classification and intent extraction.
- `tests/test_auth.py` (6 tests): Bcrypt password hashing, JWT issue, and token expiry.
- `tests/test_admin.py` (4 tests): Administrative access control and domain governance.
- `tests/test_api_endpoints.py` (4 tests): Scan history and feedback pipelines.
- `tests/test_phase7_ui_workflow.py` (2 tests): UI template serving and workflow routing.

---

## 14. Docker Deployment

The application is containerized with a production-ready `Dockerfile` and `docker-compose.yml`.

### Build and Run with Docker Compose:
```bash
docker-compose up --build -d
```

### Accessing Containerized Application:
- Application Portal: `http://localhost:8000`
- API Documentation: `http://localhost:8000/docs`
- Healthcheck: `http://localhost:8000/api/health`

### Stop Container:
```bash
docker-compose down
```

---

## 15. Limitations

1. **Demonstration Dataset Disclosure**:
   > **Model performance is based on the available demo dataset and should not be interpreted as production performance.**
2. **Optical Character Recognition Constraints**:
   - Accuracy on heavily degraded, handwritten, or low-contrast screenshot images depends on local Tesseract OCR engine installation and language pack availability.
3. **Phone Number Intelligence**:
   - Reputation checks currently analyze format compliance, Indian operator prefix ranges, and internal platform scam reporting frequency; commercial telecom lookup APIs require enterprise carrier licensing.
4. **Adversarial Human-in-the-Loop Constraint**:
   - To prevent data poisoning attacks, automated unattended model retraining is intentionally disabled. Community reports must be verified by administrators prior to offline supervised retraining.

---

## 16. Future Enhancements

1. **Transformer Fine-Tuning**: Integration of fine-tuned multilingual transformer models (e.g., `xlm-roberta-base` or `indic-bert`) for expanded colloquial Indic dialects.
2. **Browser Extension**: Real-time Chromium/Firefox browser extension that continuously evaluates visited URLs against the `/api/analyze/url` endpoint.
3. **Audio Deepfake & Voice Phishing (Vishing) Detection**: Ingesting incoming voice call clips to detect synthetic voice clones and conversational coercion patterns.
4. **Federated Threat Intelligence**: Secure cryptographic sharing of verified scam URLs and indicators across participating financial institutions.

---

## 17. Project Metadata & Credentials

- **Project Title**: ScamShield AI – Multi-Modal AI Scam Detection & Risk Intelligence Platform
- **Default Administrator Account**:
  - **Email**: `admin@scamshield.ai`
  - **Password**: `Admin@123`
- **Academic Context**: B.Tech Final Year Engineering Project
- **Year**: 2026
