from music import *

# Configuración del tempo y la parte para la melodía
melodyPart = Part(LEAD_1_SQUARE, 0)
bassPart = Part(LEAD_8_BASS_LEAD, 1)
sustainPart = Part(LEAD_4_CHIFF, 3)
echoPart = Part(LEAD_3_CALLIOPE, 2)

# Configurar el tempo para todas las partes
melodyPart.setTempo(130)
bassPart.setTempo(130)
sustainPart.setTempo(130)
echoPart.setTempo(130)

# Melodía principal
melodyNotes = (
    [REST, REST, REST, REST] +

    # Frase 1
    [E4, F4, G4, E4, D4, C4, REST] * 2 +
    [E4, F4, G4, E4, C4, A4, REST] +
    [E4, F4, G4, E4, C4, D4, REST] +

    # Frase 2
    [E4, F4, G4, E4, D4, C4, REST] +
    [E4, F4, G4, E4, C4, D4, REST] +
    [E4, F4, G4, E4, C4, A4, REST] +
    [E4, F4, G4, E4, C4, D4, REST] +

    # Estribillo (Chorus)
    [C5, D5, E5, C5, G4, A4, C5, C5] +
    [G4, C5, C5, C5, E5, D5, REST] +
    [C5, D5, E5, C5, G4, A4, C5, C5] +
    [G5, F5, E5, D5, C5, C5, REST, REST] +

    # Frase 3
    [E4, F4, G4, E4, D4, C4, REST] +
    [E4, F4, G4, E4, C4, D4, REST] +
    [E4, F4, G4, E4, C4, A4, REST] +
    [E4, F4, G4, E4, C4, D4, REST] +

    # Estribillo (Chorus)
    [C5, D5, E5, C5, G4, A4, C5, C5] +
    [G4, C5, C5, C5, E5, D5, REST] +
    [C5, D5, E5, C5, G4, A4, C5, C5] +
    [G5, F5, E5, D5, C5, C5, REST, REST] +

    # Estribillo (Chorus)
    [C5, D5, E5, C5, G4, A4, C5, C5] +
    [G4, C5, C5, C5, E5, D5, REST] +
    [C5, D5, E5, C5, G4, A4, C5, C5] +
    [G5, F5, E5, D5, C5, C5, REST, REST] +

    # Frase 3
    [E4, F4, G4, E4, D4, C4, REST] +
    [E4, F4, G4, E4, C4, D4, REST] +
    [E4, F4, G4, E4, C4, A4, REST] +
    [E4, F4, G4, E4, C4, D4, REST]
)

durations_melody = (
    [WN, WN, WN, WN] +

    # Frase 1
    [SN, SN, DQN, DQN, QN, HN, DQN] * 4 +

    # Frase 2
    [SN, SN, DQN, DQN, QN, HN, DQN] * 4 +

    # Estribillo (Coro)
    [SN, SN, DQN, DQN, QN, EN, QN, DQN] +
    [QN, QN, QN, EN, QN, QN, DHN] +
    [SN, SN, DQN, DQN, QN, EN, QN, DQN] +
    [QN, QN, QN, QN, QN, QN, DQN, QN] +

    # Frase 3
    [SN, SN, DQN, DQN, QN, HN, DQN] * 4 +

    # Estribillo (Coro)
    [SN, SN, DQN, DQN, QN, EN, QN, DQN] +
    [QN, QN, QN, EN, QN, QN, DHN] +
    [SN, SN, DQN, DQN, QN, EN, QN, DQN] +
    [QN, QN, QN, QN, QN, QN, DQN, QN] +

    # Estribillo (Coro)
    [SN, SN, DQN, DQN, QN, EN, QN, DQN] +
    [QN, QN, QN, EN, QN, QN, DHN] +
    [SN, SN, DQN, DQN, QN, EN, QN, DQN] +
    [QN, QN, QN, QN, QN, QN, DQN, QN] +

    # Frase 3
    [SN, SN, DQN, DQN, QN, HN, DQN] * 4
)

echoNotes = (
    [REST, REST] * 6 +
    [G4, B4, C5, REST, C5, REST, B4, C5, REST, C5, REST] * 4 +
    [REST, REST] * 4 +
    [C6, B5, G5, REST, G5, C6, B5, G5, REST, G5, REST] * 8 +
    [REST, REST] * 8 +
    [C6, B5, G5, REST, G5, C6, B5, G5, REST, G5, REST] * 4
)

