from summarizer import summarize
from transcriber import transcribe

def audio_to_text_summ(filepath : str) -> str:

    sum : str = ""
    
    trs : str = transcribe('/home/pancake/Music/starboy-weeknd.mp3', 'base')
    sum = summarize(trs)

    return sum