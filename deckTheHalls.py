from music import *      

# WN = Whole Note, HN = Half Note, QN = Quarter Note, EN = Eighth Note, SN = Sixteenth Note

rightHand = Phrase(0.0)
leftHand = Phrase(0.0)

pianoPart = Part(VIOLIN, 0)
pianoPart.setTempo(120)

mainThemeRH = [
    G4, F4, E4, D4,
    C4, D4, E4, C4,
]

durationMainThemeRH = [
    DQN, EN, QN, QN,
    QN, QN, QN, QN
]

mainThemeLH = [
    C3,
    C3,
]

durationMainThemeLH = [
    WN,
    WN,
]


pitches1RH   = [
    D4, E4, F4, D4, E4, D4,
    C4, B3, C4,
    D4, E4, F4, D4,
    E4, F4, G4, D4,
    E4, F4, G4, A4, B4, C5,
    B4, A4, G4 
]

durations1RH = [
    EN, EN, EN, EN, DQN, EN,
    QN, QN, HN,
    DQN, EN, QN, QN,
    DQN, EN, QN, QN,
    EN, EN, QN, EN, EN, QN,
    QN, QN, HN
]

pitches1LH   = [
    F3,
    G3, C3,
    G3,
    C3,
    C3, D3,
    G3, D3, G3
]
durations1LH = [
    WN,
    HN, HN,
    WN,
    WN,
    HN, HN,
    QN, QN, HN
]

lastPartRH = [
    A4, A4, A4, A4, G4, F4,
    E4, D4, C4
]

durationsLastPartRH = [
    EN, EN, EN, EN, DQN, EN,
    QN, QN, HN
]

lastPartLH = [
    C3, C3,
    G3, C3
]

durationsLastPartLH = [
    HN, HN,
    HN, HN
]

rightHand.addNoteList(mainThemeRH, durationMainThemeRH)
leftHand.addNoteList(mainThemeLH, durationMainThemeLH)

rightHand.addNoteList(pitches1RH, durations1RH)
leftHand.addNoteList(pitches1LH, durations1LH)

rightHand.addNoteList(mainThemeRH, durationMainThemeRH)
leftHand.addNoteList(mainThemeLH, durationMainThemeLH)

rightHand.addNoteList(lastPartRH, durationsLastPartRH)
leftHand.addNoteList(lastPartLH, durationsLastPartLH)

pianoPart.addPhrase(rightHand)   
pianoPart.addPhrase(leftHand)   


Play.midi(pianoPart)


