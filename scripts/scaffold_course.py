import os
from pathlib import Path

# --- Configuration ---
SYLLABUS = [
    {"id": 1, "module": "Módulo 1 – Fundamentos", "title": "Introdução às Estruturas de Dados"},
    {"id": 2, "module": "Módulo 1 – Fundamentos", "title": "Revisão de Lógica e Funções"},
    {"id": 3, "module": "Módulo 2 – Estruturas Básicas", "title": "Arrays (Vetores)"},
    {"id": 4, "module": "Módulo 2 – Estruturas Básicas", "title": "Matrizes"},
    {"id": 5, "module": "Módulo 2 – Estruturas Básicas", "title": "Análise de Complexidade (Big-O)"},
    {"id": 6, "module": "Módulo 3 – Listas", "title": "Listas Encadeadas"},
    {"id": 7, "module": "Módulo 3 – Listas", "title": "Listas Duplamente Encadeadas"},
    {"id": 8, "module": "Módulo 4 – Sequenciais", "title": "Pilhas (Stacks)"},
    {"id": 9, "module": "Módulo 4 – Sequenciais", "title": "Filas (Queues)"},
    {"id": 10, "module": "Módulo 5 – Avançado", "title": "Recursão Aplicada"},
    {"id": 11, "module": "Módulo 5 – Avançado", "title": "Árvores – Conceitos Básicos"},
    {"id": 12, "module": "Módulo 5 – Avançado", "title": "Árvores Binárias"},
    {"id": 13, "module": "Módulo 5 – Avançado", "title": "Árvores de Busca Binária (BST)"},
    {"id": 14, "module": "Módulo 6 – Avançado II", "title": "Tabelas Hash"},
    {"id": 15, "module": "Módulo 6 – Avançado II", "title": "Introdução a Grafos"},
    {"id": 16, "module": "Módulo 6 – Avançado II", "title": "Projeto Final"},
]

DIRS = [
    "docs/aulas",
    "docs/slides/.src",
    "docs/quizzes/.src",
    "docs/exercicios",
    "docs/projetos",
    "docs/assets/images"
]

# --- Templates ---

TEMPLATE_AULA = """# {title}

## 🎯 Objetivos da Aula
- [ ] Compreender os conceitos de {title}
- [ ] Aplicar em problemas reais
- [ ] Analisar a eficiência da estrutura

## 🧠 Conceito Principal

!!! info "O que é?"
    Breve explicação sobre {title}.

### 📊 Representação Visual

```mermaid
graph TD
    A[Início] --> B[Processamento]
    B --> C{{Decisão}}
    C -->|Sim| D[Resultado 1]
    C -->|Não| E[Resultado 2]
```

## 💻 Exemplo Prático (C)

```c
#include <stdio.h>

int main() {{
    printf("Exemplo de {title}\\n");
    return 0;
}}
```

### 🚀 Execução no Terminal

```termynal
$ gcc programa.c -o programa
$ ./programa
Exemplo de {title}
```

!!! tip "Dica de Ouro"
    Sempre verifique o uso de memória.

## 📝 Resumo
Nesta aula aprendemos sobre...

---
## 🏁 Próximos Passos

<div class="grid cards" markdown>

-   :material-presentation: **Acessar Slides**
    -   [Ver Slides da Aula](../slides/slide-{id:02d}.html)

-   :material-school: **Quiz**
    -   [Responder Quiz](../quizzes/quiz-{id:02d}.md)

-   :material-dumbbell: **Exercícios**
    -   [Lista de Exercícios](../exercicios/exercicio-{id:02d}.md)

-   :material-rocket: **Projeto**
    -   [Mini Projeto](../projetos/projeto-{id:02d}.md)

</div>
"""

TEMPLATE_SLIDE = """# {title}
## Aula {id:02d}

---

## 🎯 Objetivos
- Compreender {title}
- Ver exemplos práticos
- Resolver problemas

---

## 💡 Introdução
Explicação conceitual breve...

---

## 📊 Diagrama

```mermaid
graph LR
    A[Dado] --> B(Estrutura)
    B --> C[Informação]
```

---

## 💻 Código Exemplo

```c
// Código aqui
```

---

## 🏁 Conclusão
- Revisão dos pontos principais

---

<!-- .element: class="fragment" -->
# Próxima Aula: ...
"""

TEMPLATE_QUIZ = """# Quiz {id:02d}: {title}

**Teste seus conhecimentos.**

1. O que define melhor {title}?
    - ( ) Opção A
    - (x) Opção B
    - ( ) Opção C
    *Explicação: Opção B é a correta pois...*

2. Pergunta 2 aqui?
    - ( ) Verdadeiro
    - (x) Falso
    *Explicação: Justificativa aqui.*
"""

