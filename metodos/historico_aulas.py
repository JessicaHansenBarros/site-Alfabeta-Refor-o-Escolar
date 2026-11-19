from classes.portal import PortalAlfabeta
from classes.professor import Professor


def exibir_historico(portal: PortalAlfabeta, professor: Professor) -> None:
    print("\n--- HISTÓRICO DE AULAS ---")
    aulas_exibir = portal.listar_aulas(professor)

    if not aulas_exibir:
        print("Nenhuma aula registrada até o momento.")
        return

    for i, aula in enumerate(aulas_exibir, start=1):
        print(f"{i}. {aula.descrever()}")

    print(f"\nTotal de aulas registradas: {len(aulas_exibir)}")
