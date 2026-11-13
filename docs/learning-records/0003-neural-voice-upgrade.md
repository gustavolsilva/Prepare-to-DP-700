# Atualização: Síntese de Áudio Neural Humana (pt-BR-AntonioNeural)

O usuário apontou que a narração anterior (feita por síntese robótica básica) soava artificial e mecânica.

### Implementação
- Substituímos o gerador tradicional pelo modelo neural de alta fidelidade `pt-BR-AntonioNeural` (Microsoft Neural Voices).
- O áudio gerado (`assets/audio/lesson-0001-pt.mp3`) agora possui entonação fluida de linguagem falada humana natural, com pausas adequadas de respiração e dicção profissional em português brasileiro.
- O arquivo é servido diretamente pelo servidor local via streaming HTTP de áudio HTML5.

