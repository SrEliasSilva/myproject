import git

repo = git.Repo('https://github.com/SrEliasSilva/devforever.git')

repo.git.add('rl_ler_nfe_xml.py')


repo.git.commit(m='Adicionando novo recurso ao programa')

