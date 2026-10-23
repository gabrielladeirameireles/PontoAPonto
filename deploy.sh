
MENSAGEM=${1:-"update: atualizacao do projeto Ponto a Ponto"}

echo "----------------------------------------"
echo "Iniciando processo de automacao Git..."
echo "----------------------------------------"

git add .

git commit -m "$MENSAGEM"

git push origin main

echo "----------------------------------------"
echo "Processo concluido com sucesso."
echo "----------------------------------------"