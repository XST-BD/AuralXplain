from .summarizer import summarize
from .transcriber import transcribe

def audio_to_text_summ(filepath : str, download: bool, downloadfilename: str) -> str:

    sum : str = ""
    
    trs : str = transcribe(filepath, 'base')
    print(trs)
    sum = summarize(trs)

    print(sum)

    if download:
        with open(downloadfilename, "w") as f:
            f.write(sum)

    return sum 
