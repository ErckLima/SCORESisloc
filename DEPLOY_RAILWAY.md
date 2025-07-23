# 🚀 Deploy no Railway - Sistema Score

## 📋 **Pré-requisitos**
- Conta no GitHub (gratuita)
- Conta no Railway (gratuita)

---

## 🎯 **Passo a Passo Completo**

### **1. Preparar Repositório GitHub**

1. **Acesse:** https://github.com
2. **Faça login** na sua conta
3. **Clique em:** "New repository" (botão verde)
4. **Configure:**
   - Repository name: `sistema-score`
   - Description: `Sistema de Cálculo de Score - Analistas`
   - ✅ Public (deixe marcado)
   - ✅ Add a README file
5. **Clique:** "Create repository"

### **2. Upload dos Arquivos**

1. **Na página do repositório criado:**
   - Clique em "uploading an existing file"
2. **Arraste todos os arquivos** desta pasta para a área de upload
3. **Commit changes:**
   - Título: `Deploy inicial do sistema`
   - Descrição: `Sistema completo com interface de admin`
4. **Clique:** "Commit changes"

### **3. Deploy no Railway**

1. **Acesse:** https://railway.app
2. **Clique:** "Login" → "Login with GitHub"
3. **Autorize** o Railway no GitHub
4. **No Dashboard:**
   - Clique "New Project"
   - Selecione "Deploy from GitHub repo"
   - Escolha o repositório `sistema-score`
5. **Aguarde** o deploy automático (2-3 minutos)

### **4. Configurar Domínio**

1. **No painel do Railway:**
   - Clique na aba "Settings"
   - Seção "Domains"
   - Clique "Generate Domain"
2. **Copie o link** gerado (ex: `sistema-score-production.up.railway.app`)

---

## ✅ **Pronto! Sistema Online**

### **🌐 Acessos:**
- **Sistema Principal:** `https://seu-dominio.up.railway.app`
- **Administração:** `https://seu-dominio.up.railway.app/adm`

### **🔑 Credenciais:**
- **Usuário:** `admin`
- **Senha:** `1234`

---

## 🔧 **Configurações Avançadas (Opcional)**

### **Variáveis de Ambiente**
No Railway, aba "Variables":
- `SECRET_KEY`: `sua-chave-super-secreta-aqui`
- `FLASK_ENV`: `production`

### **Domínio Personalizado**
1. No Railway: Settings → Domains
2. Clique "Custom Domain"
3. Digite seu domínio
4. Configure DNS conforme instruções

---

## 📊 **Monitoramento**

### **Logs em Tempo Real:**
- Railway Dashboard → aba "Deployments"
- Clique no deployment ativo
- Aba "Logs" para ver atividade

### **Métricas:**
- CPU, RAM e tráfego na aba "Metrics"
- Alertas automáticos por email

---

## 🆘 **Solução de Problemas**

### **Deploy Falhou:**
1. Verifique logs na aba "Deployments"
2. Confirme se todos os arquivos foram enviados
3. Redeploy: Settings → "Redeploy"

### **Site não carrega:**
1. Aguarde 2-3 minutos após deploy
2. Verifique se domínio foi gerado
3. Teste em aba anônima do navegador

### **Erro 500:**
1. Verifique logs para detalhes
2. Confirme se `metas_times.json` existe
3. Redeploy se necessário

---

## 💰 **Custos**

### **Plano Gratuito:**
- ✅ $5 de crédito mensal
- ✅ Sem cold start
- ✅ SSL automático
- ✅ Domínio gratuito

### **Uso Estimado:**
- Sistema pequeno: ~$1-2/mês
- Crédito gratuito cobre tranquilamente

---

## 🔄 **Atualizações Futuras**

### **Para atualizar o sistema:**
1. Modifique arquivos no GitHub
2. Commit as mudanças
3. Railway faz redeploy automático

### **Backup das Metas:**
- Baixe `metas_times.json` periodicamente
- Railway mantém dados persistentes

---

## 🎉 **Resultado Final**

✅ **Sistema 100% online**
✅ **Acesso instantâneo (sem cold start)**
✅ **SSL/HTTPS automático**
✅ **Domínio profissional**
✅ **Backup automático**
✅ **Monitoramento incluído**

**Seu sistema estará acessível 24/7 para todos os usuários!** 🚀

