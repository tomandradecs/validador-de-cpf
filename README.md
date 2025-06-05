Validador de CPF em Python
Sobre o Projeto
Este é um Validador de CPF desenvolvido em Python, focado em verificar a autenticidade de números de CPF (apenas os 11 dígitos numéricos) de acordo com o algoritmo oficial da Receita Federal Brasileira. O projeto é uma função concisa e eficiente que retorna True para CPFs válidos e False para inválidos, incluindo a verificação de casos especiais como CPFs com todos os dígitos repetidos. É um ótimo exercício para aprofundar o conhecimento em manipulação de strings, lógica condicional e aplicação de algoritmos matemáticos.

✨ Funcionalidades
Validação Algorítmica: Implementa o cálculo dos dois dígitos verificadores do CPF.
Checagem de Formato: Verifica se o CPF possui exatamente 11 dígitos e se são todos numéricos.
Tratamento de CPFs Inválidos Comuns: Identifica e marca como inválidos CPFs com todos os dígitos iguais (ex: 11111111111), que são inválidos por regra.
Retorno Booleano: A função validar_cpf() é simples de usar, retornando True ou False.

🚀 Como Usar
Este projeto é uma função que pode ser integrada em outros sistemas. Para testá-la diretamente:

Clone o repositório:

Bash

git clone https://github.com/tomandradecs/validador-de-cpf.git
cd validador-de-cpf

Execute o script Python:

Bash

python validar_cpf.py
O script contém exemplos de uso no bloco if __name__ == "__main__": que demonstram como a função se comporta com diferentes tipos de CPFs (válidos, inválidos, com dígitos repetidos, formato incorreto, etc.).

Exemplo de saída:

--- Testes de Validação de CPF ---
CPF 12345678909: Válido
CPF 12345678900: Inválido
CPF 00000000000: Inválido
CPF 11111111111: Inválido
CPF 99999999999: Inválido
CPF 1234567890a: Inválido
CPF 123456789: Inválido
CPF 123456789012: Inválido
CPF 12345678901: Inválido
CPF 98765432100: Inválido

🛠️ Tecnologias Utilizadas
Python 3.x

🤝 Contribuição
Ideias para aprimorar o validador (ex: aceitar CPFs com pontos e traços, ou integrar a uma interface)? Sua contribuição é bem-vinda!

Abra uma Issue para discutir sua sugestão ou um problema.
Faça um Fork do projeto.
Crie uma nova branch para suas alterações.
Envie um Pull Request detalhando suas modificações.

📄 Licença
Este projeto está licenciado sob a Licença MIT. Para mais detalhes, consulte o arquivo LICENSE.

📧 Contato
Tom Andrade - tom_andrade.ad@outlook.com

LinkedIn: linkedin.com/in/tom-andrade-08476a367/

GitHub: github.com/tomandradecs
