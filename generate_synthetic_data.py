# generate_synthetic_data.py

import pandas as pd
import numpy as np

def generate_synthetic_data(n=10000, seed=42):
    np.random.seed(seed)

    # 1. Geração de datas (últimos 12 meses)
    start = pd.Timestamp('2024-04-18') - pd.Timedelta(days=365)
    end   = pd.Timestamp('2024-04-18')
    dates = pd.to_datetime(
        np.random.randint(start.value // 10**9, end.value // 10**9, n),
        unit='s'
    )

    # 2. Geração de valores e 2% de outliers
    amount = np.random.normal(loc=50, scale=15, size=n)
    outlier_idx = np.random.choice(n, size=int(0.02 * n), replace=False)
    amount[outlier_idx] = np.random.uniform(100, 200, size=len(outlier_idx))

    # 3. Flags de isenção (20% True) e tipos de isenção
    exemption_flag = np.random.choice([True, False], size=n, p=[0.2, 0.8])
    types = ['VIP', 'Promoção', 'ErroSistema', 'CoberturaEspecial']
    exemption_type = [np.random.choice(types) if flag else None for flag in exemption_flag]

    # 4. Categorias de cliente, canal de pagamento e região
    customer_category = np.random.choice(
        ['Retail','Corporate','Government'], size=n, p=[0.6,0.3,0.1]
    )
    payment_channel = np.random.choice(
        ['Cartão','Boleto','PIX'], size=n, p=[0.5,0.2,0.3]
    )
    region = np.random.choice(
        ['Norte','Nordeste','Centro-Oeste','Sudeste','Sul'], size=n
    )

    # 5. Montagem do DataFrame
    df = pd.DataFrame({
        'transaction_id': np.arange(1, n+1),
        'date': dates,
        'amount': amount,
        'exemption_flag': exemption_flag,
        'exemption_type': exemption_type,
        'customer_category': customer_category,
        'payment_channel': payment_channel,
        'region': region
    })

    # 6. Simulação de dados faltantes (~1%) e limpeza
    for col in ['exemption_type', 'region']:
        missing_idx = np.random.choice(n, size=int(0.01 * n), replace=False)
        df.loc[missing_idx, col] = None

    df['exemption_type'].fillna('None', inplace=True)
    df['region'].fillna('Unknown', inplace=True)
    df['date'] = pd.to_datetime(df['date'])
    df.drop_duplicates(subset='transaction_id', inplace=True)

    return df

if __name__ == '__main__':
    df = generate_synthetic_data()
    df.to_csv('synthetic_transactions.csv', index=False)
    print(f"Base sintética criada com {len(df)} registros em 'synthetic_transactions.csv'")
