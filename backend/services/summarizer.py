from transformers import pipeline

# ✅ Use a better summarization model (T5-base or Pegasus)
summarizer = pipeline("summarization", model="t5-base")

def summarize_answer(answer_text):
    """
    Summarize the StackOverflow answer using Hugging Face T5-base model.
    """
    if len(answer_text.split()) < 20:  # ✅ Avoid summarizing very short text
        return answer_text  # Return the text as is

    summary = summarizer(answer_text, max_length=150, min_length=50, do_sample=True)
    return summary[0]['summary_text']
