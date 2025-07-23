# Sistema de Score - Atualizações Implementadas

## 🎯 Principais Mudanças

### 1. Metas Específicas por Time
Cada time agora possui suas próprias metas para cada indicador:

**FISCAL - ANÁLISE**
- Resolvidos: 92
- TMR: 7,9 horas
- SLA: 85%
- FCR: 50%
- CSAT: 97%

**FISCAL - ATENDIMENTO**
- Resolvidos: 122
- TMR: 2,2 horas
- SLA: 95%
- FCR: 63%
- CSAT: 97%

**RENTAL - ANÁLISE**
- Resolvidos: 120
- TMR: 9,5 horas
- SLA: 85%
- FCR: 45%
- CSAT: 97%

**RENTAL - ATENDIMENTO**
- Resolvidos: 121
- TMR: 4,4 horas
- SLA: 90%
- FCR: 62%
- CSAT: 97%

**BACKOFFICE - ANÁLISE**
- Resolvidos: 127
- TMR: 6,7 horas
- SLA: 85%
- FCR: 57%
- CSAT: 97%

**BACKOFFICE - ATENDIMENTO**
- Resolvidos: 138
- TMR: 1,4 horas
- SLA: 95%
- FCR: 67%
- CSAT: 97%

### 2. Novos Cálculos Implementados

Os cálculos agora usam as metas específicas de cada time:

- **% de Resolvidas** = (Valor_Preenchido.Resolvido / Meta.Resolvidos.time) × 100
- **% de TMR** = (Meta.TMR.time / Valor_Preenchido.TMR) × 100
- **% de SLA** = (Valor_Preenchido.SLA / Meta.SLA.time) × 100
- **% de FCR** = (Valor_Preenchido.FCR / Meta.FCR.time) × 100
- **% de CSAT** = (Valor_Preenchido.CSAT / Meta.CSAT.time) × 100

**Score Final** = (((% de Resolvidas × 30) + (% de TMR × 20) + (% de SLA × 20) + (% de FCR × 15) + (% de CSAT × 15)) / 5) / 1000

### 3. Interface de Administração

Nova rota `/admin/metas` para gerenciar as metas:
- Visualização de todas as metas por time
- Edição individual por time
- Salvamento em lote de todas as metas
- Interface moderna e responsiva
- Validações de dados

### 4. Estrutura de Arquivos

```
score-sistema-atualizado/
├── app.py                    # Aplicação principal com novas rotas
├── metas_times.json         # Arquivo de metas (criado automaticamente)
├── templates/
│   ├── index.html           # Interface principal (atualizada)
│   ├── home.html            # Painel admin (atualizado)
│   ├── admin_metas.html     # Nova interface de metas
│   └── login.html           # Login de administração
├── requirements.txt         # Dependências
├── instalar_e_executar.bat  # Script Windows
├── instalar_e_executar.sh   # Script Linux/Mac
└── README.md               # Instruções de uso
```

## 🚀 Como Usar

### Execução
1. Execute `instalar_e_executar.bat` (Windows) ou `instalar_e_executar.sh` (Linux/Mac)
2. Ou manualmente: `pip install -r requirements.txt && python app.py`
3. Acesse: http://localhost:5000

### Administração
1. Clique em "Administração" na página principal
2. Login: `admin` / Senha: `1234`
3. Acesse "Gerenciar Metas" para configurar as metas dos times

### Cálculo de Score
1. Selecione o time/núcleo
2. Preencha os valores obtidos
3. O sistema calculará automaticamente usando as metas específicas do time

## 🔧 APIs Disponíveis

- `GET /api/nucleos` - Lista times disponíveis
- `POST /api/calculate-score` - Calcula score com metas específicas
- `GET /api/metas` - Obtém todas as metas (requer login)
- `POST /api/metas` - Atualiza todas as metas (requer login)
- `PUT /api/metas/<time>` - Atualiza metas de um time específico (requer login)

## ✅ Funcionalidades Testadas

- ✅ Cálculo de score com metas específicas
- ✅ Interface de administração de metas
- ✅ Salvamento e carregamento de metas
- ✅ Validações de dados
- ✅ Responsividade da interface
- ✅ Sistema de autenticação
- ✅ APIs REST funcionais

## 📊 Exemplo de Teste

**Time:** Fiscal Análise
**Valores inseridos:**
- Resolvidos: 85
- TMR: 6,5 horas
- SLA: 90%
- FCR: 55%
- CSAT: 95%

**Resultado:**
- % Resolvidas: 92,39%
- % TMR: 121,54%
- % SLA: 105,88%
- % FCR: 110%
- % CSAT: 97,94%
- **Score Final: 2,09**

