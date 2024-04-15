import pandas as pd
import spacy 

#setting up dataframe 
df = pd.read_csv('raw\slang.csv')
word_and_def = df[['Slang term','Definition']]
word_and_def.set_index('Slang term',inplace=True)

#language model loading and testing
nlp = spacy.load('en_core_web_lg')
s1 = nlp('Steve believes in the God of the Bible')
s2 = nlp('Adam is a Christian by faith')
s3 = nlp('Used to describe someone who is behaving or expressing themselves in a resentful, bitter, or irritated manner.')
s4 = nlp('Term used to express a feeling of shock, embarrassment, or disappointment toward something or someone.')

sim=[-99]
match='Error'


#convert df to dict bc im lazy and dont like to learn
words_dict = dict(zip(df['Slang term'], df['Definition']))

user_word = input('Enter the word you want to find a synonym for: ')

#if input already in dict
if user_word in words_dict.keys():
    user_defi = words_dict[user_word]
else:
    user_defi = input(f'Please enter a concise (1-2 sentence) definiton for "{user_word}": ')
    words_dict[user_word] = user_defi




# user_defi = word_and_def.loc[user_word].values[0] #this does the same thing as the print later



for defi in words_dict.values():
    sim_score = (nlp(user_defi)).similarity(nlp(defi))
    if sim_score > max(sim) and (sim_score != 1):
        match = defi
        #print(f'NEXT BEST DEFI: {match}')
    sim.append(sim_score)

for word, defi in words_dict.items():
    if defi == match:
        match_word = word
print(f'The next best slang word in my dictionary is "{match_word}"')
print(f'The definition for {match_word} is:\n"{match}"')





