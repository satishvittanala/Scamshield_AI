import argparse
import sys
from backend.database import SessionLocal, engine, Base
from backend.models import User
from backend.auth import get_password_hash
from backend.config import settings

def create_or_update_admin(name: str, email: str, password: str):
    """Safely creates or resets the development administrator account."""
    Base.metadata.create_all(bind=engine)
    
    with SessionLocal() as db:
        user = db.query(User).filter(User.email == email.lower()).first()
        hashed = get_password_hash(password)
        if user:
            user.name = name
            user.password_hash = hashed
            user.role = "ADMIN"
            db.commit()
            print(f"[SUCCESS] Existing user '{email}' successfully promoted/updated to ADMIN role.")
        else:
            admin_user = User(
                name=name,
                email=email.lower(),
                password_hash=hashed,
                role="ADMIN"
            )
            db.add(admin_user)
            db.commit()
            db.refresh(admin_user)
            print(f"[SUCCESS] New administrator '{email}' successfully created with ID #{admin_user.id}.")

def main():
    parser = argparse.ArgumentParser(description="ScamShield AI – Safe Administrator Setup Command")
    parser.add_argument("--name", default=settings.ADMIN_NAME, help="Admin display name")
    parser.add_argument("--email", default=settings.ADMIN_EMAIL, help="Admin email address")
    parser.add_argument("--password", default=settings.ADMIN_PASSWORD, help="Admin secure password")
    
    args = parser.parse_args()
    
    print("=" * 60)
    print(" ScamShield AI - Administrator Provisioning Utility")
    print("=" * 60)
    create_or_update_admin(args.name, args.email, args.password)
    print(f"Role: ADMIN | Email: {args.email}")
    print("=" * 60)

if __name__ == "__main__":
    main()
