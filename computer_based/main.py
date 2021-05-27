import login, getFeatures
import pandas as pd

# login.login.run()
features = getFeatures.run(0.01, 20)  # record for 3 seconds with 0.01s interval

feat_df = pd.DataFrame(features)
print(feat_df.head(10))

feat_df.to_csv('test.csv')  # save data into CSV
