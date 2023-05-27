#Mesmo que, as vezes, o windows esconda as extensões, praticamente todos os arquivos as contém, e utilizasse "." para denota-lás
#por exemplo, GIFS contem '.gif', e imagens podem conter '.jpg', '.png', '.jpeg', entre outras
#nesse programa, pergunte ao usuário o nome do arquivo (com a resposta sendom, por exemplo 'ashua.jpg') 
# e de um output do tipo de arquivo, sendo as extensões utilizadas como paremetro:
#.gif
#.jpg
#.jpeg
#.png
#.pdf
#.txt
#.zip
#caso tenha alguma dessas extensões, dar um output do tipo de arquivo, sendo eles:
# - Imagem
# - Texto
# - Zip

# mais o tipo de extensão, separados por '/', então, se um usuário escrevesse:
#   cat.jpg

#o output seria:
#   image/jpg

#ou
#   notas.pdf
#output de:
#    texto/pdf

#caso tenha outra extensão, dar um output de 'application/octet-stream', que é um padrão
# lembre-se da documentação: docs.python.org/3/library/stdtypes.html#string-methods.