import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados
df = pd.read_csv('synthetic_transactions.csv')

# 1. Isenção por categoria de cliente
cat_pct = df.groupby('customer_category')['exemption_flag'].mean() * 100
cat_pct.plot(kind='bar', title='Percentual de Isenção por Categoria de Cliente')
plt.ylabel('% de Isenção')
plt.tight_layout()
plt.savefig('fig_customer.png')
plt.clf()

# 2. Isenção por canal de pagamento
chan_pct = df.groupby('payment_channel')['exemption_flag'].mean() * 100
chan_pct.plot(kind='bar', title='Percentual de Isenção por Canal de Pagamento')
plt.ylabel('% de Isenção')
plt.tight_layout()
plt.savefig('fig_channel.png')
plt.clf()

# 3. Isenção por região
region_pct = df.groupby('region')['exemption_flag'].mean() * 100
region_pct.plot(kind='bar', title='Percentual de Isenção por Região')
plt.ylabel('% de Isenção')
plt.tight_layout()
plt.savefig('fig_region.png')
plt.clf()

# 4. Distribuição dos valores de transação
df['amount'].plot(kind='hist', bins=50, title='Distribuição dos Valores de Transação')
plt.xlabel('Valor da Transação (R$)')
plt.tight_layout()
plt.savefig('fig_distribution.png')
plt.clf()

print("Gráficos salvos com sucesso!")
