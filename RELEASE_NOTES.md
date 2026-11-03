# FIRE TAIL 0.9.24 — pés digitígrados, corrida de rato, arco em L, mochila nova e modo tático

Versão 0.9.24 (03/11/2026). Para jogar pelo launcher: procure a atualização 0.9.24, conclua o download e selecione Embarcar.

## Personagem
- **Pés digitígrados de 3 pontos de chão** (meio do pé, base dos dedos, ponta), com ossos novos no rig do jogo: metatarso, planta e dedos.
  - **No apoio** a base dos dedos fica parada no chão do mundo. No fim do passo o calcanhar sobe e a planta gira sobre a base dos dedos, que continuam no chão.
  - **Na saída** os dedos descolam por último e dobram para baixo. No ar o tornozelo recolhe, e a planta se abre e assenta antes de pousar.
  - **Ritmo:** andando há sempre um pé no chão (62% do ciclo). Correndo há fase de voo (40%).
- **Pé em degrau (IK):** cada pé procura o chão de verdade debaixo dele (degrau, meio bloco) e o quadril desce o que o pé mais baixo precisar.
- **Corrida de rato:** referência do vídeo do Pablo.
  - O corpo fica quase na horizontal.
  - A coluna arqueia e estica a cada passada.
  - As patas de trás vão quase juntas (meio-galope).
  - As mãos viram patas da frente de verdade: tocam o chão e pousam depois do voo.
- **Arco:**
  - ombros mais de frente;
  - braço do arco esticado;
  - mão da corda com o **cotovelo para fora na altura do ombro, em L**, e o antebraço voltado para a corda;
  - a flecha liga as duas mãos. Vale parado, andando e mirando.
- **Ferramentas pela base, como na folha de referência:**
  - picareta ~60° para a frente, com cabo mais grosso e cabeça maior;
  - pá com a lâmina para cima, segura perto da alça em D;
  - machado e espada com a cabeça e a lâmina para cima.
- **Mochila 3D nova** (modelo do Pablo) encaixada nas costas, com as alças modeladas. As aljavas são addon nas laterais.

## Batalha
- **Números** inteiros ou com no máximo 1 casa decimal (dano, cura, vida, registro).
- **Exclamação e números presos ao personagem no mapa:** mover a câmera (WASD) não os arrasta.
- **Ao atacar ou atirar, o personagem vira para o alvo** e fica naquela direção.
  - **Corpo a corpo:** golpe com a ferramenta.
  - **Arco:** puxa a corda, solta, e a flecha sai rápida, com arco baixo e rastro. Quanto mais dano, mais vermelho e mais grosso fica o rastro; o crítico deixa o rastro ainda mais forte.
- **Dados:**
  - arremesso mais alto, mais tempo quicando e dados maiores;
  - pousam com a **face sorteada para cima** no lugar onde caíram e só depois deslizam para a fila do cálculo;
  - o quadro é mais alto e os dados não vazam.
- **Cálculo:** sobe de trás da HUD inferior com um elástico, fica inteiro e legível acima dela e desce ao terminar (sem o "bump").
- **Desafios estilo Dofus** no lugar do "objetivo":
  - cada batalha sorteia 2 desafios, em hexágonos na esquerda. O nome e a regra aparecem ao passar o mouse;
  - os desafios: Zumbi, Estátua, Intocável, Nômade, Foco, Relâmpago, Arqueiro, Bárbaro e Juntos;
  - cada um cumprido dá XP. A tela de vitória lista os cumpridos;
  - criaturas grandes demais ainda só podem ser expulsas (automático, com um hexágono azul).

## Modo tático
- **Botão sob o minimapa** (⚔ Tático / ⚡ Tempo real) e item no menu de pausa. Só troca fora da batalha.
- **Modo tático ligado:**
  - encostar numa criatura **não fere**; abre a batalha por turnos com a criatura na frente da iniciativa;
  - se o Tail bater ou atirar primeiro, causa o dano inicial e a batalha começa com vocês na frente.
- **Modo tático desligado:** combate em tempo real; as criaturas ferem ao encostar.
- **Visão tática dentro da batalha:** botão ▦ (G). Mostra um tabuleiro limpo e esconde a vegetação.

## Mundo e leitura
- **Recorte da tocha:** o círculo que deixa ver o que está atrás nasce na tocha, como a luz dela vindo de trás. É maior e mostra a tocha e o personagem em volta.
- **Chama atrás de objetos:** aparece só como contorno (sem preenchimento).
- **Silhuetas de criaturas:**
  - uma criatura atrás do próprio Tail não ganha silhueta;
  - criaturas de outro andar também não; só as do mesmo andar.
- **Andares:** o que está abaixo do andar do Tail escurece também na superfície. Os degraus de meio bloco não escurecem.
- **Grama vista de cima:** as quinas externas da borda de terra fazem curva.
- **Mato de sprite** (capim curto e mato alto) voltou à textura de antes da 0.9.22. Só a grama volumétrica ficou mais fina.

## Itens e ofícios
- **Lampião:** fica na cauda, pendurado pela alça. A luz é firme e mais curta, e o vidro protege da chuva.
- **Tocha de óleo de baleia** e **Óleo de baleia:**
  - usar o óleo dá o estado "Óleo de baleia" (3 min);
  - enquanto ele durar, a chuva não apaga a tocha;
  - o óleo só gasta com a tocha acesa.
- **Ferreiro:** fabricar sobe o nível do ofício, e o nível libera peças de metal: anel de bronze (nv 1), lampião (nv 2) e tocha de óleo (nv 3). O óleo de baleia é de Alquimia (nv 2).
- **Cartas:** a aba Cartas só mostra número quando há carta nova, ainda não lida.

## Validação
- TypeScript sem erros e 296 testes.
  - Novos testes: desafios, e o toque no modo tático, que vira batalha sem dano.
- Laboratório de animação novo (`anim-lab.html` + `e2e/cloud/anim.mjs`): renderiza tiras de quadros do rato de lado, de frente, em 3/4 e de cima. Com ele foram conferidos o andar, a corrida, a escada, o arco e as ferramentas.

## Pendências
- **Clipes da Mixamo:** os clipes da pasta ANIMATION serviram de referência de pose. Tocar os clipes de verdade exige passar o boneco do rig procedural para animação por esqueleto; fica para uma etapa própria.
- **Silhueta "só contorno" da mochila:** a hipótese ainda não foi confirmada numa captura do caso real.
- **Quinas internas da borda de grama:** ainda retas.
