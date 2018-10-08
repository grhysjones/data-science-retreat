import sys

from palladium.config import get_config


def predict(features):
    model = get_config()['model_persister'].read()
    result = model.predict_proba([features])[0]
    for class_, proba in zip(model.classes_, result):
        print("{}: {:.1f}%".format(class_, proba*100))


if __name__ == '__main__':
    predict([float(v) for v in sys.argv[1:]])
