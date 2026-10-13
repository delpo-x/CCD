#!/bin/bash
# Build murder-generator on Ubuntu 26.04 (WSL2). Run as root from the repo folder.
# OCaml 4.7 (required via esy) does not compile with GCC 15 as-is: this wrapper works around it.
set -e
apt-get update -qq
DEBIAN_FRONTEND=noninteractive apt-get install -y nodejs npm build-essential m4 git curl unzip python3
npm i -g esy

cat > /usr/local/bin/gcc <<'WRAP'
#!/bin/sh
for a in "$@"; do
  case "$a" in
    signals_asm.c) sed -i "s/sig_alt_stack\[SIGSTKSZ\]/sig_alt_stack[65536]/" signals_asm.c ;;
  esac
done
exec /usr/bin/gcc -std=gnu89 -fcommon -fpermissive -Wno-error "$@"
WRAP
chmod +x /usr/local/bin/gcc

# version.ml is generated from `git rev-parse HEAD`, so the sources must be in a git repo.
[ -d .git ] || { git init -q && git add -A && git -c user.name=x -c user.email=x@x commit -qm init; }

export ESY__PREFIX=$HOME/.esy
esy install
esy build
echo "Done. Terminal UI: esy run"
echo "Web UI: mkdir -p web && cp _build/default/js/main.js translations.json web/ && cp -R data web/ && cd web && python3 -m http.server 8000"