durations_echo = (
    [WN, WN]*6 +
    [EN, EN, EN, EN, QN, EN, EN, EN, EN, QN, HN] * 4 +
    [WN, WN]*4 +
    [EN, EN, EN, EN, QN, EN, EN, EN, EN, QN, HN] * 8 +
    [WN, WN]*8 +
    [EN, EN, EN, EN, QN, EN, EN, EN, EN, QN, HN] * 4
)

bassNotes = (
    # Intro - 2
    [C4, C3, C4, C3, C4, C3, C4, C3, C4, F3, F4, F3, F4, F3, F4, F3] +
    [C4, C3, C4, C3, C4, C3, C4, C3, C4, G3, G4, G3, G4, G3, G4, G3] +

    # Frase 1 - 6
    [C4, C3, C4, C3, C4, C3, C4, C3, C4, F3, F4, F3, F4, F3, F4, F3] * 3 +
    [C4, C3, C4, C3, C4, C3, C4, C3, C4, G3, G4, G3, G4, G3, G4, G3] +

    # Frase 2 - 10
    [C4, C3, C4, C3, C4, C3, C4, C3, C4, F3, F4, F3, F4, F3, F4, F3] * 3 +
    [C4, C3, C4, C3, C4, C3, C4, C3, C4, G3, G4, G3, G4, G3, G4, G3] +

    # Estribillo (Coro) - 14
    [C4, C3, C4, C3, C4, C3, C4, C3, C4, F3, F4, F3, F4, F3, F4, F3] +
    [C4, C3, C4, C3, C4, C3, C4, C3, C4, G3, G4, G3, G4, G3, G4, G3] +
    [C4, C3, C4, C3, C4, C3, C4, C3, C4, F3, F4, F3, F4, F3, F4, F3] +
    [G4, G3, G4, G3, G4, G3, G4, G3, G4, C3, C4, C3, C4, C3, C4, C3] +

    # Frase 3 - 18
    [C4, C3, C4, C3, C4, C3, C4, C3, C4, F3, F4, F3, F4, F3, F4, F3] * 3 +
    [C4, C3, C4, C3, C4, C3, C4, C3, C4, G3, G4, G3, G4, G3, G4, G3] +

    # Estribillo (Coro) - 22
    [C4, C3, C4, C3, C4, C3, C4, C3, C4, F3, F4, F3, F4, F3, F4, F3] +
    [C4, C3, C4, C3, C4, C3, C4, C3, C4, G3, G4, G3, G4, G3, G4, G3] +
    [C4, C3, C4, C3, C4, C3, C4, C3, C4, F3, F4, F3, F4, F3, F4, F3] +
    [G4, G3, G4, G3, G4, G3, G4, G3, G4, C3, C4, C3, C4, C3, C4, C3] +

    # Estribillo (Coro) - 26
    [C4, C3, C4, C3, C4, C3, C4, C3, C4, F3, F4, F3, F4, F3, F4, F3] +
    [C4, C3, C4, C3, C4, C3, C4, C3, C4, G3, G4, G3, G4, G3, G4, G3] +
    [C4, C3, C4, C3, C4, C3, C4, C3, C4, F3, F4, F3, F4, F3, F4, F3] +
    [G4, G3, G4, G3, G4, G3, G4, G3, G4, C3, C4, C3, C4, C3, C4, C3] +

    # Frase 3 - 30
    [C4, C4, C4, C4, C4, F4, F4, F4]*3 +
    [C4, C4, C4, C4, C4, G4, G4, G4]

)

durations_bass = (
    [EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN, EN] * 26 +
    [QN, QN, QN, QN, QN, QN, QN, QN] * 4
)

sustainNotes = (
    [REST, REST]*22 +
    [C3, F4]*4 +
    [REST, REST] * 4 +
    [C3, F4]*4
)

durations_sustain = (
    [WN, WN,]*22 +
    [WN, WN]*12
)

# Creacion de frases
melodyPhrase = Phrase(0.0)
melodyPhrase.addNoteList(melodyNotes, durations_melody)

echoPhrase = Phrase(0.0)
echoPhrase.addNoteList(echoNotes, durations_echo)

bassPhrase = Phrase(0.0)
bassPhrase.addNoteList(bassNotes, durations_bass)

sustainPhrase = Phrase(0.0)
sustainPhrase.addNoteList(sustainNotes, durations_sustain)

# Añadir frases a las partes
melodyPart.addPhrase(melodyPhrase)
bassPart.addPhrase(bassPhrase)
sustainPart.addPhrase(sustainPhrase)
echoPart.addPhrase(echoPhrase)

# Reproducir todas las partes
Play.midi(sustainPart)
Play.midi(melodyPart)
Play.midi(bassPart)
Play.midi(echoPart)
