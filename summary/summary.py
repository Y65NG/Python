from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
from nltk.tokenize import sent_tokenize, word_tokenize 
import numpy as np
import networkx as nx

def read_article(file_name):
    with open(file_name, 'r') as f:
        filedata = f.read().strip()
        sentences = sent_tokenize(filedata)

    return sentences

def build_similarity_matrix(sentences, stop_words):
    similarity_matrix = np.zeros((len(sentences), len(sentences)))
    
    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 == idx2:
                continue
            similarity_matrix[idx1][idx2] = sentence_similarity(sentences[idx1], sentences[idx2], stop_words)

    return similarity_matrix

def generate_summary(file_name, topn=5):
    stop_words = stopwords.words('english')
    summary = []
    
    sentences = read_article(file_name)
    sentence_similarity_matrix = build_similarity_matrix(sentences, stop_words)
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_matrix)
    scores = nx.pagerank(sentence_similarity_graph)

if __name__ == '__main__':
    sentences = read_article("text.txt")
    print(build_similarity_matrix(sentences, stopwords.words('english')))