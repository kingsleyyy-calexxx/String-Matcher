import spacy

nlp = spacy.load("en_core_web_md")

def tokenize(text):

    #String pre-processing to convert it into lowercase
    tokens = [token.text.lower() for token in nlp(text)]
    return tokens

def fnSimilar(str1, str2):
    if not str1.strip() or not str2.strip():
        return -1
    # Tokenization - Conversion of strings into tokens (individual words)
    tokens1 = tokenize(str1)
    tokens2 = tokenize(str2)
    if not tokens1 or not tokens2:
        return -1

    try:
        similarity = nlp(" ".join(tokens1)).similarity(nlp(" ".join(tokens2)))
        final = similarity * 100
        return final
    except Exception:
        return 0


str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

percentage = fnSimilar(str1, str2)
try:
    print(f"Similarity Percentage: {percentage:.2f}%")
except Exception as e:
    print("Undefined Exception has occured!",e)
