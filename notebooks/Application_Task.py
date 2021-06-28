import pandas as pd
import nltk


if __name__ == '__main__':
    df = pd.read_csv('../input/20210103_hundenamen.csv')
    names = [name for name in df.iloc[:, 0] if nltk.edit_distance(name, 'Luca') == 1]
    print(','.join(set(names)))