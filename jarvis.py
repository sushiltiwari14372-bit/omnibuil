from google import genai
import os

# 1. Setup with your 2026 API Key
client = genai.Client(api_key="AIzaSyAR0JFYPwuCNGJlHaDpftLCO3l0xPS0BBM")

def update_site():
    file_path = "index.html"
    
    if os.path.exists(file_path) and os.stat(file_path).st_size > 0:
        with open(file_path, "r") as f:
            current_code = f.read()
    else:
        current_code = ""

    print("\n--- OMNIBUILD CORE ONLINE ---")
    user_input = input("Sir, what is our next objective? ")
    
    config = {
        "system_instruction": (
            "You are the Lead Architect for OmniBuild. "
            "Design Style: Ultra-modern, Dark Theme, Glassmorphism, 'Inter' Google Font. "
            "Output: Provide ONLY the full HTML/CSS code. No conversational text."
        )
    }

    print("\n[SYSTEM] Synthesizing code via Gemini 2.5 Flash...")
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash", 
            contents=f"Current Code:\n{current_code}\n\nTask: {user_input}",
            config=config
        )
        
        clean_code = response.text.replace("```html", "").replace("```", "").strip()
        
        with open(file_path, "w") as f:
            f.write(clean_code)
        
        print("\n[SUCCESS] Deployment complete. Check index.html.")

    except Exception as e:
        print(f"\n[CRITICAL ERROR] {e}")

if __name__ == "__main__":
    update_site()
