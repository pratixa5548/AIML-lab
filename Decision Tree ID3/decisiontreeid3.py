import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn import preprocessing

def main():
    print("🟢 Decision Tree Classifier (ID3 Algorithm)\n")

    # Step 1: User-defined dataset
    num_attributes = int(input("Enter number of attributes: "))
    attribute_names = []
    domains = []

    for i in range(num_attributes):
        attr = input(f"Enter name of attribute {i+1}: ")
        values = input(f"Enter possible values for {attr} (comma separated): ").split(',')
        values = [v.strip() for v in values]
        attribute_names.append(attr)
        domains.append(values)

    target_attribute = input("Enter name of target attribute (e.g. PlayTennis): ")
    target_values = input(f"Enter possible values for {target_attribute} (comma separated): ").split(',')
    target_values = [v.strip() for v in target_values]

    num_examples = int(input("\nEnter number of examples: "))
    data = {attr: [] for attr in attribute_names}
    data[target_attribute] = []

    print("\n🔹 Enter examples one by one:")
    for i in range(num_examples):
        print(f"\nExample {i+1}:")
        for attr in attribute_names:
            val = input(f"  {attr}: ").strip()
            data[attr].append(val)
        label = input(f"  {target_attribute}: ").strip()
        data[target_attribute].append(label)

    df = pd.DataFrame(data)

    # Step 2: Encode the categorical values
    le_dict = {}
    encoded_df = pd.DataFrame()
    for col in df.columns:
        le = preprocessing.LabelEncoder()
        encoded_df[col] = le.fit_transform(df[col])
        le_dict[col] = le

    X = encoded_df.drop(target_attribute, axis=1)
    y = encoded_df[target_attribute]

    # Step 3: Train the decision tree
    clf = DecisionTreeClassifier(criterion='entropy')
    clf.fit(X, y)

    # Step 4: Display the root node
    root_feature_index = clf.tree_.feature[0]
    root_feature = X.columns[root_feature_index]
    print("\n📍 Root node of the decision tree:", root_feature)

    # Step 5: Show the full decision tree rules
    print("\n🧠 Decision Tree (ID3) Rules:\n")
    print(export_text(clf, feature_names=list(X.columns)))

    # Step 6: Take test input from user
    print("\n🔍 Make a prediction based on input values:")
    sample_data = []
    for attr in attribute_names:
        val = input(f"  Enter value for {attr}: ").strip()
        sample_data.append(val)

    sample_df = pd.DataFrame([sample_data], columns=attribute_names)
    for col in sample_df.columns:
        sample_df[col] = le_dict[col].transform(sample_df[col])

    prediction = clf.predict(sample_df)
    result = le_dict[target_attribute].inverse_transform(prediction)
    print("\n📈 Prediction:", target_attribute, "=", result[0])

if __name__ == "__main__":
    main()
