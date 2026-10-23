document.addEventListener('DOMContentLoaded', function() {
    // Elementos da interface
    const menuToggle = document.getElementById('menuToggle');
    const nav = document.querySelector('.nav');
    const mapElement = document.getElementById('map');
    const tipoDescarteFilter = document.getElementById('tipoDescarte');
    const buscaLocalInput = document.getElementById('buscaLocal');
    const localizacaoAtualBtn = document.getElementById('localizacaoAtual');
    const contadorPontos = document.getElementById('contadorPontos');
    const detalhesModal = document.getElementById('detalhesModal');
    const closeModal = document.querySelector('.close-modal');
    
    // Menu responsivo
    menuToggle.addEventListener('click', () => {
        nav.classList.toggle('active');
    });
    
    // Inicializar mapa
    const map = L.map('map').setView([-23.413, -51.426], 13);
    
    // Adicionar tile layer
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);
    
    // Grupo de marcadores
    const markerGroup = L.layerGroup().addTo(map);
    
    // Função para determinar ícone baseado nos tipos
    function getIconForTipos(tipos) {
        const colorMap = {
            'Eletrônicos': 'green',
            'Baterias': 'red',
            'Lâmpadas': 'blue',
            'Pilhas': 'orange'
        };
        
        // Usa o primeiro tipo para determinar a cor
        const primeiroTipo = Array.isArray(tipos) && tipos.length > 0 ? tipos[0] : 'Eletrônicos';
        const cor = colorMap[primeiroTipo] || 'green';
        
        // Cria ícone simples do Leaflet (sem awesome-markers por enquanto)
        return L.icon({
            iconUrl: `https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-${cor}.png`,
            shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
            iconSize: [25, 41],
            iconAnchor: [12, 41],
            popupAnchor: [1, -34],
            shadowSize: [41, 41]
        });
    }
    
    // Carregar pontos de coleta
    function carregarPontosColeta(filtro = 'todos') {
        fetch('/api/pontos-coleta')
            .then(response => response.json())
            .then(pontos => {
                console.log('Pontos carregados:', pontos); // Para debug
                markerGroup.clearLayers();
                
                let pontosFiltrados = pontos;
                if (filtro !== 'todos') {
                    pontosFiltrados = pontos.filter(p => {
                        // Verifica se algum dos tipos corresponde ao filtro
                        const tipos = p.tipos_descarte || [];
                        return tipos.some(tipo => 
                            tipo.toLowerCase().includes(filtro.toLowerCase())
                        );
                    });
                }
                
                // Atualizar contador
                contadorPontos.textContent = pontosFiltrados.length;
                
                // Adicionar marcadores
                pontosFiltrados.forEach(ponto => {
                    const tipos = Array.isArray(ponto.tipos_descarte) ? ponto.tipos_descarte : [];
                    const icon = getIconForTipos(tipos);
                    
                    const marker = L.marker([ponto.latitude, ponto.longitude], { icon })
                        .addTo(markerGroup);
                    
                    // Formatar tipos para exibição
                    const tiposFormatados = tipos.length > 0 ? tipos.join(', ') : 'Não especificado';
                    
                    marker.bindPopup(`
                        <div class="popup-content">
                            <h3>${ponto.nome}</h3>
                            <p><strong>Endereço:</strong> ${ponto.endereco}</p>
                            <p><strong>Aceita:</strong> ${tiposFormatados}</p>
                            <p><strong>Horário:</strong> ${ponto.horario_funcionamento || 'Não informado'}</p>
                            <p><strong>Telefone:</strong> ${ponto.telefone || 'Não informado'}</p>
                            <button onclick="abrirDetalhes(${ponto.id})" class="btn-detalhes" style="
                                background: #2ecc71;
                                color: white;
                                border: none;
                                padding: 8px 16px;
                                border-radius: 4px;
                                cursor: pointer;
                                margin-top: 10px;
                                width: 100%;
                            ">
                                Ver detalhes
                            </button>
                        </div>
                    `);
                    
                    marker.pontoId = ponto.id;
                    marker.on('click', function() {
                        // Atualizar detalhes do modal
                        document.getElementById('modalTitulo').textContent = ponto.nome;
                        document.getElementById('modalEndereco').textContent = ponto.endereco;
                        document.getElementById('modalTipo').textContent = tiposFormatados;
                        document.getElementById('modalHorario').textContent = ponto.horario_funcionamento || 'Não informado';
                        document.getElementById('modalTelefone').textContent = ponto.telefone || 'Não informado';
                        
                        // Buscar avaliações para este ponto
                        fetch(`/api/feedback?ponto_id=${ponto.id}`)
                            .then(res => res.json())
                            .then(avaliacoes => {
                                const container = document.getElementById('modalAvaliacoes');
                                if (avaliacoes.length > 0) {
                                    let html = '<ul style="list-style: none; padding: 0;">';
                                    avaliacoes.forEach(av => {
                                        const estrelas = '★'.repeat(av.avaliacao || 0) + '☆'.repeat(5 - (av.avaliacao || 0));
                                        html += `<li style="margin-bottom: 10px; padding: 10px; background: #f8f9fa; border-radius: 4px;">
                                            <strong>${estrelas}</strong><br>
                                            ${av.comentario || 'Sem comentário'}
                                        </li>`;
                                    });
                                    html += '</ul>';
                                    container.innerHTML = html;
                                } else {
                                    container.innerHTML = '<p style="color: #666; font-style: italic;">Nenhuma avaliação ainda. Seja o primeiro a avaliar!</p>';
                                }
                            })
                            .catch(error => {
                                console.error('Erro ao carregar avaliações:', error);
                                document.getElementById('modalAvaliacoes').innerHTML = 
                                    '<p style="color: #666;">Não foi possível carregar as avaliações.</p>';
                            });
                        
                        detalhesModal.style.display = 'flex';
                    });
                });
                
                // Se houver pontos, ajustar o zoom para mostrar todos
                if (pontosFiltrados.length > 0) {
                    const bounds = L.latLngBounds(pontosFiltrados.map(p => [p.latitude, p.longitude]));
                    map.fitBounds(bounds, { padding: [50, 50] });
                }
            })
            .catch(error => {
                console.error('Erro ao carregar pontos:', error);
                contadorPontos.textContent = '0';
                
                // Mostrar erro no mapa
                markerGroup.clearLayers();
                const errorMarker = L.marker([-23.413, -51.426])
                    .addTo(markerGroup)
                    .bindPopup(`
                        <div style="color: #e74c3c; text-align: center;">
                            <h3>Erro ao carregar pontos</h3>
                            <p>${error.message}</p>
                            <button onclick="location.reload()" style="
                                background: #3498db;
                                color: white;
                                border: none;
                                padding: 8px 16px;
                                border-radius: 4px;
                                cursor: pointer;
                                margin-top: 10px;
                            ">
                                Tentar novamente
                            </button>
                        </div>
                    `)
                    .openPopup();
            });
    }
    
    // Filtros
    tipoDescarteFilter.addEventListener('change', function() {
        carregarPontosColeta(this.value === 'todos' ? 'todos' : this.value);
    });
    
    // Busca por localização
    if (localizacaoAtualBtn) {
        localizacaoAtualBtn.addEventListener('click', function() {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(function(position) {
                    map.setView([position.coords.latitude, position.coords.longitude], 15);
                    L.marker([position.coords.latitude, position.coords.longitude])
                        .addTo(map)
                        .bindPopup('Você está aqui!')
                        .openPopup();
                }, function(error) {
                    alert('Não foi possível obter sua localização. Verifique as permissões do navegador.');
                });
            } else {
                alert('Geolocalização não suportada pelo navegador.');
            }
        });
    }
    
    // Busca por endereço
    if (buscaLocalInput) {
        buscaLocalInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                const query = this.value.trim();
                if (query.length > 3) {
                    fetch(`https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(query)}&limit=1`)
                        .then(response => response.json())
                        .then(data => {
                            if (data.length > 0) {
                                const lat = parseFloat(data[0].lat);
                                const lon = parseFloat(data[0].lon);
                                map.setView([lat, lon], 15);
                            } else {
                                alert('Endereço não encontrado.');
                            }
                        })
                        .catch(error => {
                            console.error('Erro na busca:', error);
                            alert('Erro ao buscar endereço.');
                        });
                } else {
                    alert('Digite pelo menos 4 caracteres para buscar.');
                }
            }
        });
    }
    
    // Fechar modal
    closeModal.addEventListener('click', function() {
        detalhesModal.style.display = 'none';
    });
    
    // Fechar modal ao clicar fora
    window.addEventListener('click', function(event) {
        if (event.target === detalhesModal) {
            detalhesModal.style.display = 'none';
        }
    });
    
    // Carregar pontos inicialmente
    carregarPontosColeta();
});

// Função global para abrir detalhes
function abrirDetalhes(pontoId) {
    console.log('Abrir detalhes do ponto:', pontoId);
    // Você pode implementar navegação para página de detalhes se quiser
}