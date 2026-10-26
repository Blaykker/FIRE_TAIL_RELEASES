# FIRE TAIL 0.9.16

- Corrigida a validação que recusava batalhas com Bram, Lyra, Orin, Elian e javali. Eventos confiáveis usam o relé enquanto o canal direto ainda está conectando.
- Ataque básico e ação de carta separados; cartas livres podem ser usadas mais de uma vez. Clique normal usa/seleciona a carta; botão direito abre a inspeção.
- Arco e pá aparecem em Receitas → Ferramentas após aprender suas páginas. Páginas têm ícone próprio e explicam o consumo. Ícones pequenos priorizam pixel art; queijo, balde e itens sem ilustração usam modelos.
- Caixas simples de suprimentos; baú fecha ao começar a andar. Cabeçalho, abas contínuas, famílias do bestiário e diálogo/loja revisados.
- Escada mais longa e abertura correspondente no convés permitem chegar ao porão. Pontos de reparo recebem materiais gradualmente, mostram porcentagem e alteram partes do navio ao concluir.
- Capim mais estreito e curvo em massas distribuídas por ruído, bordas de terra estendidas às laterais e transições de piso independentes de obstáculos superiores.
- Espuma reduzida sobre o nadador, peixes provisórios ocultados, contorno externo revisto e símbolos pintados dos dados restaurados em faces separadas.
- Horizonte: luz ampla atrás da silhueta do Cthulhu, apagando antes dos limites do plano, sem iluminar um retângulo de imagem.

Validação: testes de simulação e protocolo; interface de receitas, categorias, mercante e baú; batalha Bram/Lyra, ação do convidado e saída sincronizada por transporte local e Supabase/WebRTC na mesma máquina. Isso não substitui testes entre dispositivos e redes diferentes. Depósitos de reparos simultâneos por vários jogadores ainda exigem validação de concorrência. Desempenho depende da máquina; não há garantia de 60 FPS nesta alpha.
