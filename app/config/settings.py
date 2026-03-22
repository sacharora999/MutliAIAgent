from dotenv import load_dotenv
load_dotenv()

class Settings:
    ALLOWED_MODEL_NAMES = [
        "gpt-3.5-turbo",
        "gpt-4o-mini",
        "gpt-4.1-nano"
    ]

settings=Settings()