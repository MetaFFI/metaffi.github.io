# metaffi.github.io

Source for the [MetaFFI website](https://metaffi.github.io) — a multi-lingual interoperability system.

Built with [Jekyll](https://jekyllrb.com/) and the [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) theme, deployed via GitHub Pages.

## Local Development

```bash
bundle install
bundle exec jekyll serve
```

## Regenerating Performance Figures

```bash
python scripts/generate_web_figures.py
```

Requires `matplotlib` and `numpy`. Reads data from `../tests/results/`.
