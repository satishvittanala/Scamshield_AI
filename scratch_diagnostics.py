import os
from backend.services.ocr_service import TESSERACT_AVAILABLE
from backend.services.risk_engine import evaluate_risk
from backend.services.url_analyzer import analyze_url
from backend.services.conversation_analyzer import analyze_conversation

print("Searching for tesseract.exe...")
found = []
for p in [
    r"C:\Program Files\Tesseract-OCR\tesseract.exe",
    r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
    os.path.expandvars(r"%LOCALAPPDATA%\Programs\Tesseract-OCR\tesseract.exe"),
    r"C:\Users\satis\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
]:
    if os.path.exists(p):
        found.append(p)
print("Found Tesseract at:", found)

print("\n--- TESTING URL ACCURACY ---")
urls = [
    "https://www.google.com",
    "https://www.amazon.in",
    "https://www.onlinesbi.sbi",
    "http://sbi-login-verification.xyz/online-banking/update",
    "http://free-iphone-reward.top/claim",
    "http://go0gle.com/login",
    "https://bit.ly/3x91"
]
for u in urls:
    res = evaluate_risk(input_url=u)
    print(f"{u}\n  -> pred={res['prediction']}, risk={res['risk_score']}, cat={res['category']}, threat={res['threat_level']}, legit={res.get('url_details', {}).get('is_legitimate')}")

print("\n--- TESTING TEXT ACCURACY ---")
texts = [
    ("Scam 1 (Bank)", "URGENT: Your SBI account will be blocked today due to pending KYC. Click http://sbi-update.xyz to verify immediately and send OTP."),
    ("Scam 2 (Lottery)", "Congratulations! You have won Rs 50,00,000 in KBC Lucky Draw! Contact manager to claim your prize immediately."),
    ("Scam 3 (Job)", "Part time work from home job: Earn Rs 3000 daily by liking YouTube videos. Contact HR on Telegram @job_support."),
    ("Scam 4 (Electricity)", "Dear consumer your electricity power will be disconnected tonight at 9:30 pm from power office. please contact officer at 9876543210 immediately."),
    ("Safe 1 (Chat)", "Hi Priya, are we still meeting for lunch tomorrow at 1pm? Let me know!"),
    ("Safe 2 (Legit Bank OTP)", "Your OTP for transaction of Rs 1,500 at Flipkart is 492019. Do NOT share OTP with anyone including bank staff."),
    ("Safe 3 (Bank Credit)", "Dear Customer, your Account ending 5678 has been credited with Rs 45,000 towards salary for Sep 2026. Available balance Rs 62,300.")
]
for label, t in texts:
    res = evaluate_risk(input_text=t)
    print(f"{label}\n  -> pred={res['prediction']}, risk={res['risk_score']}, cat={res['category']}, threat={res['threat_level']}")

print("\n--- TESTING CONVERSATION ACCURACY ---")
conv_scam = [
    {"sender": "Scammer", "message": "I am calling from your bank."},
    {"sender": "Scammer", "message": "Your KYC has expired."},
    {"sender": "Scammer", "message": "Your account will be blocked."},
    {"sender": "Scammer", "message": "Send the OTP you received."}
]
res_c_scam = analyze_conversation(conv_scam)
print(f"Scam Conv\n  -> pred={res_c_scam['final_prediction']}, risk={res_c_scam['conversation_risk_score']}, cat={res_c_scam['category']}, pattern={res_c_scam['escalation_pattern']}")

conv_safe = [
    {"sender": "Alice", "message": "Hey, are you free this weekend?"},
    {"sender": "Bob", "message": "Yes, I am free on Saturday afternoon."},
    {"sender": "Alice", "message": "Great, let us go watch the new movie."}
]
res_c_safe = analyze_conversation(conv_safe)
print(f"Safe Conv\n  -> pred={res_c_safe['final_prediction']}, risk={res_c_safe['conversation_risk_score']}, cat={res_c_safe['category']}, pattern={res_c_safe['escalation_pattern']}")
