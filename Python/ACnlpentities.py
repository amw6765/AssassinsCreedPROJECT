from collections import Counter
import pygal
import spacy as spacy

#nlp = spacy.cli.download("en_core_web_sm")
nlp = spacy.load('en_core_web_sm')
#lemmatizer = nlp.get_pipe("lemmatizer")
#print(lemmatizer.mode)  # 'rule'

acDiologue = open('acDiologue.txt', 'r', encoding='utf8', errors='ignore')

words = acDiologue.read()
#print(words)
nlpwords = nlp(words)

def entitycollector(words):
    ents = []
    count = 0
    for entity in words.ents:
        if entity.label_ == "GPE" or entity.label_ == "LOC" or entity.label_ == "NORP":
            if entity.text != "DR" and entity.text != "Swordfish" and entity.text != "Gla" and entity.text != "Animus" and entity.text != "Poseidon" and entity.text != "Kleon" and entity.text != "Pythia" and entity.text != "Aspasia" and entity.text != "Hippokrates" and entity.text != "Aristophanes":
                count += 1

                ents.append(entity.text)
                print(count, ": ", entity, entity.label_, spacy.explain(entity.label_))

    return ents

listEnts = entitycollector(nlpwords)
ent_freq = Counter(listEnts)
topTen = ent_freq.most_common(10)
print(topTen)
lastTen = ent_freq.most_common()[:-5:-1]

bar_chartOver10 = pygal.Bar()
bar_chartTopTen = pygal.Bar()

bar_chartOver10.title = 'Noun Lemma Forms in Disney Songs'
bar_chartTopTen.title='Top ten places and peoples in AC Odyssey'

for a in ent_freq:
    # verb_freq is a dictionary structure, so we return its key and its value:
    print(a, ent_freq[a])
    if ent_freq[a] > 10:
        bar_chartOver10.add(a, ent_freq[a])


for t in topTen:
    # this is a list of tuples, so we return its values like this:
    print(t[0], t[1])
    bar_chartTopTen.add(t[0], t[1])

# print(bar_chart)
print(bar_chartOver10.render(is_unicode=True))
bar_chartOver10.render_to_file('bar_chartOver10.svg')
bar_chartTopTen.render_to_file('bar_chartTopTen.svg')


# On windows ctrl / comments out blocks.
# On mac command / comments out blocks

# lowercaseList = []
# for l in listVerbs:
#     l = str(l).lower()
#     lowercaseList.append(l)
# setVerbs = set(lowercaseList)
# count = 0
# for s in setVerbs:
#     count += 1
# print(sorted(setVerbs))
# print(count)
