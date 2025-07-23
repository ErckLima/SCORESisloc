from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import json
import os

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'  # Necessária para usar sessões

# Usuário e senha fixos para exemplo
USUARIO_VALIDO = 'admin'
SENHA_VALIDA = '1234'

def carregar_metas_times(caminho_arquivo='metas_times.json'):
    """Carrega as metas específicas de cada time do arquivo JSON"""
    try:
        if not os.path.exists(caminho_arquivo):
            # Se o arquivo não existir, cria com valores padrão
            metas_padrao = {
                "Fiscal analise": {
                    "resolvidos": 92,
                    "tmr": 7.9,
                    "sla": 85,
                    "fcr": 50,
                    "csat": 97
                },
                "Fiscal atendimento": {
                    "resolvidos": 122,
                    "tmr": 2.2,
                    "sla": 95,
                    "fcr": 63,
                    "csat": 97
                },
                "Rental analise": {
                    "resolvidos": 120,
                    "tmr": 9.5,
                    "sla": 85,
                    "fcr": 45,
                    "csat": 97
                },
                "Rental atendimento": {
                    "resolvidos": 121,
                    "tmr": 4.4,
                    "sla": 90,
                    "fcr": 62,
                    "csat": 97
                },
                "Back analise": {
                    "resolvidos": 127,
                    "tmr": 6.7,
                    "sla": 85,
                    "fcr": 57,
                    "csat": 97
                },
                "Back atendimento": {
                    "resolvidos": 138,
                    "tmr": 1.4,
                    "sla": 95,
                    "fcr": 67,
                    "csat": 97
                }
            }
            salvar_metas_times(metas_padrao, caminho_arquivo)
            return metas_padrao
        
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
        return dados
    
    except FileNotFoundError:
        print("Arquivo de metas não encontrado.")
        return {}
    except json.JSONDecodeError:
        print("Erro ao ler o conteúdo JSON das metas.")
        return {}

