import contractions
from .spanish import spanish_contractions
from .french import french_contractions
from .italian import italian_contractions
from .romanian import romanian_contractions

def expand_contractions(sentence, lang_code):
    if lang_code == 'en':
        contractions_dict = contractions.contractions_dict
    elif lang_code == 'es':
        contractions_dict = spanish_contractions
    elif lang_code == 'fr':
        contractions_dict = french_contractions
    elif lang_code == 'it':
        contractions_dict = italian_contractions
    elif lang_code == 'ro':
        contractions_dict = romanian_contractions
    else:
        raise ValueError("Unsupported language code")

    for contraction, expansion in contractions_dict.items():
        sentence = sentence.replace(contraction, expansion)

    return sentence
