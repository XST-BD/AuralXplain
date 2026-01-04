from summarizer import summarize
from transcriber import transcribe

def audio_to_text_summ(filepath : str):

    trs : str = transcribe('/home/pancake/Music/starboy-weeknd.mp3', 'base')
    print(trs)

    sum = summarize(trs)
    print(sum)