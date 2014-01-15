from api.models import Action, ActionCategory


def get_action():
    pass

def create_or_update_action(action_id=None,**action_data):

    """
        Creates or updates Action bject according to existance of the action
    """
    action = Action.objects.filter(id=action_id)
    if action:
        action = action[0]
        action.__dict__.update(action_data)
        action.save()
    else:
        action = Action.objects.create(**action_data)
    return action
