from transformers import pipeline

_SUMMARIZER = None

def get_summarizer():
    global _SUMMARIZER
    if _SUMMARIZER is None:
        _SUMMARIZER = pipeline(
            "summarization",
            model="sshleifer/distilbart-cnn-12-6",
            device=-1   # CPU
        )
    return _SUMMARIZER

def chunk_text(text: str, max_chars: int = 3000) -> list[str]:
    chunks = []
    current = ""

    for sentence in text.split("\n"):
        if len(current) + len(sentence) < max_chars:
            current += sentence + " "
        else:
            chunks.append(current.strip())
            current = sentence + " "

    if current.strip():
        chunks.append(current.strip())

    return chunks

def summarize_chunks(chunks: list[str]) -> list[str]:
    summarizer = get_summarizer()
    summaries = []

    for chunk in chunks:
        result = summarizer(
            chunk,
            max_length=120,
            min_length=50,
            do_sample=False
        )
        summaries.append(result[0]["summary_text"])

    return summaries

def summarize(text: str) -> str:
    chunks = chunk_text(text)
    partial_summaries = summarize_chunks(chunks)

    if len(partial_summaries) == 1:
        return partial_summaries[0]

    combined = "\n".join(partial_summaries)
    return combined


