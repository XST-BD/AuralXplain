from .summarizer import summarize
from .transcriber import transcribe

def audio_to_text_summ(filepath : str) -> str:

    sum : str = ""
    
    trs : str = transcribe(filepath, 'base')
    print(trs)
    sum = summarize(trs)

    print(sum)
    return sum 

