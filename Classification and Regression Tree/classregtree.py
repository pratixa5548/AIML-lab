import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn import preprocessing

def run_cart():
    # Step 1: Load sample dataset (PlayTennis)
    data = {
        'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain',
                    'Rain', 'Overcast', 'Sunny',
                    'Sunny', 'Rain', 'Sunny', 'Overcast', 'Overcast', 'Rain'],
        'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool',
                        'Cool', 'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild'],
        'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal',
                     'Normal', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High'],
        'Wind': ['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong',
                 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Strong'],
        'PlayTennis': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes',
                       'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
    }

    df = pd.DataFrame(data)

    # Step 2: Encode categorical variables
    le_dict = {}
    encoded_df = pd.DataFrame()
    for col in df.columns:
        le = preprocessing.LabelEncoder()
        encoded_df[col] = le.fit_transform(df[col])
        le_dict[col] = le  # Save encoder for reverse lookup

    # Step 3: Separate features and target
    X = encoded_df.drop('PlayTennis', axis=1)
    y = encoded_df['PlayTennis']

    # Step 4: Train CART Decision Tree (uses Gini index by default)
    clf = DecisionTreeClassifier(criterion='gini')
    clf.fit(X, y)

    # Step 5: Print root node feature
    root_index = clf.tree_.feature[0]
    root_feature = X.columns[root_index]
    print(f"\n📍 Root node of CART decision tree: {root_feature}")

    # Step 6: Print the full decision rules
    print("\n🧠 CART Decision Tree Rules (Gini Index):\n")
    print(export_text(clf, feature_names=list(X.columns)))

    # Step 7: User input for prediction
    print("\n🔢 Enter the values for prediction:")
    outlook = input("Outlook (Sunny/Overcast/Rain): ").capitalize()
    temperature = input("Temperature (Hot/Mild/Cool): ").capitalize()
    humidity = input("Humidity (High/Normal): ").capitalize()
    wind = input("Wind (Weak/Strong): ").capitalize()

    # Create sample dataframe and encode it
    sample = pd.DataFrame([[outlook, temperature, humidity, wind]], columns=X.columns)
    for col in sample.columns:
        sample[col] = le_dict[col].transform(sample[col])

    # Predict and decode the result
    prediction = clf.predict(sample)
    predicted_class = le_dict['PlayTennis'].inverse_transform(prediction)
    print(f"\n🔍 Prediction for [{outlook}, {temperature}, {humidity}, {wind}]: PlayTennis = {predicted_class[0]}")

if __name__ == "__main__":
    run_cart()
