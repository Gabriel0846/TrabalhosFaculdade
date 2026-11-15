document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.getElementById('menuToggle');
    const nav = document.querySelector('.nav');
    const tipoDescarteFilter = document.getElementById('tipoDescarte');
    const contadorPontos = document.getElementById('contadorPontos');
    const detalhesModal = document.getElementById('detalhesModal');
    const closeModal = document.querySelector('.close-modal');
    
    if (menuToggle) menuToggle.addEventListener('click', () => nav.classList.toggle('active'));
    
    const map = L.map('map').setView([-23.413, -51.426], 13);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { attribution: '&copy; OpenStreetMap' }).addTo(map);
    const markerGroup = L.layerGroup().addTo(map);
    
    // SEGURANÇA XSS NO MAPA
    function escapeHtml(text) {
        if (!text) return '';
        const div = document.createElement('div');
        div.textContent = String(text);
        return div.innerHTML;
    }
    
    function getIconForTipos(tipos) {
        const colorMap = { 'Eletrônicos': 'green', 'Baterias': 'red', 'Lâmpadas': 'blue', 'Pilhas': 'orange' };
        const primeiroTipo = Array.isArray(tipos) && tipos.length > 0 ? tipos[0] : 'Eletrônicos';
        const cor = colorMap[primeiroTipo] || 'green';
        return L.icon({
            iconUrl: `https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-${cor}.png`,
            shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
            iconSize: [25, 41], iconAnchor: [12, 41], popupAnchor: [1, -34], shadowSize: [41, 41]
        });
    }
    
    function carregarPontosColeta(filtro = 'todos') {
        fetch('/api/pontos-coleta')
            .then(response => response.json())
            .then(pontos => {
                markerGroup.clearLayers();
                let pontosFiltrados = pontos;
                if (filtro !== 'todos') {
                    pontosFiltrados = pontos.filter(p => (p.tipos_descarte || []).some(tipo => tipo.toLowerCase().includes(filtro.toLowerCase())));
                }
                contadorPontos.textContent = pontosFiltrados.length;
                
                pontosFiltrados.forEach(ponto => {
                    const tipos = Array.isArray(ponto.tipos_descarte) ? ponto.tipos_descarte : [];
                    const icon = getIconForTipos(tipos);
                    const marker = L.marker([ponto.latitude, ponto.longitude], { icon }).addTo(markerGroup);
                    const tiposFormatados = tipos.length > 0 ? tipos.join(', ') : 'Não especificado';
                    
                    marker.bindPopup(`
                        <div class="popup-content">
                            <h3>${escapeHtml(ponto.nome)}</h3>
                            <p><strong>Endereço:</strong> ${escapeHtml(ponto.endereco)}</p>
                            <p><strong>Aceita:</strong> ${escapeHtml(tiposFormatados)}</p>
                            <button onclick="abrirDetalhes(${ponto.id})" style="background:#2ecc71; color:white; border:none; padding:8px 16px; border-radius:4px; margin-top:10px; width:100%;">Ver detalhes</button>
                        </div>
                    `);
                    
                    marker.on('click', function() {
                        document.getElementById('modalTitulo').textContent = ponto.nome;
                        document.getElementById('modalEndereco').textContent = ponto.endereco;
                        document.getElementById('modalTipo').textContent = tiposFormatados;
                        document.getElementById('modalHorario').textContent = ponto.horario_funcionamento || 'Não informado';
                        document.getElementById('modalTelefone').textContent = ponto.telefone || 'Não informado';
                        detalhesModal.style.display = 'flex';
                    });
                });
                
                if (pontosFiltrados.length > 0) {
                    map.fitBounds(L.latLngBounds(pontosFiltrados.map(p => [p.latitude, p.longitude])), { padding: [50, 50] });
                }
            })
            .catch(error => console.error('Erro ao carregar pontos:', error));
    }
    
    if(tipoDescarteFilter) tipoDescarteFilter.addEventListener('change', function() { carregarPontosColeta(this.value); });
    
    if(closeModal) closeModal.addEventListener('click', () => detalhesModal.style.display = 'none');
    window.addEventListener('click', (event) => { if (event.target === detalhesModal) detalhesModal.style.display = 'none'; });
    
    carregarPontosColeta();
});
function abrirDetalhes(id) { console.log('Detalhe:', id); }