api = input("Enter your api key: ").strip()
from google import genai
client = genai.Client(api_key=api)
def ask_ai(question):
    prompt = f"""
    You are answering a Google Form.

    Rules:
    - If the question is an Multiple choice question, choose the right option and give no explaination
    - If the question is subjective, give the appropirate answer and do not make it too long
    - If the question asks for personal information like name or contact, return "User input" 

    Question:
    {question}
    """
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text.strip()


from playwright.sync_api import sync_playwright

url = input("Enter Google Form URL: ").strip()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto(url, wait_until="networkidle")

    #print(page.locator("body").inner_text())
    questions = page.locator('div[role="listitem"]')
    all_questions = []
    print("Questions found:", questions.count())
    for i in range(questions.count()):
        question_block = questions.nth(i).inner_text()
        all_questions.append(question_block)
    print("Content: ")
    print(all_questions)

    for question in all_questions:

        answer = ask_ai(question)

        print("\nQUESTION:")
        print(question)

        print("\nANSWER:")
        print(answer)

        print("\n" + "=" * 40)

    input("Press Enter to close...")

    browser.close()