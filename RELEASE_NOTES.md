# FIRE TAIL 0.9.21 — inventário estável, cartas novas, cerco da centopeia e efeitos de HQ

Versão 0.9.21 (02/11/2026). Para jogar pelo launcher: procure a atualização 0.9.21, conclua o download e selecione Embarcar.

## Batalha

- **Dados rolavam mais de uma vez.** No coop, cada atualização da batalha que chegava pela rede recriava as rolagens, e a tela rolava os mesmos dados de novo (até 6 vezes). Agora cada rolagem tem um número único e aparece **uma vez só**.
- **Cálculo nascendo da HUD**:
  - o resumo do confronto virou uma aba presa à moldura de baixo;
  - os dados ficam na mesma linha, à esquerda (jogador) e à direita (inimigo), colados na HUD;
  - o quadro fica centralizado na HUD, não na tela.
- **Efeito de HQ**: um estouro vermelho com "!" quando a criatura entra em combate e quando alguém leva dano (maior no crítico).
- **Centopeia e serpente se movem como corpos longos.** Antes, encostadas num herói, elas ficavam paradas. Agora deslizam em volta da presa para **cercá-la**:
  - quando o cerco começa a fechar, aparece o aviso "está cercando";
  - com 3 partes do corpo em volta da presa, o ataque vira **APERTO**: se ferir, o herói cai **ABATIDO**.
- **Abatido**:
  - a casa mostra a marca "ABATIDO";
  - um aliado ao lado gasta **1 ação** para levantá-lo;
  - o herói volta com ~30% da vida (antes era 1).
- **Árvore de habilidades**:
  - **Passo de batalha** dá +1 PM por nível, nos níveis 3, 6 e 10;
  - **Ritmo de batalha** dá +1 PA por nível; agora exige nível 5 e depois 12.

## Inventário

- **Abas da mochila numa linha só.** A aba de cartas de batalha passa a se chamar **Baralho**.
- **Modos da bolsa**: Tudo, Munição, Recursos, Minerais, **Missão** e **Cartas**.
  - Itens de missão (como o volante) e cartas ou registros vão para um **bolso sem limite** e não ocupam espaço.
  - A carta abre sozinha na primeira vez e fica para reler na aba Cartas.
  - Saves antigos: cartas que estavam na mochila vão para o bolso.
- **Itens que "sumiam"**:
  - não dá mais para soltar item num espaço trancado da barra rápida ou da bolsa;
  - mandar para a barra cheia avisa e não mexe em nada;
  - pilhas iguais se juntam entre baú e mochila;
  - moedas de venda ou duelo sem espaço caem no chão em vez de sumir.
- **Baú de missão × baú normal**:
  - o baú de missão entrega o conteúdo inteiro **a cada jogador, uma vez**, e só se couber na mochila; senão avisa e não tira nada;
  - o baú normal continua sendo depósito.
  - Os baús de suprimento da praia agora são de missão.

## Cartas

- **Custo em PA**: losangos azuis em coluna, de cima para baixo, logo abaixo do losango da categoria, sem encostar nele. A base da carta ficou só para o texto, e a arte aparece inteira.
- **Carta ampliada**: é a mesma carta, só maior. Saiu a versão quadrada que cortava a ilustração.
- **Atos dos Tripulantes · Registro 27**: a carta do naufrágio foi reescrita na alegoria de Atos 27. Ela conta a carga lançada ao mar, o menor dos presos que se levanta e a chegada de todos vivos.

## Tutorial

- **A primeira tarefa é quebrar uma pedra.** A picareta cai aos pés de quem acorda.
- **Nova ordem**: pedra → olhar ao redor → caixa e tocha → pá → arco → Atos dos Tripulantes. Saves no meio do tutorial são convertidos para a nova ordem.

## Social e conta

- **Balão de fala** sobre o personagem que está falando, enquanto o diálogo está aberto.
- **Silhueta verde** em quem você está **seguindo** e em quem está **invisível** (você ou alguém do grupo).
- **Esqueci a senha** na tela de entrar: o jogo envia um link de recuperação por e-mail. O link abre a versão web, que pede a senha nova.
  - Requer `https://fire-tail-six.vercel.app/**` nas Redirect URLs do Supabase Auth.

## Publicação

- O feed do site (`fire-tail-web/releases/channel.json`) agora segue o feed do GitHub por uma regra de rota na Vercel. O launcher 0.2.5 recebe as versões novas sem precisar republicar o site.

## Validação

- TypeScript sem erros e 287 testes.
- Capturas no navegador de nuvem: diálogo, mochila, carta ampliada e batalha com a centopeia cercando.

## Pendências

- Praia com ondas e faixa larga, arquipélago, Biblioteca e barco no grid: plano em `docs/design/MUNDO-ARQUIPELAGO-2026-11-02.md`.
- Recuperação de senha no **site**: o código do site não está em git local; fica para a próxima publicação dele.
- Ver senha de jogador no painel: **não é possível nem seguro**, porque a senha é guardada só como hash. A alternativa é o painel enviar o link de recuperação.
