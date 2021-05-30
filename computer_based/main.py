import login, getFeatures, getNewEntries
import pandas as pd
import pickle
import numpy as np

# FOR REGISTRATION
# login.login.run()
'''
features = getFeatures.run(0.01, 300)  # record for 3 seconds with 0.01s interval

feat_df = pd.DataFrame(features)
print(feat_df)

feat_df.to_csv('dataset.csv', index=False)  # save data into CSV
'''

''''''
# FOR TYPICAL USERS
from sklearn.decomposition import PCA
import sklearn.preprocessing as pproc

pca = PCA(n_components=0.99)
scaler = pproc.StandardScaler()

pkl_filename = 'models/user1_ocSVM.pkl'
with open(pkl_filename, 'rb') as file:
    pickle_model = pickle.load(file)

entries = 20
while True:
    count = 0
    instantData = []
    for newEntry in getNewEntries.run():
        if newEntry == [[]]:
            continue

        if count == entries:
            break

        instantData.extend(newEntry)

        count += 1

    X_scaled = scaler.fit_transform(instantData)
    X_PCA = pca.fit_transform(X_scaled)
    pred = pickle_model.fit_predict(X_PCA)
    scores_test = pickle_model.score_samples(X_PCA)
    thresh_test = np.quantile(scores_test, 0.03)
    # index = np.where(scores_test <= thresh_test)
    # values_test = X_PCA[index]

    #CHECK THESE TWO TO DETERMINE THE GENUINE USER
    print(scores_test <= thresh_test)
    print(pred)


    # print("P(anomaly) = ", (pred == -1).sum() / entries * 100)
