
# Harmonic App 🎶

Aplicativo musical feito com [Flet](https://flet.dev) para estudo de escalas, formação de acordes e campos harmônicos.

## Funcionalidades

- Estudo de Escalas (Modos, Pentatônicas, Blues)
- Formação de Acordes (maior, menor, com 7ª, diminuto etc)
- Campo Harmônico
- Exportação/Impressão de PDF

## Como executar localmente

```bash
pip install -r requirements.txt
flet run main.py --web
```

## Deploy no Render

1. Crie uma conta em https://render.com
2. Crie um novo Web Service
3. Use os comandos abaixo:

- **Build command**:
```bash
pip install -r requirements.txt
```

- **Start command**:
```bash
flet run main.py --web
```

Depois aponte seu domínio na Hostinger para o link gerado.
