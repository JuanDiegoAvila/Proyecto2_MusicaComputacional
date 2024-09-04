from music import *    

# original tempo: 110.0

score = Score("Chiptune", 110.0)

channelPart = Part(SAWTOOTH, 0)
drumPart = Part("Drums", 0, 9)

channel1Phrase = Phrase(12.0)
channel2Phrase = Phrase(0.0)
channel3Phrase = Phrase(0.0)

drumChannel = Phrase(16.00)

drumPitches = [
    CBS, MRC, CBS, MRC, CBS, MRC, CBS, MRC,
    CBS, MRC, CBS, MRC, CBS, MRC, CBS, MRC
] * 28

drumDurations = [
    SN, SN, SN, SN, SN, SN, SN, SN,
    SN, SN, SN, SN, SN, SN, SN, SN
] * 28
    
channel1Pitches = [
    REST, A4, G4,

    FS4, D4, E4, FS4,
    E4, CS4, D4, E4,
    FS4, D4, E4, FS4, D4,
    E4, A4,

    B4, D4, D4, B4,
    A4, CS4, CS4, A4,
    B4, G4, A4, B4, A4, G4, FS4,
    FS4, G4, FS4, E4,

    FS5, D5, E5, FS5,
    E5, CS5, D5, E5,
    FS5, D5, E5, FS5, D5,
    E5, A5,

    B5, D5, D5, B5,
    A5, CS5, CS5, A5,
    B5, G5, A5, A5, G5, FS5, E5,
    E5, D5, D5,

    E4, D4, D4,
    E4, D4, D4,
    E4, D4, E4, E4,
    FS4,

    B4, D4, FS4, B4, D5, B4, FS4, D4,
    CS5, FS4, AS4, CS5, E5, AS4, FS4, E4,
    B4, D4, G4, B4, D5, B4, G4, D4,
    A4, D4, FS4, A4, D5, A4, FS4, D4,

    CS5, AS4, G4, CS5, E5, CS5, AS4, CS5,
    D5, B4, FS4, D5, D5, B4, GS4, D5,
    CS5, A4, E4, A4, E5, CS5, A4, CS5, 
    A5, REST 
]

channel1Durations = [
    DHN, EN, EN,

    DQN, EN, QN, QN,
    DQN, EN, QN, QN,
    DQN, EN, QN, EN, EN,
    HN, HN,

    DQN, EN, QN, QN,
    DQN, EN, QN, QN,
    QN, EN, EN, EN, EN, EN, EN,
    QN, EN, EN, HN,

    DQN, EN, QN, QN,
    DQN, EN, QN, QN,
    DQN, EN, QN, EN, EN,
    HN, HN,

    DQN, EN, QN, QN,
    DQN, EN, QN, QN,
    QN, EN, EN, EN, EN, EN, EN,
    DQN, EN, HN,

    DQN, EN, HN,
    DQN, EN, HN,
    DQN, EN, QN, QN,
    WN,

    EN, EN, EN, EN, EN, EN, EN, EN,
    EN, EN, EN, EN, EN, EN, EN, EN,
    EN, EN, EN, EN, EN, EN, EN, EN,
    EN, EN, EN, EN, EN, EN, EN, EN,

    EN, EN, EN, EN, EN, EN, EN, EN,
    EN, EN, EN, EN, EN, EN, EN, EN,
    EN, EN, EN, EN, EN, EN, EN, EN,
    HN, HN
]

channel2Pitches = [
    FS3, A3, D4, A3, FS3,
    E3, A3, CS4, A3, G3,
    FS3, B3, D4, B3, A3,
    G3, A3, CS4,
    
    D3, FS3, A3, FS3, A3, FS3,
    CS3, G3, A3, G3, A3, G3,
    D3, FS3, A3, FS3, A3, FS3,
    CS3, G3, A3, G3, FS3, E3,

    D3, FS3, B3, FS3, B3, FS3, B3, FS3,
    CS3, FS3, A3, FS3, A3, FS3, A3, FS3,
    D3, G3, B3, G3, B3, G3, B3, G3,
    CS3, G3, A3, G3, A3, G3, FS3, E3,

    D3, FS3, A3, FS3, A3, FS3, A3, FS3,
    CS3, G3, A3, G3, A3, G3, A3, G3,
    D3, FS3, A3, FS3, A3, FS3, A3, FS3,
    CS3, G3, A3, G3, A3, G3, FS3, E3,

    D3, FS3, B3, FS3, B3, FS3, B3, FS3,
    CS3, FS3, A3, FS3, A3, FS3, A3, FS3,
    D3, G3, B3, G3, C3, G3, A3, G3,
    D3, FS3, A3, FS3, A3, FS3,

    D3, FS3, B3, FS3, B3, FS3,
    D3, G3, B3, G3, B3, G3,
    E3, G3, B3, G3, B3, G3,
    CS3, E3, AS3, E3, AS3, E3,

    B3, D3, D3, B3,
    AS3, CS3, CS3, AS3,
    B3, D3, D3, B3,
    A3, D3, D3, A3,

    AS3, E3, E3, AS3,
    B3, FS3, E3, B3,
    E3, A3, CS4, A3, CS4, A3,
    CS3, G3, A3, A3, G3
]

