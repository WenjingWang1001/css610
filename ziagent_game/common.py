'''
    This file is used to store default settings.
'''

__all__ = ['nagents', 'move_choices', 'get_id']

nagents = 100

# Game select
move_choices = (
    'swerve',
    'straight',
)


def get_id(obj_class):

    # if not obj_id:
    try:
        all_ids = [a.id for a in obj_class.instances.values()]
        last_id = sorted(all_ids)[-1]
        return last_id + 1
    except (AttributeError, IndexError) as e:
        return 1

    

# class Timer():
#     def __init__(self):