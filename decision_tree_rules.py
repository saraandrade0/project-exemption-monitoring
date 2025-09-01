import sys
import pandas as pd


print("Executando com Python:", sys.executable)

import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text


def main():
    # 1. Carregar dados sintéticos gerados previamente
    df = pd.read_csv('synthetic_transactions.csv')

    # 2. One-hot encoding de variáveis categóricas
    df_encoded = pd.get_dummies(
        df,
        columns=['exemption_type', 'customer_category', 'payment_channel', 'region'],
        drop_first=True
    )

    # 3. Definir features (X) e alvo (y)
    # Remover colunas não numéricas e não usadas
    X = df_encoded.drop(['transaction_id', 'date', 'exemption_flag'], axis=1)
    y = df_encoded['exemption_flag']

    # 4. Treinar a árvore de decisão
    clf = DecisionTreeClassifier(
        max_depth=3,
        min_samples_leaf=200,
        random_state=42
    )
    clf.fit(X, y)

    # 5. Extrair e exibir regras da árvore
    rules = export_text(clf, feature_names=list(X.columns))
    print("Regras extraídas da árvore de decisão (profundidade=3):\n")
    print(rules)

if __name__ == '__main__':
    main()
