from orm.models import EmailVariant, ConnectedAccount, Contact


def reset_template_counter(current_counter: int, total_template: int) -> int:
    if current_counter >= total_template:
        return 0
    return current_counter + 1


def total_counter(templates: [EmailVariant], contacts: [Contact], connected_accounts: [ConnectedAccount]) -> (
        int, int, int):
    return len(templates), len(contacts), len(connected_accounts)
