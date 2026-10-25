# FIRE TAIL 0.9.11 — tripulantes, naufrágio e exploração

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
