from stackoverflow_api import get_stackoverflow_answers
from summarizer import summarize_answer

test_query = "Fix CORS error in Flask"

answers = get_stackoverflow_answers(test_query)
if answers:
    print("\n🔗 Top StackOverflow Questions:")
    for idx, ans in enumerate(answers):
        print(f"{idx + 1}. {ans['title']} - {ans['link']}")

    print("\n📌 Generating AI Summary...")
    summary = summarize_answer(answers[0]["title"])
    print("\n✅ AI Summary:")
    print(summary)
else:
    print("\n❌ No relevant StackOverflow questions found.")
