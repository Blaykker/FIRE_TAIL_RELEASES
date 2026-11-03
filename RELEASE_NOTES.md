# FIRE TAIL 0.9.23 — Tail novo (Tripo + rig Mixamo)

Versão 0.9.23 (03/11/2026). Para jogar pelo launcher: procure a atualização 0.9.23, conclua o download e selecione Embarcar.

## Personagem
- **Tail v6 é o modelo padrão.** Malha do Tripo enviada pelo Pablo, com a textura e os UVs originais (sem re-bake).
- **Rig no padrão Mixamo** (60 ossos). Detalhes e arquivos em `FIRE_TAIL_ASSETS/characters/tail-v6-20261103`.
  - Ombro isolado, braço, antebraço e mão.
  - Polegar e 3 dedos.
  - Perna digitígrada em 6 pontos, conforme o desenho do Pablo: quadril → joelho → calcanhar (para trás) → meio do pé → base dos dedos → ponta. Os 3 últimos pontos ficam no chão e formam o pé; os dedos têm eixo próprio.
  - Orelhas e 8 ossos de cauda.
- **Ferramentas pela base**: picareta, machado, espada e foice ficam presos pela base do cabo, apontando ~45° para a frente. A direção vem do corpo, não da mão, e por isso lê igual de frente, de lado e de costas. No golpe a pegada volta para a mão e a esquerda ajuda no cabo. Ajuste em `TUNE.hold`.
- **No jogo** a malha entra sem a cauda, porque o jogo desenha a cauda com a tocha. Saves e configurações antigas com o boneco antigo passam para o v6 uma vez.
- **Nome**: o cronista agora se chama **Luke**.

## Batalha
- **Exclamação** mais quadrada, estilo mangá: cunha inclinada com linhas de impacto curtas, em pixel art.
- **Dados** contidos na largura da HUD de baixo e centralizados com ela. O cálculo fica no meio, os dados saem do meio para fora e ficam um pouco mais baixos.
- **Barras de disposição** removidas do painel. Continuam valendo nas regras: no objetivo Expulsar, as criaturas fogem quando perdem metade da vida somada.

## Mundo e itens
- **Pedra em meio bloco**: o bloco de pedra é colocado como meio bloco, e outro bloco no mesmo lugar completa a pilastra.
- **Quinas preservadas**: ao quebrar um bloco, os vizinhos que já eram chanfrados continuam chanfrados.
- **Degrau com a pá**: Shift + pá em cima de um bloco corta o meio bloco de cima e vira degrau. Não exige mais a habilidade.

## Carta
- "Página anterior" e "Próxima página" ficam na base da carta, com o número da página. Só ficam ativas quando existe a página; desativadas aparecem apagadas.
- O ✕ no canto guarda a carta.

## Teste
- **Atalho de teste** no menu de pausa: "⚑ porta do chefe" leva direto para perto do Rei Sapo. É fácil de remover.

## Estudo
- `docs/design/DUNGEON-E-COMBATE-HIBRIDO-2026-11-03.md`:
  - dungeon por salas com chave, como no Dofus;
  - transição para o tático "parando o tempo", como no Divinity;
  - ação (ABS) para as criaturas pequenas e tático para os chefes.
- Nada disso está implementado ainda.
