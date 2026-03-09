import pickle
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from modules.feature_extraction import extract_feature


def authenticate(image_path):

    feature = extract_feature(image_path)

    with open("database/features.pkl","rb") as f:
        db = pickle.load(f)

    best_user = None
    best_score = -1

    for user, db_feature in db.items():

        score = cosine_similarity(
            feature.reshape(1,-1),
            db_feature.reshape(1,-1)
        )[0][0]

        if score > best_score:
            best_score = score
            best_user = user

    return best_user, best_score