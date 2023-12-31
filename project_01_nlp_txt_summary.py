# -*- coding: utf-8 -*-
"""Project_01_nlp_txt_summary.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QpzS7F39uEPqQRhKGf8dSTiSgFLz2vn-
"""

pip install nltk

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from nltk.tokenize.treebank import TreebankWordDetokenizer

nltk.download('punkt')
nltk.download('stopwords')

def text_summarizer(text, num_sentences=5):
    # Tokenize the text into sentences and words
    sentences = sent_tokenize(text)
    words = word_tokenize(text)

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]

    # Calculate word frequency
    freq_dist = FreqDist(words)

    # Rank sentences based on word frequency
    ranked_sentences = sorted([(i, sum([freq_dist[word] for word in word_tokenize(sent.lower()) if word.isalnum()])) for i, sent in enumerate(sentences)],
                              key=lambda x: x[1], reverse=True)

    # Select the top N sentences for the summary
    selected_sentences = sorted([sentences[i] for i, _ in ranked_sentences[:num_sentences]])

    # Detokenize the selected sentences to form the final summary
    summary = TreebankWordDetokenizer().detokenize(selected_sentences)

    return summary

text_to_summarize = """
It was a sweltering day with the sun overhead when birds and animals could find very little to drink to quench their thirst. Among them was a thirsty crow who searched for water all over the fields. He looked everywhere, but there was not a drop to drink.

He felt weak and sad and thought to himself, “Caw, caw, caw. I have been searching for water since the morning, but there is not a drop in sight!” “The thirst is making me dizzy.”

Just as the crow was glooming, he suddenly saw a water pitcher. “Thank goodness! I hope there is some water in that little pitcher.”

He flew straight down to that pitcher to see if water was left in it. And to his surprise, there was some water in the pitcher.

As the crow pushed his head into the pitcher, it could not go deeper. “Oh no. I could not get to the water.” The pitcher was high with a narrow neck, and the water level was too low. He tried pushing the pitcher to a side for the water to flow out. “If I tilt this pitcher, maybe the water would come out, and I will easily drink it.” But the pitcher was very heavy to tilt.

The crow did not lose hope. He looked around and started thinking of a way to get water out of the pitcher. Then, an idea struck him! He saw some pebbles on the ground. The crow started collecting pebbles one by one and dropped them into the pitcher. As more and more pebbles went into the pitcher, the water rose up. Soon enough, the water came to a level through which the crow could drink water. He drank the water happily and thanked mother nature.

"""

summary = text_summarizer(text_to_summarize)
print(summary)

