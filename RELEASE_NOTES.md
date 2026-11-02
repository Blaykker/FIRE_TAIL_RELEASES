# FIRE TAIL 0.9.20 — Atos 27, serpente e batalha sem dados de movimento

Versão 0.9.20, preparada para publicação em 02/11/2026. Para jogar pelo launcher instalado: procure a atualização 0.9.20, conclua o download e selecione Embarcar.

## Interface proporcional (celular e iPad)

- Em telas menores que 1180×680, a interface inteira é desenhada num espaço virtual e **reduzida na mesma proporção**. Isso inclui a HUD de exploração, o minimapa, a batalha, os diálogos, a mochila e o chat. O jogo continua visível em vez de ficar coberto por botões gigantes.
  - Escala aproximada: iPhone deitado 0,57; iPad 0,87; iPad Air deitado e desktop 1.
- O layout responde ao tamanho virtual (container queries `@container hud` e unidades `cqw/cqh`), então a tela não fica "compacta" e reduzida ao mesmo tempo.
- Os **controles de toque** mantêm tamanho de polegar (no mínimo ~82% do tamanho de desenho).
- **Configurações → Vídeo → Tamanho da interface** (0,8–1,2) permite ajustar ao gosto. O ajuste fica salvo no aparelho.

## Batalha

- **Movimento sem dados.** O dado de movimento no início do turno foi removido. Cada personagem tem **PM fixo por tipo**, como já acontecia com o PA (Tail/Lyra 4, Bram/Orin/Elian 3; inimigos com valores próprios). Cartas e habilidades podem somar PM; bônus de PA ficam mais raros e mais fortes.
- **HUD inferior** reorganizada:
  - o **PA** fica dentro da HUD, logo acima da caixa de PM;
  - a moldura começa mais baixa, perto da barra de vida, e as **cartas passam por cima dela**;
  - "Vida" está maior.
- **Dados**: ataque vermelho e defesa azul para os dois lados; jogador à esquerda e inimigo à direita.
  - Câmera ortográfica, sem distorção.
  - Espaçamento corrigido e os dados que contam ficam mais perto do centro.
  - O resumo do confronto fica centralizado logo acima da HUD.
- **Painel de batalha** (guia do turno + registro) no canto inferior esquerdo. Dano, crítico, cura e bloqueio aparecem destacados.
- **Modo tático** (botão ▦ ou tecla **G**): xadrez legível no chão da arena. Esconde grama, decoração, vaga-lumes e chuva. A escolha fica salva.
- **Ajuda (Mouse Guard):** cada aliado encostado no alvo dá +1 dado ao atacante, no máximo +2.
- **Ordem Natural:** criaturas 2+ degraus acima dos ratos não morrem, são afugentadas. Preparado para corujas e outros bichos maiores.

## Serpente da lenha (nova criatura)

- Corpo de 4 casas; a cabeça é o ponto fraco.
- A mordida envenena e os anéis prendem quem ela fere: a vítima perde a próxima vez.
- O fogo da cauda do Tail dá +1 dado contra ela.
- Aparece na mata da ilha, perto de árvores.
- Tem entrada no bestiário, modelo 3D, retrato e sincronia no coop.

## Narrativa (direção de 02/11)

- Arara, tartaruga e lagartixa saem da ilha. Entram três personagens da trama:
  - **o Centurião**, rato romano de capa vermelha;
  - **o Cronista**, camundongo médico e historiador;
  - **o Legionário**, rato com escudo e lança.
- Os três têm modelos 3D e retratos em silhueta a nanquim. Os saves antigos são migrados.
- O navio do menu mostra a guarda romana.
- O tutorial da praia é conduzido pela **Voz** («…»), sempre no formato problema → solução guiada.
- O **minimapa mostra os NPCs** (losangos; quando estão longe, ficam presos à borda). O mapa grande mostra os nomes.
- Documentos:
  - `docs/design/NARRATIVA-ATOS27-2026-11-02.md`;
  - `docs/design/MOUSE-GUARD-ESTUDO-2026-11-02.md`.

## Estabilidade e ferramentas

- `package-lock.json`: o `@xmldom/xmldom` apontava para um pacote inexistente (0.9.13). Isso derrubava os deploys git da Vercel desde a 0.9.19. Corrigido para 0.9.12.
- O coop não sincronizava o **javali**: os convidados recebiam o tipo −1. Corrigido junto com a serpente.
- Piso do naufrágio: corrigido o teste que falhava na 0.9.19.
- **NPCs da trama não montavam** (o `mergeGeometries` recebia peças com atributos diferentes e devolvia null). Isso travava a ilha e o navio do menu. Corrigido, com teste próprio.
- Teste com 2 clientes (coop local) passou: mesmo encontro, mesmas unidades e mesma vez nos dois, PM fixo e a serpente sincronizada. Ver `docs/validation/coop-0.9.20-2026-11-02.md`.
- Validação: TypeScript sem erros, 282 testes (54 arquivos), build web ok.
- Avaliador de demo:
  - ferramenta `tools/demo-audit.mjs` (`--build`, `--e2e URL`, `--json`);
  - agente `.claude/agents/demo-readiness.md`;
  - relatórios em `docs/validation/`.

## Pendências conhecidas

- A cena de abertura ainda é a discussão do queijo. Falta a depressão + "ninguém vai morrer".
- Ainda faltam o contador das 276 almas e o puzzle da torre.
- A serpente ainda não está ligada à história.
- Falta um teste com 2 computadores em rede real nesta versão (o teste local de 2 clientes passou).
- O desempenho não foi medido fora do ambiente de desenvolvimento.
