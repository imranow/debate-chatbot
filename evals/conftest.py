from dotenv import load_dotenv

# Ensure .env is loaded before any backend imports.
# override=True is needed in case empty env vars shadow .env values.
load_dotenv(override=True)