TEMPLATE_EXERCICIO = """# Exercícios: {title}

## 🟩 Nível: Básico
1. Exercício 1...
2. Exercício 2...

## 🟨 Nível: Intermediário
3. Exercício 3...
4. Exercício 4...

## 🟥 Nível: Desafio
5. Exercício 5...
"""

TEMPLATE_PROJETO = """# Projeto: {title}

## 📝 Descrição
Implemente um sistema que...

## 📋 Requisitos
- [ ] Requisito 1
- [ ] Requisito 2

## 🚀 Desafio Extra
Adicione a funcionalidade...
"""

TEMPLATE_INDEX = """# Bem-vindo ao Curso de Estruturas de Dados 🚀

## 📚 Sobre o Curso
Este curso aborda os fundamentos e implementações das principais estruturas de dados.

## 🗺️ Mapa do Tesouro

<div class="grid cards" markdown>

-   :material-rocket: **Começar Agora**
    -   [Ir para Aula 01](aulas/aula-01.md)

-   :material-book-open-page-variant: **Plano de Ensino**
    -   [Ver Cronograma](plano-ensino.md)

</div>
"""

# --- Execution ---

def create_files():
    # 1. Ensure Directories
    for d in DIRS:
        Path(d).mkdir(parents=True, exist_ok=True)
    
    # 2. Create Index if missing
    if not Path("docs/index.md").exists():
        Path("docs/index.md").write_text(TEMPLATE_INDEX, encoding="utf-8")
        print("Created index.md")

    # 3. Generate Content
    for lesson in SYLLABUS:
        lid = lesson["id"]
        title = lesson["title"]
        
        # Paths
        p_aula = Path(f"docs/aulas/aula-{lid:02d}.md")
        p_slide = Path(f"docs/slides/.src/slide-{lid:02d}.md")
        p_quiz = Path(f"docs/quizzes/.src/quiz-{lid:02d}.md")
        p_exerc = Path(f"docs/exercicios/exercicio-{lid:02d}.md")
        p_proj = Path(f"docs/projetos/projeto-{lid:02d}.md")
        
        # Write Files
        p_aula.write_text(TEMPLATE_AULA.format(id=lid, title=title), encoding="utf-8")
        p_slide.write_text(TEMPLATE_SLIDE.format(id=lid, title=title), encoding="utf-8")
        p_quiz.write_text(TEMPLATE_QUIZ.format(id=lid, title=title), encoding="utf-8")
        p_exerc.write_text(TEMPLATE_EXERCICIO.format(id=lid, title=title), encoding="utf-8")
        p_proj.write_text(TEMPLATE_PROJETO.format(id=lid, title=title), encoding="utf-8")
            
        print(f"Generated Lesson {lid:02d}: {title}")

def generate_nav_yaml():
    nav = ["nav:", "  - Início: index.md"]
    
    nav.append("  - Aulas:")
    nav.append("      - aulas/index.md")
    
    current_module = None
    
    for lesson in SYLLABUS:
        module = lesson["module"]
        title = lesson["title"]
        lid = lesson["id"]
        filename = f"aulas/aula-{lid:02d}.md"
        
        if module != current_module:
            nav.append(f"      - {module}:")
            current_module = module
        
        nav.append(f"        - 'Aula {lid:02d} - {title}': {filename}")
    
    nav.append("  - Materiais:")
    nav.append("      - materiais.md")
    nav.append("      - Slides: slides/index.md")
    nav.append("      - Exercícios: exercicios/index.md")
    nav.append("      - Quizzes: quizzes/")
    nav.append("      - Projetos: projetos/")
    nav.append("      - Setups: setups/index.md")
    nav.append("  - Impressão: print_page.md")
    
    return "\n".join(nav)

def update_mkdocs():
    mkdocs_path = Path("mkdocs.yml")
    content = mkdocs_path.read_text(encoding="utf-8")
    
    # Remove existing 'nav:' if present (simplistic approach, assumes nav is at end or distinct)
    # We will append the new nav
    # Better: finding where nav starts
    
    if "nav:" in content:
        content = content.split("nav:")[0] # Truncate everything after nav:
    
    new_nav = generate_nav_yaml()
    
    final_content = content.strip() + "\n\n" + new_nav + "\n"
    mkdocs_path.write_text(final_content, encoding="utf-8")
    print("Updated mkdocs.yml navigation")

if __name__ == "__main__":
    create_files()
    update_mkdocs()