channel2Durations = [
    EN, EN, HN, EN, EN,
    EN, EN, HN, EN, EN,
    EN, EN, HN, EN, EN,
    EN, EN, DHN,

    EN, EN, DQN, EN, EN, EN,
    EN, EN, DQN, EN, EN, EN,
    EN, EN, DQN, EN, EN, EN,
    EN, EN, DQN, EN, EN, EN,

    EN, EN, EN, EN, EN, EN, EN, EN,
    EN, EN, EN, EN, EN, EN, EN, EN,
    EN, EN, EN, EN, EN, EN, EN, EN,
    EN, EN, EN, EN, EN, EN, EN, EN,

    EN, EN, EN, EN, EN, EN, EN, EN,
    EN, EN, EN, EN, EN, EN, EN, EN,
    EN, EN, EN, EN, EN, EN, EN, EN,
    EN, EN, EN, EN, EN, EN, EN, EN,

    EN, EN, EN, EN, EN, EN, EN, EN,
    EN, EN, EN, EN, EN, EN, EN, EN,
    EN, EN, EN, EN, EN, EN, EN, EN,
    EN, EN, DQN, EN, EN, EN,

    EN, EN, DQN, EN, EN, EN,
    EN, EN, DQN, EN, EN, EN,
    EN, EN, DQN, EN, EN, EN,
    EN, EN, DQN, EN, EN, EN,

    DQN, EN, QN, QN,
    DQN, EN, QN, QN,
    DQN, EN, QN, QN,
    DQN, EN, QN, QN,

    DQN, EN, QN, QN,
    DQN, EN, QN, QN,
    EN, EN, DQN, EN, EN, EN,
    EN, EN, HN, EN, EN
]

channel3Pitches = [
    D3, D3,
    CS3, CS3,
    B2, B2, 
    A2, A2,

    D2, D2, D3,
    A2, A2, A2,
    D2, D2, D3,
    A2, A2, A2,

    B2, B2, B2,
    FS2, FS2, FS2,
    G2, G2, G2,
    A2, A2, E3, A2,

    D2, D2, D3,
    A2, A2, A2,
    D2, D2, D3,
    A2, A2, A2,

    B2, B2, B2,
    FS2, FS2, FS2,
    G2, G2, A2, E2,
    D2, D2, D3,

    B2, B2, B2,
    G2, G2, G2,
    E2, E2, E2,
    FS2, FS2, FS2,

    B2, B2,
    FS2, FS2,
    G2, G2,
    B2, B2,

    CS3, CS3,
    B2, E2,
    A2, A2,
    A2, A2
]

channel3Durations = [
    DHN, QN,
    DHN, QN,
    DHN, QN,
    DHN, QN,

    DQN, EN, HN,
    DQN, EN, HN,
    DQN, EN, HN,
    DQN, EN, HN,

    DQN, EN, HN,
    DQN, EN, HN,
    DQN, EN, HN,
    DQN, EN, QN, QN,

    DQN, EN, HN,
    DQN, EN, HN,
    DQN, EN, HN,
    DQN, EN, HN,

    DQN, EN, HN,
    DQN, EN, HN,
    DQN, EN, QN, QN,
    DQN, EN, HN,

    DQN, EN, HN,
    DQN, EN, HN,
    DQN, EN, HN,
    DQN, EN, HN,

    HN, HN,
    HN, HN,
    HN, HN,
    HN, HN,

    HN, HN,
    HN, HN,
    HN, HN,
    HN, HN
]

channel1Phrase.addNoteList(channel1Pitches, channel1Durations)
channel2Phrase.addNoteList(channel2Pitches, channel2Durations)
channel3Phrase.addNoteList(channel3Pitches, channel3Durations)

drumChannel.addNoteList(drumPitches, drumDurations)

channelPart.addPhrase(channel1Phrase)
channelPart.addPhrase(channel2Phrase)
channelPart.addPhrase(channel3Phrase)
drumPart.addPhrase(drumChannel)

channel1Phrase2 = channel1Phrase.copy()
channel2Phrase2 = channel2Phrase.copy()
channel3Phrase2 = channel3Phrase.copy()
drumChannel2 = drumChannel.copy()

channel1Phrase2.setStartTime(channel1Phrase.getStartTime() + 32 * 4)
channel2Phrase2.setStartTime(channel2Phrase.getStartTime() + 32 * 4)
channel3Phrase2.setStartTime(channel3Phrase.getStartTime() + 32 * 4)
drumChannel2.setStartTime(drumChannel.getStartTime() + 32 * 4)

chanel2Part = channelPart.copy()
drum2Part = drumPart.copy()

chanel2Part.addPhrase(channel1Phrase2)
chanel2Part.addPhrase(channel2Phrase2)
chanel2Part.addPhrase(channel3Phrase2)
drum2Part.addPhrase(drumChannel2)

score.addPart(channelPart)
score.addPart(drumPart)

score.addPart(chanel2Part)
score.addPart(drum2Part)

Write.midi(score, "chiptune.mid")
Play.midi(score)
