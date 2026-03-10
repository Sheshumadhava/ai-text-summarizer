from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

text = """
Artificial Intelligence is transforming industries by enabling machines to learn from data.
Machine learning models can analyze large datasets and identify patterns that humans may miss.
Natural Language Processing allows computers to understand and generate human language.
These technologies are widely used in healthcare, finance, and education.
"""

parser = PlaintextParser.from_string(text, Tokenizer("english"))
summarizer = LsaSummarizer()

summary = summarizer(parser.document, 2)

print("Summary:\n")

for sentence in summary:
    print(sentence)