# FIRE TAIL 0.9.22 — conflito à Mouse Guard, grama nova e exclamação em pixel art

Versão 0.9.22 (02/11/2026). Para jogar pelo launcher: procure a atualização 0.9.22, conclua o download e selecione Embarcar.

## Conflito à Mouse Guard (adaptação própria)

- **Objetivo do conflito** escolhido no começo da batalha: **Vencer** (derrubar todas as criaturas) ou **Expulsar** (derrubar a disposição delas à metade; as criaturas fogem). Bichos 2+ degraus acima dos ratos na Ordem Natural só podem ser expulsos.
- **Disposição**: a vida somada de cada lado no começo, em duas barras no painel da esquerda. Com o objetivo Expulsar, a barra delas mostra a marca da metade.
- **Novas ações**, além de Atacar:
  - **Defender** (1 PA): +2 dados de defesa até a sua próxima vez.
  - **Fintar**: contra quem está na defesa (🛡), a defesa dele não rola; contra quem não está, você rola 1 dado a menos.
  - **Manobrar** (1 PA): +1 PM e o alvo fica **exposto** (◎): o próximo ataque de qualquer aliado contra ele rola +2 dados.
- **Criaturas**: as feridas (≤40%) se defendem; quem ataca um herói na defesa finta.
- **Acordo**: quem vence ainda paga conforme a disposição que perdeu. Menos de 25%, nada; 25–50%, perde 1 comida, munição ou material; 50% ou mais, perde 2. Nunca ferramentas, equipamento ou itens de missão. Aparece na tela de vitória.

## Visual

- **Grama**:
  - lâminas finas de ponta arredondada, com a luz do chão, formando uma massa;
  - **sem o tapete verde por baixo**: o chão e o grid de batalha aparecem;
  - animação em degraus;
  - dentro da arena de batalha a grama fica baixa;
  - menos instâncias, então carrega mais rápido.
- **Mato alto**: lâminas de 2 px com ponta arredondada, mais numerosas.
- **Exclamação**: só o "!", em pixel art de pixels grandes, sem estrela por trás, com animação em degraus.
- **Dados**: um pouco acima do cálculo, como se fossem jogados ao lado dele.

## Validação

- TypeScript sem erros e 291 testes, incluindo os de Expulsar, Defender, Fintar, Manobrar e Acordo.
- Capturas no navegador de nuvem: ilha com a grama nova e batalha com o objetivo, as barras de disposição e as ações novas.

## Pendências

- O modelo do Tail no Blender depende do Blender MCP conectado.
- Objetivos Escapar e Capturar/Resgatar.
