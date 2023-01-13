import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if path_file in str(instance._data):
        return None
    txt_dic = txt_importer(path_file)

    data_process = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_dic),
        "linhas_do_arquivo": txt_dic
    }

    instance.enqueue(data_process)
    return sys.stdout.write(str(data_process))


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos", file=sys.stdout)
    else:
        file = instance.dequeue()
        print(f"Arquivo {file['nome_do_arquivo']} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
