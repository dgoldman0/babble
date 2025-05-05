# Let's call it... Louvéchant?

import random

V = ["a", "e", "i", "o", "u", "é", "è", "ê", "ou", "oi", "eu", "au"]
C = ["b", "c", "ch", "cl", "d", "f", "g", "gr", "j", "l", "m", "n", "p", "pr", "qu", "r", "s", "t", "tr", "v", "z"]

# Some real French-like syllables (mix of CV, CVC): Repeats most except bleu to reduce frequency.
SYLLABLES = [
    "cha", "bleu", "tou", "ron", "mon", "ver", "gui", "dra", "sai", "pri",
    "tra", "lieu", "che", "nau", "loi", "fei", "vra", "lou", "ris", "gre", "fon", "sou", "ne", "lé", "ri", "cha", "tou", "ron", "mon", "ver", "gui", "dra", "sai", "pri",
    "tra", "lieu", "che", "nau", "loi", "fei", "vra", "lou", "ris", "gre", "fon", "sou", "ne", "lé", "ri",

]
# Some common French endings

ENDINGS = ["e", "é", "eur", "ette", "ance", "isme", "oir", "eux", "ment"]

def generate_syllable():
    return random.choice(SYLLABLES)

def generate_word(min_syll=1, max_syll=3):
    n = random.randint(min_syll, max_syll)
    word = ''.join(generate_syllable() for _ in range(n))
    
    # Optionally add a Frenchy suffix
    if random.random() < 0.5:
        word += random.choice(ENDINGS)
    return word

def generate_phrase(n: int = 10) -> str:
    return " ".join(generate_word() for _ in range(n))

def format_text(text):
    words = text.split()
    lines = []
    
    i = 0
    while i < len(words):
        # Decide how many lines in this stanza (1 to 4)
        stanza_line_count = random.randint(2, 4)
        stanza = []

        for _ in range(stanza_line_count):
            # Decide how many words in this line (3 to 8)
            word_count = random.randint(3, 9)
            line_words = words[i:i + word_count]
            if not line_words:
                break
            sentence = ' '.join(line_words).capitalize()
            sentence += '?' if random.random() < 0.1 else '.'
            stanza.append(sentence)
            i += word_count
            if i >= len(words):
                break
        
        lines.extend(stanza)
        lines.append('')  # Empty line between stanzas

    return '\n'.join(lines).strip()

# quick demo
if __name__ == "__main__":
    content = ""
    for _ in range(20):
        content += ' ' + generate_phrase()

    content = format_text(content)
    print(content)

