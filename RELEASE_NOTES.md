# FIRE TAIL 0.9.18 — ofícios e decisões táticas

Versão 0.9.18, preparada para publicação em 31/10/2026. Primeira implementação derivada da pesquisa de sistemas, com regras e desenhos próprios do Fire Tail.

- Movimento: alcance destacado e caminho usam a mesma interrupção ao entrar perto de um inimigo. Linha de visão simétrica, com fechamento de cantos e passagem por obstáculos baixos explicitamente permitidos.
- Polvo e Rei Sapo procuram distância e linha de tiro; criaturas de contato procuram aproximação. A decisão considera posições e obstáculos, sem consultar armadilhas ocultas. O guia de turno explica o comportamento.
- Carpintaria, Costura, Alquimia e Ferraria no perfil do tripulante, com experiência por fabricação e desbloqueios por nível.
- Aba Ofícios no diário: seis receitas, ingredientes, nível atual/exigido, experiência e motivo de bloqueio.
- Itens novos: tábua de bordo, cordão de seda, atadura de ervas, antídoto de bordo, colete de trilha e anel de fôlego. Ícones vetoriais originais.
- Cadeia madeira → tábuas → baú; seda → cordão → atadura/colete/anel. O baú mantém o custo equivalente de seis madeiras e um ferro.
- Fabricação confirma ingredientes e resultado juntos. Mochila cheia não consome materiais nem concede experiência; espaços de inventário bloqueados continuam indisponíveis.
- Colete com representação no personagem e bônus de exploração; anel com regeneração de stamina. Antídoto remove veneno também na batalha, consumindo a ação.
- Aplicativo e pacote principal alinhados em 0.9.18. Saves conservam os IDs anteriores.

Validação: 263 testes em 50 arquivos, compilação TypeScript e distribuição web gerada. Teste de interface em desenvolvimento: fabricar dez cordões, atingir Costura 3, criar/equipar colete, salvar e recarregar preservando equipamento, materiais e experiência; encontro no mapa com polvo à distância; usar antídoto gastando a ação e observar o ataque do inimigo. Capturas e resultado reproduzível em `e2e/out/alpha-0918/`. A distribuição compilada carregou o menu 0.9.18; o fluxo autenticado de produção não foi testado, pois requer a conta do jogador.

Para jogar pelo launcher instalado: procure a atualização 0.9.18, conclua o download e selecione Embarcar. O jogo é distribuído separadamente do instalador do launcher.

Os novos corpo, rig e mochila modular continuam em revisão de arte e não substituem os modelos atuais. Esta versão não inclui prospecção, nova divisão de drops, forjamagia, profissões completas, catálogo inteiro de 118 itens ou todas as mecânicas de classe pesquisadas. O build ainda sinaliza arquivos JavaScript grandes; não houve certificação de desempenho em outros computadores ou validação de equilíbrio de longo prazo.
