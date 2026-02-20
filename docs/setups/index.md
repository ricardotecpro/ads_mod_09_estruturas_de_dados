# Ambiente de Desenvolvimento 🛠️

Para acompanhar este curso, você precisará de um compilador C e um editor de código.

## 💻 Requisitos
- **Compilador C**: GCC (Recomendado) ou Clang.
- **IDE/Editor**: [Visual Studio Code](https://code.visualstudio.com/).

## 🚀 Passos para Instalação

### Windows (MinGW-w64)
1. Baixe o instalador do [MSYS2](https://www.msys2.org/).
2. Siga as instruções e instale o pacote `mingw-w64-x86_64-gcc`.
3. Adicione o caminho `bin` às variáveis de ambiente (PATH).

### Linux (Ubuntu/Debian)
Execute no terminal:
```bash
sudo apt update
sudo apt install build-essential
```

### macOS
Instale as ferramentas de linha de comando do Xcode:
```bash
xcode-select --install
```

## 📝 Configuração do VS Code
Instale a extensão **C/C++** da Microsoft para suporte a IntelliSense e depuração.

---
!!! tip "Teste seu ambiente"
    Abra um terminal e digite `gcc --version`. Se aparecer a versão do compilador, você está pronto!