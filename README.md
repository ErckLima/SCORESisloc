# 📊 Sistema de Cálculo de Score - Analistas

Sistema web para calcular scores de performance de analistas com metas específicas por time.

## 🚀 Deploy Rápido

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/sistema-score)

## ✨ Funcionalidades

- 📊 **Cálculo de Score** com metas específicas por time
- 🎯 **6 Times Configurados** (Fiscal, Rental, Back - Análise/Atendimento)
- 🔧 **Interface de Administração** para gerenciar metas
- 📱 **Design Responsivo** para desktop e mobile
- 🔐 **Sistema de Autenticação** para área administrativa
- 💾 **Persistência de Dados** em JSON

## 🎯 Times e Metas

### Fiscal Análise
- Resolvidos: 92 | TMR: 7,9h | SLA: 85% | FCR: 50% | CSAT: 97%

### Fiscal Atendimento  
- Resolvidos: 122 | TMR: 2,2h | SLA: 95% | FCR: 63% | CSAT: 97%

### Rental Análise
- Resolvidos: 120 | TMR: 9,5h | SLA: 85% | FCR: 45% | CSAT: 97%

### Rental Atendimento
- Resolvidos: 121 | TMR: 4,4h | SLA: 90% | FCR: 62% | CSAT: 97%

### Back Análise
- Resolvidos: 127 | TMR: 6,7h | SLA: 85% | FCR: 57% | CSAT: 97%

### Back Atendimento
- Resolvidos: 138 | TMR: 1,4h | SLA: 95% | FCR: 67% | CSAT: 97%

## 🧮 Fórmula de Cálculo

```
% Resolvidas = (Valor_Inserido / Meta_Time) × 100
% TMR = (Meta_TMR_Time / Valor_Inserido) × 100  
% SLA = (Valor_Inserido / Meta_SLA_Time) × 100
% FCR = (Valor_Inserido / Meta_FCR_Time) × 100
% CSAT = (Valor_Inserido / Meta_CSAT_Time) × 100

Score = (((% Resolvidas × 30) + (% TMR × 20) + (% SLA × 20) + (% FCR × 15) + (% CSAT × 15)) / 5) / 1000
```

## 🔑 Credenciais

- **Usuário:** `admin`
- **Senha:** `1234`

## 🛠️ Tecnologias

- **Backend:** Python Flask
- **Frontend:** HTML5, CSS3, JavaScript
- **Deploy:** Railway
- **Dados:** JSON

## 📱 Uso

1. **Acesse** o sistema
2. **Selecione** o time/núcleo
3. **Preencha** os valores obtidos
4. **Calcule** o score automaticamente

### Administração
1. **Clique** em "Administração"
2. **Login** com credenciais
3. **Gerencie** metas dos times

## 🚀 Deploy Local

```bash
# Clonar repositório
git clone https://github.com/seu-usuario/sistema-score.git
cd sistema-score

# Instalar dependências
pip install -r requirements.txt

# Executar
python app.py

# Acessar
http://localhost:5000
```

## 📄 Licença

MIT License - Livre para uso comercial e pessoal.

---

**Desenvolvido para otimizar a gestão de performance de equipes de análise e atendimento.** 📊✨

