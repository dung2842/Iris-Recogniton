import pickle
from modules.feature_extraction import extract_feature

def enroll_user(username, image_path):

    feature = extract_feature(image_path)

    db = {}

    try:
        with open("database/features.pkl","rb") as f:
            db = pickle.load(f)
    except:
        pass

    db[username] = feature

    with open("database/features.pkl","wb") as f:
        pickle.dump(db,f)