from .summarizer import summarize
from .transcriber import transcribe

def media_to_text_summ(filepath : str) -> str:

    sum : str = ""
    trs : str = transcribe(filepath, 'base')
    sum = summarize(trs)
    return sum 


def download_summ(summary: str, downloadfilename: str):

    with open(downloadfilename, "w") as f:
        f.write(summary)