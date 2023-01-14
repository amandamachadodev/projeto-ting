def exists_word(word, instance):
    exists = list()
    result = list()
    for file in instance._data:
        for index, line in enumerate(file["linhas_do_arquivo"], start=1):
            if word.upper() in line.upper():
                exists.append({"linha": index})

        if len(exists) != 0:
            result.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": exists,
            })
        return result

def search_by_word(word, instance):
    """Aqui irá sua implementação"""
