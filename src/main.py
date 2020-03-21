# 1) Read "dictionary.txt and postings.txt" to compute term frequency weight
import os.path
from ComputeWeights import GetTfWeights, NormalizeDocLength


def main():
    tf_weights = GetTfWeights()
    for i in tf_weights:
        print(i)
    print(len(tf_weights))

    normalized_docs = NormalizeDocLength(tf_weights)

    # for n in normalized_docs:
    #    print(n)

    return


if __name__ == "__main__":
    main()