def salvar_metas_times(metas, caminho_arquivo='metas_times.json'):
    """Salva as metas dos times no arquivo JSON"""
    try:
        with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(metas, arquivo, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Erro ao salvar metas: {e}")
        return False

@app.route('/')
def index():
    """Página principal"""
    session.pop('usuario', None)  # Limpa a sessão (logout automático)
    return render_template('index.html')

@app.route('/homeadm')
def home():
    """Página home do administrador"""
    if 'usuario' in session:
        return render_template('home.html', usuario=session['usuario'])
    return redirect(url_for('login'))

@app.route('/adm', methods=['GET', 'POST'])
def adm():
    """Página de login do administrador"""
    erro = None

    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        if usuario == USUARIO_VALIDO and senha == SENHA_VALIDA:
            session['usuario'] = usuario
            return redirect(url_for('home'))
        else:
            erro = 'Usuário ou senha inválidos.'
    
    # Se já estiver logado, vai para home
    if 'usuario' in session:
        return redirect(url_for('home'))

    return render_template('login.html', erro=erro)

@app.route('/admin/metas')
def admin_metas():
    """Página de administração das metas"""
    if 'usuario' not in session:
        return redirect(url_for('adm'))
    
    metas = carregar_metas_times()
    return render_template('admin_metas.html', metas=metas)

@app.route('/api/calculate-score', methods=['POST'])
def calculate_score():
    """Calcula o score baseado nos dados fornecidos e metas específicas do time"""
    try:
        data = request.json
        
        # Extrair dados do request
        nucleo_tipo = data.get('nucleo_tipo')
        solicitacoes_resolvidas = float(data.get('solicitacoes_resolvidas', 0))
        tmr = float(data.get('tmr', 0))
        sla = float(data.get('sla', 0))
        fcr = float(data.get('fcr', 0))
        csat = float(data.get('csat', 0))
        
        # Carregar metas dos times
        metas_times = carregar_metas_times()
        
        # Validar se o núcleo/tipo existe
        if nucleo_tipo not in metas_times:
            return jsonify({'error': 'Núcleo/tipo inválido'}), 400
        
        # Obter metas específicas do time
        metas_time = metas_times[nucleo_tipo]
        
        # Evitar divisão por zero
        if tmr == 0 or metas_time['tmr'] == 0:
            return jsonify({'error': 'Valores inválidos para cálculo (TMR não pode ser zero)'}), 400
        
        # Calcular métricas conforme especificado
        # % de Resolvidas = ((Valor_Preenchido.Resolvido / Meta.Resolvidos.time) * 100)
        perc_resolvidos = (solicitacoes_resolvidas / metas_time['resolvidos']) * 100
        
        # % de TMR = ((Meta.TMR.time / Valor_Preenchido.TMR) * 100)
        perc_tmr = (metas_time['tmr'] / tmr) * 100
        
        # % de SLA = ((Valor_Preenchido.SLA / Meta.SLA.time) * 100)
        perc_sla = (sla / metas_time['sla']) * 100
        
        # % de FCR = ((Valor_Preenchido.FCR / Meta.FCR.time) * 100)
        perc_fcr = (fcr / metas_time['fcr']) * 100
        
        # % de CSAT = ((Valor_Preenchido.CSAT / Meta.CSAT.time) * 100)
        perc_csat = (csat / metas_time['csat']) * 100
        
        # Calcular score final
        # Score = (((% de Resolvidas * 30 ) + (% de TMR * 20) + (% de SLA * 20) + (% de FCR * 15) + (% de CSAT * 15)) /5 ) /1000)
        score = (((perc_resolvidos * 30) + (perc_tmr * 20) + (perc_sla * 20) + (perc_fcr * 15) + (perc_csat * 15)) / 5) / 1000
        
        return jsonify({
            'score': round(score, 2),
            'metricas': {
                'perc_resolvidos': round(perc_resolvidos, 2),
                'perc_tmr': round(perc_tmr, 2),
                'perc_sla': round(perc_sla, 2),
                'perc_fcr': round(perc_fcr, 2),
                'perc_csat': round(perc_csat, 2)
            },
            'metas_time': metas_time,
            'valores_inseridos': {
                'resolvidos': solicitacoes_resolvidas,
                'tmr': tmr,
                'sla': sla,
                'fcr': fcr,
                'csat': csat
            }
        })
        
    except (ValueError, TypeError) as e:
        return jsonify({'error': 'Dados inválidos fornecidos'}), 400
    except Exception as e:
        return jsonify({'error': f'Erro interno do servidor: {str(e)}'}), 500

@app.route('/api/nucleos', methods=['GET'])
def get_nucleos():
    """Retorna lista de núcleos/tipos disponíveis"""
    metas_times = carregar_metas_times()
    return jsonify(list(metas_times.keys()))

@app.route('/api/metas', methods=['GET'])
def get_metas():
    """Retorna todas as metas dos times"""
    if 'usuario' not in session:
        return jsonify({'error': 'Acesso negado'}), 401
    
    metas = carregar_metas_times()
    return jsonify(metas)

@app.route('/api/metas', methods=['POST'])
def update_metas():
    """Atualiza as metas dos times"""
    if 'usuario' not in session:
        return jsonify({'error': 'Acesso negado'}), 401
    
    try:
        novas_metas = request.json
        
        # Validar estrutura das metas
        for time, metas in novas_metas.items():
            if not all(key in metas for key in ['resolvidos', 'tmr', 'sla', 'fcr', 'csat']):
                return jsonify({'error': f'Estrutura inválida para o time {time}'}), 400
            
            # Validar tipos de dados
            try:
                float(metas['resolvidos'])
                float(metas['tmr'])
                float(metas['sla'])
                float(metas['fcr'])
                float(metas['csat'])
            except (ValueError, TypeError):
                return jsonify({'error': f'Valores inválidos para o time {time}'}), 400
        
        # Salvar as novas metas
        if salvar_metas_times(novas_metas):
            return jsonify({'message': 'Metas atualizadas com sucesso'})
        else:
            return jsonify({'error': 'Erro ao salvar metas'}), 500
            
    except Exception as e:
        return jsonify({'error': f'Erro interno: {str(e)}'}), 500

@app.route('/api/metas/<time>', methods=['PUT'])
def update_meta_time(time):
    """Atualiza as metas de um time específico"""
    if 'usuario' not in session:
        return jsonify({'error': 'Acesso negado'}), 401
    
    try:
        metas_atuais = carregar_metas_times()
        
        if time not in metas_atuais:
            return jsonify({'error': 'Time não encontrado'}), 404
        
        novas_metas_time = request.json
        
        # Validar estrutura
        if not all(key in novas_metas_time for key in ['resolvidos', 'tmr', 'sla', 'fcr', 'csat']):
            return jsonify({'error': 'Estrutura inválida'}), 400
        
        # Validar tipos de dados
        try:
            float(novas_metas_time['resolvidos'])
            float(novas_metas_time['tmr'])
            float(novas_metas_time['sla'])
            float(novas_metas_time['fcr'])
            float(novas_metas_time['csat'])
        except (ValueError, TypeError):
            return jsonify({'error': 'Valores inválidos'}), 400
        
        # Atualizar metas do time específico
        metas_atuais[time] = novas_metas_time
        
        if salvar_metas_times(metas_atuais):
            return jsonify({'message': f'Metas do time {time} atualizadas com sucesso'})
        else:
            return jsonify({'error': 'Erro ao salvar metas'}), 500
            
    except Exception as e:
        return jsonify({'error': f'Erro interno: {str(e)}'}), 500

@app.route('/logout')
def logout():
    """Logout do usuário"""
    session.pop('usuario', None)
    return redirect(url_for('adm'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

