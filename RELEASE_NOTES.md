# FIRE TAIL 0.9.29 — Silhuetas, profundidade e combate

- Temperatura acima das barras do avatar; parte inferior reservada aos status. Ajustes no contador de flechas, atalhos dos slots, retratos e desafios do grupo.
- Proporções dos modelos medidas pela cabeça, sem contar orelhas, capacetes ou armas. Lucas acompanha o camundongo; imperiais e esqueleto são maiores; centopeia alongada. Materiais importados recebem iluminação toon mais legível.
- Sombra projetada reúne corpo e equipamentos numa silhueta única. Contorno preto dos atores e seleção branca exterior respeitam a profundidade. Correção do formato de profundidade/stencil e redução de tremulação visual.
- Centopeia de cinco casas e serpente de oito: corpo segue a cabeça casa a casa, inclusive na sincronização cooperativa. Ataques pelas costas e em extremidades críticas recebem dado adicional. Nova carta de terra em linha, com prévia e efeito sequencial.
- Game Over aguarda confirmação para renascer; o personagem morto fica parado enquanto o mundo continua. Criaturas se orientam para o alvo e cartas sem PA suficiente aparecem desativadas.
- Praia com areia contínua sob as ondas, transição de água suavizada e marca de areia molhada. Fundo marinho com desníveis, baús submersos e aproximação na profundidade correta. Escavações guardam até oito níveis de profundidade no salvamento.
- Ajustes no porão, ocultação da carga superior, marcador luminoso de reparo e exclusão de objetos naturais da fogueira. Baús podem ser recolhidos e reposicionados; colocação permite rotação.
- Ferramentas do tutorial ficam posicionadas desde o início. A primeira coleta conduz ao inventário e à ação de equipar.
- Entrada com vinheta SP e carregamento da ilustração da escada; modelos e shaders são preparados antes do menu. Isso concentra a espera inicial e reduz trabalho durante as transições.
- Controle: L1/R1 alternam abas, analógico esquerdo move a câmera na batalha, direito seleciona, R2 confirma; PS e touchpad deixam de abrir inventário. Fechar jogo aparece somente na página inicial.

Verificação: 335 testes automatizados e checagem TypeScript. A compilação, o navegador e o fluxo cooperativo são conferidos antes da publicação.

Limites desta entrega: profundidade é representada por alturas e escavações em camadas, sem túneis volumétricos arbitrários abaixo do nível zero. Animações continuam básicas. Safari/Mac e DualShock físico precisam de validação presencial; os testes automatizados usam Edge e controle simulado. A espera inicial depende do aparelho e não foi medida em hardware do jogador. As páginas Steam/Google Play continuam sendo prévias, sem publicação nas lojas.
