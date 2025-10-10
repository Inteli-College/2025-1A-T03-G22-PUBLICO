---
title: Sprint Conclusion
slug: /sprint-conclusion
---

## 📄  5 – Documentação da Decisão Técnica

### 🎯 Objetivo

Registrar de forma clara e estruturada todas as decisões tomadas ao longo da implementação da arquitetura de recuperação de dados baseada na abordagem RAG (Retrieval-Augmented Generation). Esta documentação serve como suporte técnico para futuras evoluções e integrações com LLMs.

---

### 🔎 Escolha da estratégia de busca: Busca Vetorial

A busca vetorial foi escolhida em detrimento da busca por palavras-chave ou abordagem híbrida devido à natureza jurídica e densa dos documentos analisados (ex: editais e RFPs). Esses documentos utilizam variações linguísticas e estruturas pouco padronizadas, tornando inviável uma busca tradicional baseada apenas em termos exatos.

A **busca vetorial com embeddings semânticos** permite que o sistema compreenda o significado das perguntas do usuário e localize trechos relevantes mesmo que a linguagem usada seja diferente da consulta textual.

---

### 🧠 Modelo de Embeddings utilizado

O modelo adotado foi o `all-MiniLM-L6-v2`, disponibilizado pela biblioteca `sentence-transformers`. Os motivos da escolha incluem:

- Alto desempenho semântico (captura contexto e sinônimos)
- Leve e rápido — ideal para protótipos e ambientes locais
- Embeddings de 384 dimensões, balanceando precisão vs. performance

---

### ✂️ Estrutura dos documentos (chunking)

Para indexação eficiente no vetor semântico, os documentos são divididos da seguinte forma:

- Tamanho do chunk: **500 tokens (palavras)**  
- Sobreposição: **100 tokens**  
- Estratégia: simples divisão por palavras com `split()` para identificar contextos e garantir consistência entre os trechos no momento da consulta.

Essa segmentação garante que os conteúdos fiquem com tamanho aceitável para memória vetorial, preservando sentido mesmo quando analisados fora de contexto completo.

---

### 🗃️ Base vetorial utilizada: FAISS

A ferramenta escolhida para armazenar e consultar a base vetorial foi o **FAISS (Facebook AI Similarity Search)**. As razões da escolha incluem:

- Gratuito e open source
- Alta performance em buscas por similaridade (cosine/L2)
- Fácil integração com arrays NumPy e embeddings do SentenceTransformers

O índice foi criado utilizando:
- Tipo: `IndexFlatL2` (distância euclidiana simples)
- Tamanho do vetor: 384 dimensões
- Comando de persistência: `faiss.write_index(index, "index_edital.faiss")`

---

### 🧪 Exemplos de índice criado e testes realizados

**Documento de teste:** Edital SP001/2024 – EMBASA  
**Etapas executadas:**
- Texto extraído com `pdfplumber`
- Chunking executado com sobreposição
- Vetorização com `MiniLM`
- Armazenamento com FAISS

**Consulta realizada:**  
> Quais são os requisitos financeiros do edital?

**Resultados retornados:**
- Trechos mencionando “balanço patrimonial”, “patrimônio líquido mínimo” e “DFL (disponibilidade financeira líquida)”, exatamente como exigido no edital.

---

### 📈 Volume estimado por edital

Em testes realizados com o edital SP001/2024 (aproximadamente 22 páginas de conteúdo textual útil), o sistema gerou:

- **Cerca de 50 a 60 chunks por edital**, com variação de acordo com:
  - Complexidade do texto
  - Existência de tabelas ou anexos sem texto legível
  - Formatação do conteúdo (densidade de palavras por parágrafo)

---

### ✅ Conclusão da Sprint

A estrutura implementada nesta sprint entrega um protótipo funcional de sistema de recuperação semântica para documentos públicos complexos. A base FAISS está preparada para ser integrada a um modelo LLM, utilizando os chunks mais relevantes como contexto para geração de respostas confiáveis e informativas aos usuários das áreas de sales e pré-sales.

---
