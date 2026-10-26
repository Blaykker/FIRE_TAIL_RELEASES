# FIRE TAIL 0.9.12 — contas, cartas e desempenho

- Salvamento local por conta com sincronização, revisões e preservação de conflitos entre dispositivos. Recuperação explícita de mundos antigos deste computador. O alpha publicado exige login.
- Cartas de tarô com o mesmo layout na mão, coleção e ficha do tripulante. Turnos de 21 segundos, novos ícones de ação, dados mais próximos do HUD e cores por etapa preservando a pintura dos símbolos.
- Mochila com compartimentos, slots identificados, oito novas ilustrações ampliadas de equipamentos e progressão de profissões com desbloqueios de receitas.
- Correção da resolução interna quando o pós-processamento está desligado, reflexos limitados a 10 Hz e mar do menu animado na GPU. Medição de referência: 58 FPS médios na ilha em GTX 750 Ti, janela 1280×720 e buffer 640×360, sombras e pós-processamento desligados. O resultado varia com a configuração e a cena.
- Novo fogo volumétrico estilizado no barco, sombras em dither, silhueta no horizonte iluminada pelo relâmpago, capas leves e carga de queijo lançada ao mar na cinemática.
- Naufrágio com mastros de acesso, suporte na escada, salto curto entre vãos, poucas cargas de queijo recuperáveis e acampamento em terra. Parrot, Gecko e Tartaruga são NPCs da trilha narrativa, sem voltar à seleção jogável.
- Recompensas por relatos: 3 queijos por bug e 7 por sugestão, registradas no servidor e sem duplicar relatos iguais.

228 testes do jogo passaram, além da verificação TypeScript e compilação de produção. Conta, revisões e recompensas também foram verificadas em transação revertida no banco.

Launcher Mac 0.3.0 disponível separadamente para Apple Silicon e Intel no mesmo repositório. Sem Developer ID e sem notarização Apple; abertura verificada em executores Mac nativos, instalação no aparelho do jogador ainda em teste. Atualiza o cliente pelo feed e avisa sobre novos instaladores do launcher.

Este é um alpha: multiplayer prolongado, voz entre redes diferentes e progressão de convidados continuam em teste. A campanha completa de resgate e o envio automático de convites por e-mail não fazem parte desta entrega. JavaScript compilado e recursos do cliente são públicos; o projeto-fonte permanece separado.

## Histórico: 0.9.11

- Olhos pintados curvos, maiores e legíveis de frente/perfil; sobrancelhas junto ao rosto. Correção dos índices da malha de contorno, cel shading dos ratos e orelhas menores e mais baixas.
- Orin com instrumento voltado para a frente e boina simples; capa mais presente na Lyra.
- Aba Tripulante: ilustração animada, atributos em gráfico, profissões, talentos e cartas próprias. Prática de mineração, lenhador, escavação, arquearia, armas, defesa, esquiva, artesanato, tecnologia, negociação e sobrevivência preservada no save.
- Até três talentos de exploração por tripulante, desbloqueados em Genética. A capa da Lyra oculta por seis segundos e atacar a revela; na batalha, sua carta Manto das estrelas retira Lyra da mira até a próxima vez. Todos os ratos mantêm corrida e rolada.
- Mochila abaixo do minimapa, avisos abaixo dela com vidro e borda interna em degradê; categorias compactas, ícones de habilidades ajustados e baú com mochila lateral.
- Novo mercante corvo com modelo e retrato dedicados, diálogo e chat integrados à estética de vidro.
- Barco do menu utilizado também no naufrágio, em três partes com esqueleto, carga e convés caminhável. Abertura de partidas novas sem equipamentos, tutorial por ações e movimento de levantar adaptado das fases do FBX fornecido. Saves antigos preservam seus equipamentos.
- Discussão do barco com balões pixelados, cauda branca e símbolos à frente do fogo, ocultos durante a seleção aproximada. Fogueira com o mesmo shader estilizado da tocha, fumaça mais leve, sombras projetadas, vela curva com vento e vulto submarino discreto.
- Vida de criaturas com preenchimento estável, contorno colorido externo e seleção de objetos também sem pós-processamento. Dados com cores por função e dano em destaque por mais tempo.
- Flechas atravessam vazios e obstáculos baixos; caminhar por pedras continua bloqueado. Picareta pode romper um obstáculo adjacente por ação na batalha. Rotas de perseguição com busca de caminho e cache limitado.
- Voz por proximidade ou grupo, com ativação explícita, mute e liberação do microfone ao desligar/sair. Áudio não é gravado.
- Builds públicos sem mapas de código-fonte. O JavaScript compilado e os recursos necessários ao cliente continuam públicos e inspecionáveis.

## Verificação e limites do alpha

215 testes passaram em 41 arquivos, além de TypeScript e compilação de produção. Há testes de navegação, máscara de tiro compartilhada, talentos, persistência, olhos, tutorial e ciclo da voz. A voz foi conferida com áudio simulado; áudio real entre duas máquinas e redes com NAT restritivo ainda precisa de teste, podendo exigir TURN. Os talentos com botões atuam na exploração; no combate são usadas as cartas próprias.

O corte de meio bloco com pá também é liberado pela profissão Escavação no nível 3 (Shift + pá no solo sobre um bloco); a pá não minera paredes. Isso não cria terrenos abaixo do limite inferior do mundo.

Esta entrega permanece alpha para testes convidados, com balanceamento e testes prolongados de multiplayer em andamento. Não representa uma campanha/demo concluída nem garante 60 FPS em todo equipamento. Convites automáticos por e-mail continuam dependendo da ativação do remetente.
