from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_cors import CORS
from flask_login import login_user, logout_user, login_required, current_user
from database import db, init_db, login_manager
from models import User, PontoColeta, Feedback
import os
import json
from datetime import datetime

app = Flask(__name__)
CORS(app)
init_db(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ========== ROTAS PÚBLICAS ==========
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/feedback')
def feedback_page():
    return render_template('feedback.html')

@app.route('/tutoriais')
def tutoriais():
    return render_template('tutorial.html')

# ========== API PÚBLICA ==========
@app.route('/api/pontos-coleta', methods=['GET'])
def get_pontos_coleta():
    try:
        pontos = PontoColeta.query.filter_by(ativo=True, oculto=False).all()
        resultado = []
        
        for p in pontos:
            try:
                tipos = json.loads(p.tipos_descarte) if p.tipos_descarte else []
            except (json.JSONDecodeError, TypeError):
                tipos = [p.tipos_descarte] if p.tipos_descarte else []
            
            resultado.append({
                'id': p.id,
                'nome': p.nome,
                'endereco': p.endereco,
                'tipos_descarte': tipos,
                'latitude': p.latitude,
                'longitude': p.longitude,
                'telefone': p.telefone or 'Não informado',
                'horario_funcionamento': p.horario_funcionamento or 'Não informado',
                'observacoes': p.observacoes
            })
        
        return jsonify(resultado)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/feedback', methods=['POST'])
def add_feedback():
    try:
        data = request.json
        feedback = Feedback(
            ponto_coleta_id=data.get('ponto_coleta_id'),
            avaliacao=data.get('avaliacao'),
            comentario=data.get('comentario'),
            tipo_feedback=data.get('tipo_feedback'),
            contato=data.get('contato')
        )
        db.session.add(feedback)
        db.session.commit()
        return jsonify({'message': 'Feedback enviado com sucesso!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# ========== ROTAS DE ADMINISTRAÇÃO ==========
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password) and user.is_admin:
            login_user(user)
            return redirect(url_for('admin_dashboard'))
        else:
            return render_template('admin_login.html', error='Credenciais inválidas')
    
    return render_template('admin_login.html')

@app.route('/admin/logout')
@login_required
def admin_logout():
    logout_user()
    return redirect(url_for('admin_login'))

@app.route('/admin')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        return redirect(url_for('admin_login'))
    
    return render_template('admin_dashboard.html')

# ========== API ADMIN - PONTOS DE COLETA ==========
@app.route('/admin/api/pontos-coleta', methods=['GET'])
@login_required
def admin_get_pontos_coleta():
    pontos = PontoColeta.query.all()
    return jsonify([{
        'id': p.id,
        'nome': p.nome,
        'endereco': p.endereco,
        'tipos_descarte': json.loads(p.tipos_descarte),
        'latitude': p.latitude,
        'longitude': p.longitude,
        'telefone': p.telefone,
        'horario_funcionamento': p.horario_funcionamento,
        'observacoes': p.observacoes,
        'ativo': p.ativo,
        'oculto': p.oculto,
        'data_cadastro': p.data_cadastro.isoformat() if p.data_cadastro else None
    } for p in pontos])

@app.route('/admin/api/pontos-coleta', methods=['POST'])
@login_required
def admin_add_ponto_coleta():
    try:
        data = request.json
        tipos_descarte = json.dumps(data['tipos_descarte'])
        
        novo_ponto = PontoColeta(
            nome=data['nome'],
            endereco=data['endereco'],
            tipos_descarte=tipos_descarte,
            latitude=float(data['latitude']),
            longitude=float(data['longitude']),
            telefone=data.get('telefone', ''),
            horario_funcionamento=data.get('horario_funcionamento', ''),
            observacoes=data.get('observacoes', ''),
            ativo=data.get('ativo', True),
            oculto=data.get('oculto', False)
        )
        db.session.add(novo_ponto)
        db.session.commit()
        return jsonify({'message': 'Ponto de coleta adicionado com sucesso!', 'id': novo_ponto.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/admin/api/pontos-coleta/<int:id>', methods=['PUT'])
@login_required
def admin_update_ponto_coleta(id):
    try:
        data = request.json
        ponto = PontoColeta.query.get_or_404(id)
        
        ponto.nome = data.get('nome', ponto.nome)
        ponto.endereco = data.get('endereco', ponto.endereco)
        
        if 'tipos_descarte' in data:
            ponto.tipos_descarte = json.dumps(data['tipos_descarte'])
        
        ponto.latitude = float(data.get('latitude', ponto.latitude))
        ponto.longitude = float(data.get('longitude', ponto.longitude))
        ponto.telefone = data.get('telefone', ponto.telefone)
        ponto.horario_funcionamento = data.get('horario_funcionamento', ponto.horario_funcionamento)
        ponto.observacoes = data.get('observacoes', ponto.observacoes)
        ponto.ativo = data.get('ativo', ponto.ativo)
        ponto.oculto = data.get('oculto', ponto.oculto)
        
        db.session.commit()
        return jsonify({'message': 'Ponto de coleta atualizado com sucesso!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/admin/api/pontos-coleta/<int:id>', methods=['DELETE'])
@login_required
def admin_delete_ponto_coleta(id):
    try:
        ponto = PontoColeta.query.get_or_404(id)
        db.session.delete(ponto)
        db.session.commit()
        return jsonify({'message': 'Ponto de coleta excluído com sucesso!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# ========== API ADMIN - FEEDBACKS ==========
@app.route('/admin/api/feedbacks', methods=['GET'])
@login_required
def admin_get_feedbacks():
    feedbacks = Feedback.query.order_by(Feedback.lido, Feedback.data_criacao.desc()).all()
    return jsonify([{
        'id': f.id,
        'ponto_coleta_id': f.ponto_coleta_id,
        'ponto_nome': f.ponto_coleta.nome if f.ponto_coleta else 'Não especificado',
        'avaliacao': f.avaliacao,
        'comentario': f.comentario,
        'tipo_feedback': f.tipo_feedback,
        'contato': f.contato,
        'data_criacao': f.data_criacao.isoformat() if f.data_criacao else None,
        'lido': f.lido,
        'salvo': f.salvo,
        'respondido': f.respondido,
        'resposta': f.resposta,
        'data_resposta': f.data_resposta.isoformat() if f.data_resposta else None
    } for f in feedbacks])

@app.route('/admin/api/feedbacks/<int:id>/lido', methods=['PUT'])
@login_required
def admin_marcar_feedback_lido(id):
    try:
        feedback = Feedback.query.get_or_404(id)
        feedback.lido = not feedback.lido
        db.session.commit()
        return jsonify({'message': 'Status de leitura atualizado!', 'lido': feedback.lido})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/admin/api/feedbacks/<int:id>/salvo', methods=['PUT'])
@login_required
def admin_marcar_feedback_salvo(id):
    try:
        feedback = Feedback.query.get_or_404(id)
        feedback.salvo = not feedback.salvo
        db.session.commit()
        return jsonify({'message': 'Status de salvamento atualizado!', 'salvo': feedback.salvo})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/admin/api/feedbacks/<int:id>/responder', methods=['PUT'])
@login_required
def admin_responder_feedback(id):
    try:
        data = request.json
        feedback = Feedback.query.get_or_404(id)
        feedback.resposta = data.get('resposta')
        feedback.respondido = True if data.get('resposta') else False
        feedback.data_resposta = datetime.utcnow()
        db.session.commit()
        return jsonify({'message': 'Resposta enviada com sucesso!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/admin/api/feedbacks/<int:id>', methods=['DELETE'])
@login_required
def admin_delete_feedback(id):
    try:
        feedback = Feedback.query.get_or_404(id)
        db.session.delete(feedback)
        db.session.commit()
        return jsonify({'message': 'Feedback excluído com sucesso!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# ========== ROTAS DE ESTATÍSTICAS ==========
@app.route('/admin/api/estatisticas', methods=['GET'])
@login_required
def admin_get_estatisticas():
    total_pontos = PontoColeta.query.count()
    pontos_ativos = PontoColeta.query.filter_by(ativo=True, oculto=False).count()
    pontos_ocultos = PontoColeta.query.filter_by(oculto=True).count()
    
    total_feedbacks = Feedback.query.count()
    feedbacks_nao_lidos = Feedback.query.filter_by(lido=False).count()
    feedbacks_salvos = Feedback.query.filter_by(salvo=True).count()
    feedbacks_respondidos = Feedback.query.filter_by(respondido=True).count()
    
    # Média de avaliações
    feedbacks_com_avaliacao = Feedback.query.filter(Feedback.avaliacao.isnot(None)).all()
    media_avaliacao = 0
    if feedbacks_com_avaliacao:
        media_avaliacao = sum(f.avaliacao for f in feedbacks_com_avaliacao) / len(feedbacks_com_avaliacao)
    
    return jsonify({
        'total_pontos': total_pontos,
        'pontos_ativos': pontos_ativos,
        'pontos_ocultos': pontos_ocultos,
        'total_feedbacks': total_feedbacks,
        'feedbacks_nao_lidos': feedbacks_nao_lidos,
        'feedbacks_salvos': feedbacks_salvos,
        'feedbacks_respondidos': feedbacks_respondidos,
        'media_avaliacao': round(media_avaliacao, 1)
    })

if __name__ == '__main__':
    # Criar diretórios se não existirem
    for dir_path in ['templates', 'static/css', 'static/js']:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            print(f"Diretório criado: {dir_path}")
    
    app.run(debug=True, host='0.0.0.0', port=5000)