# Sistema de Cálculo de Score - Analistas

Sistema simples em Python Flask para calcular o score dos analistas baseado em suas métricas de performance.

## 📋 Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes do Python)

## 🚀 Instalação e Execução

### 1. Baixar e extrair o projeto
Extraia todos os arquivos em uma pasta de sua escolha.

### 2. Abrir terminal/prompt de comando
Navegue até a pasta do projeto:
```bash
cd caminho/para/score-sistema-simples
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Executar a aplicação
```bash
python app.py
```

### 5. Acessar no navegador
Abra seu navegador e acesse:
```
http://localhost:5000
```

## 📁 Estrutura do Projeto

```
score-sistema-simples/
├── app.py              # Aplicação principal Flask
├── requirements.txt    # Dependências do projeto
├── README.md          # Este arquivo
└── templates/
    └── index.html     # Interface web
```

## 💻 Como Usar

1. **Selecione o Núcleo/Tipo** no dropdown
2. **Preencha os campos:**
   - Solicitações Resolvidas (número inteiro)
   - TMR em horas (ex: 1.5)
   - %SLA (0-100)
   - %FCR (0-100)
   - %CSAT (0-100)
3. **Clique em "Calcular Score"**
4. **Veja o resultado** com o score final e todas as métricas

## 🔢 Valores dos Núcleos

- **Fiscal Análise**: 100
- **Back Análise**: 200
- **Rental Análise**: 500
- **Fiscal Atendimento**: 150
- **Back Atendimento**: 250
- **Rental Atendimento**: 550

## 📊 Fórmula de Cálculo

1. **% Resolvidos da Meta** = (Solicitações Resolvidas / Valor do Núcleo) × 100
2. **% TMR da Meta** = (Valor do Núcleo / TMR) × 100
3. **% SLA da Meta** = (SLA / Valor do Núcleo) × 100
4. **% FCR da Meta** = (FCR / Valor do Núcleo) × 100
5. **% CSAT da Meta** = (CSAT / Valor do Núcleo) × 100

**Score Final** = (((1×30) + (2×20) + (3×20) + (4×15) + (5×15)) / 5) / 1000

## 🛑 Para Parar a Aplicação

No terminal onde a aplicação está rodando, pressione:
```
Ctrl + C
```

## ❗ Solução de Problemas

### Erro: "Flask não encontrado"
```bash
pip install Flask
```

### Erro: "Porta 5000 já está em uso"
Modifique a linha final do arquivo `app.py`:
```python
app.run(host='0.0.0.0', port=5001, debug=True)  # Mude para porta 5001
```

### Erro: "Python não encontrado"
Certifique-se de que o Python está instalado e no PATH do sistema.

## 🌐 API Endpoints

### POST /api/calculate-score
Calcula o score baseado nos dados fornecidos.

### GET /api/nucleos
Retorna lista de núcleos disponíveis.

## 📱 Compatibilidade

- ✅ Desktop (Chrome, Firefox, Safari, Edge)
- ✅ Mobile (responsivo)
- ✅ Windows, macOS, Linux

